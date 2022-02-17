import onnxruntime
import cv2
import numpy as np
import yaml
with open('../config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


class Model():
    def __init__(self):
        print("loading onnx model and warming up")
        self.model = onnxruntime.InferenceSession(config['model_path'], None)
        img = np.zeros([320,320,3],dtype=np.float32)
        _ = self.onnx_inf(self.model,img)
        print("ONNX model_ready")
                        
    def onnx_inf(self,session,img):
        output_dict = {}
        img = img[np.newaxis,...].astype(np.float32)
        input_name = session.get_inputs()[0].name
        onnx_output_name = [out.name for out in session.get_outputs()] 
        result = session.run(onnx_output_name, {input_name: img})        
        output_dict['keypoint_scores'] = result[0][0]
        output_dict['kpts'] = result[1][0]
        output_dict['number_detections'] = result[2][0]
        output_dict['person_scores'] = result[3][0]
        output_dict['person_box'] = result[5][0]
        return output_dict     
    
    def infer(self,image):
        resized_image = cv2.resize(image,(320,320))
        output_dict = self.onnx_inf(self.model, resized_image)
        return output_dict
    

        
    
    

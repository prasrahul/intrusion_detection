import logging
import queue
import time
import traceback
from threading import Thread
import yaml

import cv2

from onnx_utils.model_onnx import Model
from post_process.intrusion_detection import intruion
from post_process.social_distance import soc_dis

#loading the config file
with open('../config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    
print("Processing at : ",config['processing_fps'])

model = Model()

#Queue for frames
frame_q = queue.Queue()

#Variable for processing nth frame
mod = int(config['original_fps']/config['processing_fps'])

def read():
    time.sleep(1)
    if config['type'] == 1:
        feed1 = cv2.VideoCapture(0)
    else : 
        feed1 = cv2.VideoCapture(config["video_path"])
    fps_counter = 0
    while True:
        # st = time.time()
        try :
            ret,image = feed1.read()
            if not ret :
                print("Not able to read the frames - BREAKING")
                if config['type'] == 1:
                    feed1 = cv2.VideoCapture(0)
                else : 
                    feed1 = cv2.VideoCapture(config["video_path"])
            
        except Exception as e:
            print("Not able to read the frames - BREAKING(out)",e)
            if config['type'] == 1:
                feed1 = cv2.VideoCapture(0)
            else : 
                feed1 = cv2.VideoCapture(config["video_path"])

        
        if fps_counter % mod == 0:
            fps_counter +=1
            time.sleep(0.04)
            frame_q.put((1,image))
        else:
            fps_counter +=1
            

def main():
    print("starting main func")
    if 1 in config['process']:
        print("activating Intrusion detection ")
    if 2 in config['process']: 
        print("activating Social distance")
    while True:
        (cam_id,image) = frame_q.get()
        try:
            output_dict = model.infer(image)
            if 1 in config['process']:
                image = intruion(output_dict,image)
                
            if 2 in config['process']: 
                image = soc_dis(image,output_dict)
                         
            cv2.imshow("output", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        except Exception as e:
            print(f"Main (cam-1) : {traceback.format_exc()}")       
            

if __name__ == '__main__':
    Thread(target=read,daemon=True).start()
    main()
    
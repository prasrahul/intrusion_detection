class Config():
    def __init__(self):
        self.type = 1
        self.video_path = ""
        self.model_path = "../models/centernetMobilenet_kpts.onnx"
        #self.model_path = "mbwithnd.onnx"
        self.orginal_fps = 25
        self.processing_fps = 5
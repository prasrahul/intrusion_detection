import logging
import queue
import time
import traceback
from threading import Thread
import yaml

import cv2

from onnx_utils.model_onnx import Model

#loading the config file
with open('../config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    
model = Model()
print(config['original_fps'])

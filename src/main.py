import logging
import queue
import time
import traceback
from threading import Thread

import onnxruntime
import cv2

from config import Config
from onnx_loading.model_onnx import Model


config = Config()
model = Model()
print(config.orginal_fps)

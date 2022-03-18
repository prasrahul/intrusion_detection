
# import required module
from playsound import playsound
import time
import cv2
import datetime
import os
# for playing note.wav file

def play_sound(audio_q):
    end_time = time.time() + 3
    if not os.path.exists("../violation_images"):
        os.makedirs("../violation_images")
        print("created violation folder")
    
    while True:
        time.sleep(0.005)
        val,image = audio_q.get()
        if time.time() > end_time:
            if val == 1 :
                end_time = time.time() + 3
                playsound('audio_utils/Violation detected.wav')
                time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                save_path = "../violation_images"+ "/" + time_now + '.jpg'
                cv2.imwrite(save_path,image)
                print("image saved")
                # end_time = time.time() + 3
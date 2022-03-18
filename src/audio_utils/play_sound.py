
# import required module
from playsound import playsound
import time
  
# for playing note.wav file

def play_sound(audio_q):
    
    end_time = time.time() + 3
    while True:
        time.sleep(0.01)
        val = audio_q.get()
        if time.time() > end_time:
            if val == 1 :
                end_time = time.time() + 3
                playsound('audio_utils/Violation detected.wav')
                # end_time = time.time() + 3
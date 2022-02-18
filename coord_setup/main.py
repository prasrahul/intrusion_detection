import yaml
from utils import *

#loading the config file
with open('../config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    
if config['type'] == 1:
    video_file = 0
else : 
    video_file = config["video_path"]
    
def main(video_file,filename):
    """
    entry point of the file
    """
    img_process = Image_Process(filename)
    image_path = img_process.capture_image(video_file)
    img_process.get_line_coor(image_path)

if __name__ == '__main__':
    main(video_file,"out")

    
# /home/prasanna/mirrag/videos/Cam-1[Trim].mp4

# roi = img[y1:y2, x1:x2]
"""
Here's a visualization for cropping a ROI from an image

-------------------------------------------
|                                         | 
|    (x1, y1)                             |
|      ------------------------           |
|      |                      |           |
|      |                      |           | 
|      |         ROI          |           |  
|      |                      |           |   
|      |                      |           |   
|      |                      |           |       
|      ------------------------           |   
|                           (x2, y2)      |    
|                                         |             
|                                         |             
|                                         |             
-------------------------------------------"""


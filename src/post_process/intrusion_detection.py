import yaml
import cv2
import numpy as np

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

with open('../config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    
def intruion(output_dict,image):
    pts = np.array([config['intrusion_coords'][0],
                    config['intrusion_coords'][1],
                    config['intrusion_coords'][2],
                    config['intrusion_coords'][3]], np.int32)
            
    pts = pts.reshape((-1,1,2))
    cv2.polylines(image,[pts],True,(255,255,255),5)
    im_height, im_width, c = image.shape
    for i in range(int(output_dict['number_detections'])):
        if output_dict['person_scores'][i] > 0.60:
            (x_min, x_max, y_min, y_max) = (
                output_dict['person_box'][i][1] * im_width, output_dict['person_box'][i][3] * im_width,
                output_dict['person_box'][i][0] * im_height, output_dict['person_box'][i][2] * im_height)
            p1 = (int(x_min), int(y_min))
            p2 = (int(x_max), int(y_max))
            cx = int((x_min + x_max) / 2)
            cy = int((y_min + y_max) / 2)
            cv2.rectangle(image, p1, p2, (0, 255, 0), 2)
            cv2.circle(image, (int(cx), int(cy)), 3, (0, 0, 0), 3)
            
            point = Point(cx,cy)
            polygon = Polygon([config['intrusion_coords'][0],
                               config['intrusion_coords'][1],
                               config['intrusion_coords'][2],
                               config['intrusion_coords'][3]])
            if polygon.contains(point) :
                cv2.rectangle(image, p1, p2, (0, 0, 255), 2)
        for j in range(0,17):
            if output_dict['keypoint_scores'][i][j] > 0.60:
                (cy, cx) = (output_dict['kpts'][i][j][0] * im_height, output_dict['kpts'][i][j][1] * im_width)
                cv2.circle(image, (int(cx), int(cy)), 2, (255, 255, 255), 2)
                        
    return image
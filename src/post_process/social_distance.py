import cv2
import numpy as np

def soc_dis(image_np,output_dict):
    data = []
    im_height, im_width, c = image_np.shape

    for i in range(int(output_dict['number_detections'])):
        if output_dict['person_scores'][i] > 0.60:
            (x_min, x_max, y_min, y_max) = (
                output_dict['person_box'][i][1] * im_width, output_dict['person_box'][i][3] * im_width,
                output_dict['person_box'][i][0] * im_height, output_dict['person_box'][i][2] * im_height)
            cx = int((x_max+x_min)/2)
            cy = int((y_max+y_min)/2)

            p1 = (int(x_min), int(y_min))
            p2 = (int(x_max), int(y_max))

            cv2.circle(image_np,(cx,cy),2,(0,255,0),cv2.FILLED)
            data.append([i,[cx,cy],[p1,p2]])

        #print(data)

        if len(data) >= 2:
            for j in data:
                for e in data:
                    if e[0] != j[0]:
                        distance = np.sqrt((j[1][0]-e[1][0])**2+(j[1][1]-e[1][1])**2)
                        #print(distance)
                        if (distance <255) and (distance >70):
                            cv2.rectangle(image_np, j[2][0], j[2][1], (0, 0, 255), 2, 1)
                            cv2.rectangle(image_np, e[2][0], e[2][1], (0, 0, 255), 2, 1)
                            cv2.line(image_np,(j[1][0],j[1][1]),(e[1][0],e[1][1]),(0, 0, 255), 1)
                
    return image_np

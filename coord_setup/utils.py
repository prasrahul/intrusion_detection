import cv2
import os
import datetime

class Image_Process():
    def __init__(self,filename):
        self.coords = []
        self.roi = []
        self.filename = filename
        
    def capture_image(self,video_file):
        """
        saves a image for further processing
        Args:
            video file
        """ 
        feed = cv2.VideoCapture(video_file)
        while True:
            ret, frame = feed.read()
            print("original image shape:",frame.shape)
            break
        image_name = "out"


        try: 
            os.mkdir("images") 
        except OSError as error: 
            print("/n")
        cv2.imwrite(f"images/{image_name}.jpg",frame)
        print(f"{image_name}.jpg is saved successfully")

        feed.release()
        cv2.destroyAllWindows()
        self.image_name = image_name
        return image_name

    def get_line_coor(self,image_name):
        """
        Gets the line Coordinates and saves in the txt file for future processing,
        Please follow the order: Bottom Left, Top Left, Bottom Right and Top right

        Args:
            image_name ([str]): [Processing file name ]
        """
        print("Please follow the order: Bottom Left, Top Left, Bottom Right and Top right")
        image_path = f"images/{image_name}.jpg"

        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                print(f"{x,y}")
                self.coords.append([x,y])
                if len(self.coords) == 2:
                    cv2.line(img,(self.coords[0][0], self.coords[0][1]),(self.coords[1][0], self.coords[1][1]),(255,255,255),3)
                if len(self.coords) == 3:
                    cv2.line(img,(self.coords[1][0], self.coords[1][1]),(self.coords[2][0], self.coords[2][1]),(255,255,255),3)
                if len(self.coords) == 4:
                    cv2.line(img,(self.coords[2][0], self.coords[2][1]),(self.coords[3][0], self.coords[3][1]),(255,255,255),3)
                    cv2.line(img,(self.coords[0][0], self.coords[0][1]),(self.coords[3][0], self.coords[3][1]),(255,255,255),3)
                font = cv2.FONT_HERSHEY_SIMPLEX
                strXY = str(x)+", "+str(y)
                cv2.putText(img, strXY, (x,y), font, 0.7, (255,255,0), 2)
                cv2.imshow("image", img)

        img = cv2.imread(image_path)
        print(img.shape)
        while(1):
            cv2.imshow("image", img)
            cv2.setMouseCallback('image',click_event)
            k = cv2.waitKey(20) & 0xFF
            if (k == 27)  or (len(self.coords) > 4):
                print(self.coords)
                break
        try: 
            os.mkdir("data") 
        except OSError as error: 
            print("\n")

        txt_file = open(f"data/{self.filename}.txt","a")
        t = datetime.datetime.now()
        txt_file.write(f"\n\n{t}\n")
        txt_file.write("Line coordinates:"+str(self.coords)+"\n")
        txt_file.close()
        print("Text file created")








     
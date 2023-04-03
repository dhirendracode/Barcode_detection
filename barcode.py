# Import necessary libraries

from pyzbar.pyzbar import decode
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def barcode_items_scan(Image_path):
    image_1=cv2.imread(Image_path)
    image_2=cv2.imread(Image_path)
    image_3=cv2.imread(Image_path)
    image_4=cv2.imread(Image_path)
    image_5=cv2.imread(Image_path) # creating instances of image to provide separate output.
    cv2.imwrite("Input_ Image.png",image_1) # shows input image.
    data_list=[]
    for obdecode in decode(image_1):
        data_list.append(obdecode.data)
    barcode_rep={bar:data_list.count(bar) for bar in data_list}
    for (key,values) in barcode_rep.items():
        print("The barcode/QR-code ID",key,"is detected",values,"times") # Shows repetation of barcode/QR-code.
    all_cord=[]
    for decod_img in decode(image_1):
        cord_list=[p for p in decod_img.rect]
        all_cord.append(cord_list)
    for cord in range(len(all_cord)):
        x_1=all_cord[cord][0]
        y_1=all_cord[cord][1]
        w_1=all_cord[cord][2]
        h_1=all_cord[cord][3]
        img=cv2.rectangle(image_1,(x_1,y_1),(x_1+w_1,y_1+h_1),(255,0,0),10)
        cv2.imwrite("barcode_detect.png",img) # Shows image of barcode detection
    gray = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((2,2),np.uint8)
    thresh = cv2.dilate(thresh,kernel,iterations = 18)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    thresh = cv2.erode(thresh,None,iterations =12)
    thresh = cv2.dilate(thresh,None,iterations=7)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        x_2,y_2,w_2,h_2 = cv2.boundingRect(cont)
        img_1 = cv2.rectangle(image_2,(x_2,y_2),(x_2+w_2,y_2+h_2),(0,0,0),8)
        cv2.imwrite("items_detected.png",img_1) # Shows barcode of item detection
        for ann in all_cord:
            count = 0
            x_1=ann[0]
            y_1=ann[1]
            w_1=ann[2]
            h_1=ann[3]
            c1=(x_1+(w_1/2),y_1+(h_1)/2) # Calculation of corner points of bounding box
            c2=(x_1+(w_1/2),y_1-(h_1)/2)
            c3=(x_1-(w_1/2),y_1+(h_1)/2)
            c4=(x_1-(w_1/2),y_1-(h_1)/2)  
            if (x_2-(w_2/2)) < c1[0]  and (x_2+(w_2/2)) > c1[0] and (y_2-(h_2/2)) < c1[1] and (y_2+(h_2/2)) > c1[1]:
                count += 1
            if (x_2-(w_2/2)) < c2[0]  and (x_2+(w_2/2)) > c2[0] and (y_2-(h_2/2)) < c2[1] and (y_2+(h_2/2)) > c2[1]:
                count += 1
            if (x_2-(w_2/2)) < c3[0]  and (x_2+(w_2/2)) > c3[0] and (y_2-(h_2/2)) < c3[1] and (y_2+(h_2/2)) > c3[1]:
                count += 1
            if (x_2-(w_2/2)) < c4[0]  and (x_2+(w_2/2)) > c4[0] and (y_2-(h_2/2)) < c4[1] and (y_2+(h_2/2)) > c4[1]:
                count += 1
        
                
            if count ==0:
                img_2 = cv2.rectangle(image_3,(x_2,y_2),(x_2+w_2,y_2+h_2),(0,0,255),8)
                # cv2.imwrite("items_with_no_barcode.png",img_2)
                break
            elif count < 4:
                img_3 = cv2.rectangle(image_4,(x_2,y_2),(x_2+w_2,y_2+h_2),(0,255,255),8)
                cv2.imwrite('partial_detect.png',img_3)
                break
            else:
                img_4 = cv2.rectangle(image_5,(x_2,y_2),(x_2+w_2,y_2+h_2),(0,0,0),8)
                cv2.imwrite('only_items.png',img_4)
                break
            
barcode_items_scan("/home/dhirendra/Downloads/all_barcode-20230331T074017Z-001/all_barcode/IMG_20220303_175324.jpg") # Testing Image



    
        
    
    
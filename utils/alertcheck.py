import cv2
from playsound import playsound
import pandas as pd
from scipy.spatial import distance

#crossed=0

def drawboxtosafeline(image_np,p1,p2,Line_Position2,Orientation, im_width, im_height):
    distance_from_line  = 0
    #global crossed
    print (p1, p2, Line_Position2[0], Line_Position2[1])
    sap1 = Line_Position2[0]
    sap2 = Line_Position2[1]
    if (p1[0]> sap1[0] and p1[0] > sap2[0] and p2[0] > sap1[0] and p2[0] > sap2[0]):
        distance_from_line = 1
    elif (p1[0] < sap1[0] and p1[0] < sap2[0] and p2[0] < sap1[0] and p2[0] < sap2[0]):
        distance_from_line = 1
    else:
        distance_from_line = 0
    if distance_from_line > 0:
        l1 = []
        mid1= p1
        mid2 = p2
        com_mid_1 = Line_Position2[0]
        com_mid_2 = Line_Position2[1]
        print(type(mid1))
        print(type(com_mid_1))
        line1 = distance.euclidean(mid1, com_mid_1)
        line2 = distance.euclidean(mid1, com_mid_2)
        line3 = distance.euclidean(mid2, com_mid_1)
        line4 = distance.euclidean(mid2, com_mid_2)
        l1.append(line1)
        l1.append(line2)
        l1.append(line3)
        l1.append(line4)
        print(l1)
        refObj = distance.euclidean(sap1, sap2)/21
        if(min(l1) == line1):
            cv2.line(img=image_np, pt1=mid1, pt2=(com_mid_1[0], mid1[1]), color=(255, 0, 0), thickness=5, lineType=8,
                 shift=0)
            distance_from_line = line1/refObj
        elif(min(l1) == line2):
            cv2.line(img=image_np, pt1=mid1, pt2=(com_mid_2[0], mid1[1]), color=(255, 0, 0), thickness=5, lineType=8,
                     shift=0)
            distance_from_line = line2/refObj
        elif (min(l1) == line3):
            cv2.line(img=image_np, pt1=mid2, pt2=(com_mid_1[0], mid2[1]), color=(255, 0, 0), thickness=5, lineType=8,
                     shift=0)
            distance_from_line = line3/refObj
        elif (min(l1) == line4):
            cv2.line(img=image_np, pt1=mid2, pt2=(com_mid_2[0], mid2[1]), color=(255, 0, 0), thickness=5, lineType=8,shift=0)
            distance_from_line = line4/refObj
    color = (52, 235, 183)
    cv2.putText(image_np, 'distance from camera: ' + str("{0:.2f}".format(distance_from_line) + ' inches'),
                (int(im_width * 0.65), int(im_height * 0.9)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 2)
    if (distance_from_line <  10) :
            
             #crossed+=1
        posii=int(image_np.shape[1]/2)
        cv2.putText(image_np, "ALERT", (posii, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0,0), 2)
        cv2.putText(image_np, str(distance_from_line), (posii-100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)
			 #sound = os.path.join()

        cv2.rectangle(image_np, (posii-20,20), (posii+85,60), (255,0,0), thickness=3, lineType=8, shift=0)
             #to write into xl-sheet            
        return 1
    else:
        return 0
    
   



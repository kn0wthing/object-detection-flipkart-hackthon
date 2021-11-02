#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:14:52 2019

@author: subodh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 12:44:16 2019

@author: subodh
"""

# python deep_learning_object_detection.py --image images/example_01.jpg --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel
import pandas as pd
import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt 

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    #ap.add_argument("-i", "--image", required=True,
    #            help="path to input image")
    ap.add_argument("-p", "--prototxt", required=True,
                help="path to Caffe 'deploy' prototxt file")
    ap.add_argument("-m", "--model", required=True,
                help="path to Caffe pre-trained model")
    ap.add_argument("-c", "--con", type=float, default=0.2,
                help="minimum probability to filter weak detections")
    args = vars(ap.parse_args())

COLORS = np.random.uniform(0, 255, size=(150, 3))
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
#net = cv2.dnn.readNetFromCaffe(MobileNetSSD_deploy.prototxt.txt, MobileNetSSD_deploy.caffemodel)
listt = []
df = pd.read_csv("t.csv")

data = pd.DataFrame()
data['format'] = df['image_name']
for i in range(data.shape[0]):
    data['format'][i] = 'images/' + data['format'][i]
for j in range(100):
    image = cv2.imread(data['format'][j])
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    
    net.setInput(blob)
    detections = net.forward()
    for i in np.arange(0, detections.shape[2]):
        con = detections[0, 0, i, 2]
        if con > args["con"]:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            if(i == 1):
                listt.append(j)
                break
            df['x1'][j] = startX
            df['y2'][j] = endY
            df['x2'][j] = endX
            df['y1'][j] = startY
            #cv2.rectangle(image, (startX, startY), (endX, endY),COLORS[idx], 2)
        #cv2.imwrite("Output.jpg", image)
        #cv2.waitKey(0)
#plt.imshow(image)
#plt.show()
#cv2.waitKey(0)
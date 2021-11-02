#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:02:50 2019

@author: subodh
"""
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
def get_bbox_labels(imagefile):
    imagefile = imagefile.split('.')[0]
    xmlfile ='/home/subodh/ESRI DATA/training_data' +'/'+ 'labels'+ '/'+ imagefile+ '.xml'
    # print(xmlfile)
    tree = ET.parse(xmlfile)
    xmlroot = tree.getroot()

    bboxes  = []
    classes = []
    for child in xmlroot:
        if child.tag == 'object':
            xmin, ymin, xmax, ymax = float(child[1][0].text),float(child[1][1].text), float(child[1][2].text),float(child[1][3].text)
            bboxes.append([imagefile,xmin, ymin, xmax, ymax,child[0].text])
            #bboxes.append([ymin, xmin, ymax, xmax])
            #classes.append(child[0].text)
    return bboxes

lst = []
lstt = []
for i in range(3748):
    if(i<10):
        a = '00000000'+str(i)+'.jpg'
        lstt.append(a)
    elif(10<=i<100):
        a = '0000000'+str(i)+'.jpg'
        lstt.append(a)
    elif(100<=i<1000):
        a = '000000'+str(i)+'.jpg'
        lstt.append(a)
    else:
        a = '00000'+str(i)+'.jpg'
        lstt.append(a)
columns = ['image','xmin','ymin','xmax','ymax','class']
df = pd.DataFrame(columns=columns)
for i in range(len(lstt)):
    lst = get_bbox_labels(str(lstt[i]))
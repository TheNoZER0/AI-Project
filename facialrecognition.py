from deepface import DeepFace
import cv2
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

dfs = DeepFace.find(img_path = "img1.jpg", db_path = "C:\Users\hyper\Documents\AI Project\Database")
objs = DeepFace.analyze(img_path = "img4.jpg", 
        actions = ['age', 'gender', 'race', 'emotion']
)

def initiatecamera():
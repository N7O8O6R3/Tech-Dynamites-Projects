import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep
import shelve


def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}
    shelf_train_data = shelve.open('trainingData.yml','w')
    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                print(f)
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                #train_data.write(str(encoding))
                #print(encoding)
                #print(f.split(".")[0])
                shelf_train_data[f.split(".")[0]] = encoding
	
                #print(encoded)

    #print("--->",encoded)
    #train_data.write(str(encoded)) 
    
    shelf_train_data.close()
    #return encoded
    
get_encoded_faces()

#Created by : Noor Hasan Shaik

This code is recognize the multiple faces from a picture and mark them attendance

To run this 

    pip3 install cmake
    pip3 install dlib
    pip3 install face_recognition
    pip3 install numpy
    pip3 install opencv-python
    pip3 install shelve
    pip3 install openpyxl

First train your faces. Put all the faces that you want to train in faces folder.

    Run python train_face.py.

Next put tha image that you want to test and rename it as test.jpg

    Now run python face_rec.py

It will recognize all the faces in picture and mark attendance in attendance.xlsx file.

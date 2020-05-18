from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import face_recognition
import cv2
import sys
import numpy as np
from os import path
import pickle



def index(request):
    _name= request.GET.get('action')
    _path= request.GET.get('path')
    if(_name=="train"):
        if(path.exists("encodings.enc")==False):
            f_en=[]
            f_ls=[]
            with open("encodings.enc","wb") as fl:
                pickle.dump(f_en,fl)
            fl.close()
            with open("facelist.enc","wb") as fl:
                pickle.dump(f_ls,fl)
            fl.close()

        image_path= _path+".jpeg"

        face= face_recognition.load_image_file(image_path)
        face_enc= face_recognition.face_encodings(face)[0]
        face_label= _path

        fl= open("encodings.enc","rb")
        known_face_encodings= pickle.load(fl)
        fl.close()

        fl= open("encodings.enc","wb")
        known_face_encodings.append(face_enc)
        pickle.dump(known_face_encodings,fl)
        fl.close()

        fl= open("facelist.enc","rb")
        known_face_list= pickle.load(fl)
        fl.close()

        fl= open("facelist.enc","wb")
        known_face_list.append(face_label)
        pickle.dump(known_face_list,fl)
        fl.close()
        return JsonResponse("name:{}".format(_name),safe=False)

    if(_name=="test"):
        fl=open("encodings.enc","rb")
        known_face_encodings= pickle.load(fl)
        fl.close()

        fl= open("facelist.enc","rb")
        known_face_names= pickle.load(fl)
        fl.close()
        
        frame= cv2.imread(_path+".jpeg")

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names=[]
        resp={}
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                face_names.append(name)
            resp["name"]=face_names
        return JsonResponse(resp,safe=False)


    
# Create your views here.

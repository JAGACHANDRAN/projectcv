import cv2
import mediapipe as mp
import os
hand_detct=mp.solutions.hands.Hands()
draw_utits=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    f_h,f_w,c=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detct.process(rgb_frame)
    hands=output.multi_hand_landmarks
    #print(hands)
    f=[]
    l=[]
    if hands:
        for hand in hands:
            draw_utits.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*f_w)
                y=int(landmark.y*f_h)
                l.append([id,x,y])
                #print(x,y)
    if len(l)!=0:
        if l[8][2]<l[6][2]:
            f.append(1)
        else:
            f.append(0)
        if l[12][2] < l[10][2]:
            f.append(1)
        else:
            f.append(0)
        if l[16][2] < l[14][2]:
            f.append(1)
        else:
            f.append(0)
        if l[20][2] < l[18][2]:
            f.append(1)
        else:
            f.append(0)
        if l[4][1] > l[3][1]:
            f.append(1)
        else:
            f.append(0)
    s=sum(f)
    if s==1:
        os.system('shutdown/s /t 10')


    cv2.imshow('frame',frame)
    cv2.waitKey(1)
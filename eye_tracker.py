import cv2
import numpy as np
import dlib

vid = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()

face_feature_finder = dlib.shape_predictor("face_landmarks.dat")

#draws the eye coolly
def draw_eye_cool():
    #around
    eye_points = np.array([(landmarks.part(36).x, landmarks.part(36).y),
                            (landmarks.part(37).x, landmarks.part(37).y),
                            (landmarks.part(38).x, landmarks.part(38).y),
                            (landmarks.part(39).x, landmarks.part(39).y),
                            (landmarks.part(40).x, landmarks.part(40).y),
                            (landmarks.part(41).x, landmarks.part(41).y)
                            ], np.int32)

    cv2.polylines(frm, [eye_points], True, (255,0,0), 1)
    

    #cross section
    cv2.line(frm, (landmarks.part(36).x, landmarks.part(36).y), (landmarks.part(39).x, landmarks.part(39).y), (256,0,0),1)
    cv2.line(frm, (landmarks.part(37).x, landmarks.part(37).y), (landmarks.part(40).x, landmarks.part(40).y), (256,0,0),1)
    cv2.line(frm, (landmarks.part(38).x, landmarks.part(38).y), (landmarks.part(41).x, landmarks.part(41).y), (256,0,0),1)
while True:
    _, frm = vid.read()

    grscl = cv2.cvtColor(frm,cv2.COLOR_BGR2GRAY)


    face_array = detector(grscl)
    
    for face in face_array:
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(frm, (left, top), (right, bottom), (0,0,255),2)

        landmarks = face_feature_finder(grscl, face)

        draw_eye_cool()
    
    cv2.imshow("Frame",frm)
    

    key = cv2.waitKey(1)

    if key == 27:
        break

vid.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
import dlib

vid = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()

face_feature_finder = dlib.shape_predictor("face_landmarks.dat")


while True:
    _, frm = vid.read()
    _, frm_clean = vid.read()

    grscl = cv2.cvtColor(frm,cv2.COLOR_BGR2GRAY)


    face_array = detector(grscl)
    
    for face in face_array:
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(frm, (left, top), (right, bottom), (0,0,255),2)

        landmarks = face_feature_finder(grscl, face)

        eye_points = np.array([(landmarks.part(36).x, landmarks.part(36).y),
                            (landmarks.part(37).x, landmarks.part(37).y),
                            (landmarks.part(38).x, landmarks.part(38).y),
                            (landmarks.part(39).x, landmarks.part(39).y),
                            (landmarks.part(40).x, landmarks.part(40).y),
                            (landmarks.part(41).x, landmarks.part(41).y)
                            ], np.int32)

        cv2.polylines(frm, [eye_points], True, (255,0,0), 1)
        cv2.line(frm, (landmarks.part(36).x, landmarks.part(36).y), (landmarks.part(39).x, landmarks.part(39).y), (0,0,255),1)
        cv2.line(frm, (landmarks.part(37).x, landmarks.part(37).y), (landmarks.part(40).x, landmarks.part(40).y), (0,0,255),1)
        cv2.line(frm, (landmarks.part(38).x, landmarks.part(38).y), (landmarks.part(41).x, landmarks.part(41).y), (0,0,255),1)

        eye_x_min = np.min(eye_points[:,0])
        eye_x_max = np.max(eye_points[:,0])
        eye_y_min = np.min(eye_points[:,1])
        eye_y_max = np.max(eye_points[:,1])

        eye_frm = frm_clean[eye_y_min:eye_y_max, eye_x_min:eye_x_max]
        eye = cv2.resize(eye_frm, None, fx = 8, fy = 8)

        eye_grscl = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
        _, eye_threshold = cv2.threshold(eye_grscl, 65, 255, cv2.THRESH_BINARY)

        eye_height, eye_width = eye_threshold.shape

        #left and right switched
        eye_right_bound = eye_threshold[0:eye_height, eye_width//6:eye_width//2]
        eye_left_bound = eye_threshold[0:eye_height, 2*eye_width//3:eye_width]

        eye_r_dark = cv2.countNonZero(eye_right_bound)
        eye_l_dark = cv2.countNonZero(eye_left_bound)
        
        eye_dark_ratio = 0
        if eye_l_dark != 0:
            eye_dark_ratio = eye_r_dark/eye_l_dark
        else:
            eye_dark_ratio = 1.5

        cv2.putText(frm, str(eye_r_dark), (64, 128),1,2,(0,255,0),2)
        cv2.putText(frm, str(eye_l_dark), (64, 192),1,2,(0,255,0),2)

        if (eye_dark_ratio > 0 and eye_dark_ratio < 1) or eye_r_dark == 0:
            cv2.putText(frm, "RIGHT", (128, 128),1,2,(0,255,0),2)
        elif eye_l_dark == 0 or eye_dark_ratio > 1:
            cv2.putText(frm, "LEFT", (128, 192),1,2,(0,255,0),2)

        cv2.imshow("Left", eye_left_bound)
        cv2.imshow("Right", eye_right_bound)
        cv2.imshow("Threshold", eye_threshold)
        cv2.imshow("Eye",eye)

    
    cv2.imshow("Frame",frm)
    

    key = cv2.waitKey(1)

    if key == 27:
        break

vid.release()
cv2.destroyAllWindows()
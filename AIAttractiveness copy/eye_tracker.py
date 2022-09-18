#used for video capture and marking
import cv2

#used in arrays
import numpy as np

#used to locate faces and features
import dlib

import time

    
def track_eye(direction, results):

    vid = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()

    face_feature_finder = dlib.shape_predictor("face_landmarks.dat")

    time_end = time.time() + 10

    while time.time() < time_end:
        _, frm = vid.read()
        _, frm_clean = vid.read()

        grscl = cv2.cvtColor(frm,cv2.COLOR_BGR2GRAY)


        #detects all faces in video
        face_array = detector(grscl)
        
        #locates eye and performs gaze analysis for each fact in face_array
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
            eye_left_bound = eye_threshold[0:eye_height, eye_width//6:int(eye_width/2.25)]
            eye_right_bound = eye_threshold[0:eye_height, int(eye_width/2):eye_width]

            eye_l_dark = cv2.countNonZero(eye_left_bound)
            eye_r_dark = cv2.countNonZero(eye_right_bound)

            cv2.putText(frm, str(eye_r_dark), (64, 128),1,2,(0,255,0),2)
            cv2.putText(frm, str(eye_l_dark), (64, 192),1,2,(0,255,0),2)

            if eye_l_dark == 0 and eye_r_dark == 0:
                CLOSER = "Get closer/ensure eyes are visible."
                cv2.putText(frm, CLOSER, (32, 256),1,2,(0,255,0),2)
            
            if eye_r_dark > eye_l_dark + int(eye_width/1.25):
                cv2.putText(frm, "RIGHT", (192, 128),1,2,(0,255,0),2)
                direction = True
                results.append(direction)
            else:
                cv2.putText(frm, "LEFT", (192, 192),1,2,(0,255,0),2)
                direction = False
                results.append(direction)

            #used to display the eyes and bounds

            # cv2.imshow("Left", eye_left_bound)
            # cv2.imshow("Right", eye_right_bound)
            # cv2.imshow("Threshold", eye_threshold)
            # cv2.imshow("Eye",eye)
        
        if len(face_array) == 0:
                CLOSER = "Get closer/ensure face is visible."
                cv2.putText(frm, CLOSER, (32, 256),1,2,(0,255,0),2)

        cv2.imshow("Frame",frm)
        #print(direction)
        

        key = cv2.waitKey(1)

        if key == 27:
            break

    vid.release()

    cv2.destroyAllWindows()
    return results


# direction = False
# results = []
# track_eye(direction, results)
# right = 0
# left = 0
# for dir in results:
#     if dir:
#         right += 1
#     else:
#         left += 1
# print(right,left)
import cv2
import mediapipe as mp
import numpy as np

pose = None
mp_pose = None
mp_drawing = None

def initMarkerTracking():
    global pose, mp_pose, mp_drawing
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_drawing = mp.solutions.drawing_utils

def getMarkers(frame, showBodyMarkers, showAnonymization):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for pose detection
    results = pose.process(frame_rgb)

    # Draw the pose annotations on the frame
    if results.pose_landmarks and showBodyMarkers:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    if showAnonymization:
        left_eye = getMarkerPosition(results.pose_landmarks, 2)
        right_eye = getMarkerPosition(results.pose_landmarks, 5)
        nose = getMarkerPosition(results.pose_landmarks, 0)
        x1 = int(left_eye[0] * frame.shape[1])
        x2 = int(right_eye[0] * frame.shape[1])
        y1 = int(left_eye[1] * frame.shape[0])
        y2 = int(right_eye[1] * frame.shape[0])
        z =  int(nose[1] * frame.shape[0])
        width = int(np.abs(x2-x1) * 2)
        height = int(np.abs(y1-z)) * 2
        top_left = (int(x1+width*0.5), int(y1-height*1.5))
        bottom_right = (int(x2 - width*0.5), int(y2 + height*1.5))

        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 0), -1)


    return frame, results.pose_landmarks

def getMarkerPosition(markerList, markerID):
    # MarkerIDs:
    # NOSE = 0
    # LEFT_EYE_INNER = 1
    # LEFT_EYE = 2
    # LEFT_EYE_OUTER = 3
    # RIGHT_EYE_INNER = 4
    # RIGHT_EYE = 5
    # RIGHT_EYE_OUTER = 6
    # LEFT_EAR = 7
    # RIGHT_EAR = 8
    # MOUTH_LEFT = 9
    # MOUTH_RIGHT = 10
    # LEFT_SHOULDER = 11
    # RIGHT_SHOULDER = 12
    # LEFT_ELBOW = 13
    # RIGHT_ELBOW = 14
    # LEFT_WRIST = 15
    # RIGHT_WRIST = 16
    # LEFT_PINKY = 17
    # RIGHT_PINKY = 18
    # LEFT_INDEX = 19
    # RIGHT_INDEX = 20
    # LEFT_THUMB = 21
    # RIGHT_THUMB = 22
    # LEFT_HIP = 23
    # RIGHT_HIP = 24
    # LEFT_KNEE = 25
    # RIGHT_KNEE = 26
    # LEFT_ANKLE = 27
    # RIGHT_ANKLE = 28
    # LEFT_HEEL = 29
    # RIGHT_HEEL = 30
    # LEFT_FOOT_INDEX = 31
    # RIGHT_FOOT_INDEX = 32

    if markerList != None:
        marker = markerList.landmark[markerID]
        return marker.x, marker.y
    else:
        return -1, -1

def displayWebcam(frame):
    mirrored_frame = cv2.flip(frame, 1)
    cv2.imshow('Webcam Feed', mirrored_frame)


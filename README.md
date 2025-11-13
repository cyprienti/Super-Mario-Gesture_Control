# Super-Mario-Gesture-Control
This project extends a Super Mario Python game by adding gesture-based control using OpenCV and MediaPipe.Instead of controlling Mario only with the keyboard, players can move and jump using head, hand, or foot movements, depending on their assigned body parts.

# Features

  -  Control Mario using your body, not just the keyboard.
  -  Real-time pose estimation using MediaPipe Holistic / Pose / Hands.
  -  Integration with the game’s action system:

    post_action(Action.LEFT) → Move left

    post_action(Action.RIGHT) → Move right

    post_action(Action.JUMP) → Jump

    (and corresponding *_STOP commands)

  -  Optional face anonymization (black bar) and marker visualization toggle for privacy.
  -  Adjustable to use head, hands, or feet for input based on your assignment.

# Implementation Tasks
     custom_input_thread() — in body_tracking_task.py
Access the webcam stream using OpenCV.
    For each frame:
      Pass the frame to       getMarkerListAndShowMarkers().

Receive the processed frame and the list of detected markers.

Send the marker     list to custom_input_loop()     for control logic.

Display the frame in the game window using     displayWebcam(frame, markerList).

     getMarkerListAndShowMarkers() — in body_tracking_task.py

  Input: A single webcam frame and a boolean to decide whether to draw markers.

Detect and return a list of body landmarks (NormalizedLandmarkList) using MediaPipe.

If visualization is enabled, draw the landmarks on the frame.

  Output: (frame_with_markers, marker_list)

     custom_input_loop() — in custom_input_task.py

Input: A list of MediaPipe landmarks (markerList).

Use marker coordinates to determine the player’s movements and gestures.

Map the detected gestures to Mario’s actions:

    post_action(Action.LEFT)
    post_action(Action.RIGHT)
    post_action(Action.JUMP)
    post_action(Action.LEFT_STOP)
    post_action(Action.RIGHT_STOP)
    post_action(Action.JUMP_STOP)

# How to Run

Create a virtual environment and activate it:

    python -m venv venv
    source venv/bin/activate      # on macOS/Linux
    venv\Scripts\activate         # on Windows

Install dependencies:

    pip install -r requirements.txt

Run the main script:

    python main.py

The Super Mario window opens — press Enter to start.

Control Mario using your assigned body parts (head, hands, or feet).

# Restrictions
  -  You must implement your own logic using MediaPipe landmarks.
  -  Do not use pre-built or automated gesture-recognition libraries.
  -  Only OpenCV and MediaPipe may be used for tracking and visualization.

# Learning Objectives
  -  Understand pose estimation and gesture recognition using MediaPipe.
  -  Integrate real-time computer vision input into an interactive game.
  -  Map human motion to game controls.
  -  Apply modular programming and real-time event handling

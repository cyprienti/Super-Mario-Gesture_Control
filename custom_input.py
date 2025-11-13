from time import sleep

from game_files.custom_actions import post_action, Action
from body_tracking import *

showBodyMarkers = True
showAnonymization = False

# Main Loop of the custom input detection <- Implement this Function
def custom_input_loop(markerList):
    import Action
    import getMarkerPosition

    def custom_input_loop(markerList):
        # Example: Using the wrist positions to control Mario
        left_wrist_x, left_wrist_y = getMarkerPosition(markerList, 15)
        right_wrist_x, right_wrist_y = getMarkerPosition(markerList, 16)

        # Define thresholds for movement
        left_threshold = 0.3
        right_threshold = 0.7
        jump_threshold = 0.5
        shoot_threshold = 0.2

        # Move left if left wrist is left of the threshold
        if left_wrist_x < left_threshold:
            post_action(Action.LEFT)
        else:
            post_action(Action.LEFT_STOP)

        # Move right if right wrist is right of the threshold
        if right_wrist_x > right_threshold:
            post_action(Action.RIGHT)
        else:
            post_action(Action.RIGHT_STOP)

        # Jump if left wrist is above the threshold
        if left_wrist_y < jump_threshold:
            post_action(Action.JUMP)
        else:
            post_action(Action.JUMP_STOP)

        # Shoot if right wrist is below the threshold
        if right_wrist_y > shoot_threshold:
            post_action(Action.SHOOT)
        else:
            post_action(Action.SHOOT_STOP)

    ##ToDO: Implementieren Sie die Steuerung von Mario. Als Input erhält diese Funktion die markerList.
    ## Es gibt 33 verschiedene Marker, die das System tracken kann. Eine Übersicht aller Marker und
    ## ihre entsprechende IDs können Sie im body_tracking.py Skript in der Methode getMarkerPosition() einsehen.
    ## Die X und Y Koordinate erhalten Sie mittels der entsprechenden ID und der gennannten Methode
    ## getMarkerPosition(). Die Koordinaten der Nase erhalten Sie zum Beispiel folgendermaßen:
    ## markerX, markerY = getMarkerPosition(markerList, 0)
    ## Basierend auf den Bewegungen Ihrer Körperteile bzw. der Koordinaten der Marker soll nun Mario gesteuert werden.
    ## Sie müssen also die Bewegungen bzw die Veränderung der Marker Koordinaten auf die entsprechenden
    ## Befehle an Mario mappen. Mario soll nach links und rechts laufen sowie springen können. Schießen ist optional.
    ## Mario kann über die folgenden Befehle gesteuert werden:
    ## post_action(Action.LEFT) --> Nach Links Laufen
    ## post_action(Action.LEFT_STOP) --> Nicht mehr nach Links Laufen
    ## post_action(Action.RIGHT) --> Nach Rechts Laufen
    ## post_action(Action.RIGHT_STOP) --> Nicht mehr nach Rechts Laufen
    ## post_action(Action.JUMP) --> Springen
    ## post_action(Action.JUMP_STOP) --> Nicht mehr Springen
    ## post_action(Action.JUMP) --> Springen
    ## post_action(Action.JUMP_STOP) --> Nicht mehr Springen
    ## post_action(Action.SHOOT) --> Schießen
    ## post_action(Action.SHOOT_STOP) --> Nicht mehr Schießen

    # REPLACE WITH ACTUAL IMPLEMENTATION
    x, y = getMarkerPosition(markerList, 0)




# Thread function of the custom input detection
def custom_input_thread(stop_event):
    # Initialize Marker Tracking
    initMarkerTracking()

    # Initialize the webcam (0 is the default camera)
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while not stop_event.is_set():
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, ret is True
        if not ret:
            break

        # Get body markers and visualize them if you want to
        frame, markerList = getMarkers(frame, showBodyMarkers, showAnonymization)

        # Process the markerList as input
        custom_input_loop(markerList)

        displayWebcam(frame)

        # Break the loop with the 'ESC' or 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close any open windows
    cap.release()
    cv2.destroyAllWindows()

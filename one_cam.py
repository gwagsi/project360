import cv2

def open_camera_direct_show(camera_index):
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_index} using DirectShow.")
        return None
    else:
        return cap


def main():
    camera_index = 0  # Adjust this if you have multiple cameras

    # Open the camera using DirectShow
    cap = open_camera_direct_show(camera_index)

    if cap is None:
        return
    
    # Set your desired frame width and height
    frame_width = 640
    frame_height = 480

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('DirectShow Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

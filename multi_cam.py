import cv2

def list_available_cameras():
    index = 0
    available_cameras = []

    while True:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)  # Use DirectShow for Windows
        if not cap.read()[0]:
            break
        else:
            available_cameras.append(index)
        cap.release()
        index += 1

    return available_cameras

def display_camera_feed(camera_index, frame_width=640, frame_height=480):
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_index} using DirectShow.")
        return

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
    available_cameras = list_available_cameras()

    if not available_cameras:
        print("No cameras available.")
    else:
        print("Available cameras:")
        for i, index in enumerate(available_cameras):
            print(f"{i+1}. Camera {index}")

        while True:
            try:
                choice = int(input("Enter the number of the camera you want to use: ")) - 1  
                if 0 <= choice < len(available_cameras):
                    display_camera_feed(available_cameras[choice])
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

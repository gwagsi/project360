import threading
import cv2
import queue

frame_queue = queue.Queue()

def list_available_cameras():
    index = 0
    available_cameras = []

    while True:
        cap = cv2.VideoCapture(index)  # Use DirectShow for Windows
        if not cap.read()[0]:
            break
        else:
            available_cameras.append(index)
        cap.release()
        index += 1

    return available_cameras
def capture_from_multiple_cameras(camera_indices, frame_width=640, frame_height=480):
    caps = [cv2.VideoCapture(index, cv2.CAP_DSHOW) for index in camera_indices]

    for cap in caps:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    while True:
        frames = []
        for cap in caps:
            grabbed, frame = cap.read()  # Grab frame (non-blocking)
            if grabbed:
                frames.append(frame)

        if not frames:  # Check if any frames were captured
            break

        # Combine frames horizontally (adjust as needed)
        combined_frame = np.hstack(frames)

        cv2.imshow("Combined Camera Feed", combined_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for cap in caps:
        cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    available_cameras = list_available_cameras() # Function to list available cameras (same as before)

    if not available_cameras:
        print("No cameras available.")
    else:
        # Example: Capture from the first two available cameras
        capture_from_multiple_cameras(available_cameras[:2]) 
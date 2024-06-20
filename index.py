import subprocess
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
def display_camera_feed_ffplay(camera_index, resolution="1280x720", framerate=30, pixel_format="yuyv422"):
    cmd = [
        "ffplay",  # Use ffplay for real-time display
        "-f", "avfoundation",
        "-video_size", resolution,
        "-pixel_format", pixel_format,  # Set pixel format if needed
        "-framerate", str(framerate),  # Set capture frame rate
        "-i", str(camera_index)  # Input from the specified camera
    ]

    # Start the ffplay process
    subprocess.Popen(cmd)
    
def main():
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
                    display_camera_feed_ffplay(available_cameras[choice])
                    input("Press Enter to stop ffplay and select another camera...\n")
                    break  # Exit loop after displaying one camera
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
if __name__ == '__main__':
    main()
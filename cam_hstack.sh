#!/bin/bash

# Camera Input Devices (Check with "ffmpeg -f avfoundation -list_devices true -i ''")
input1="1"  # Example: First camera might be "0"
input2="2"  # Example: Second camera might be "1"
 
# Output Formatted File Name
output_prefix="camera_hstack_%05d.jpg"
output_file="outputew.mp4"
# Frame Rate
framerate=30 

# Output RTMP Stream URL
rtmp_url="rtmp://34.133.131.240:1935/stream3" 
# Optional: Set video resolution
width=1280
height=720

# ffmpeg command to record and stack
ffmpeg \
    -f avfoundation -framerate "$framerate" -i "$input1" \
    -f avfoundation -framerate "$framerate" -i "$input2" \
    -filter_complex "[0:v][1:v]hstack=inputs=2,format=yuv420p[stacked]; \
                     [stacked]v360=input=dfisheye:ih_fov=180:iv_fov=180:output=equirect[out]" \
    -map "[out]" -c:v libx264 -f flv "$rtmp_url"
    
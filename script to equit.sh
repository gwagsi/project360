#!/bin/bash

# Camera Input Devices (Check with "ffmpeg -f avfoundation -list_devices true -i ''")
input1="0"  # Example: First camera might be "0"
input2="1"  # Example: Second camera might be "1"
 
# Output Formatted File Name
output_prefix="camera_hstack_%05d.jpg"

# Frame Rate
framerate=30 

# Optional: Set video resolution
width=1280
height=720

# ffmpeg command to record and stack
ffmpeg \
    -f avfoundation -framerate "$framerate" -video_size "${width}x${height}" -i "$input1" \
    -f avfoundation -framerate "$framerate" -video_size "${width}x${height}" -i "$input2" \
    -filter_complex "[0:v][1:v]hstack=inputs=2" \
    -update 1 "$output_prefix" \
    -loglevel error  # Hide ffmpeg output messages except errors

#!/bin/bash

# Camera Input Devices
input1="0"  # Update with your camera's ID
input2="1"  # Update with your camera's ID

output_prefix="camera_hstack_%05d.jpg"

# Automatic Pixel Format Selection
pix_fmt1="" # Leave empty to let ffmpeg automatically select based on the camera
pix_fmt2=""

# Find Supported Modes and Resolutions
ffmpeg -f avfoundation -list_devices true -i ""

# Ask the user to choose a resolution and framerate from the supported modes
echo "Select a resolution and framerate:"
read -p "Enter the desired mode (e.g., '1280x720@30'): " chosen_mode

# Parse the chosen mode
IFS='x@' read -ra mode_parts <<< "$chosen_mode"
width="${mode_parts[0]}"
height="${mode_parts[1]}"
framerate="${mode_parts[2]}"

# ffmpeg command to record and stack
ffmpeg \
    -f avfoundation -framerate "$framerate" -video_size "${width}x${height}" -pix_fmt "$pix_fmt1" -i "$input1" \
    -f avfoundation -framerate "$framerate" -video_size "${width}x${height}" -pix_fmt "$pix_fmt2" -i "$input2" \
    -filter_complex "[0:v][1:v]hstack=inputs=2" \
    -update 1 "$output_prefix" \
    -loglevel error  # Hide ffmpeg output messages except errors

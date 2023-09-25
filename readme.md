# Realtime Video Processing

## Description

This project was created as part of my 'Efficient Video Encoding' subject. This project is a demonstration of efficient video encoding using Python and the OpenCV library. It captures video from a webcam, applies grayscale and Gaussian blur processing to each frame, and then saves the processed frames as an output video file in the MP4 format.

## Prerequisites

Before running this code, ensure you have the following prerequisites installed:
- Python 3.x
- OpenCV (cv2) library

## Usage

<<<<<<< HEAD
- git clone git@github.com:Himanshu-Badgujar/Realtime-Video-Processing.git
- Open the script in integrated development environment.
- Run
=======
1. Clone this repository to your local machine or download the script.
2. Open the script in a text editor or integrated development environment (IDE).
3. Customize the following parameters according to your requirements:
   - `output_filename`: The name of the output video file (e.g., 'output.mp4').
   - `fps`: The frames per second for the output video (e.g., 30).
   - `output_dimensions`: The dimensions of the output video frames in the format (width, height).
   - `cap = cv2.VideoCapture(0)`: Change `0` to the appropriate camera index or video file path if you want to capture from a different source.
   - You can adjust the Gaussian blur parameters by modifying the values in `cv2.GaussianBlur(gray_frame, (25, 25), 0)` to control the degree of blurring.
4. Save your changes.
5. Run the script using Python.
>>>>>>> e9834d3c5817ca7ffa8a3de1423ae3cabab91ef4

## Contribution

Contributions are welcome! If you find any issues or want to enhance this project, please feel free to open a pull request.

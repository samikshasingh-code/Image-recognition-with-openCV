# Image-recognition-with-openCV
Abstract
This project, Image Recognition with OpenCV, aims to demonstrate fundamental image processing and object detection techniques using OpenCV and Python. The focus is on applying basic computer vision concepts like grayscale conversion, resizing, image detection, and face detection using Haar cascades. A simple GUI was also developed for user-friendly interaction. This project lays the foundation for more advanced AI applications in image recognition and computer vision.

🎯 Objective
To build a simple image recognition system that processes images and detects faces or objects using the OpenCV library.

🛠️ Tools and Technologies Used
Language: Python 3.x
Library: OpenCV
Other Tools: Tkinter (for GUI), GitHub (for version control)

🔍 Modules Implemented
1. Image Loading and Display
Used OpenCV’s cv2.imread() to load images.
Displayed using cv2.imshow().

2. Grayscale Conversion
Converted colored image to grayscale using cv2.cvtColor().

3. Image Resizing
Resized the image to a uniform dimension using cv2.resize().

4. Saving Processed Image
Saved the processed image using cv2.imwrite().

5. Face Detection
Implemented Haar Cascade Classifier to detect human faces.

Used haarcascade_frontalface_default.xml from OpenCV.

6. GUI Implementation
Created a user interface using Tkinter.

GUI lets users select an image and see detection results.

🧠 Working Process (Step-by-Step)
Set up Python and OpenCV.
Created and tested code to load and display images.
Added grayscale conversion, resizing, and save functions.
Integrated face detection using Haar cascades.
Designed a GUI with buttons to:
Upload an image
Detect face
View result


import cv2  # Import OpenCV library

# Step 1: Load the image
img = cv2.imread('images/sample.jpg')

# Check if image is loaded
if img is None:
    print("Error: Could not load image.")
    exit()

# Step 2: Convert image to grayscale (Haar Cascade works on grayscale images)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 4: Detect faces in the image
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Step 5: Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Step 6: Show the result
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 7: Save the result
cv2.imwrite("images/detected_faces.jpg", img)
print("Detected faces saved as 'images/detected_faces.jpg'")

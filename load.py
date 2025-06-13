import cv2  # Import OpenCV library

# Step 1: Load the image from the 'images' folder
img = cv2.imread('images/sample.jpg')

# Check if image is loaded successfully
if img is None:
    print("Error: Could not load image. Make sure 'sample.jpg' is in the 'images' folder.")
    exit()

# Step 2: Display the original image
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 3: Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 4: Resize the image to 400x400 pixels
resized = cv2.resize(img, (400, 400))
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 5: Save the resized image as a new file
cv2.imwrite("images/resized.jpg", resized)
print("Resized image saved as 'images/resized.jpg'")

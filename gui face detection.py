import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Main detection function
def detect_from_image():
    file_path = filedialog.askopenfilename(
        title="📁 Select Image File",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    
    if not file_path:
        return

    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("❌ Error", "Failed to load image.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

    # Convert image to RGB and display in GUI
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_pil = img_pil.resize((450, 350))  # Resize to fit GUI
    img_tk = ImageTk.PhotoImage(img_pil)

    image_label.config(image=img_tk)
    image_label.image = img_tk  # Keep reference

    status_label.config(text=f"✅ Detected {len(faces)} face(s) and eyes", fg="#009900")

# --- GUI SETUP ---
window = tk.Tk()
window.title("✨ Face & Eye Detection App")
window.geometry("520x600")
window.configure(bg="#f0faff")

# Title label
title_label = tk.Label(window, text="🔍 Image Recognition with OpenCV", font=("Helvetica", 16, "bold"), bg="#f0faff", fg="#0a66c2")
title_label.pack(pady=10)

# Upload button
upload_btn = tk.Button(
    window, text="📷 Upload Image & Detect", font=("Helvetica", 13),
    bg="#007bff", fg="white", padx=20, pady=5,
    command=detect_from_image
)
upload_btn.pack(pady=15)

# Image display label
image_label = tk.Label(window, bg="#d6f5f5", width=450, height=350, relief="groove", bd=2)
image_label.pack(pady=10)

# Status label
status_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f0faff", fg="#006600")
status_label.pack(pady=5)

# Exit button
exit_btn = tk.Button(window, text="🚪 Exit", font=("Helvetica", 12), bg="#555", fg="white", width=10, command=window.quit)
exit_btn.pack(pady=15)

window.mainloop()

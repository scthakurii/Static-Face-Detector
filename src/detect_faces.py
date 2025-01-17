import cv2
from src.utils import ensure_dir, load_image, save_image

def detect_faces(image_path, cascade_path, output_dir):
    """Detect faces in an image using Haar cascades."""
    ensure_dir(output_dir)
    
    # Load Haar cascade
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Load image
    image = load_image(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    print(f"Detected {len(faces)} faces.")

    # Annotate and save image
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    output_path = f"{output_dir}/detected_faces.jpg"
    save_image(image, output_path)
    print(f"Saved result to {output_path}")

# Uncomment to run as a standalone script
# if __name__ == "__main__":
#     detect_faces("../datasets/image_1.jpg", "../models/haarcascades/haarcascade_frontalface_default.xml", "../outputs")

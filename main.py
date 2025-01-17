from src.capture import capture_images
from src.detect_faces import detect_faces

def main():
    # Step 1: Capture images
    print("Capturing images...")
    capture_images("datasets", num_images=5)

    # Step 2: Detect faces
    print("Detecting faces...")
    cascade_path = "models/haarcascades/haarcascade_frontalface_default.xml"
    detect_faces("datasets/image_1.jpg", cascade_path, "outputs")

if __name__ == "__main__":
    main()

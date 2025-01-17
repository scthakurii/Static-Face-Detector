import cv2
from src.utils import ensure_dir

def capture_images(output_dir, num_images=5):
    """Capture images from the webcam."""
    ensure_dir(output_dir)
    cap = cv2.VideoCapture(0)

    print("Press 'c' to capture an image. Press 'q' to quit.")
    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break
        
        cv2.imshow("Webcam", frame)
        key = cv2.waitKey(1)
        
        if key == ord('c'):
            image_path = f"{output_dir}/image_{count + 1}.jpg"
            cv2.imwrite(image_path, frame)
            print(f"Image saved at {image_path}")
            count += 1
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Uncomment to run as a standalone script
# if __name__ == "__main__":
#     capture_images("../datasets", num_images=5)

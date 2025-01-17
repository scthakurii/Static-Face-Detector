import os
import cv2

def ensure_dir(directory):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_image(image_path):
    """Load an image from a given path."""
    return cv2.imread(image_path)

def save_image(image, output_path):
    """Save an image to the specified path."""
    cv2.imwrite(output_path, image)

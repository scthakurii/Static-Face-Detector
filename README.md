# Static Face Detection Project

## Overview
This project is a Python-based static face detection application that uses the OpenCV library and Haar cascade classifiers to detect faces in images. The modular structure makes it easy to extend and maintain.

---

## Features
- Detect faces in static images using Haar cascades.
- Modular design with separate scripts for capturing images, detecting faces, and utility functions.
- Organized directory structure for better maintainability.

---

## Directory Structure
```plaintext
face_detection_project/
├── datasets/            # For storing images or videos
├── models/              # For pre-trained models
│   └── haarcascades/    # Pre-trained Haar cascade XML files
├── outputs/             # For saving results (annotated images, etc.)
├── src/                 # Source code
│   ├── capture.py       # Script for image capture
│   ├── detect_faces.py  # Script for face detection
│   ├── utils.py         # Helper functions
└── main.py              # Main script to run the project

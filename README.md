# NumberPlate-Detection-System
This project is a Number Plate Detection System that uses OpenCV and Tesseract OCR to detect and extract text from license plates in images. The program identifies rectangular regions of interest, applies edge detection, and processes the plate area to read text accurately.

Features
Converts the input image to grayscale for preprocessing.
Applies Canny edge detection to highlight contours.
Finds contours and selects candidates with rectangular shapes (approximation with 4 vertices).
Isolates the region containing the license plate and enhances it using bilateral filtering and thresholding.
Extracts text using Tesseract OCR and displays it on the original image.
How It Works
Load and Preprocess the Image:
The image is converted to grayscale and processed with Canny edge detection to identify potential contours.

Contour Detection:
The algorithm sorts and filters contours to locate rectangular shapes, which are likely license plates.

Plate Detection and Text Extraction:
The selected region is filtered and thresholded for better OCR recognition.

Display Results:
The license plate text is displayed on the image with bounding boxes and printed on the console.

Requirements
Python 3.x
OpenCV
Tesseract OCR (pytesseract)

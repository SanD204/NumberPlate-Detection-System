import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

image = cv2.imread('car2.jpg')
cv2.imshow("Original",image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale",gray_image)

canny_edge = cv2.Canny(gray_image, 170, 200)
cv2.imshow("canny Edge",canny_edge)

contours, new  = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours=sorted(contours, key = cv2.contourArea, reverse = True)[:30]
contour_with_license_plate = None
license_plate = None
x = None
y = None
w = None
h = None
for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)
        if len(approx) == 4:                                          
            contour_with_license_plate = approx
            x, y, w, h = cv2.boundingRect(contour)
            license_plate = gray_image[y:y + h, x:x + w]
            break
(thresh, license_plate) = cv2.threshold(license_plate, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("plate",license_plate)
license_plate = cv2.bilateralFilter(license_plate, 11, 17, 17)
(thresh, license_plate) = cv2.threshold(license_plate, 150, 180, cv2.THRESH_BINARY)
text = pytesseract.image_to_string(license_plate)
image = cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 3) 
image = cv2.putText(image, text, (x-100,y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
print("License Plate :", text)
cv2.imshow("License Plate Detection",image)
cv2.waitKey(0)
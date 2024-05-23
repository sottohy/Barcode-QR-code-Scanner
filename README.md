# Barcode/QR code Scanner

### Python code to a implement a barcode/QR code scanner from a camera using OpenCV for video capture and display, and pyzbar for decoding barcodes and QR codes.

## Barcode Reader Function
The barcode_reader() function takes a single frame of video as input. It uses the pyzbar.decode method to detect barcodes within the frame. For each detected barcode, the function extracts the coordinates of the bounding box and decodes the barcode data to a UTF-8 string. It then draws a rectangle around the barcode and displays the decoded information as text on the frame. The barcode information is also written to a file named barcode_result.txt.

## Main Function
The main function handles the video capture and the display loop. It starts by opening a connection to the camera using cv2.VideoCapture(0), then the function then enters an infinite loop, where it captures frames from the camera until the user presses the 'Esc' key. For each frame, it checks if the capture was successful and if the frame is valid. If the frame is valid, it passes the frame to the barcode_reader function to detect and annotate any barcodes. The processed frame is then displayed in a window titled 'Barcode Scanner' using cv2.imshow. 


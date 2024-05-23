import cv2
from pyzbar import pyzbar

def barcode_reader(frame):
    # Decoding the information from the barcode
    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        # Get the bounding box coordinates of the barcode
        x, y, w, h = barcode.rect

        # Decode the barcode data to a string
        barcodeInfo = barcode.data.decode('utf-8')

        # Draw a rectangle around the barcode
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

        # Put the barcode information text above the rectangle
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcodeInfo, (x + 6, y - 6), font, 2.0, (255, 0, 255), 1)

        # Write the barcode information to a file
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode: " + barcodeInfo)

    return frame


def main():
    camera = cv2.VideoCapture(0)
    #ret, frame = camera.read()

    while True:
        # Capture the next frame from the camera
        ret, frame = camera.read()

        # Call the barcode_reader function
        frame = barcode_reader(frame)
        
        # Display the processed frame in a window
        cv2.imshow('Barcode Scanner', frame)
        
        # Break the loop if the 'Esc' key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()



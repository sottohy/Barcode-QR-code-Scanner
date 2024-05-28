# Barcode Scanner

Python application to read barcodes/QR codes from a webcam feed. It detects barcodes, draws rectangles around them, and displays the decoded information on the screen.

## Features

- Real-time barcode detection from a webcam feed.
- Draws a rectangle around detected barcodes.
- Displays decoded barcode information on the screen.
- Saves decoded barcode information to a file.

## Requirements

- Python 3.7 or later
- OpenCV
- Pyzbar

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sottohy/Barcode-QR-code-Scanner.git
   cd Barcode-QR-code-Scanner
2. Install the required packages:
   ```
   pip install opencv-python pyzbar 
## Usage

1. Run the application:
   ```
   python barcode_scanner.py
2.The webcam feed will open, and the application will start detecting barcodes in real-time.


## Code Overview
- barcode_reader(frame): Decodes barcodes from the given frame, draws rectangles around them, displays the decoded information, and writes the information to a file.
- main(): Captures frames from the webcam, processes them using barcode_reader(), and displays the processed frames in a window.




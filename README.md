# QR Code Generator

This Python application generates QR codes from comma-separated values using the Tkinter library for the graphical user interface and the `qrcode` library for QR code generation. It provides a simple and user-friendly interface to input values and view the corresponding QR codes.

## Features

- **Generate QR Codes:** Create QR codes from comma-separated values entered in the input field.
- **Scrollable View:** View multiple QR codes with a vertical scrollbar if the number of QR codes exceeds the visible area.
- **Label Wrapping:** The text labels for each QR code wrap to the next line if they are too long.
- **Mouse Wheel Scrolling:** Scroll through the list of QR codes using the mouse wheel.

## Installation

To use this application, ensure you have Python installed on your system. You will also need to install the required Python libraries.

1. Clone the repository:
    ```bash
    git clone https://github.com/ushanrashmika23/QR-Code.git
    cd QR-Code
    ```

2. Install the required libraries:
    ```bash
    pip install pillow qrcode
    ```

## Usage

1. **Run the Application:**
   Execute the Python script to launch the GUI application:
   ```bash
   python qr_code_generator.py

# CSV to QR Code Generator

## Overview

This Python application uses Tkinter to create a graphical user interface for generating QR codes from comma-separated values. Each QR code is displayed alongside a label describing its content. The application supports vertical scrolling and text wrapping to accommodate multiple QR codes and long labels.

## Features

- **Generate QR Codes:** Create QR codes from a list of comma-separated values.
- **Scrollable Canvas:** A vertically scrollable canvas to accommodate a large number of QR codes.
- **Text Wrapping:** Labels for each QR code automatically wrap if the text is too long.
- **Mouse Wheel Scrolling:** Scroll through the QR codes using the mouse wheel.

## Requirements

- Python 3.x
- Tkinter (comes with Python standard library)
- Pillow (`PIL` library)
- `qrcode` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/csv-to-qr-code-generator.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd csv-to-qr-code-generator
    ```

3. **Install the required libraries:**

    ```bash
    pip install pillow qrcode
    ```

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Enter comma-separated values** in the input field.

3. **Click "Generate QR Codes"** or press `Enter` to create QR codes for the entered values.

4. **Scroll** through the QR codes using the vertical scrollbar or mouse wheel.

## Code Explanation

- **generate_qr_codes():** This function clears any previous QR codes, generates new QR codes from the input values, and displays them in a scrollable frame.
- **on_generate_button_click(event=None):** This function triggers QR code generation when the button is clicked or the `Enter` key is pressed.
- **on_mouse_wheel(event):** This function handles vertical scrolling using the mouse wheel.
- **Tkinter Layout:** Uses a `Canvas` with a `Frame` to display QR codes and their labels. Labels are wrapped to fit within the available space.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

1. **Fork the repository**
2. **Create a new branch:**

    ```bash
    git checkout -b feature/your-feature
    ```

3. **Commit your changes:**

    ```bash
    git commit -am 'Add new feature'
    ```

4. **Push to the branch:**

    ```bash
    git push origin feature/your-feature
    ```

5. **Create a new Pull Request** on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note:** This README assumes you have basic knowledge of Git and GitHub. Modify the links and repository information according to your setup.

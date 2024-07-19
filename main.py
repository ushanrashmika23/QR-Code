import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr_codes():
    # Clear previous QR codes
    for widget in qr_frame.winfo_children():
        widget.destroy()

    # Get the CSV input from the entry widget
    csv_values = entry.get()
    values = [value.strip() for value in csv_values.split(',')]

    for value in values:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=4,
        )
        qr.add_data(value)
        qr.make(fit=True)

        qr_image = qr.make_image(fill='black', back_color='white')
        qr_image_tk = ImageTk.PhotoImage(qr_image)

        # Create a frame for each QR code and its label
        qr_code_container = tk.Frame(qr_frame, padx=10, pady=5)
        qr_code_container.pack(anchor='w', fill=tk.X)

        # Create a label for the QR code
        qr_code_label = tk.Label(qr_code_container, image=qr_image_tk)
        qr_code_label.image = qr_image_tk  # Keep a reference to avoid garbage collection
        qr_code_label.pack(side=tk.LEFT)

        # Create a label for the meaning with text wrapping
        meaning_label = tk.Label(qr_code_container, text=value, wraplength=300, anchor='w', justify=tk.LEFT)
        meaning_label.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

    # Update scroll region
    qr_frame.update_idletasks()
    qr_canvas.config(scrollregion=qr_canvas.bbox("all"))

def on_generate_button_click(event=None):
    csv_values = entry.get()
    if csv_values:
        generate_qr_codes()
    else:
        messagebox.showwarning("Input Error", "Please enter comma-separated values.")

def on_mouse_wheel(event):
    # Scroll the canvas vertically based on the mouse wheel movement
    qr_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Create the main window
root = tk.Tk()
root.title("CSV to QR Code Generator")

# Create a label and entry to get CSV input from the user
label = tk.Label(root, text="Enter comma-separated values:")
label.pack(padx=10, pady=5)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Bind the Enter key to the on_generate_button_click function
entry.bind('<Return>', on_generate_button_click)

# Create a button to generate the QR codes
generate_button = tk.Button(root, text="Generate QR Codes", command=on_generate_button_click)
generate_button.pack(padx=10, pady=10)

# Create a canvas and a frame for the QR codes
qr_canvas = tk.Canvas(root, width=600, height=400)
qr_canvas.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

scrollbar_y = tk.Scrollbar(root, orient=tk.VERTICAL, command=qr_canvas.yview)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

qr_canvas.configure(yscrollcommand=scrollbar_y.set)

qr_frame = tk.Frame(qr_canvas)
qr_canvas.create_window((0, 0), window=qr_frame, anchor="nw")

# Bind the mouse wheel event to the canvas
root.bind_all("<MouseWheel>", on_mouse_wheel)

# Run the Tkinter event loop
root.mainloop()

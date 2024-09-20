from tkinter import *
import qrcode
import os

# Create the root window
root = Tk()
root.title("QR Generator")
root.geometry("1000x500")
root.configure(bg="#E6E6FA")
root.resizable(False, False)

# Icon image
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# Create and place the image view label
Image_view = Label(root, bg="#E6E6FA")
Image_view.pack(padx=50, pady=10, side=RIGHT)


def generate():
    name = title.get()
    text = entry.get()

    # Create directory if it doesn't exist
    directory = "QR Code"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate and save QR code
    file_path = os.path.join(directory, str(name) + ".png")
    qr = qrcode.make(text)
    qr.save(file_path)

    global Image

    # Load the generated QR code image and display it
    Image = PhotoImage(file=file_path)
    Image_view.config(image=Image)
    Image_view.image = Image  # Keep a reference to avoid garbage collection


# Create and place the widgets
Label(root, text="Title", fg="#4B0082", bg="#E6E6FA", font=15).place(x=50, y=170)
title = Entry(root, width=13, font="arial 15")
title.place(x=50, y=200)

entry = Entry(root, width=28, font="arial 15")
entry.place(x=50, y=250)

Button(root, text="Generate", width=20, height=2, bg="#4B0082", fg="white", command=generate).place(x=50, y=300)

# Start the main event loop
root.mainloop()

# generate qr code for the links

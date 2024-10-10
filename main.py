from tkinter import *
from PIL import Image, ImageTk

class FACE_RECOGNITION:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Set the window size
        self.root.title("Face Recognition System")  # Set the window title

        # Load and resize the first image
        img = Image.open(r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\1.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)  # Resize the image
        self.photoimg1 = ImageTk.PhotoImage(img)
        
        # Create a label to display the first image
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)
        
        # Load and resize the second image
        img1 = Image.open(r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\2.jpeg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img1)
        
        # Create a label to display the second image
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)
        
        # Load and resize the third image
        img2 = Image.open(r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\3.jpeg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img2)
        
        # Create a label to display the third image
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=400, height=130)
        
        # Load and resize the background image
        img3 = Image.open(r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\4.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img3)  
        
        # Create a label to display the background image
        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl = Label(bg_img, text="SMART CLASS ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        # Create buttons with images and labels
        button_width = 160
        button_height = 160
        button_gap = 100  # Gap between buttons

        self.create_button(bg_img, r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\student.jpg", "Student Details", 100, 100, button_width, button_height)
        self.create_button(bg_img, r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\1.jpg", "Face Detector", 100 + button_width + button_gap, 100, button_width, button_height)
        self.create_button(bg_img, r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\6.jpeg", "Attendance", 100 + 2 * (button_width + button_gap), 100, button_width, button_height)
        self.create_button(bg_img, r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\7.png", "Help Desk", 100 + 3 * (button_width + button_gap), 100, button_width, button_height)
        
        self.create_button(bg_img, r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\8.jpeg", "Train Data", 100, 300, button_width, button_height)
        self.create_button(bg_img, r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\9.jpeg", "Photos", 100 + button_width + button_gap, 300, button_width, button_height)
        self.create_button(bg_img, r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\10.jpeg", "Developer", 100 + 2 * (button_width + button_gap), 300, button_width, button_height)
        self.create_button(bg_img, r"C:\Users\pathi\OneDrive\Desktop\FACE_RECOGNITION\images\11.jpeg", "Exit", 100 + 3 * (button_width + button_gap), 300, button_width, button_height)

    def create_button(self, bg_img, img_path, text, x, y, width, height):
        img = Image.open(img_path)
        img = img.resize((150, 150), Image.ANTIALIAS)  # Keep the image size
        photo = ImageTk.PhotoImage(img)

        button_img = Button(bg_img, image=photo, cursor="hand2")
        button_img.image = photo  # Keep a reference to avoid garbage collection
        button_img.place(x=x, y=y, width=width, height=height)

        button_text = Button(bg_img, text=text, cursor="hand2", font=("times new roman", 10, "bold"), bg="white", fg="red")
        button_text.place(x=x, y=y + height, width=width, height=30)  # Position text button below image


# Main loop to run the application
if __name__ == "__main__":
    root = Tk()  # Create the main window
    obj = FACE_RECOGNITION(root)  # Create an object of the FACE_RECOGNITION class
    root.mainloop()  # Start the main event loop

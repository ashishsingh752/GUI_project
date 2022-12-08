import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("img4.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        border = tk.LabelFrame(self, text="Phase Transformation",
                               bg="ivory", bd=10, font=("Times New Roman", 25))
        border.pack(fill="both",  expand="yes", padx=200, pady=250)

        L1 = tk.Label(border, text="From Phase", font=(
            "Times New Roman", 15), bg="ivory")
        L1.place(x=50, y=70)
        T1 = tk.Entry(border, width=30, bd=5)
        T1.place(x=180, y=70)

        L2 = tk.Label(border, text="To Phase", font=(
            "Times New Roman", 15), bg="ivory")
        L2.place(x=50, y=100)
        T2 = tk.Entry(border, width=30, bd=5)
        T2.place(x=180, y=100)

        def verify():
            if T1.get() == '3' and T2.get() == '2':
                controller.show_frame(SecondPage)
            elif T1.get() == '3' and T2.get() == '5':
                controller.show_frame(ThirdPage)
            elif T1.get() == '3' and T2.get() == '6':
                controller.show_frame(ForthPage)
            elif T1.get() == '3' and T2.get() == '7':
                controller.show_frame(SixthPage)
            else:
                messagebox.showinfo(
                    "Error", "Sorry, Your Entry Is  Not Valid Here!! 😔")
        Button = tk.Button(border, text="Submit", font=(
            "zz", 15), fg="red", command=verify)
        Button.place(x=250, y=130)

        label=tk.Label(border,text="Ashish Singh (121EE0368)", font=(
            "Times New Roman", 13 ), bg="ivory")
        label.place(x=370, y=220)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("ashish.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Button = tk.Button(self, text="Home", font=(
            "zz", 15), fg="red", command=lambda: controller.show_frame(FirstPage))
        Button.place(x=900, y=600)


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("3to51.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Button = tk.Button(self, text="Next", font=(
            "zz", 15), fg="red", command=lambda: controller.show_frame(FifthPage))
        Button.place(x=920, y=600)

        Button = tk.Button(self, text="Home", font=(
            "zz", 15), fg="red", command=lambda: controller.show_frame(FirstPage))
        Button.place(x=850, y=600)


class FifthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("3to52.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Button = tk.Button(self, text="Home", font=(
            "zz", 15), fg="red", command=lambda: controller.show_frame(FirstPage))
        Button.place(x=900, y=600)
        Button = tk.Button(self, text="Back", font=(
            "zz", 15), fg="red", command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=840, y=600)


class ForthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("3to6.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Button = tk.Button(self, text="Home", font=(
            "zz", 15), fg="red", command=lambda: controller.show_frame(FirstPage))
        Button.place(x=900, y=600)


class SixthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("3to7.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Button = tk.Button(self, text="Home", font=(
            "zz", 15), fg="red", command=lambda: controller.show_frame(FirstPage))
        Button.place(x=900, y=600)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a new window

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=800)
        window.grid_columnconfigure(0, minsize=1000)

        self.frames = {}

        for F in (FirstPage, SecondPage, ThirdPage, ForthPage, FifthPage, SixthPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.mainloop()

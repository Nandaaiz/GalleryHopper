import tkinter as tk

window = tk.Tk()
window.title("GalleryHopper")
window.geometry("600x400")

label = tk.Label(window, text="Welcome to GalleryHopper!")
label.pack()

button = tk.Button(window, text="Click me!", command=lambda: print("Hello!"))
button.pack()

window.mainloop()
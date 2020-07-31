from tkinter import *

root = Tk()

root.title("MPC - M")
root.geometry("1024x768")

playlist_box = Listbox(root, bg="#00b894", fg="#dfe6e9", width=100)
playlist_box.pack(pady=50)

root.mainloop()
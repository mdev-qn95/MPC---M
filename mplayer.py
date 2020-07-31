from tkinter import *

root = Tk()

root.title("MPC - M")
root.geometry("1024x768")

# Create Playlist Box
playlist_box = Listbox(root, bg="#00b894", fg="#dfe6e9", width=100)
playlist_box.pack(pady=50)

#Create Button Frame
control_frame = Frame(root)
control_frame.pack(pady=20)

#Create Play/Stop etc Buttons
back_button = Button(control_frame, text="Back")
forward_button = Button(control_frame, text="Forward")
play_button = Button(control_frame, text="Play")
pause_button = Button(control_frame, text="Pause")
stop_button = Button(control_frame, text="Stop")

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

root.mainloop()
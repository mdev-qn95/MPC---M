from tkinter import *

root = Tk()

root.title("MPC - M")
root.geometry("1024x768")

# Create Playlist Box
playlist_box = Listbox(root, bg="#00b894", fg="#dfe6e9", width=100)
playlist_box.pack(pady=20)

# Define Button Image For Controls
back_button_img = PhotoImage(file='images/back50.png')
forward_button_img = PhotoImage(file='images/forward50.png')
play_button_img = PhotoImage(file='images/play50.png')
pause_button_img = PhotoImage(file='images/pause50.png')
stop_button_img = PhotoImage(file='images/stop50.png')

#Create Button Frame
control_frame = Frame(root)
control_frame.pack(pady=20)

#Create Play/Stop etc Buttons
back_button = Button(control_frame, image=back_button_img, borderwidth=0)
forward_button = Button(control_frame, image=forward_button_img, borderwidth=0)
play_button = Button(control_frame, image=play_button_img, borderwidth=0)
pause_button = Button(control_frame, image=pause_button_img, borderwidth=0)
stop_button = Button(control_frame, image=stop_button_img, borderwidth=0)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

root.mainloop()
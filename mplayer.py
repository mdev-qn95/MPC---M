from tkinter import *
from tkinter import filedialog

root = Tk()

root.title("MPC - M")
root.geometry("1024x768")

# Create Function To Add One Song To Playlist
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    my_label.config(text=song)

# Create Function To Add Many Songs To Playlist
def add_many_songs():
    pass

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

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu Dropdows
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)

# Add One Song To Playlist
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)

# Add Many Songs To Playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

#Temporary Label
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
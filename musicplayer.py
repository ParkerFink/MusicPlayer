import tkinter
import os

from pygame import mixer
from tkinter import ttk

mixer.init()


volume = 0.5

def play(currentSong):
    cwd = os.getcwd()
    mixer.music.load(cwd + '/music/' + currentSong)
    mixer.music.set_volume(volume)
    mixer.music.play()


def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def volume_up():
    global volume
    print(volume)
    volume += 0.1
    if volume >= 1:
        volume = 1

def volume_down():
    global volume
    print(volume)
    volume -= 0.1
    if volume <= 0:
        volume = 0

main_window = tkinter.Tk()
main_window.title("Music Player")
main_window.geometry("800x500")

#create the main frame
main_frame = tkinter.Frame(main_window)
main_frame.pack(fill="both", expand=1)

#create a canvas
main_canvas = tkinter.Canvas(main_frame)
main_canvas.pack(side='left', fill="both", expand=1)


#add a scrollbar to the canvas
scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=main_canvas.yview)
scrollbar.pack(side="right", fill='y')

#configure the canvas 
main_canvas.configure(yscrollcommand=scrollbar.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

#create another frame inside the canvas
secondary_frame = tkinter.Frame(main_canvas)


#add the new frame to a window in the canvas
main_canvas.create_window((0,0), window=secondary_frame, anchor='nw')


#main buttons

## pause
pause = tkinter.Button(secondary_frame, text="Pause", width=15, command=pause)
pause.pack(padx=15, pady=15)

## resume
resume = tkinter.Button(secondary_frame, text="Resume", width=15, command=resume)
resume.pack(padx=15, pady=15)

volumeUp = tkinter.Button(secondary_frame, text="Volume + ", width=15, command=volume_up)
volumeUp.pack(padx=15, pady=15)

volumeDown = tkinter.Button(secondary_frame, text="Volume - ", width=15, command=volume_down)
volumeDown.pack(padx=15, pady=15)


for song in os.listdir('music/'):
    #currentlyPlaying = song
    song = os.path.splitext(song)[0]
    button = tkinter.Button(secondary_frame, text=song, width=15, command= lambda song=song: play(song + '.mp3'))
    button.pack()


main_window.mainloop()
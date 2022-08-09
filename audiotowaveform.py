from tkinter import *
from tkinter import filedialog
import subprocess

#root window enable obviously
root=Tk()
root.title("Audio To Waveform Converter")
root.geometry("700x700")

def audiobrowseclick():
    #Sir Where is the file
    root.filename=filedialog.askopenfilename(initialdir="/", title="Browse for Audio File...", filetypes=[("Audio Files", ".mp3 .wav .ogg .aiff .wma .aac")])
    #right here
    #ok storing that location
    global audiofile
    audiofile= root.filename
    #sir what would you like the resolution to be
    global resolution
    resolution=StringVar()
    resolution.set("Choose Resolution:")
    resdrop=OptionMenu(root, resolution, "1920x1080", "1280x720", "852x480", "640x360", "426x240", "256x144")
    resdrop.pack()
    #sir what would you like the wave mode to be
    advancedwarninglabel=Label(root, text="Advanced:Choose Wave Mode")
    advancedwarninglabel.pack()
    global mode
    mode=StringVar()
    mode.set("cline")
    modedrop=OptionMenu(root, mode, "cline", "point", "line", "p2p")
    modedrop.pack()
    #sir would you like to convert the audio
    Convert=Button(root, text="Convert To Audio Waveform", command=converttowaveform)
    Convert.pack()
    return audiofile
    return resolution
    return mode
def converttowaveform():
    Wait=Label(root, text="Please Wait...")
    Wait.pack()
    #yes i would
    #Sir where would you like the file
    root.filename=filedialog.asksaveasfilename(initialdir="/", title="Save...", filetypes=[("Video Files", ".mp4, .mov, .wmv, .avi, .avchd, .flv, .mkv, .webm")])
    #right here.
    #ok im converting the file and putting it where you want it.
    convert=subprocess.call(f'ffmpeg -i "{audiofile}" -filter_complex "[0:a]showwaves=s={resolution.get()}:mode={mode.get()},format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -c:a copy "{root.filename}"')
    Done=Label(root, text="Done!")
    Done.pack()
    

#starting text
Titlelabel=Label(root, text="Audio File To Waveform Converter", font="Montserrat")
Titlelabel.pack()

#Browse Button
Browse=Button(root, text="Browse For Audio File...", padx=50, command=audiobrowseclick)
Browse.pack()

root.mainloop()

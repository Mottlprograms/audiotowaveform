from tkinter import *
from tkinter import filedialog
import subprocess
import customtkinter


class Start(customtkinter.CTk):
    #root window enable obviously
    root=customtkinter.CTk()
    root.title("Audio To Waveform Converter")
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("E:\Python\darklightsync.json")
    root.geometry("400x300")
    root.iconbitmap("E:\Python\images.ico")

class mainUI(customtkinter.CTk):
    
    def converttowaveform():
        Wait=customtkinter.CTkLabel(Start.root, text="Please Wait...")
        Wait.pack()
        #yes i would
        #Sir where would you like the file
        Start.root.filename=filedialog.asksaveasfilename(initialdir="/", title="Save...", filetypes=[("Video Files", ".mp4, .mov, .wmv, .avi, .avchd, .flv, .mkv, .webm")])
        #right here.
        #ok im converting the file and putting it where you want it.
        convert=subprocess.call(f'ffmpeg -i "{audiofile}" -filter_complex "[0:a]showwaves=s={resolution.get()}:mode={mode.get()},format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -c:a copy "{Start.root.filename}"')
        Done=customtkinter.CTkLabel(Start.root, text="Done!")
        Done.pack()
    
    def audiobrowseclick():
        #Sir Where is the file
        Start.root.filename=filedialog.askopenfilename(initialdir="/", title="Browse for Audio File...", filetypes=[("Audio Files", ".mp3 .wav .ogg .aiff .wma .aac")])
        #right here
        #ok storing that location
        global audiofile
        audiofile= Start.root.filename
        #sir what would you like the resolution to be
        global resolution
        resolution=StringVar()
        resolution.set("Choose Resolution:")
        resdrop=customtkinter.CTkOptionMenu(Start.root, variable=resolution, values=["1920x1080", "1280x720", "852x480", "640x360", "426x240", "256x144"])
        resdrop.pack()
        #sir what would you like the wave mode to be
        advancedwarninglabel=customtkinter.CTkLabel(Start.root, text="Advanced:Choose Wave Mode")
        advancedwarninglabel.pack()
        global mode
        mode=StringVar()
        mode.set("cline")
        modedrop=customtkinter.CTkOptionMenu(Start.root, variable=mode, values=["cline", "point", "line", "p2p"])
        modedrop.pack()
        #sir would you like to convert the audio
        Convert=customtkinter.CTkButton(Start.root, text="Convert To Audio Waveform", command=mainUI.converttowaveform)
        Convert.pack()
        return audiofile
        return resolution
        return mode


    #starting text
    Titlelabel=customtkinter.CTkLabel(Start.root, text="Audio File To Waveform Converter")
    Titlelabel.pack()

    #Browse Button
    Browse=customtkinter.CTkButton(Start.root, text="Browse For Audio File...", padx=50, command=audiobrowseclick)
    Browse.pack()

Start.root.mainloop()

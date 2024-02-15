import customtkinter
from tkinter import filedialog
from moviepy.editor import AudioFileClip, ImageClip

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x600")
app.title("Quick Instagram Audio Clip Maker")

image_path = ''
audio_path = ''
output_path = ''

def add_static_image_to_audio():
    audio_clip = AudioFileClip(audio_path).subclip(0, 58)
    image_clip = ImageClip(image_path).set_duration(audio_clip.duration)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.fps = 1
    video_clip.write_videofile(output_path, fps=video_clip.fps)

def getImagePath():
    global image_path
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if image_path:
        image_entry.delete(0, "end")
        image_entry.insert(0, image_path)
        
def getAudioPath():
    global audio_path
    audio_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio files", "*.wav *.mp3 *.aac")])
    if audio_path:
        audio_entry.delete(0, "end")
        audio_entry.insert(0, audio_path)
    
def getOutputPath():
    global output_path
    output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    if output_path:
        output_entry.delete(0, "end")
        output_entry.insert(0, output_path)

image_entry = customtkinter.CTkEntry(app, placeholder_text="Select image...")
image_entry.pack(pady=10)
image_button = customtkinter.CTkButton(app, text="Choose Image", command=getImagePath)
image_button.pack(pady=5)

audio_entry = customtkinter.CTkEntry(app, placeholder_text="Select audio...")
audio_entry.pack(pady=10)
audio_button = customtkinter.CTkButton(app, text="Choose Audio", command=getAudioPath)
audio_button.pack(pady=5)

output_entry = customtkinter.CTkEntry(app, placeholder_text="Output file name...")
output_entry.pack(pady=10)
output_button = customtkinter.CTkButton(app, text="Output File", command=getOutputPath)
output_button.pack(pady=5)

create_video_button = customtkinter.CTkButton(app, text="Create Video", command=add_static_image_to_audio)
create_video_button.pack(pady=20)

app.mainloop()
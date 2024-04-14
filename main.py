import customtkinter
from tkinter import filedialog, messagebox
from moviepy.editor import AudioFileClip, ImageClip
import os

class AppUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.uiDefaults()
        self.imageFunctions()
        self.audioFunctions()
        self.outputFunctions()
        self.createVideoFunctions()
        
        self.image_path = ''
        self.audio_path = ''
        self.output_path = ''
    
    def uiDefaults(self):
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        
        self.geometry("800x600")
        self.title("Quick Instagram Audio Clip Maker")

    def imageFunctions(self):
        self.image_entry = customtkinter.CTkEntry(self, placeholder_text="Select image...")
        self.image_entry.pack(pady=10)
        
        self.image_button = customtkinter.CTkButton(self, text="Choose Image", command=self.getImagePath)
        self.image_button.pack(pady=5)
        
    def audioFunctions(self):
        self.audio_entry = customtkinter.CTkEntry(self, placeholder_text="Select audio...")
        self.audio_entry.pack(pady=10)
        
        self.audio_button = customtkinter.CTkButton(self, text="Choose Audio", command=self.getAudioPath)
        self.audio_button.pack(pady=5)
                
    def outputFunctions(self):
        self.output_entry = customtkinter.CTkEntry(self, placeholder_text="Output file name...")
        self.output_entry.pack(pady=10)
        
        self.output_button = customtkinter.CTkButton(self, text="Output File", command=self.getOutputPath)
        self.output_button.pack(pady=5)
        
    def createVideoFunctions(self):
        self.create_video_button = customtkinter.CTkButton(self, text="Create Video", command=self.createVideo)
        self.create_video_button.pack(pady=20)
        
    def createVideo(self):
        try:
            add_static_image_to_audio(self.image_path, self.audio_path, self.output_path)
            messagebox.showinfo("Success", "Video has been completed")
            
            self.showInFolder(self.output_path)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def showInFolder(self, path):
        path = os.path.normpath(path)
        if os.path.isfile(path):
            dir_path = os.path.dirname(path)
            file_name = os.path.basename(path)
            os.system(f'explorer /select, "{path}"')
        else:
            messagebox.showerror("Error", "Video file not found")
            
    def getImagePath(self):
        self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            self.image_entry.delete(0, "end")
            self.image_entry.insert(0, self.image_path)
            
    def getAudioPath(self):
        self.audio_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio files", "*.wav *.mp3 *.aac")])
        if self.audio_path:
            self.audio_entry.delete(0, "end")
            self.audio_entry.insert(0, self.audio_path)
                  
    def getOutputPath(self):
        self.output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if self.output_path:
            self.output_entry.delete(0, "end")
            self.output_entry.insert(0, self.output_path)
            
def add_static_image_to_audio(image_path, audio_path, output_path):
    audio_clip = AudioFileClip(audio_path).subclip(0, 58)
    image_clip = ImageClip(image_path).set_duration(audio_clip.duration)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.fps = 1
    video_clip.write_videofile(output_path, fps=video_clip.fps)

if __name__ == "__main__":
    app = AppUI()
    app.mainloop()
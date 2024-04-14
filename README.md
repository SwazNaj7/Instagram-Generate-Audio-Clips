# Instagram-Generate-Audio-Clips

## Overview
This Python application allows users to generate audio clips suitable for Instagram posts without the need for a video editor. It automates the process of creating shareable audio content quickly and efficiently.

## Features
- **Quick Audio Generation**: Create audio clips for Instagram with just a few commands.
- **No Video Editing Required**: Eliminates the complexity of using traditional video editing software.

## Installation

To set up the Instagram-Generate-Audio-Clips app on your local machine, follow these steps:

```bash
git clone https://github.com/SwazNaj7/Instagram-Generate-Audio-Clips
cd Instagram-Generate-Audio-Clips
pip install -r requirements.txt 
```
## Running This Application

Simply navigate to the same directory as the main.py file and run

# Customizing the Length of Video Clips

The `add_static_image_to_audio` function is set up to create video clips with a default duration. If you would like to customize the length of your video to match the length of your audio clip or to set it to a specific duration, you will need to modify the `subclip` method in the `add_static_image_to_audio` function.

By default, the video is set to a length of 58 seconds as shown:

```python
def add_static_image_to_audio(image_path, audio_path, output_path):
    audio_clip = AudioFileClip(audio_path).subclip(0, 58)
    image_clip = ImageClip(image_path).set_duration(audio_clip.duration)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.fps = 1
    video_clip.write_videofile(output_path, fps=video_clip.fps)
```

```python
audio_clip = AudioFileClip(audio_path).subclip(0, 58)
```

If you wish to specify a custom length, change the values within the .subclip(start_time, end_time) method to match your desired start and end times in seconds. For example, to create a clip that starts at 10 seconds and ends at 120 seconds, you would do the following:

```python
audio_clip = AudioFileClip(audio_path).subclip(10, 120)
```

Or if you wish to use full length of your audio clip remove the .subclip() method as shown below

```python
audio_clip = AudioFileClip(audio_path)
```

```bash
python main.py

import moviepy
import moviepy.editor

video = moviepy.editor.VideoFileClip("nombreDelArchivo.mp4")

audio = video.audio
audio.write_audiofile("new_audio.mp3")
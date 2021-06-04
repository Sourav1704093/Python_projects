import moviepy.editor as mp

video_clip = mp.VideoFileClip("test.mp4")

video_clip.audio.write_audiofile("result.mp3")

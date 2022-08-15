from moviepy.editor import VideoClip, VideoFileClip, concatenate_videoclips
from numpy import concatenate

clip1 = VideoFileClip("https://store1.gofile.io/download/direct/67c6fbc6-332b-458c-ad7c-032558c0cb66/s2.mp4").subclip(10, 20)
clip2 = VideoFileClip("https://store5.gofile.io/download/direct/e540020a-9953-4798-bc5d-7247e1d4fae9/fpv.mp4").subclip(5, 10)

clip3 = VideoFileClip("one.mp4").subclip(5, 10)

combined = concatenate_videoclips([clip1, clip2, clip3])
combined.write_videofile("c.mp4")

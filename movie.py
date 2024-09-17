import moviepy.editor as mv
from math import floor

clip = mv.VideoFileClip("clip1.mp4")

NumClips = floor(clip.duration / 7)

subclip1 = clip.subclip(1, NumClips)
subclip2 = clip.subclip(NumClips+1, 2*NumClips)
subclip3 = clip.subclip(2*NumClips + 1, 3*NumClips)
subclip4 = clip.subclip(3*NumClips + 1, 4*NumClips)
subclip5 = clip.subclip(4*NumClips + 1, 5*NumClips)



# print(NumClips)
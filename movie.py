import moviepy.editor as mv
from math import floor
import random

clip = mv.VideoFileClip("clip1.mp4")

NumClips = floor(clip.duration / 44)


# subclip1 = clip.subclip(1, NumClips)
# subclip2 = clip.subclip(NumClips+1, 2*NumClips)
# subclip3 = clip.subclip(2*NumClips + 1, 3*NumClips)
# subclip4 = clip.subclip(3*NumClips + 1, 4*NumClips)
# subclip5 = clip.subclip(4*NumClips + 1, 5*NumClips)
# subclip6 = clip.subclip(5*NumClips + 1, 6*NumClips)
clipsArray = [
        clip.subclip(1, NumClips), 
        clip.subclip(NumClips+1, 2*NumClips), 
        clip.subclip(2*NumClips + 1, 3*NumClips), 
        clip.subclip(3*NumClips + 1, 4*NumClips),   
        clip.subclip(4*NumClips + 1, 5*NumClips),
        clip.subclip(5*NumClips + 1, 6*NumClips),
        clip.subclip(6*NumClips + 1, 7*NumClips)
              ]

DeliveredClips = int(input('How many clips do you want?'))

for clps in enumerate(clipsArray):
    # dodo dogshit fart
    
    
    

# print(NumClips)
from moviepy.editor import VideoFileClip, concatenate_videoclips
import random

# Load the video file
clip = VideoFileClip("clip1.mp4")

SaveEachSubClip = input('Do you want to save each subclip? (y/n): ')
NumOfClipsDesired = int(input('How many clips do you want?: '))

while True:
    if SaveEachSubClip.lower() == 'y':
        SaveSub = True
        break
    elif SaveEachSubClip.lower() == 'n':
        SaveSub = False
        break
    else:
        print('Only use y or n.')
        SaveEachSubClip = input('Do you want to save each subclip? (y/n): ')

# Set the duration for each subclip (6 seconds)
clip_length = 6
total_duration = clip.duration  # Get total duration of the video

# Calculate how many 6-second clips we can create
num_clips = int(total_duration // clip_length)

# Step 1: Create subclips
subclips = []
for i in range(num_clips):
    start_time = i * clip_length
    end_time = min((i + 1) * clip_length, total_duration)  # Ensure not to go past video length
    subclip = clip.subclip(start_time, end_time)
    if SaveSub is True:
        subclip.write_videofile(f"subclip{i + 1}.mp4", codec="libx264", audio_codec="aac")
    subclips.append(subclip)

# Step 2: Shuffle the list
random.shuffle(subclips)

# Step 3: Group subclips into batches of 7 (which will be ~40 seconds)
grouped_clips = [subclips[i:i + 7] for i in range(0, len(subclips), 7)]

# Step 4: Concatenate subclips in each group and save them
i = 0
i = 0
for idx, group in enumerate(grouped_clips):
    if group:  # Make sure the group isn't empty
        concatenated_clip = concatenate_videoclips(group)
        concatenated_clip.write_videofile(f"output_40sec_clip_{idx + 1}.mp4", codec="libx264", audio_codec="aac")
        i += 1
        if i >= NumOfClipsDesired:
            break  # Stop once you've made the desired number of clips
print('DONE')
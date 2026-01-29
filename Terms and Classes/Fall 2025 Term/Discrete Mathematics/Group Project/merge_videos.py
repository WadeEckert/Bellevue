from moviepy.editor import VideoFileClip, concatenate_videoclips

# Replace these with the paths to your videos on your computer
zach_path = "NEW_Zach Eaton_MA315_GP_video.mp4"
devin_path = "Devin-MA315_Group Project_Final Submission.mp4"
wade_path = "Wade Cryptography PPT V1.mp4"

# Load the videos
zach = VideoFileClip(zach_path)
devin = VideoFileClip(devin_path)
wade = VideoFileClip(wade_path)

# Combine in order
final_clip = concatenate_videoclips([zach, devin, wade])

# Export the final merged video
final_clip.write_videofile("MA315_Final_Group_Presentation.mp4",
                           codec="libx264",
                           audio_codec="aac")
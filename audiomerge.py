import os
import random
from moviepy.editor import *

videoclip = VideoFileClip("combined.mp4")
audioclipfl = random.choice(os.listdir("./Music"))
audioclipsl = "/" + audioclipfl
audioclipf = str(audioclipsl)
audioclipfi = "./Music"
audioclip = AudioFileClip(audioclipfi + audioclipf)
audioclip = audioclip.volumex(2)

new_audioclip = CompositeAudioClip([videoclip.audio, audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("finalized.mp4")

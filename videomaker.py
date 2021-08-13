from moviepy.editor import *
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import random
import threading
import time
import subprocess

clipf1 = random.choice(os.listdir("./Clips"))
clipf2 = random.choice(os.listdir("./Clips"))

clipsl = "/" + clipf1
clipf = str(clipsl)
clip1fi = "./Clips"
clip1 = VideoFileClip(clip1fi + clipf)


clipsl2 = "/" + clipf2
clipf2 = str(clipsl2)
clip2fi = "./Clips"
clip2 = VideoFileClip(clip2fi + clipf2)
clip1 = clip1.volumex(.4)
clip2 = clip2.volumex(.4)
result_clip = concatenate_videoclips([clip1,clip2], method="compose", padding=1)
result_clip.write_videofile('combined.mp4')

subprocess.call("python audiomerge.py 1", shell=True)
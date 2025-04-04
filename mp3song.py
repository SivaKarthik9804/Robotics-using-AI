@author: Karthik
"""

import pygame
import os
def play_mp3(file_path):
    pygame.mixer.init()
    if not os.path.exists(file_path):
        print(f"the file {file_path} does not exist.")
        return
    try:
        #load and play the mp3 file
        pygame.mixer.music.load(file_path)
        print(f"playing {os.path.basename(file_path)}...")
        pygame.mixer.music.play()
        #wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"an error occurred while playing the file:{e}")
    finally:
        #stop the music and quit pygame mixer
        pygame.mixer.music.stop()
        pygame.mixer.quit()
if __name__=="__main__":
    mp3_file_path= r"[yourfile in mp3 format that must be given with its path]"
    play_mp3(mp3_file_path)
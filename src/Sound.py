import pygame
import time
import config

class SoundPlayer:
    def __init__(self):
        self.sound_files = config.SOUND_FILES
        self.array_index = 0
        self.last_played = 0
        self.extension = False 
        self.debounce = 1
        pygame.mixer.init()

    def playSound(self):
        current_time = time.time()
        if self.extension == True:
            self.debounce = 2.5
        else:
            self.debounce = 1
        
        if current_time - self.last_played > self.debounce:
            sound_file = self.sound_files[min(self.array_index, len(self.sound_files) - 1)]
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            self.last_played = current_time

            self._updateIndex()

    def _updateIndex(self):
        if self.array_index < 4:
            self.array_index += 1
        elif self.array_index == 4:
            self.extension = True
            self.array_index += 1
        elif self.array_index == 5:
            self.array_index = 5
            self.extension = False    


    def reset(self):
        self.array_index = 0
        self.extension = False

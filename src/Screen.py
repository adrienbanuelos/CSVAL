import cv2
import numpy as np
import mss
from Sound import SoundPlayer
import config
import win32api as wp

class ScreenCapture:
    def __init__(self):
        self.region_width = 250
        self.region_height = 100
        self.resolution = 1920, 1080
        self.lower_color = np.array((150, 1, 255), dtype="uint8")
        self.upper_color = np.array((150, 40, 255), dtype="uint8")
        self.region = config.REGION
        self.debug_mode = False # debug mode 

        self.sound_player = SoundPlayer()

    def detectColor(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_color, self.upper_color)
        return np.any(mask), mask
    
    def getScreen(self):
        with mss.mss() as sct:
            while True:
                screen = np.array(sct.grab(self.region))
                color_detected, mask = self.detectColor(screen)
                
                if self.debug_mode:
                    resized_screen = cv2.resize(screen, (screen.shape[1]*3, screen.shape[0]*3))
                    resized_mask = cv2.resize(mask, (mask.shape[1]*3, mask.shape[0]*3))
                    cv2.imshow("Frame", resized_screen)
                    cv2.imshow("Mask", resized_mask)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        cv2.destroyAllWindows()
                        break

                if color_detected:
                    self.sound_player.playSound()

                
                    
    def debugScreen(self):
        with mss.mss() as sct:
            while True:
                screen = np.array(sct.grab(self.region))
                screen = cv2.resize(screen, (screen.shape[1]*3, screen.shape[0]*3))
                cv2.imshow("Captured Area", screen)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break

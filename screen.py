import cv2
import numpy
import mss
import pygame
import threading
import time
pygame.mixer.init()

# Screen Configuration
region_width = 250
region_height = 100
resolution = 1920, 1080
monitor = {
    "top": int((resolution[1] - region_height) / 2) + 490,
    "left": int((resolution[0] - region_width) / 2),
    "width": region_width,
    "height": region_height
}
upper_color = (150, 40, 255)
lower_color = (150, 0, 255)

# Sound Configuration
soundfile_array = [
    "C:\\Users\\adrie\\OneDrive\\Desktop\\Csvalorant\\sounds\\kill1.mp3", #0
    "C:\\Users\\adrie\\OneDrive\\Desktop\\Csvalorant\\sounds\\kill2.mp3", #1
    "C:\\Users\\adrie\\OneDrive\\Desktop\\Csvalorant\\sounds\\kill3.mp3", #2
    "C:\\Users\\adrie\\OneDrive\\Desktop\\Csvalorant\\sounds\\kill4.mp3", #3 
    "C:\\Users\\adrie\\OneDrive\\Desktop\\Csvalorant\\sounds\\kill5.mp3", #4
    "C:\\Users\\adrie\\OneDrive\\Desktop\\Csvalorant\\sounds\\kill5.mp3"  #5
]

array_index = 0
lastplayed = 0
debounce = 1
extension = False

def playSound(soundfile_array):
    global lastplayed, array_index, extension
    current_time = time.time()
    print("Current Array Index: ", array_index)
    if extension == True:
        debounce = 2.5
    else:
        debounce = 1
    print("Current Debounce: ", debounce)
    
    if current_time - lastplayed > debounce:
        soundfile = soundfile_array[min(array_index, len(soundfile_array) - 1)]
        print("Playing Sound: ", soundfile) # Debugging
        pygame.mixer.music.load(soundfile)
        pygame.mixer.music.play()
        lastplayed = current_time

        if array_index < 4:
            array_index += 1
        elif array_index == 4:
            extension = True
            array_index += 1
        elif array_index == 5:
            array_index = 5
            extension = False

    print("Extension for next sound: ", extension)

def detectColor(frame, lower, upper):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = numpy.array(lower, dtype="uint8")
    upper = numpy.array(upper, dtype="uint8")
    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    if numpy.any(mask):
        #print("Color detected")
        threading.Thread(target=playSound, args=(soundfile_array,)).start()

def captureScreen():
    with mss.mss() as sct:
        while True:
            screen = numpy.array(sct.grab(monitor))
            detectColor(screen, lower_color, upper_color)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__ == "__main__":
    captureScreen()
from Screen import ScreenCapture
import win32api as wp
import threading
import time

capture_screen = ScreenCapture()

def reset():
        print("Reset Array Index")
        capture_screen.sound_player.reset()

def main():
    def begin():
        capture_screen.getScreen()
    capture_thread = threading.Thread(target=begin)
    capture_thread.start()

    while True:
        if wp.GetAsyncKeyState(0x42) < 0:
            reset()
            time.sleep(0.2)

if __name__ == "__main__":
    main()

from pynput.keyboard import Key,Controller
from time import sleep




keyboard = Controller()
def volumeup(self):
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        sleep(0.1)

def volumedown(self):
        keyboard.press(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        sleep(0.1)
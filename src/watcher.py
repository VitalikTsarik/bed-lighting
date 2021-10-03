import atexit
import json

from rpi_ws281x import PixelStrip, Color
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from effects import colorWipe, Effects, effect2FuncMapping
from led_controller import STATUS_PATH

LED_COUNT = 60 * 10 - 18  # Number of LED pixels: LED/m * m
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)


class LedHandler(FileSystemEventHandler):
    def on_closed(self, event):
        if event.src_path == STATUS_PATH:
            try:
                with open(STATUS_PATH, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                color = data.get('color') or {}
                red = color.get('red') or 0
                green = color.get('green') or 0
                blue = color.get('blue') or 0
                effect = data.get('effect') or Effects.COLOR_WIPE.value

                effectFunc = effect2FuncMapping[effect]
                effectFunc(strip, Color(red, green, blue))

            except OSError:
                print('File reading error')


@atexit.register
def on_thread_stop():
    colorWipe(strip)


if __name__ == '__main__':
    strip.begin()

    event_handler = LedHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.')
    observer.start()

    observer.join()

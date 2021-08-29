import json

from rpi_ws281x import PixelStrip, Color
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from effects import colorWipe
from led_controller import STATUS_PATH

LED_COUNT = 30  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()


class LedHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == STATUS_PATH:
            try:
                colors = json.loads(open(STATUS_PATH, 'r', encoding='utf-8').read())
                print('colors: ', colors)
                print('type of color: ', type(colors['red']))
                color = Color(colors['red'], colors['green'], colors['blue'])
                colorWipe(strip, color)

            except OSError:
                print('File reading error')
                LedHandler()


event_handler = LedHandler()
observer = Observer()
observer.schedule(event_handler, path=STATUS_PATH)
observer.start()

observer.join()

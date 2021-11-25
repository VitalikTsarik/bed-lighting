import time
from enum import Enum

from rpi_ws281x import Color


def colorWipe(strip, color=Color(0, 0, 0)):
    """Wipe all color across display."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)

    strip.show()


def theaterChase(strip, color=Color(0, 100, 0), wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def wheel(pos=30):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(
                (int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def scrollOut(strip, color=Color(0, 100, 0), wait_ms=10):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


class Effects(Enum):
    INSTANT = 'instant'
    CHASE = 'chase'
    CHASE_RAINBOW = 'chaseRainbow'
    RAINBOW = 'rainbow'
    RAINBOW_CYCLE = 'rainbowCycle'
    SCROLL_OUT = 'scrollOut'


effect2FuncMapping = {
    Effects.INSTANT.value: colorWipe,
    Effects.CHASE.value: theaterChase,
    Effects.CHASE_RAINBOW.value: theaterChaseRainbow,
    Effects.RAINBOW.value: rainbow,
    Effects.RAINBOW_CYCLE.value: rainbowCycle,
    Effects.SCROLL_OUT.value: scrollOut,
}

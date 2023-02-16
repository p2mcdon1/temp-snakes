from animation import Animation
from stripFactory import StripFactory


class ColorWave(Animation):

    def __init__(self):
        Animation.__init__(self)

        numpix = self.parms.count

        stripFactory = StripFactory()

        self.strip = stripFactory.build()

        colors_rgb = self.parms.getColors()

        # see notes about supporting white-light
        colors = colors_rgb

        step = round(numpix / len(colors))
        current_pixel = 0

        for color1, color2 in zip(colors, colors[1:]):
            self.strip.set_pixel_line_gradient(
                current_pixel, current_pixel + step, color1, color2)
            current_pixel += step

        self.strip.set_pixel_line_gradient(
            current_pixel, numpix - 1, self.parms.violet, self.parms.electricPurple)

    # override
    def onRun(self, runFlag):
        print('starting to run ColorWave...')

        while runFlag():
            self.strip.rotate_right(1)
            self.rest()
            self.strip.show()

        print('done running ColorWave')

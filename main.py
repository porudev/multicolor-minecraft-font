from math import sqrt
from PIL import Image, ImageDraw, ImageFont


def draw_minecraft_font(image, text, font_size, x, y):
    shadow = list(text)
    while '§' in "".join(shadow):
        uncoloured_text_location = shadow.index('§')
        del shadow[uncoloured_text_location: uncoloured_text_location+2]
    shadow = ''.join(shadow)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("minecraft_font.ttf", font_size)
    colours = {
        '4': '#AA0000',
        'c': '#FF5555',
        '6': '#FFAA00',
        'e': '#FFFF55',
        '2': '#00AA00',
        'a': '#55FF55',
        'b': '#55FFFF',
        '3': '#00AAAA',
        '1': '#0000AA',
        '9': '#5555FF',
        'd': '#FF55FF',
        '5': '#AA00AA',
        'f': '#FFFFFF',
        '7': '#AAAAAA',
        '8': '#555555',
        '0': '#000000'
    }
    reference = 'off'
    b = 0

    def colour(c):
        global reference, n
        if c == '§':
            reference = 'on'
            return reference
        else:
            if reference == 'on':
                n = c
                reference = 'off'
                return 'on'
            else:
                return colours[n]

    if '+' in shadow:
        for c in shadow:
            x2 = y + font.getsize(c)[1] / 8.5 + b
            y2 = y + font.getsize(c)[1] / 8.5
            if c == '+':
                h = font.getsize(c)[1]
                y2 -= h / 10
            draw.text(xy=(x2, y2), text=f"{c}", font=font, fill=f'#555555')
            b += font.getsize(c)[0]
            if c == '+':
                y2 += h / 10
    else:
        x2 = y + font.getsize('a')[1] / 8.5 + b
        y2 = y + font.getsize('a')[1] / 8.5
        draw.text(xy=(x2, y2), text=f"{shadow}", font=font, fill=f'#555555')

    for c in text:
        if c == '+':
            h = font.getsize(c)[1]
            y -= h / 10
        if colour(c) != 'on':
            draw.text(xy=(x, y), text=f"{c}", font=font, fill=f'{colour(c)}')
            x += font.getsize(c)[0]
            if c == '+':
                y += h / 10

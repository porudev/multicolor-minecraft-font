from math import sqrt

from PIL import ImageDraw, ImageFont


def draw_minecraft_font(image, text, x, y, size):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("assets/fonts/minecraft_font.ttf", size)
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
    
    res = 'off'
    x2 = x + sqrt(size)/2
    y2 = y + sqrt(size)/2

    def colour(c):
        global res, n
        if c == '§' or c == '&':
            res = 'on'
            return res
        else:
            if res == 'on':
                n = c
                res = 'off'
                return 'on'
            else:
                return colours[n]

    for c in text:
        if c == '+':
            y2 -= 5
        if colour(c) != 'on':
            draw.text(xy=(x2, y2), text=f"{c}", font=font, fill=f'#2A2A2A')
            x2 += font.getsize(c)[0]
            if c == '+':
                y2 += 5

    for c in text:
        if c == '+':
            y = -5
        if colour(c) != 'on':
            draw.text(xy=(x, y), text=f"{c}", font=font, fill=f'{colour(c)}')
            x += font.getsize(c)[0]
            if c == '+':
                y += 5

#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont


def add_roll(char):
    if char == '@':
        return 1
    return 0

def remove(lines):
    cleared = []
    accessible = 0
    for line_no, line in enumerate(lines):
        cleared.append('')
        for char_no, char in enumerate(line.rstrip()):
            if char != "@":
                cleared[line_no]+='.'
                #print('.', end='')
                continue
            rolls = 0
            top = line_no - 1
            bottom = line_no + 1
            left = char_no - 1
            right = char_no + 1
            if top >= 0:
                if left >= 0:
                    rolls+=add_roll(lines[top][left])
                rolls+=add_roll(lines[top][char_no])
                if right < len(lines):
                    rolls+=add_roll(lines[top][right])
            if left >= 0:
                rolls+=add_roll(lines[line_no][left])
            if right < len(lines):
                rolls+=add_roll(lines[line_no][right])
            if bottom < len(lines):
                if left >= 0:
                    rolls+=add_roll(lines[bottom][left])
                rolls+=add_roll(lines[bottom][char_no])
                if right < len(lines):
                    rolls+=add_roll(lines[bottom][right])
            if rolls < 4:
                accessible+=1
                cleared[line_no]+='x'
                #print('x', end='')
            else:
                cleared[line_no]+='@'
                #print('@', end='')
        #print("\n", end='')
    return(accessible, cleared)

def ascii_to_image(ascii_lines, font_size=16, font_path='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'):
    font = ImageFont.truetype(font_path)
    width = 850
    height = len(ascii_lines) * font_size
    img = Image.new("RGB", (width, height), color="black")
    draw = ImageDraw.Draw(img)
    for i, line in enumerate(ascii_lines):
        draw.text((0, i * font_size), line, font=font, fill="green")
    return img


with open("../data/day4_input.txt") as f:
    lines = f.readlines()
    cleared = lines
    accessible = 1
    frames = []
    removed = 0
    while accessible > 0:
        accessible, cleared = remove(cleared)
        frames.append(ascii_to_image(cleared))
        removed += accessible
        print(f"Accessible this round: {accessible}")
    print(f"Total removed: {removed}")
    if frames:
        frames[0].save(
         "animation.gif",
         save_all=True,
         append_images=frames[1:],
         duration=200,
         loop=0
        )
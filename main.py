#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""

Quick & dirt script to convert a string bitwise into a PNG raster graphics file format.

Requires Python 3.3+ and Pillow  (see requirements.txt)

"""

import sys
if sys.version_info[0:2] < (3, 3):
    raise "Must be using Python 3.3+"

try:
    from PIL import Image
except ImportError:
    print("\n\nRequires Pillow. See requirements.txt\n\n")

# String is not longer then 8 ASCII characters
STRING = 'AnOctet'
# Basic image size
B_WIDTH = 8
B_HEIGHT = 8
# Updated image size
U_WIDTH = 512
U_HEIGHT = 512
# Bit state related color A Bit value from 7 bits characters set and value painted
#C_7BITS_0 = (154, 205, 50, 255) #yellowgreen
#C_7BITS_1 = (0, 191, 255, 255)  #deepbluesky
C_7BITS_0 = (255, 255, 255, 255) #white
C_7BITS_1 = (0, 191, 255, 255)  #deepbluesky
# Parity bits bitwise color
C_PBITS_0 = (255, 255, 255, 255) 
C_PBITS_1 = (255, 69, 0, 255)  #redorange
# Debug
DEBUG = 1


def chars_to_bin(string):
    """
    Convert characters of a string to a 7 bits long binary format
    """
    #return ['{:b}'.format(ord(character)) for character in string]

    list_of_7bits_items = ['{:b}'.format(ord(character)) for character in string]

    if len(list_of_7bits_items)<8:
        for i in range (8 - len(list_of_7bits_items)):
            list_of_7bits_items.append('{0:07b}'.format(ord(' ')))

    return list_of_7bits_items


def parity_bit_octets(list_of_7bits_items):
    list_octets_items = []
    """
    Adding a parity bit to 7 bits to make an octet
    """

    for char_of_7bits in list_of_7bits_items:
        str_to_int = list(map(int, char_of_7bits))
        # add parity bit
        str_to_int.append((sum(str_to_int)+1)%2)
        list_octets_items.append(str_to_int)
    return list_octets_items

def generate_image(b_width, b_height, list_octets_items, debug, u_width, u_height):
    """
    Generate an image from list of octets

    """
    #Create basic image using basic width and height
    b_image = Image.new('RGBA', (b_width, b_height), 'black')

    #Create pixel map
    pixel_map = b_image.load()

    # Columns and rows are indexed to the width and height of the pixel map respectively.
    # Pixel map is generated from the defined basic width and height. The 7th bits/pixels
    # in a row are defined as a parity bit. Those painted in red (1) and white (0).
    # Rest of bits/pixels from 0-6 in a row are in blue (0) and green (1).
    for column in range(b_image.size[0]):
        for row in range(b_image.size[1]):
            if row != 7:
                if list_octets_items[column][row]:
                    pixel_map[column, row] = C_7BITS_1
                else:
                    pixel_map[column, row] = C_7BITS_0
            else:
                if list_octets_items[column][row]:
                    pixel_map[column, row] = C_PBITS_1
                else:
                    pixel_map[column, row] = C_PBITS_0
            if debug:
                print("col: ", column, "row:", row, "bit:", list_octets_items[column][row], "RGBA:", pixel_map[column, row])
            else:
                pass

    # Resizing and transforming of generated basic image in to updated image. Save and show result.
    u_image = b_image.resize((u_width, u_height), Image.BOX).rotate(90).transpose(Image.FLIP_TOP_BOTTOM)
    u_image.save('logo.png')
    u_image.show()

"""
Main function

"""

def main():
    list_7bits_items = chars_to_bin(STRING)
    list_octets_items = parity_bit_octets(list_7bits_items)

    if DEBUG:
        print(list_7bits_items)
        print(list_octets_items)
        generate_image(B_WIDTH, B_HEIGHT, list_octets_items, DEBUG, U_WIDTH, U_HEIGHT)
    else:
        generate_image(B_WIDTH, B_HEIGHT, list_octets_items, DEBUG, U_WIDTH, U_HEIGHT)



if __name__ == "__main__":
    main()

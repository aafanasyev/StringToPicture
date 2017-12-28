# StringToPicture

Convert a string to picture
===========================

This script generates an 8x8 pixels raster graphic file in PNG format. Multiple formats are supported. An image is generated bitwise from an 8 character ASCII string.
Color of pixels depends on the state of a single bit, grabbed from a character represented in 7 bits ASCII format plus 1 parity bit (one octet).
The 8x8 pixel map filled with values from a list of 8 elements where 8 bits each. Color values could be set manually for set of 7 bits and a parity bit.

Usage
=====
Download script.

Set preferred values for:
    # String is not longer then 8 ASCII characters
    STRING = 'mainline'
    # Basic image size
    B_WIDTH = 8
    B_HEIGHT = 8
    # Updated image size
    U_WIDTH = 512
    U_HEIGHT = 512
    # Bit state related color A Bit value from 7 bits characters set and value painted
    C_7BITS_0 = (0,191,250,255)
    C_7BITS_1 = (0,128,0,255)
    # Parity bits bitwise color
    C_PBITS_0 = (255,255,255,255) 
    C_PBITS_1 = (255,69,0,255)

Execute script by:
    $ python main.py

This will produce an decent-looking image of a bitwise colored 8 ASCII characters string.
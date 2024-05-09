#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """Initialize a variable to keep track of the number of bytes in the current UTF-8 character
    """
    num_bytes = 0

    for num in data:

        if num >> 6 == 0b10:

            num_bytes -= 1

            if num_bytes < 0:
                return False
        else:

            if num >> 7 == 0b0:
                num_bytes = 0
            elif num >> 5 == 0b110:
                num_bytes = 1
            elif num >> 4 == 0b1110:
                num_bytes = 2
            elif num >> 3 == 0b11110:
                num_bytes = 3
            else:

                return False
                return num_bytes == 0

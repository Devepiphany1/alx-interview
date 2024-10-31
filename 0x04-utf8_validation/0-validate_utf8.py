#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes expected for the current character
    num_bytes_expected = 0

    for byte in data:
        # Get the 8 least significant bits of the byte
        byte &= 0xFF
        
        if num_bytes_expected == 0:
            # Determine how many bytes the current character will use
            if (byte >> 7) == 0b0:  # 1-byte character (0xxxxxxx)
                num_bytes_expected = 0
            elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                num_bytes_expected = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                num_bytes_expected = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                num_bytes_expected = 3
            else:
                return False  # Invalid first byte
        else:
            # Check for continuation bytes (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes_expected -= 1

    # If we are expecting more bytes, it's invalid
    return num_bytes_expected == 0
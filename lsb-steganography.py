from PIL import Image

def encode_text_in_image(image_path, text):
    # open image
    img = Image.open(image_path)

    # check format
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    width, height = img.size
    pixels = img.load()

    # convert text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    binary_length = format(len(binary_text), '016b')

    index = 0

    # iterating through every pixel of image
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]

            # hiding text length to the first 16 pixels
            if index < len(binary_length):
                new_r = int(bin(r)[2:-1] +binary_length[index], 2)
                pixels[x, y] = (new_r, g, b, a)
                index += 1
            # hiding text
            elif index < len(binary_text) + len(binary_length):
                new_r = int(bin(r)[2:-1] + binary_text)
                pixels[x, y] = (new_r, g, b, a)
                index += 1
            else:
                break

        if index >= len(binary_text) + len(binary_length):
            break

    # saving image
    img.save("encoded.jpg")
    print("text encoded into image")

def decode_text_from_image(image_path):
    # open image
    img = Image.open(image_path)

    # check format
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    width, height = img.size
    pixels = img.load()

    binary_length = ''
    binary_text = ''
    decoded_text = ''

    index = 0

    # iterating through every pixel of image
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]

            # extract last bit of pixel r-channel
            last_bit = bin(r)[-1]

            if index < 16:
                binary_length += last_bit
            else:
                binary_text += last_bit

            index += 1

            if index == 16 + len(binary_text):
                break

        if index == 16 + len(binary_text):
            break

    length = int(binary_length, 2)

    # decoding text
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        decoded_text += chr(int(byte, 2))

    return decoded_text[:length]

# encode
encode_text_in_image("input.jpg", "Hello, world!")

# decode
decoded_text = decode_text_from_image("encoded.jpg")
print(f"Decoded text: {decoded_text}")
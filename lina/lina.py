from PIL import Image
import os
import argparse

DELIMETER = "#|#|#|#"

class SizeOverError(Exception):
    pass

def list_imagepath(dr):
    imagenames = list(filter(lambda x: x.endswith(".png"), os.listdir(dr)))
    imagepaths = []
    for imagename in imagenames:
        imagepath = dr + "/" + imagename
        imagepaths.append(imagepath)
    return imagepaths


def list_images(imagepaths):
    images = []
    for imagepath in imagepaths:
        images.append(Image.open(imagepath))
    return images

def capacity_of_images(images):
    result = 0
    for image in images:
        result += capacity_of_image(image)
    return result


def message_to_binary(message):
    if type(message) == str:
        return ''.join([ format(ord(i), "08b") for i in message])
    elif type(message) == bytes:
        return [ format(i, "08b") for i in message ]
    elif type(message) == bytearray:
        return [ format(i, "08b") for i in bytes(message) ]
    elif type(message) == int:
        return format(message, "08b")

def setlsb(component, bit):
    return component & ~1 | int(bit)

def getbit(c):
    return c & 1


def split(binary):
    index = 0
    n_array = []
    while index < len(binary):
        if len(binary) - index < 8:
            break
        byte = ""
        for i in range(0, 8):
            byte += binary[index + i]
        n = int(byte, 2)
        n_array.append(n)
        index += 8
    return bytearray(bytes(n_array))

def cut_bytes(data):
    delimeter = DELIMETER.encode()
    delimeter = bytearray(delimeter)
    j = 0
    for i in range(len(data)):
        if data[i] == delimeter[j]:
            j = j + 1
        else:
            j = 0
        if j >= len(delimeter):
            return data[:i - len(delimeter) + 1]
    return data



def reveal(image):
    width, height = image.size
    binary = ""
    delimeter = DELIMETER.encode()
    delimeter = message_to_binary(delimeter)
    delimeter = "".join(delimeter)
    buf = ""
    for row in range(height):
        for col in range(width):
            pixel = image.getpixel((col, row))
            if image.mode == "RGBA":
                pixel = pixel[:3]
            for color in pixel:
                if len(buf) == len(delimeter):
                    buf = buf[1:len(delimeter)]
                buf += str(getbit(color))
                binary += str(getbit(color))
                if buf == delimeter:
                    return cut_bytes(split(binary))
    return cut_bytes(split(binary))
                
def capacity_of_image(image):
    width, height = image.size
    len_del = len(bytearray(DELIMETER.encode()))
    return (width * height * 3) // 8 - len_del

def hide(image, data):
    if image.mode not in ["RGB", "RGBA"]:
        image = image.convert("RGB")
    encoded = image.copy()
    width, height = image.size
    n_bytes = width * height * 3 // 8
    file_bytes = len(data)
    delimeter = DELIMETER.encode()
    delimeter = bytearray(delimeter)
    if file_bytes + len(delimeter) > n_bytes:
        raise SizeOverError("file size is too large")
    index = 0
    content = data
    content = bytearray(content)
    content.extend(delimeter)
    binary_content = message_to_binary(content)
    binary = "".join(binary_content)
    len_binary = len(binary)
    for row in range(height):
        for col in range(width):
            if index < len_binary:
                pixel = image.getpixel((col, row))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                r = setlsb(r, binary[index])
                if index + 1 < len_binary:
                    g = setlsb(g, binary[index + 1])
                if index + 2 < len_binary:
                    b = setlsb(b, binary[index + 2])
                if image.mode == "RGBA":
                    encoded.putpixel((col, row), (r, g, b, pixel[3]))
                else:
                    encoded.putpixel((col, row), (r, g, b))
                index += 3
            else:
                image.close()
                return encoded
    return encoded


from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


def create_aes(password, iv):
    sha = SHA256.new()
    sha.update(password.encode())
    key = sha.digest()
    return AES.new(key, AES.MODE_CFB, iv)

def encrypt(data, password):
    iv = Random.new().read(AES.block_size)
    return iv + create_aes(password, iv).encrypt(data)


def decrypt(data, password):
    iv, cipher = data[:AES.block_size], data[AES.block_size:]
    return create_aes(password, iv).decrypt(cipher)

def hide_into_album(filepath, password, fr, to):
    imagepaths = list_imagepath(fr)
    imagepaths.sort(reverse=True)
    images = list_images(imagepaths)
    f = open(filepath, "rb")
    data = f.read()
    encrypted = encrypt(data, password)
    len_encrypted = len(encrypted)
    if capacity_of_images(images) < len_encrypted:
        raise SizeOverError("size over")
        return
    remain = bytearray(encrypted)
    for image in images:
        capacity = capacity_of_image(image)
        size = capacity
        if len(remain) < capacity:
            size = len(remain)
        encoded = hide(image, remain[:size])
        encoded.save(to + "/" + os.path.basename(image.filename))
        remain = remain[size:]
        image.close()
    f.close()

def reveal_from_album(password, fr, output_file):
    imagepaths = list_imagepath(fr)
    imagepaths.sort(reverse=True)
    images = list_images(imagepaths)
    f = open(output_file, "wb")
    result = bytearray()
    for image in images:
        result.extend(reveal(image))
        image.close()
    result = bytes(result)
    result = decrypt(result, password)
    f.write(result)
    f.close()

def main():
    parser = argparse.ArgumentParser(description="lina is a steganography program. It can hide a binary file or a text file into multiple png images. ")
    parser.add_argument("mode", help="hide or reveal")
    parser.add_argument("-p", "--password")
    parser.add_argument("-i", "--in", help="input")
    parser.add_argument("-o", "--out", help="output")
    parser.add_argument("-d", "--file")
    args = vars(parser.parse_args())
    if args["mode"] == "hide":
        if args["password"] == None or args["file"] == None or args["in"] == None or args["out"] == None:
            parser.print_help()
            return
        hide_into_album(args["file"], args["password"], args["in"], args["out"])
    elif args["mode"] == "reveal":
        if args["password"] == None or args["in"] == None or args["out"] == None:
            parser.print_help()
            return
        reveal_from_album(args["password"], args["in"], args["out"])
    else:
        parser.print_help()
    
if __name__ == "__main__":
    main()

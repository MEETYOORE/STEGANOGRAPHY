# Python program implementing Image Steganography

# PIL module is used to extract
# pixels of image and modify it
from PIL import Image

# use to create an image of x,y dimension and set individual pixel
def create_image(x_dimension,y_dimension):
    # Create a new image with mode 'RGB' and size (width, height)
    image = Image.new('RGB', (x_dimension, y_dimension))

    # Set custom RGB values for each pixel
    for y in range(y_dimension):
        for x in range(x_dimension):
            # Set RGB values (R, G, B) for each pixel
            # Set pixel color based on even/odd positions
            if (x + y) % 2 == 0:
                # Even position: set pixel to white (255, 255, 255)
                image.putpixel((x, y), (255, 255, 255))
            else:
                # Odd position: set pixel to black (0, 0, 0)
                image.putpixel((x, y), (0, 0, 0))

    # Save the image
    image.save('/Users/rohit/Desktop/custom_image.png')

    # Show the image (optional)
    image.show()

#check the pixel RGB values 
def checkPixels(image_path):
    # Open the image
    image = Image.open(image_path)

    # Get the image size
    height = image.height
    width  = image.width

    # Iterate through each pixel
    for y in range(0,10):
        for x in range(0,1):
            # Get the RGB values of the pixel
            pixel = image.getpixel((x, y))
            print(f"Pixel at ({x}, {y}): {pixel}")

# Convert encoding data into 8-bit binary form using ASCII value of characters
            
def generate_Binary_Data(data):
    # list of binary codes of given data
    binary_list = []

    for i in data:
        binary_list.append(format(ord(i), '08b')) #convert to ascii then format to 8 bit binary string

    print(binary_list)
    binary_to_ascii_string(binary_list)
    return binary_list

def binary_to_ascii_string(bytes_list):
    # Convert each byte to ASCII character
    ascii_string = ''.join([chr(int(byte, 2)) for byte in bytes_list]) #convert string byte into base 2 

    print("ASCII representation:", ascii_string)


# Pixels are modified according to the 8-bit binary data and finally returned
def modPix(pix, data):

    datalist = generate_Binary_Data(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                # pix[j] -= 1

        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1


# Encode data into image
def encode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')

    data = input("Enter data to be encoded : ")
    if (len(data) == 0):
        raise ValueError('Data is empty')

    newimg = image.copy()
    encode_enc(newimg, data)

    new_img_name = input("Enter the name of new image(with extension) : ")
    # Assuming new_img_name is in the format "filename.extension"

    # Extract the file format (extension) from the filename
    file_format = new_img_name.split(".")[-1].upper()

    # Save the image with the specified file format
    newimg.save(new_img_name, file_format)


# Decode the data in the image
def decode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data


# Main Function
def main():
    a = int(input(":: Welcome to Steganography ::\n"
                        "1. Encode\n2. Decode\n"))
    if (a == 1):
        encode()

    elif (a == 2):
        print("Decoded Word :  " + decode())
    else:
        raise Exception("Enter correct input")

# Driver Code
if __name__ == '__main__' :

    # Calling main function
    main()
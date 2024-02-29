from PIL import Image

def create_image(x_dimension,y_dimension):
    # Create a new image with mode 'RGB' and size (width, height)
    image = Image.new('RGB', (x_dimension, y_dimension))

    # Set custom RGB values for each pixel
    for y in range(y_dimension):
        for x in range(x_dimension):
            # Set RGB values (R, G, B) for each pixel
            # Here, we set the pixel color based on its position
            # For demonstration, we use x and y values to determine RGB values
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

# Call the function with the path to the new image
print("before")
checkPixels("/Users/rohit/Desktop/custom_image.png")

print("after")
checkPixels("/Users/rohit/Desktop/img.png")


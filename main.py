from PIL import Image, ImageEnhance

ASCII_CHARS = ["@", "#", "8", "&", "o", ":", "*", ".", " "]

def resize(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def gray(image):
    return image.convert("L")

def enhance_contrast(image, factor=1.5):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 32] for pixel in pixels])
    return ascii_str

def main(new_width=100):
    path = input("Enter the path to an image: ")
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Unable to open image file. {e}")
        return
    
    image = resize(image, new_width)
    image = gray(image)
    image = enhance_contrast(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_img = "\n".join([ascii_str[index: index + img_width] for index in range(0, len(ascii_str), img_width)])

    print(ascii_img)
    
    with open("output.txt", "w") as f:
        f.write(ascii_img)

if __name__ == "__main__":
    main()

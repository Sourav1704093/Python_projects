from types import resolve_bases
import PIL

#create a list of ascii characters to build our output image
ascii_chars = ["@","#","$","%","?","*","+",",","*",".",":",";"]

#resize image
def resize_img(image,new_width = 100):
    width,height = image.size
    ratio = height/width
    new_height = int(new_width*ratio)
    resize_image = image.resize((new_width,new_height))
    return resize_image

#now convert the image into a grayscale image
def to_gray(image):
    grayscale_img = image.convert("L")
    return grayscale_img

def pixel_to_ascii(image):
    pixels = image.getdata()
    characters= "".join([ascii_chars[pixel//25] for pixel in pixels])
    return characters

def main(new_width = 100):
    #we will attempt to open an image for this project
    path = input("Enter the image path:")
    try:
        image = PIL.Image.open(path)
    except:
        print(path," is not valid")
        return
    
    new_img = pixel_to_ascii(to_gray(resize_img(image)))
    
    #formating method
    pixel_cnt = len(new_img)
    ascii_img = "\n".join([new_img[index:(index+new_width)] for index in range(0,pixel_cnt,new_width)])
    
    print(ascii_img)

main()

# Class used to test api functions locally
from FlowchartObjectDetection import detect
from PIL import Image


def main():
    img: Image = Image.open('./TestStuff/HelloWorld7.jpg')
    detect(img)


if __name__ == "__main__":
    main()

import sys
from PIL import Image

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: %s palette_image" % sys.argv[0]
        sys.exit(1)

    im = Image.open(sys.argv[1])
    rgb_im = im.convert('RGB')

    palette = []
    for idx in range(0, 255):
        palette.append(list(rgb_im.getpixel((idx, 0))))

    with open("palette.js", "w") as f:
        f.write("var palette = " + str(palette) + ";\n")


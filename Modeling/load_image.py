from pygame import image


def load_image(filename):
    return image.load(f"Source/Textures/{filename}.png")

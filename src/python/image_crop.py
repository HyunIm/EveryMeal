from PIL import Image


def image_cropping(name, rectangle):
    image_path = "../html/image/meal.jpg"
    (left, upper, right, lower) = rectangle

    with Image.open(image_path) as im:
        im_crop = im.crop((left, upper, right, lower))
        im_crop.save("../html/image/" + name + ".jpg")


def execute_image_crop():
    print("execute_image_crop...")
    
    image_cropping("week", (335, 485, 2285, 1105))

    image_cropping("mon", (360, 485, 750, 1100))
    image_cropping("tue", (750, 485, 1165, 1100))
    image_cropping("wed", (1165, 485, 1540, 1100))
    image_cropping("thu", (1540, 485, 1900, 1100))
    image_cropping("fri", (1900, 485, 2285, 1100))

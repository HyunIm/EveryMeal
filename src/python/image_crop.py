from PIL import Image


def image_cropping(name, rectangle):
    image_path = "../html/image/meal.jpg"
    (left, upper, right, lower) = rectangle

    with Image.open(image_path) as im:
        im_crop = im.crop((left, upper, right, lower))
        im_crop.save("../html/image/" + name + ".jpg")


def execute_image_crop():
    print("execute_image_crop...")
    
    image_cropping("week", (360, 480, 2220, 1090))

    image_cropping("mon", (360, 480, 730, 1090))
    image_cropping("tue", (730, 480, 1130, 1090))
    image_cropping("wed", (1135, 480, 1470, 1090))
    image_cropping("thu", (1475, 480, 1845, 1090))
    image_cropping("fri", (1845, 480, 2220, 1090))

    image_cropping("division", (110, 480, 360, 1090))
    image_cropping("date", (360, 165, 2220, 265))

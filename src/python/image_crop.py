from PIL import Image


def image_cropping(name, rectangle):
    image_path = "../html/image/meal.jpg"
    (left, upper, right, lower) = rectangle

    with Image.open(image_path) as im:
        im_crop = im.crop((left, upper, right, lower))
        im_crop.save("../html/image/" + name + ".jpg")


def execute_image_crop():
    print("execute_image_crop...")

    a = 325
    b = 725
    c = 1130
    d = 1515
    e = 1890
    f = 2275

    image_cropping("week", (a, 485, 2285, 1105))

    image_cropping("mon", (a, 485, b, 1100))
    image_cropping("tue", (b, 485, c, 1100))
    image_cropping("wed", (c, 485, d, 1100))
    image_cropping("thu", (d, 485, e, 1100))
    image_cropping("fri", (e, 485, f, 1100))

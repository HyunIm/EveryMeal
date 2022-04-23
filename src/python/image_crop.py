from PIL import Image


def image_cropping(name, rectangle):
    image_path = "../html/image/meal.jpg"
    (left, upper, right, lower) = rectangle

    with Image.open(image_path) as im:
        im_crop = im.crop((left, upper, right, lower))
        im_crop.save("../html/image/" + name + ".jpg")


def execute_image_crop():
    print("execute_image_crop...")

    a = 320
    b = 715
    c = 1125
    d = 1510
    e = 1890
    f = 2280

    top = 440
    bottom = 1080

    image_cropping("week", (a, top, f, bottom))

    image_cropping("mon", (a, top, b, bottom))
    image_cropping("tue", (b, top, c, bottom))
    image_cropping("wed", (c, top, d, bottom))
    image_cropping("thu", (d, top, e, bottom))
    image_cropping("fri", (e, top, f, bottom))

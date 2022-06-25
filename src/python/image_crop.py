from PIL import Image


def image_cropping(name, rectangle):
    image_path = "../html/image/meal.jpg"
    (left, upper, right, lower) = rectangle

    with Image.open(image_path) as im:
        im_crop = im.crop((left, upper, right, lower))
        im_crop.save("../html/image/" + name + ".jpg")


def execute_image_crop(location):
    print("execute_image_crop...")

    if location == '을지로':
        mon = 320
        tue = 715
        wed = 1125
        thu = 1510
        fri = 1890
        end = 2280
        top = 470
        bottom = 1065
    elif location == '명동':
        mon = 430
        tue = 755
        wed = 1080
        thu = 1405
        fri = 1735
        end = 2065
        top = 410
        bottom = 970

    image_cropping("week", (mon, top, end, bottom))

    image_cropping("mon", (mon, top, tue, bottom))
    image_cropping("tue", (tue, top, wed, bottom))
    image_cropping("wed", (wed, top, thu, bottom))
    image_cropping("thu", (thu, top, fri, bottom))
    image_cropping("fri", (fri, top, end, bottom))

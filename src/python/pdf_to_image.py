from pdf2image import convert_from_path

images = convert_from_path("data/meal.pdf")

images[0].save("../html/image/meal.jpg", "JPEG")

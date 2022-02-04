from pdf2image import convert_from_path


def execute_pdf_to_image():
    print("execute_pdf_to_image...")
    
    images = convert_from_path("data/meal.pdf")
    images[0].save("../html/image/meal.jpg")

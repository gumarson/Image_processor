from PIL import Image, ImageFilter

def to_grayscale(input_path, output_path):
    image = Image.open(input_path).convert("L")
    image.save(output_path)

def blur(input_path, output_path, radius=2):
    image = Image.open(input_path)
    blurred = image.filter(ImageFilter.GaussianBlur(radius))
    blurred.save(output_path)

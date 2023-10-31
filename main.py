## QR Code Generator using Python

import re
import qrcode as qr

# Function to validate a URL using regex
def validate_url(url):
    # Use a regular expression to check if the URL matches a valid format
    url_pattern = re.compile(r'^(http|https)://[a-zA-Z0-9\-.]+(\.[a-zA-Z]{2,5})(:[0-9]{1,5})?(/.*)?$')
    return url_pattern.match(url)

# Function to get user input for a valid URL
def get_valid_url():
    while True:
        link = input("Enter the URL: ")
        if validate_url(link):
            print(f"{link} is a valid and reachable URL\n")
            return link
        else:
            print(f"{link} is not valid and reachable URL.\nPlease try Again!\n")
            get_valid_url()

# Define a dictionary to map format choices to extensions
format_extensions = {
    '1':'jpg',
    '2':'png',
    '3':'svg',
}
# Function to get the image format choice
def get_image_format():
    while True:
        print("Select which format to save your img: ")
        print("1. jpg")
        print("2. png")
        print("3. svg")
        print("4. Quit")
        img_format = input("Enter (1/2/3/4) : ")
        if img_format == '4':
            print("Goodbye!")
            exit(0)
        elif img_format not in format_extensions:
            print(f"{img_format} is not a valid input.\nPlease Try Again!")
            get_image_format()
        else:
            return format_extensions[img_format]

# Function to generate a black and white QR Code
def generate_simple_qrcode():
    url = get_valid_url()
    img_format=get_image_format()
    name = input("File Name: ")

    img = qr.make(url)
    img.save(f"{name}.{img_format}")
    print(f"QR code successfully generated and saved as {name}.{img_format}")

# Function to generate a QR Code with customized color
def generate_custom_color_qrcode():
    url = get_valid_url()
    img_format = get_image_format()
    name = input("File Name: ")
    fcolor = input("Fill Color: ")
    bcolor = input("Background Color: ")

    qrs = qr.QRCode(version=2, error_correction=qr.constants.ERROR_CORRECT_H,box_size=10, border=4)
    qrs.add_data(url)
    qrs.make(fit=True)
    img = qrs.make_image(fill_color= fcolor, back_color = bcolor)
    img.save(f"{name}.{img_format}")
    print(f"QR code successfully generated and saved as {name}.{img_format}")

# Function to generate a QR Code with Customized and size
def generate_custom_color_size_qrcode():
    url = get_valid_url()
    img_format = get_image_format()
    name = input("File Name: ")
    fcolor = input("Fill Color: ")
    bcolor = input("Background Color: ")
    img_size = int(input("Size: "))

    qrs = qr.QRCode(version=2, error_correction=qr.constants.ERROR_CORRECT_H,box_size=img_size,border=4)
    qrs.add_data(url)
    qrs.make(fit=True)
    img = qrs.make_image(fill_color = fcolor, back_color = bcolor)
    img.save(f"{name}.{img_format}")
    print(f"QR code successfully generated and saved as {name}.{img_format}")

# Main Program
def main():
    while True:
        print("Hi, Welcome to QR CODE Generator")
        print("Select which type of QRCode you want to generate:")
        print("1. Simple QRCode (B&W)")
        print("2. Customised Color QRCode")
        print("3. Customised Color and Size QRCode")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            generate_simple_qrcode()
        elif choice == '2':
            generate_custom_color_qrcode()
        elif choice == '3':
            generate_custom_color_size_qrcode()
        elif choice == '4':
            exit(0)
        else:
            print(f"{choice} is invalid! \nTry Again!!")




if __name__ == "__main__":
    main()




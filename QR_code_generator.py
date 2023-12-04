import qrcode
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Enter url of any website here.
input_URL = "https://www.google.com/"

# Sanitize the URL to include in the filename
sanitized_url = input_URL.replace('https://', '').replace('http://', '').replace('/', '_').replace('.', '_')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

try:
    logging.info('Starting QR code generation.')
    qr.add_data(input_URL)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color="red", back_color="white")
    filename = f"{sanitized_url}_qrcode.png"
    img.save(filename)
    logging.info(f'QR code image saved as {filename}')
except Exception as e:
    logging.error(f'An error occurred during QR code generation or saving: {e}')

print(qr.data_list)

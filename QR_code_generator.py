import qrcode
import logging
from logging.handlers import RotatingFileHandler

# Logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[RotatingFileHandler('qr_code_generator.log', maxBytes=1e6, backupCount=5, mode='a')])

# Enter url of any website here.
input_URL = "https://www.google.com/"

try:
    logging.info('Starting QR code generation process.')

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(input_URL)
    qr.make(fit=True)

    # convert into image
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("url_qrcode.png")

    logging.info('QR code image successfully created.')
except Exception as e:
    logging.error('An error occurred during QR code generation: %s', str(e))

print(qr.data_list)

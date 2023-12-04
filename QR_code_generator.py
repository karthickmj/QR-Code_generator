import qrcode
import logging
from logging.handlers import RotatingFileHandler
import os

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

    logging.debug('QR code configuration set.')

    qr.add_data(input_URL)
    qr.make(fit=True)

    logging.debug('QR code data added and fit to size.')

    # convert into image
    img = qr.make_image(fill_color="red", back_color="white")
    url_safe_name = os.path.basename(input_URL).replace('http://', '').replace('https://', '').replace('/', '_')
    file_name = f"{url_safe_name}_qrcode.png"
    img.save(file_name)

    logging.info(f'QR code image successfully created: {file_name}')
except Exception as e:
    logging.error('An error occurred during QR code generation: %s', str(e))

logging.debug('QR code data list: %s', qr.data_list)
print(qr.data_list)

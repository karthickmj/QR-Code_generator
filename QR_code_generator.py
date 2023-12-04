import qrcode
import logging
from logging.handlers import RotatingFileHandler

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[RotatingFileHandler('qr_code_generator.log', maxBytes=5000, backupCount=2),
                              logging.StreamHandler()])

logger = logging.getLogger(__name__)

try:
    logger.info('Starting QR code generation')

    # Enter url of any website here.
    input_URL = "https://www.google.com/"

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

    logger.info('QR code generated and saved successfully')
except Exception as e:
    logger.error('An error occurred while generating the QR code: %s', e)
finally:
    logger.info('QR code generation process completed')

print(qr.data_list)

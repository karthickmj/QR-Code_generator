import qrcode
import logging
from logging.handlers import RotatingFileHandler

# Set up logging
logging.basicConfig(handlers=[RotatingFileHandler('qr_code_generator.log', maxBytes=10000, backupCount=1)],
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Enter url of any website here.
input_URL = "https://www.google.com/"

logging.info('Starting QR code generation')

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

logging.info('QR code generated successfully')
logging.info('QR code image saved as url_qrcode.png')

print(qr.data_list)

import qrcode


def generate_qr_code(data, fill_color='black', back_color='white', file_name='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(file_name)
    return img


def main():
    # Enter url of any website here.
    input_URL = 'https://www.google.com/'
    # Generate QR code
    generate_qr_code(input_URL, fill_color='red', back_color='white', file_name='url_qrcode.png')


if __name__ == '__main__':
    main()

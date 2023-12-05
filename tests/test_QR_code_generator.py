import unittest
import os
from QR_code_generator import generate_qr_code


class TestQRCodeGenerator(unittest.TestCase):

    def test_valid_input(self):
        # Test case for valid input
        input_data = 'Hello, World!'
        output_file = 'test_output.png'
        generate_qr_code(input_data, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

    def test_invalid_input(self):
        # Test case for invalid input
        input_data = ''
        output_file = 'test_output.png'
        with self.assertRaises(ValueError):
            generate_qr_code(input_data, output_file)

    def test_file_output(self):
        # Test case for file output
        input_data = 'Hello, World!'
        output_file = 'test_output.png'
        generate_qr_code(input_data, output_file)
        self.assertTrue(os.path.exists(output_file))
        # Add more assertions if necessary
        os.remove(output_file)


if __name__ == '__main__':
    unittest.main()

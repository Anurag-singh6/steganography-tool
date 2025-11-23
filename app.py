from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Utility to encode text into image
def encode_image(image_path, message, output_path):
    image = Image.open(image_path)
    encoded = image.copy()
    width, height = image.size
    index = 0
    message += '###'  # Delimiter to indicate end of message
    for row in range(height):
        for col in range(width):
            if index < len(message):
                r, g, b = image.getpixel((col, row))
                ascii_val = ord(message[index])
                encoded.putpixel((col, row), (r, g, ascii_val))
                index += 1
    encoded.save(output_path)

# Utility to decode text from image
def decode_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    message = ''

    for row in range(height):
        for col in range(width):
            r, g, b = image.getpixel((col, row))
            message += chr(b)
            if message.endswith('###'):
                return message[:-3]
    return ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    image = request.files['image']
    message = request.form['message']
    if image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'encoded_' + image.filename)
        encode_image(image_path, message, output_path)
        return render_template('result.html', result_image='encoded_' + image.filename, message='Message encoded successfully!')
    return redirect(url_for('index'))

@app.route('/decode', methods=['POST'])
def decode():
    image = request.files['image']
    if image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)
        message = decode_image(image_path)
        return render_template('result.html', result_message=message, message='Message decoded successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)

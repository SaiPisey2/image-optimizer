import logging
import os
import tempfile
from flask import Blueprint, jsonify, request, send_file
from PIL import Image
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from config import Config

main = Blueprint('main', __name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def verify_image(file):
    try:
        img = Image.open(file)
        img.verify()
    except IOError:
        return False
    return True

def get_images_folder():
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
    images_folder = os.path.join(current_dir, 'images')
    logging.info(f"Images folder: {images_folder}")
    
    try:
        os.makedirs(images_folder, exist_ok=True)
    except OSError as e:
        logging.error(f"Failed to create images folder: {e}")
        return None
    
    return images_folder

def compress_image(img, compression_level):
    try:
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), compression_level]
        _, compressed_img = cv2.imencode('.jpg', img, encode_param)
        
        # Check if the compressed image is valid
        if compressed_img is None:
            return None, "The given level of compression is corrupting the image"
        
        # Try to decode the compressed image to check if it's valid
        try:
            decoded_img = cv2.imdecode(compressed_img, cv2.IMREAD_COLOR)
            if decoded_img is None:
                return None, "The given level of compression is corrupting the image"
        except Exception as e:
            return None, "The given level of compression is corrupting the image"
        
        return compressed_img, None
    except Exception as e:
        logger.error(f"Failed to compress image: {e}")
        return None, "Failed to compress image"

def save_image(img, filename):
    try:
        logger.info(f"Saving image to {filename}")
        with open(filename, 'wb') as f:
            f.write(img)
        logger.info(f"Image saved to {filename}")
        return True
    except Exception as e:
        logger.error(f"Failed to save image to {filename}: {e}")
        return False

def send_image(img, filename):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            temp_filename = temp_file.name
            temp_file.write(img)
            return send_file(temp_filename, mimetype='image/jpeg', as_attachment=True, 
                             download_name=filename)
    except Exception as e:
        logger.error(f"Failed to send image: {e}")
        return jsonify({'error': 'Failed to send image'}), 500

@main.route('/')
def index():
    return jsonify({'message': 'Welcome to the image optimizer API'}), 200

@main.route('/upload', methods=['POST'])
def upload():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400

        file = request.files['image']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed'}), 400

        if not verify_image(file):
            return jsonify({'error': 'File is not an image'}), 400

        compression_level = int(request.form.get('compression_level', 50))
        if compression_level < 0 or compression_level > 100:
            return jsonify({'error': 'Compression level must be between 0 and 100'}), 400

        # Read the image file using PIL
        img = Image.open(file)

        # Convert the image to RGB mode
        img = img.convert('RGB')

        # Convert the image to a numpy array
        img_array = np.array(img)

        # Convert the numpy array to a BGR image (required by OpenCV)
        img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # Compress the image
        compressed_img, error = compress_image(img, compression_level)

        if error is not None:
            return jsonify({'error': error}), 400

        # Get the images folder path
        images_folder = get_images_folder()

        # Save the compressed image in the 'images' folder
        filename = secure_filename(file.filename)
        base_filename, _ = os.path.splitext(filename)
        compressed_filename = f"{base_filename}_compressed.jpg"
        compressed_filepath = os.path.join(images_folder, compressed_filename)
        
        if not save_image(compressed_img, compressed_filepath):
            return jsonify({'error': 'Failed to save image'}), 500

        # Send the compressed image
        return send_image(compressed_img, compressed_filename)
    except Exception as e:
        logger.error(f"Failed to process image: {e}")
        return jsonify({'error': 'Failed to process image'}), 500

@main.after_request
def cleanup(response):
    # Clean up the temporary file after sending the response
    temp_file = getattr(response, '_temp_file', None)
    if temp_file:
        os.unlink(temp_file)
    return response
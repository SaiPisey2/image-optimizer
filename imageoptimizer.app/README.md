# Image Optimizer Application

## Overview

The Image Optimizer is a web application built using Flask that allows users to upload images and compress them based on a specified compression level. The application supports various image formats and provides a simple API for image optimization.

## Features

- Upload images in formats such as PNG, JPG, JPEG, and GIF.
- Specify a compression level between 0 and 100.
- Automatically saves compressed images to a designated folder.
- Returns the compressed image for download.

## Technologies Used

- Python
- Flask
- Flask-CORS
- OpenCV
- Pillow (PIL)
- NumPy

## Installation

To set up the Image Optimizer application, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd image-optimiser
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
2. **Run the app:**
   ```bash
   python app/run.py

## API Endpoints
1. Welcome Endpoint
  URL: /
  Method: GET
  Response: A welcome message.
2. Upload Image Endpoint
  URL: /upload
  Method: POST
  Form Data:
  image: The image file to be uploaded.
  compression_level: (Optional) An integer value between 0 and 100 indicating the desired compression level (default is 50).
  Response:
  On success: Returns the compressed image for download.
  On error: Returns an error message with a corresponding HTTP status code.

# Development
## Folder Structure
```
imageoptimizer.app/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main.py
│   └── templates/
│       └── index.html
│
├── tests/
│   ├── __init__.py
│   └── test_routes.py
│
├── config.py
├── requirements.txt
└── run.py
```

## Configuration
- The application configuration is managed in config.py. You can modify the following settings as needed:
- DEBUG: Set to True for development mode, which enables debug information.
- ROOT_PATH: The root path of the application, automatically set to the directory of the configuration file.
## Logging
- The application uses Python's built-in logging module to log important events and errors. The logging level is set to INFO by default. You can adjust the logging level in the main.py file by modifying the logging.basicConfig(level=logging.INFO) line.

## Contributing
- Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

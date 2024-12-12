# Image Optimizer Application
## Overview
The Image Optimizer is a web application designed to optimize images by compressing them while maintaining quality. Built using React and Flask, this application allows users to upload images, select a compression level, and download the optimized images. The application features a user-friendly interface and provides real-time feedback on the image size before and after optimization.

## Features
- Image Upload: Users can upload images in various formats (PNG, JPG, JPEG, GIF).
- Compression Level: Users can select the desired compression level (0-100%) using a slider.
- Image Preview: Displays the original and optimized images along with their sizes.
- Download Option: Users can download the optimized image directly from the application.
- Responsive Design: The application is designed to be responsive and works well on different screen sizes.

## Technologies Used
### Frontend:

React for building the user interface.
Vite for fast development and build processes.
CSS for styling the application.
### Backend:

Flask for creating the API that handles image uploads and processing.
OpenCV and PIL for image manipulation and compression.

### File Structure
```
image-optimiser/
├── imageoptimizer.app/
│   ├── app/
│   │   ├── routes/
│   │   │   └── main.py          # Flask routes for handling image uploads and processing
│   │   └── templates/
│   │       └── index.html       # HTML template for the application
│   └── config.py                # Configuration settings for the Flask app
├── imageoptimizer.web/
│   ├── src/
│   │   ├── App.css              # CSS styles for the React application
│   │   ├── App.jsx              # Main React component
│   │   └── index.css            # Global CSS styles
│   ├── eslint.config.js          # ESLint configuration for code quality
│   └── README.md                 # Documentation for the web application
└── images/                       # Directory for storing uploaded images
```

### Installation
#### Prerequisites
Node.js and npm (for the frontend)
Python 3.x and pip (for the backend)
OpenCV and Pillow libraries for Python
Setup
Clone the repository:
```
git clone <repository-url>
cd image-optimiser
```

### Frontend Setup:

Navigate to the imageoptimizer.web directory.
Install dependencies:
```
npm install
```
Start the development server:
```
npm run dev
```

### Backend Setup:

Navigate to the imageoptimizer.app directory.
Install dependencies:
```
pip install -r requirements.txt
```
Start the Flask server:
```
flask run
```

### Usage
Open the application in your web browser (usually at http://localhost:3000 for the frontend).
Upload an image using the "Choose an Image" button.
Adjust the compression level using the slider.
Click on "Optimize Image" to process the image.
View the original and optimized images along with their sizes.
Download the optimized image using the provided button.

### Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.


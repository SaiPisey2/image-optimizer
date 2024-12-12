## The Image Optimizer is a web application built with React and Vite that allows users to upload images, optimize them by adjusting the quality, and download the optimized images. The application provides a user-friendly interface with real-time previews of both the original and optimized images, along with size reduction statistics.

## Features
Upload images and preview them before optimization.
Adjust the quality of the image using a slider.
View the size of the original and optimized images.
Download the optimized image with a custom filename.
Responsive design for mobile and desktop users.
Technologies Used
React: A JavaScript library for building user interfaces.
Vite: A build tool that provides a fast development environment.
CSS: For styling the application.
Fetch API: For making HTTP requests to the backend for image optimization.
Installation
To set up the Image Optimizer application locally, follow these steps:

## Clone the repository:

```bash
git clone https://github.com/yourusername/image-optimizer.git
cd image-optimizer
```
Install dependencies: Make sure you have Node.js installed. Then run:

```bash
npm install
```
Start the development server:

```bash
npm run dev
```

- This will start the Vite development server, and you can access the application at http://localhost:3000.

- Backend Setup: Ensure you have a backend server running at http://localhost:8015 that handles image uploads and optimizations. You may need to implement this server separately, depending on your requirements.

## Usage
- Upload an Image: Click on the "Choose an Image" button to select an image file from your device. A preview of the original image will be displayed along with its size.

- Adjust Quality: Use the quality slider to set the desired compression level (0% to 100%). The current quality percentage will be displayed.

- Optimize Image: Click the "Optimize Image" button to send the image to the backend for optimization. The optimized image will be displayed along with its size and the percentage of size reduction.

- Download Optimized Image: Click the "Download Optimized Image" button to save the optimized image to your device. The filename will be in the format original_name_optimized.extension.

## Code Structure
- src/: Contains the main application code.
- App.jsx: The main component that handles image upload, optimization, and rendering.
- App.css: The styles for the application.
- public/: Contains static assets like images and icons.

## Development Notes
The application uses React hooks for state management.
The quality slider dynamically updates its background based on the selected value.
Ensure to handle errors gracefully, especially during image uploads and optimizations.
Consider implementing additional features such as drag-and-drop file uploads or support for multiple image uploads.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

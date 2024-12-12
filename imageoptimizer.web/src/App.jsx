import { useState } from 'react'
import './App.css'

function App() {
  const [image, setImage] = useState(null)
  const [imagePreview, setImagePreview] = useState(null)
  const [optimizedImage, setOptimizedImage] = useState(null)
  const [quality, setQuality] = useState(80)
  const [optimizedImageSize, setOptimizedImageSize] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!image) return

    const formData = new FormData()
    formData.append('image', image)
    formData.append('compression_level', quality)

    try {
      console.log('Sending request with compression_level:', quality)
      const response = await fetch('http://localhost:8015/upload', {
        method: 'POST',
        body: formData,
      })
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const blob = await response.blob()
      console.log('Received blob:', blob)
      
      if (!blob.type.startsWith('image/')) {
        console.error('Received non-image response:', blob.type)
        return
      }
      
      const optimizedImageUrl = URL.createObjectURL(blob)
      console.log('Created URL:', optimizedImageUrl)
      
      if (optimizedImage) {
        URL.revokeObjectURL(optimizedImage)
      }
      
      setOptimizedImage(optimizedImageUrl)
      
      const optimizedSize = blob.size
      setOptimizedImageSize(optimizedSize)
      
    } catch (error) {
      console.error('Error during image optimization:', error)
    }
  }

  const handleImageChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0]
      setImage(file)
      
      // Create preview URL for the uploaded image
      const previewUrl = URL.createObjectURL(file)
      setImagePreview(previewUrl)
    }
  }

  const handleSliderChange = (e) => {
    const value = e.target.value;
    setQuality(parseInt(value));
    
    const percentage = (value - e.target.min) / (e.target.max - e.target.min) * 100;
    e.target.style.background = `linear-gradient(to right, var(--primary-color) ${percentage}%, #e2e8f0 ${percentage}%)`;
  }

  // Add this function to handle downloads
  const handleDownload = () => {
    if (optimizedImage) {
      // Create a temporary anchor element
      const link = document.createElement('a')
      link.href = optimizedImage
      
      // Get original file extension from uploaded image
      const extension = image.name.split('.').pop()
      // Create download filename: original_name_optimized.extension
      const fileName = `${image.name.split('.')[0]}_optimized.${extension}`
      
      link.download = fileName
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
    }
  }

  return (
    <div className="container">
      <h1 className="title">Image Optimizer</h1>
      <form onSubmit={handleSubmit} className="optimizer-form">
        {/* Original Image Preview - Above upload button */}
        {imagePreview && (
          <div className="image-container">
            <h3>Original Image</h3>
            <img src={imagePreview} alt="Original" className="preview-image" />
            <p>Original Size: {(image.size / 1024).toFixed(2)} KB</p>
          </div>
        )}

        <div className="upload-section">
          <label htmlFor="file-upload" className="file-upload-label">
            {image ? 'Image Selected ✓' : 'Choose an Image'}
          </label>
          <input 
            id="file-upload"
            type="file" 
            accept="image/*"
            onChange={handleImageChange}
            className="file-input"
          />
        </div>

        <div className="quality-section">
          <label htmlFor="quality" className="quality-label">
            Quality: {quality}%
          </label>
          <input
            type="range"
            id="quality"
            min="0"
            max="100"
            value={quality}
            onChange={handleSliderChange}
            className="quality-slider"
          />
        </div>

        <button 
          type="submit" 
          disabled={!image}
          className="submit-button"
        >
          Optimize Image
        </button>

        {/* Optimized Image Preview with Download Button */}
        {optimizedImage && (
          <div className="image-container">
            <h3>Optimized Image</h3>
            <img src={optimizedImage} alt="Optimized" className="preview-image" />
            <p>Optimized Size: {(optimizedImageSize / 1024).toFixed(2)} KB</p>
            <p>Size Reduction: {((image.size - optimizedImageSize) / image.size * 100).toFixed(1)}%</p>
            <button 
              type="button" 
              onClick={handleDownload}
              className="download-button"
            >
              Download Optimized Image
            </button>
          </div>
        )}
      </form>
    </div>
  )
}

export default App

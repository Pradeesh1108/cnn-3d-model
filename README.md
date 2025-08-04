# 🧠 CNN Visualizer with 3D Output

A Streamlit-based web application that trains a Convolutional Neural Network (CNN) on the MNIST dataset and provides interactive 3D visualizations of the model's activations and predictions.

## 📋 Description

This project demonstrates the inner workings of a CNN by visualizing how the network processes and learns from image data. The application:

- **Trains a CNN model** on the MNIST handwritten digit dataset
- **Extracts layer activations** from convolutional layers to understand feature learning
- **Visualizes activations in 3D** using Plotly for interactive exploration
- **Provides real-time predictions** with confidence scores
- **Offers 3D rendering** using Three.js for enhanced visualization

## 🚀 Features

- **Interactive Web Interface**: Built with Streamlit for easy-to-use web interface
- **Real-time Training**: Train the CNN model directly in the browser
- **3D Activation Visualization**: Explore how different layers learn features
- **MNIST Dataset**: Uses the classic handwritten digit dataset
- **Model Architecture**: Simple but effective CNN with Conv2D, MaxPooling, and Dense layers
- **Prediction Display**: Shows predicted class and confidence scores

## 🏗️ Project Structure

```
cnn-model/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── data/
│   └── load_data.py           # MNIST data loading and preprocessing
├── model/
│   ├── cnn_model.py           # CNN architecture definition
│   └── utils.py               # Training and prediction utilities
└── visualization/
    ├── cnn_3d_plot.py         # 3D activation plotting with Plotly
    └── threejs_component.py   # Three.js 3D rendering component
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd cnn-model
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to the provided URL (usually `http://localhost:8501`)

3. **Train and Visualize**:
   - Click the "Train & Visualize CNN" button
   - Watch as the model trains on MNIST data
   - Explore the 3D visualizations of layer activations
   - See real-time predictions

## 🔧 Technical Details

### Model Architecture
- **Input**: 28x28x1 grayscale images (MNIST format)
- **Conv2D Layer 1**: 32 filters, 3x3 kernel, ReLU activation
- **MaxPooling2D**: 2x2 pooling
- **Conv2D Layer 2**: 64 filters, 3x3 kernel, ReLU activation
- **MaxPooling2D**: 2x2 pooling
- **Flatten**: Convert to 1D
- **Dense Layer**: 128 units, ReLU activation
- **Output**: 10 units (digits 0-9), softmax activation

### Key Components

- **Data Loading**: Uses TensorFlow's built-in MNIST dataset with normalization
- **Training**: 5 epochs with 20% validation split
- **Visualization**: 
  - Plotly for 3D activation surfaces
  - Three.js for interactive 3D rendering
  - Streamlit for web interface

## 📊 Dependencies

- `streamlit`: Web application framework
- `tensorflow`: Deep learning framework
- `numpy`: Numerical computing
- `pandas`: Data manipulation
- `plotly`: Interactive 3D plotting

## 🎨 Visualization Features

- **3D Activation Surfaces**: Visualize how each convolutional layer learns features
- **Interactive Plotly Charts**: Zoom, rotate, and explore the 3D visualizations
- **Three.js Integration**: Additional 3D rendering capabilities
- **Real-time Updates**: See predictions and visualizations update as the model trains

## 🔍 Understanding the Visualizations

The 3D plots show:
- **X-axis**: Width of the feature maps
- **Y-axis**: Height of the feature maps  
- **Z-axis**: Layer depth (different layers are stacked)
- **Color intensity**: Activation strength (brighter = stronger activation)

This helps understand how the CNN learns hierarchical features from simple edges to complex digit patterns.
# 🔥 AI-Driven Calorie Predictor

A sophisticated machine learning web application that accurately predicts calories burned during exercise using advanced algorithms and personal metrics.

## 📋 Overview

This system leverages machine learning to estimate calorie burn based on physiological parameters and exercise data. It features both a REST API backend and an intuitive web interface for easy interaction.

## ✨ Key Features

- **🤖 ML-Powered Predictions**: Advanced model trained on exercise data
- **🌐 Dual Interface Options**: 
  - RESTful API for integration
  - Web UI for direct user interaction
- **📊 Real-time Processing**: Instant calorie predictions
- **✅ Input Validation**: Robust error handling

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip package manager

### Installation

1. **Clone and Setup**
   ```bash
   git clone <repository-url>
   cd icbt
   ```

2. **Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

### Running the Application

1. **Start the Server**
   ```bash
   python app.py
   ```

2. **Access the Application**
   - Web Interface: `http://localhost:5000`
   - API Endpoint: `http://localhost:5000/predict`

### API Documentation

**Prediction Endpoint**
- **URL**: `/predict`
- **Method**: POST
- **Request Format**:
  ```json
  {
      "features": [num1, num2, ...]
  }
  ```
  OR
  ```json
  {
      "features": {
          "feature_name1": value1,
          "feature_name2": value2
      }
  }
  ```
- **Response Format**:
  ```json
  {
      "prediction": number
  }
  ```

## 📊 Model Features

| Feature | Description | Type |
|---------|-------------|------|
| Age | Years | Numeric |
| Weight | Kilograms | Numeric |
| Height | Centimeters | Numeric |
| Duration | Exercise minutes | Numeric |
| Heart Rate | BPM | Numeric |
| Temperature | Body temp (°C) | Numeric |
| Sex | Male/Female | Categorical |

## 📁 Project Structure

```
icbt/
├── README.md
├── requirements.txt
├── app.py                # Flask application
├── model/
│   └── calorie_model.pkl # Trained ML model
└── templates/
    └── index.html       # Web interface
```

## 🛠️ Technology Stack

- **Backend**: Flask
- **ML Framework**: scikit-learn
- **Data Processing**: pandas, numpy
- **Frontend**: HTML/CSS/JavaScript

## 📈 Performance

The model achieves high accuracy in calorie prediction through:
- Cross-validation testing
- Feature importance analysis
- Regular model updates


**Built with ❤️ for health and fitness enthusiasts**

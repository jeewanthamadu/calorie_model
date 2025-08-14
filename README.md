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
- Your training-time libs installed (e.g., scikit-learn, xgboost, etc.)

Setup
1) Ensure `calorie_model.pkl` is in this folder.
2) Optional: activate your venv: `venv\Scripts\Activate.ps1`
3) Install: `python -m pip install -r requirements.txt` and also install training libs if needed (e.g., `pip install scikit-learn`).

Run
- `python app.py`
- Open `http://localhost:5000`

API
- POST `/predict`
  - JSON: `{ "features": [num, ...] }` or `{ "features": { "name": value, ... } }`
  - Response: `{ "prediction": number }` or `{ "error": message }` 
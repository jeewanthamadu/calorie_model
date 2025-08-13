Calorie Model Demo (Flask)

Run a tiny web app to test predictions from `calorie_model.pkl`.

Prerequisites
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
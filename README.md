# 🌾 AgriForecast ML — Crop Price Prediction System

A full-stack ML-powered web application for predicting crop prices across Indian states.

## 🚀 Quick Start

```bash
cd crop_prediction
pip install -r requirements.txt
python run.py
```

Open **http://localhost:5000** in your browser.

---

## 📁 Project Structure

```
crop_prediction/
├── run.py               ← Start here (entry point)
├── app.py               ← Flask REST API backend
├── ml_model.py          ← ML model (RandomForest + data generation)
├── requirements.txt     ← Python dependencies
├── models/              ← Saved model files (auto-created)
│   └── crop_predictor.pkl
└── templates/           ← HTML frontend pages
    ├── dashboard.html   ← Market overview + live prices
    ├── predictor.html   ← Interactive ML price prediction
    ├── analytics.html   ← Charts, supply/demand, correlations
    ├── portfolio.html   ← Holdings tracker with P&L
    └── history.html     ← Prediction accuracy history
```

---

## 🤖 ML Model

- **Algorithm**: Random Forest Regressor (200 trees, depth 12)
- **Training data**: 8 years of synthetic crop price data (2016–2024)
- **Features**: Year, Month, Region, Crop type, Rainfall (mm), Temperature (°C), Season flag
- **Output**: Price in USD per quintal + confidence score
- **Accuracy**: ~90–94% (MAPE-based)

### Crops Supported
Wheat, Rice, Cotton, Sugarcane, Soybean, Maize, Pulses, Onion, Tomato, Potato

### Regions Covered (15 Indian States)
Punjab, Haryana, Uttar Pradesh, Maharashtra, Rajasthan, Madhya Pradesh, Bihar,
West Bengal, Karnataka, Tamil Nadu, Gujarat, Andhra Pradesh, Himachal Pradesh,
Odisha, Jharkhand

---

## 🔌 REST API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `GET /` | GET | Redirect to dashboard |
| `GET /api/dashboard` | GET | KPIs, crop prices, market trends |
| `POST /api/predict` | POST | Price prediction for crop + region |
| `GET /api/analytics` | GET | Charts, correlations, insights |
| `GET /api/portfolio` | GET | Portfolio holdings + P&L |
| `GET /api/history` | GET | Prediction accuracy history |
| `GET /api/meta` | GET | Crops and regions list |
| `GET /api/health` | GET | Server + model status |

### Example: Predict Wheat Price in Punjab (3 months)
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"crop":"Wheat","region":"Punjab","months":3,"rainfall":85,"temperature":22}'
```

Response:
```json
{
  "prediction": {
    "crop": "Wheat",
    "region": "Punjab",
    "predicted_price_usd": 28.15,
    "predicted_price_inr": 2350.53,
    "unit": "quintal",
    "confidence": 84,
    "is_peak_season": true,
    "forecast_date": "2025-03-01"
  }
}
```

---

## 💰 Currency

All prices are displayed in **USD** (converted from INR at 1 USD = ₹83.5).

---

## 📦 Dependencies

```
flask>=2.3.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
```

Frontend uses CDN-loaded libraries (no build step needed):
- Tailwind CSS
- Chart.js
- Google Material Symbols

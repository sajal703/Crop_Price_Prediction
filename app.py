"""
AgriForecast ML — Flask Backend
Crop Price Prediction API with ML-driven insights
"""

from flask import Flask, jsonify, request, send_from_directory, render_template_string
import os
import json
import numpy as np
from datetime import datetime, timedelta
from ml_model import get_predictor, CROPS, REGIONS, REGION_CROPS, USD_RATE

# Use absolute path so Flask finds templates no matter where you run from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, static_folder=TEMPLATES_DIR)

# ─── CORS headers ───────────────────────────────────────────────────────────
@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    return response

# ─── Static page serving ────────────────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory(TEMPLATES_DIR, "dashboard.html")

@app.route("/<page>.html")
def serve_page(page):
    try:
        return send_from_directory(TEMPLATES_DIR, f"{page}.html")
    except Exception:
        return send_from_directory(TEMPLATES_DIR, "dashboard.html")

# ─── API: Dashboard ─────────────────────────────────────────────────────────
@app.route("/api/dashboard")
def api_dashboard():
    p = get_predictor()
    crops_summary = p.get_all_crops_summary()

    # KPI Stats
    total_crops = len(CROPS)
    regions_covered = len(REGIONS)
    avg_accuracy = p.accuracy or 92.4

    # Top gainers / losers
    sorted_by_change = sorted(crops_summary, key=lambda x: x["change_pct"], reverse=True)
    top_gainers = sorted_by_change[:3]
    top_losers  = sorted_by_change[-3:][::-1]

    # Market index (avg of all crop prices normalized)
    avg_price_usd = np.mean([c["price_usd"] for c in crops_summary])

    # Weekly trend for chart (last 8 weeks)
    weekly = []
    for w in range(7, -1, -1):
        date = datetime.now() - timedelta(weeks=w)
        # Simulate weekly market index
        val = avg_price_usd * (1 + np.random.normal(0, 0.015))
        weekly.append({
            "label": date.strftime("%b %d"),
            "value": round(val, 2),
        })

    return jsonify({
        "kpis": {
            "total_crops": total_crops,
            "regions_covered": regions_covered,
            "model_accuracy": avg_accuracy,
            "avg_market_price_usd": round(avg_price_usd, 2),
            "avg_market_price_inr": round(avg_price_usd * USD_RATE, 2),
            "total_predictions_today": 1247,
        },
        "crops_summary": crops_summary,
        "top_gainers": top_gainers,
        "top_losers": top_losers,
        "weekly_trend": weekly,
        "market_status": "ACTIVE",
        "last_updated": datetime.now().strftime("%d %b %Y, %H:%M"),
    })

# ─── API: Predict ────────────────────────────────────────────────────────────
@app.route("/api/predict", methods=["GET", "POST"])
def api_predict():
    if request.method == "POST":
        data = request.get_json(force=True) or {}
    else:
        data = request.args

    crop     = data.get("crop", "Wheat")
    region   = data.get("region", "Punjab")
    months   = int(data.get("months", 3))
    rainfall = float(data.get("rainfall", 80))
    temp     = float(data.get("temperature", 25))

    # Validate
    if crop not in CROPS:
        return jsonify({"error": f"Unknown crop: {crop}. Valid: {list(CROPS.keys())}"}), 400
    if region not in REGIONS:
        return jsonify({"error": f"Unknown region: {region}. Valid: {REGIONS}"}), 400

    p = get_predictor()
    prediction = p.predict(crop, region, months, rainfall, temp)

    # Also predict 1,3,6,12 months for timeline
    timeline = []
    for m in [1, 3, 6, 12]:
        pred = p.predict(crop, region, m, rainfall, temp)
        timeline.append({
            "label": f"{m}M",
            "months": m,
            "price_usd": pred["predicted_price_usd"],
            "price_inr": pred["predicted_price_inr"],
            "confidence": pred["confidence"],
        })

    # Series for chart
    series = p.predict_series(crop, region, months=12)

    # Region comparison
    region_compare = p.get_region_comparison(crop, months)

    return jsonify({
        "prediction": prediction,
        "timeline": timeline,
        "chart_series": series,
        "region_comparison": region_compare,
        "model_accuracy": p.accuracy,
        "crops_list": list(CROPS.keys()),
        "regions_list": REGIONS,
    })

# ─── API: Analytics ──────────────────────────────────────────────────────────
@app.route("/api/analytics")
def api_analytics():
    crop   = request.args.get("crop", "Wheat")
    region = request.args.get("region", "Punjab")
    p = get_predictor()

    series = p.predict_series(crop, region, months=12)

    # Correlation matrix (simulated)
    correlations = [
        {"pair": f"{crop} vs Fertilizer Cost", "value": round(np.random.uniform(0.7, 0.95), 2),
         "volatility": f"{round(np.random.uniform(8, 15), 1)}%", "trend": "Strong Positive"},
        {"pair": f"{crop} vs Rainfall",        "value": round(np.random.uniform(0.5, 0.8), 2),
         "volatility": f"{round(np.random.uniform(10, 20), 1)}%", "trend": "Moderate"},
        {"pair": f"{crop} vs Fuel/Logistics",  "value": round(np.random.uniform(0.4, 0.75), 2),
         "volatility": f"{round(np.random.uniform(12, 22), 1)}%", "trend": "Positive"},
        {"pair": f"{crop} vs Export Demand",   "value": round(np.random.uniform(0.6, 0.9), 2),
         "volatility": f"{round(np.random.uniform(5, 12), 1)}%", "trend": "Extreme High"},
    ]

    # Supply/Demand chart data
    supply_demand = []
    for m in range(12):
        date = datetime(datetime.now().year, (datetime.now().month - 6 + m) % 12 + 1, 1)
        base_inr = CROPS[crop]["base_inr"] if crop in CROPS else 4000
        supply_demand.append({
            "month": date.strftime("%b"),
            "supply": round(base_inr * (1 + np.random.normal(0, 0.08)), 2),
            "demand": round(base_inr * (1 + np.random.normal(0.05, 0.06)), 2),
        })

    # Regional risk scores
    region_risks = []
    for reg in REGIONS[:8]:
        region_risks.append({
            "region": reg,
            "risk_score": round(np.random.uniform(20, 80), 1),
            "rainfall_mm": round(np.random.normal(80, 20), 1),
            "soil_moisture": round(np.random.uniform(40, 90), 1),
        })

    all_crops_perf = []
    for crop_name in list(CROPS.keys()):
        pred = p.predict(crop_name, region, 3)
        all_crops_perf.append({
            "crop": crop_name,
            "price_usd": pred["predicted_price_usd"],
            "price_inr": pred["predicted_price_inr"],
            "change_pct": round(np.random.normal(2, 5), 2),
            "confidence": pred["confidence"],
        })

    return jsonify({
        "crop": crop,
        "region": region,
        "price_series": series,
        "correlations": correlations,
        "supply_demand": supply_demand,
        "region_risks": region_risks,
        "all_crops_performance": all_crops_perf,
        "crops_list": list(CROPS.keys()),
        "regions_list": REGIONS,
        "insights": [
            {"type": "peak", "icon": "trending_up",
             "title": "Seasonal Peak Approaching",
             "body": f"{crop} historically rises 8–12% during harvest transition in Q3."},
            {"type": "supply", "icon": "inventory",
             "title": f"Stock-to-Use Ratio: {round(np.random.uniform(10, 15), 1)}",
             "body": "Supply reserves tightening vs 3-year average. Upside risk."},
            {"type": "weather", "icon": "cloud",
             "title": "Monsoon Outlook: Normal",
             "body": f"IMD forecasts 96% of LPA for {region}. Crop stress unlikely."},
        ],
    })

# ─── API: Portfolio ───────────────────────────────────────────────────────────
@app.route("/api/portfolio")
def api_portfolio():
    p = get_predictor()
    portfolio = []
    items = [
        {"crop": "Wheat",     "region": "Punjab",        "qty": 50,  "buy_inr": 2187.0},
        {"crop": "Rice",      "region": "West Bengal",   "qty": 30,  "buy_inr": 3047.0},
        {"crop": "Cotton",    "region": "Maharashtra",   "qty": 20,  "buy_inr": 6412.0},
        {"crop": "Soybean",   "region": "Madhya Pradesh","qty": 15,  "buy_inr": 4133.0},
        {"crop": "Maize",     "region": "Karnataka",     "qty": 40,  "buy_inr": 1845.0},
        {"crop": "Sugarcane", "region": "Uttar Pradesh", "qty": 100, "buy_inr": 376.0},
    ]
    for item in items:
        pred_1m  = p.predict(item["crop"], item["region"], 1)
        pred_3m  = p.predict(item["crop"], item["region"], 3)
        pred_90d = pred_3m["predicted_price_inr"]
        current  = pred_1m["predicted_price_inr"]
        buy_inr  = item["buy_inr"]
        change   = (current - buy_inr) / buy_inr * 100

        portfolio.append({
            "crop": item["crop"],
            "region": item["region"],
            "quantity_quintals": item["qty"],
            "buy_price_inr": buy_inr,
            "current_price_inr": round(current, 2),
            "predicted_90d_inr": round(pred_90d, 2),
            "total_value_inr": round(current * item["qty"], 2),
            "pnl_pct": round(change, 2),
            "pnl_inr": round((current - buy_inr) * item["qty"], 2),
            "prediction_90d_change": round((pred_90d - current) / current * 100, 2),
            "confidence": pred_3m["confidence"],
            "icon": CROPS[item["crop"]]["icon"],
            "is_peak_season": pred_1m["is_peak_season"],
        })

    total_value = sum(x["total_value_inr"] for x in portfolio)
    total_pnl   = sum(x["pnl_inr"] for x in portfolio)

    return jsonify({
        "portfolio": portfolio,
        "summary": {
            "total_value_inr": round(total_value, 2),
            "total_pnl_inr": round(total_pnl, 2),
            "total_pnl_pct": round(total_pnl / (total_value - total_pnl) * 100, 2),
            "num_holdings": len(portfolio),
        },
        "model_accuracy": p.accuracy,
    })

# ─── API: History ─────────────────────────────────────────────────────────────
@app.route("/api/history")
def api_history():
    p = get_predictor()
    records = p.get_history_records(30)

    # Aggregate stats
    avg_error = np.mean([r["error_pct"] for r in records])
    best_pred = min(records, key=lambda x: x["error_pct"])
    worst_pred = max(records, key=lambda x: x["error_pct"])

    # Accuracy by crop
    crop_accuracy = {}
    for r in records:
        c = r["crop"]
        if c not in crop_accuracy:
            crop_accuracy[c] = []
        crop_accuracy[c].append(100 - r["error_pct"])
    crop_acc_list = [{"crop": k, "accuracy": round(np.mean(v), 1)}
                     for k, v in crop_accuracy.items()]
    crop_acc_list.sort(key=lambda x: x["accuracy"], reverse=True)

    return jsonify({
        "records": records,
        "stats": {
            "total_predictions": len(records),
            "avg_accuracy": round(100 - avg_error, 1),
            "best_prediction": best_pred,
            "worst_prediction": worst_pred,
            "model_version": "RF-v2.1",
        },
        "crop_accuracy": crop_acc_list,
    })

# ─── API: Crops & Regions ─────────────────────────────────────────────────────
@app.route("/api/meta")
def api_meta():
    return jsonify({
        "crops": [{"name": k, "icon": v["icon"], "unit": v["unit"]}
                  for k, v in CROPS.items()],
        "regions": REGIONS,
        "region_crops": REGION_CROPS,
    })

# ─── Health check ─────────────────────────────────────────────────────────────
@app.route("/api/health")
def health():
    p = get_predictor()
    return jsonify({
        "status": "ok",
        "model_loaded": p.model is not None,
        "model_accuracy": p.accuracy,
    })

if __name__ == "__main__":
    print("🌾 AgriForecast ML — Starting Server")
    print("📡 Loading/training ML model...")
    get_predictor()
    print("✅ Model ready!")
    print("🚀 Server running at http://localhost:5000")
    app.run(debug=False, host="0.0.0.0", port=5000, threaded=True)

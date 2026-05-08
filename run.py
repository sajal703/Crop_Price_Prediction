#!/usr/bin/env python3
"""
AgriForecast ML — Crop Price Prediction System
Run this to start the full application.

Usage:
  python run.py

Then open: http://localhost:5000
"""

import os
import sys

def check_dependencies():
    missing = []
    for pkg in ['flask', 'sklearn', 'pandas', 'numpy']:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"❌ Missing packages: {missing}")
        print("Run: pip install -r requirements.txt")
        sys.exit(1)
    print("✅ All dependencies found")

if __name__ == "__main__":
    print("=" * 55)
    print("  🌾  AgriForecast ML — Crop Price Predictor")
    print("=" * 55)
    check_dependencies()

    # Change to project directory so relative paths work
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    from ml_model import get_predictor
    print("\n📊 Initialising ML model (this may take ~30s first run)...")
    p = get_predictor()
    print(f"✅ Model ready — Accuracy: {p.accuracy}%")

    print("\n🚀 Starting web server...")
    print("   Dashboard  →  http://localhost:5000/dashboard.html")
    print("   Predictor  →  http://localhost:5000/predictor.html")
    print("   Analytics  →  http://localhost:5000/analytics.html")
    print("   Portfolio  →  http://localhost:5000/portfolio.html")
    print("   History    →  http://localhost:5000/history.html")
    print("\n   Press Ctrl+C to stop\n")

    from app import app
    app.run(debug=False, host="0.0.0.0", port=5000, threaded=True)

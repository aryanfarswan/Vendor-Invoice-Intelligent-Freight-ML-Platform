"""
config.py
---------
Central place for paths and constants used across the app.
Keeping this separate means model paths / filenames can change
without touching any UI or business logic code.
"""

from pathlib import Path

# ------------------------------------------------------------------
# Root directory of the project (folder containing app.py)
# ------------------------------------------------------------------
APP_DIR = Path(__file__).resolve().parent

# ------------------------------------------------------------------
# Inference scripts supplied with the trained models.
# These live in your existing `Inferencing/` folder — nothing there
# needs to move.
# ------------------------------------------------------------------
FREIGHT_INFERENCE = APP_DIR / "Inferencing" / "predict_freight.py"
INVOICE_INFERENCE = APP_DIR / "Inferencing" / "predict_invoiceflag.py"

# ------------------------------------------------------------------
# Candidate locations for the trained model artifacts.
# Your existing `models/` folder at the project root is checked first;
# the per-pipeline `Freight_cost_prediction/models/` copy is kept as
# a fallback in case the two ever drift.
# ------------------------------------------------------------------
FREIGHT_MODEL_CANDIDATES = [
    APP_DIR / "models" / "predict_freight_model.pkl",
    APP_DIR / "Freight_cost_prediction" / "models" / "predict_freight_model.pkl",
]

INVOICE_MODEL_CANDIDATES = [
    APP_DIR / "models" / "predict_flag_invoice.pkl",
]

# ------------------------------------------------------------------
# Optional: the scaler used by the invoice-flag pipeline, if your
# predict_invoiceflag.py loads it separately rather than bundling it
# inside the model pickle.
# ------------------------------------------------------------------
SCALER_PATH = APP_DIR / "models" / "scaler.pkl"

# ------------------------------------------------------------------
# Page metadata
# ------------------------------------------------------------------
PAGE_TITLE = "Vendor Invoice Intelligence & Freight ML Platform"
PAGE_ICON = "📦"

FREIGHT_MODULE_LABEL = "🚚 Freight Cost Estimator"
INVOICE_MODULE_LABEL = "🚩 Invoice Risk Auditor"

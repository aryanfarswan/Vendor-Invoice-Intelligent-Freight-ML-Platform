"""
core/model_loader.py
---------------------
Everything related to locating, importing, and loading the trained
models lives here. This is the only file that should ever need to
change if the model artifacts move, get retrained, or get renamed.
"""

from __future__ import annotations

import sys
import importlib.util
from pathlib import Path
from typing import Optional

import joblib
import numpy
import streamlit as st

from config import (
    FREIGHT_INFERENCE,
    INVOICE_INFERENCE,
    FREIGHT_MODEL_CANDIDATES,
    INVOICE_MODEL_CANDIDATES,
)

# ------------------------------------------------------------------
# Compatibility shim used by the supplied inference scripts.
# Some models were pickled under a numpy version whose internal
# module layout differs from the one installed here; this shim
# keeps joblib.load() working across that mismatch.
# ------------------------------------------------------------------
def _apply_numpy_compat_shim() -> None:
    if "numpy._core" not in sys.modules and not hasattr(numpy, "_core"):
        sys.modules["numpy._core"] = numpy.core
        if hasattr(numpy.core, "_multiarray_umath"):
            sys.modules["numpy._core._multiarray_umath"] = numpy.core._multiarray_umath


_apply_numpy_compat_shim()


def find_existing(candidates: list[Path]) -> Optional[Path]:
    """Return the first path in `candidates` that exists on disk, else None."""
    for path in candidates:
        if path.exists():
            return path
    return None


def load_inference_module(file_path: Path, module_name: str):
    """
    Dynamically load one of the supplied inference scripts without
    requiring the project to be installed as a package.
    """
    if not file_path.exists():
        return None

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        return None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@st.cache_resource
def get_models() -> dict:
    """Load both trained models and their inference modules once per session."""
    freight_module = load_inference_module(FREIGHT_INFERENCE, "predict_freight_inference")
    invoice_module = load_inference_module(INVOICE_INFERENCE, "predict_invoiceflag_inference")

    freight_model_path = find_existing(FREIGHT_MODEL_CANDIDATES)
    invoice_model_path = find_existing(INVOICE_MODEL_CANDIDATES)

    freight_model = joblib.load(freight_model_path) if freight_model_path else None
    invoice_model = joblib.load(invoice_model_path) if invoice_model_path else None

    return {
        "freight_module": freight_module,
        "invoice_module": invoice_module,
        "freight_model": freight_model,
        "invoice_model": invoice_model,
        "freight_model_path": freight_model_path,
        "invoice_model_path": invoice_model_path,
    }


def predict_freight_for_quantity(model, quantity: float) -> float:
    """Run the freight regression model for a single quantity value."""
    import pandas as pd

    input_df = pd.DataFrame({"Quantity": [quantity]})
    prediction = model.predict(input_df)
    return float(prediction[0])


def predict_invoice_flag(model, invoice_quantity, invoice_dollars, freight,
                          total_item_quantity, total_item_dollars) -> int:
    """Run the invoice risk classifier for a single invoice's parameters."""
    import pandas as pd

    input_df = pd.DataFrame(
        {
            "Invoice_quantity": [invoice_quantity],
            "Invoice_Dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars],
        }
    )
    prediction = model.predict(input_df)
    return int(round(float(prediction[0])))

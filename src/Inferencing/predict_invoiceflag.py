import sys
from pathlib import Path
import joblib
import pandas as pd
import numpy

# Compatibility shim for models saved with numpy 2.x when unpickled in numpy 1.x
if 'numpy._core' not in sys.modules and not hasattr(numpy, '_core'):
    sys.modules['numpy._core'] = numpy.core
    if hasattr(numpy.core, '_multiarray_umath'):
        sys.modules['numpy._core._multiarray_umath'] = numpy.core._multiarray_umath # type: ignore

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_MODEL_PATH = BASE_DIR / "models" / "predict_flag_invoice.pkl"

def load_model(model_path: str = None):# type: ignore
    if model_path is None:
        target_path = DEFAULT_MODEL_PATH
    else:
        target_path = Path(model_path)
    with open(target_path, 'rb') as f:
        model = joblib.load(f)
    return model

def predict_invoice_flag(input_data):
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Flag'] = model.predict(input_df).round()
    return input_df

if __name__ == '__main__':
    sample_data = {
        'Invoice_quantity': [10],
        'Invoice_Dollars': [2500],
        'Freight': [150],
        'total_item_quantity': [12],
        'total_item_dollars': [2700]
    }
    prediction = predict_invoice_flag(sample_data)
    print(prediction)

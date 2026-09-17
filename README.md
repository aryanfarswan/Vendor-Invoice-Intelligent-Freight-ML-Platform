# Invoice Intelligence System (InvoAudit AI)

A production-grade web application built with Streamlit for automated freight cost forecasting and invoice risk auditing. The user interface features an **off-white and blue** enterprise design palette, providing finance, audit, and supply chain teams with instant inference and validation.

---

## 🎨 Design & Palette System
- **Background**: Soft Off-White (`#F8FAFC`, `#F1F5F9`)
- **Card Surfaces**: Pure White (`#FFFFFF`) with subtle slate borders (`#E2E8F0`)
- **Primary Accents**: Royal & Enterprise Blues (`#1D4ED8`, `#2563EB`, `#1E3A8A`)
- **Action Elements**: Sky Blue & Slate Highlights (`#3B82F6`, `#0F172A`)
- **Risk Indicators**: Mint Green for Approved (`#ECFDF5` / `#047857`) & Coral Red for Flagged (`#FEF2F2` / `#B91C1C`)

---

## 🚀 Key Features & Modules

### 1. 📊 Executive Dashboard
- Real-time KPIs: Model accuracy rate, freight MAE index, inference throughput, and risk detection metrics.
- Complete system architecture visualization from invoice receipt to ERP payout clearance.
- One-click navigation to primary tools.

### 2. 🚚 Freight Cost Estimator (`Inferencing/predict_freight.py`)
- **Single Shipment Mode**: Interactive quantity sliders and presets (Small Parcel, Medium LTL, Full Truckload, Bulk Distribution) with cost-per-unit breakdown and dynamic cost sensitivity curves.
- **Batch Processing Mode**: Drag-and-drop CSV upload for thousands of shipments, downloadable template CSV, demo batch loader, summary aggregations, and one-click CSV export.

### 3. 🚩 Invoice Risk Auditor (`Inferencing/predict_invoiceflag.py`)
- **Single Invoice Audit**: Evaluates invoice quantities, billed dollars, and freight against warehouse receiving receipts and authorized PO amounts.
- **Preset Scenarios**: 1-click loading of clean compliant invoices, dollar mismatches (> $5 variance threshold), and unit discrepancy cases.
- **Diagnostic Signal Checklist**: Detailed breakdown of dollar variance, item reconciliation, and freight ratio analysis.
- **Batch Ledger Audit**: Portfolio-wide risk classification with metrics on total dollars at risk and automated audit status tagging.

### 4. ⚡ End-to-End Unified Verifier
- Connects both machine learning engines into a unified wizard:
  1. Benchmarks expected freight from ordered quantities.
  2. Compares billed freight and invoiced dollars against the benchmark.
  3. Classifies the entire risk profile and provides actionable ERP posting recommendations.

### 5. 🔍 System Diagnostics & Docs
- Live health status of machine learning artifacts (`predict_freight_model.pkl`, `predict_flag_invoice.pkl`, `scaler.pkl`).
- CSV schema specifications and model architecture details.

---

## 💻 How to Run

Run the Streamlit application from the project root:

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`.



```
Invoice Intelligent system
├─ .ipynb_checkpoints
├─ .streamlit
│  └─ config.toml
├─ app.py
├─ components
│  ├─ audit_card.py
│  ├─ hero_banner.py
│  ├─ predicted_card.py
│  ├─ sidebar.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ audit_card.cpython-310.pyc
│     ├─ hero_banner.cpython-310.pyc
│     ├─ predicted_card.cpython-310.pyc
│     ├─ sidebar.cpython-310.pyc
│     └─ __init__.cpython-310.pyc
├─ config.py
├─ core
│  ├─ model_loader.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ model_loader.cpython-310.pyc
│     └─ __init__.cpython-310.pyc
├─ Data
│  └─ inventory.db
├─ models
│  ├─ predict_flag_invoice.pkl
│  ├─ predict_freight_model.pkl
│  └─ scaler.pkl
├─ Notebook
│  ├─ .ipynb_checkpoints
│  │  ├─ InvoiceFlagging-checkpoint.ipynb
│  │  └─ Predicitng-frieght-cost-checkpoint.ipynb
│  ├─ InvoiceFlagging.ipynb
│  └─ Predicitng-frieght-cost.ipynb
├─ README.md
├─ src
│  ├─ Freight_cost_prediction
│  │  ├─ .ipynb_checkpoints
│  │  │  ├─ Data_preprocessing-checkpoint.py
│  │  │  ├─ model_evaluation-checkpoint.py
│  │  │  └─ train-checkpoint.py
│  │  ├─ Data_preprocessing.py
│  │  ├─ model_evaluation.py
│  │  ├─ train.py
│  │  └─ __pycache__
│  │     ├─ Data_preprocessing.cpython-310.pyc
│  │     └─ model_evaluation.cpython-310.pyc
│  ├─ Inferencing
│  │  ├─ .ipynb_checkpoints
│  │  │  └─ predict_freight-checkpoint.py
│  │  ├─ predict_freight.py
│  │  ├─ predict_invoiceflag.py
│  │  └─ __pycache__
│  │     ├─ predict_freight.cpython-310.pyc
│  │     └─ predict_invoiceflag.cpython-310.pyc
│  └─ Invoice_flagging
│     ├─ .ipynb_checkpoints
│     │  ├─ data_preprocessing-checkpoint.py
│     │  ├─ modeling_evaluation-checkpoint.py
│     │  └─ train-checkpoint.py
│     ├─ data_preprocessing.py
│     ├─ modeling_evaluation.py
│     ├─ train.py
│     └─ __pycache__
│        ├─ data_preprocessing.cpython-310.pyc
│        └─ modeling_evaluation.cpython-310.pyc
├─ styles.py
├─ views
│  ├─ freight_view.py
│  ├─ invoice_view.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ freight_view.cpython-310.pyc
│     ├─ invoice_view.cpython-310.pyc
│     └─ __init__.cpython-310.pyc
└─ __pycache__
   └─ app.cpython-310.pyc

```
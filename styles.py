"""
styles.py
---------
All CSS for the app lives here, in one place.
`inject_global_css()` is called once from app.py.

Every HTML block rendered elsewhere in the app is built from
static strings / model output only (never raw user text), so
`unsafe_allow_html=True` is safe to use here and in the
component render functions.
"""

import streamlit as st

_CSS = """
<style>
.hero-banner {
    background: linear-gradient(90deg, #0b2f7a 0%, #1a5ef0 100%);
    padding: 2rem 2.5rem;
    border-radius: 14px;
    color: white;
    margin-bottom: 1.75rem;
}
.hero-banner h1 {
    font-size: 2.05rem;
    margin: 0 0 0.6rem 0;
    color: white;
}
.hero-banner .hero-subtitle {
    color: #7dd3fc;
    font-weight: 600;
    font-size: 1.05rem;
    margin-bottom: 0.75rem;
}
.hero-banner .hero-body {
    color: #e6edff;
    font-size: 0.95rem;
    margin: 0;
    line-height: 1.5;
}

/* ---------------- Freight: predicted cost card ---------------- */
.predicted-card {
    border: 2px solid #2952e3;
    border-radius: 12px;
    padding: 1.6rem 1.8rem;
    background: white;
    height: 100%;
}
.predicted-card .label {
    color: #6b7280;
    font-weight: 700;
    letter-spacing: 0.06em;
    font-size: 0.8rem;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.predicted-card .value {
    color: #2952e3;
    font-size: 3rem;
    font-weight: 800;
    margin: 0 0 0.35rem 0;
    line-height: 1.1;
}
.predicted-card .sub {
    color: #374151;
    font-size: 0.95rem;
    margin-bottom: 1rem;
}
.predicted-card hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 1rem 0;
}
.rate-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.95rem;
    color: #374151;
}
.rate-row .rate-value {
    font-weight: 700;
    color: #111827;
}

/* ---------------- Primary buttons ---------------- */
div.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #1a5ef0, #2952e3);
    border: none;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.6rem 1rem;
}
div.stButton > button[kind="primary"]:hover {
    background: linear-gradient(90deg, #164fd1, #2444c0);
    border: none;
}

/* ---------------- Invoice: audit decision cards ---------------- */
.audit-outer {
    border-radius: 12px;
    padding: 1.4rem 1.5rem 1.6rem 1.5rem;
    margin-top: 1.25rem;
}
.audit-outer.risk-high { background-color: #fdf2f4; }
.audit-outer.risk-low  { background-color: #ecfdf5; }

.audit-header {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 700;
    font-size: 1.15rem;
    color: #111827;
    margin-bottom: 0.9rem;
}

.audit-box {
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
    text-align: center;
    font-weight: 800;
    letter-spacing: 0.01em;
    margin-bottom: 0.6rem;
    border: 1px solid transparent;
}
.audit-box.high {
    background: #fff1f2;
    border-color: #fecdd3;
    color: #b91c1c;
}
.audit-box.low {
    background: #d1fae5;
    border-color: #a7f3d0;
    color: #047857;
}

.audit-note {
    border-radius: 10px;
    padding: 0.8rem 1.2rem;
    font-size: 0.95rem;
}
.audit-note.high {
    background: #ffe4e6;
    color: #b91c1c;
}
.audit-note.low {
    background: #a7f3d0;
    color: #047857;
}
</style>
"""


def inject_global_css() -> None:
    """Render the app's scoped CSS once. Call this early in app.py."""
    st.markdown(_CSS, unsafe_allow_html=True)

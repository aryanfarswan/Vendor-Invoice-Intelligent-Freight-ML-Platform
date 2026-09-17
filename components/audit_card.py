"""
components/audit_card.py
--------------------------
Renders the "Audit Decision & Variance Diagnostics" card, switching
between the high-risk (red) and low-risk (green) treatments based on
the invoice-flag model's binary prediction.
"""

import streamlit as st

_HIGH_RISK_TEXT = "⚠️ INVOICE FLAGGED FOR AUDIT (HIGH RISK)"
_HIGH_RISK_NOTE = (
    "Action Required: Route this invoice to human AP specialist. "
    "Potential dollar leakage or order discrepancy detected."
)

_LOW_RISK_TEXT = "✅ INVOICE VERIFIED &amp; APPROVED (LOW RISK)"
_LOW_RISK_NOTE = (
    "Action: Approved for automated payout. All billed parameters "
    "align within tolerance limits."
)


def render_audit_card(flag: int) -> None:
    """
    flag: the invoice-flag model's rounded binary prediction
          (1 = high risk / needs manual audit, 0 = low risk / auto-approved)
    """
    if flag == 1:
        risk_class = "high"
        box_text = _HIGH_RISK_TEXT
        note_text = _HIGH_RISK_NOTE
    else:
        risk_class = "low"
        box_text = _LOW_RISK_TEXT
        note_text = _LOW_RISK_NOTE

    st.markdown(
        f"""
        <div class="audit-outer risk-{risk_class}">
            <div class="audit-header">🎯 Audit Decision &amp; Variance Diagnostics</div>
            <div class="audit-box {risk_class}">{box_text}</div>
            <div class="audit-note {risk_class}">{note_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

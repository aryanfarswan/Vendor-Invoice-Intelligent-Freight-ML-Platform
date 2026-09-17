"""
views/invoice_view.py
-----------------------
The "Invoice Risk Auditor" module: five invoice parameters feeding the
trained classifier, with the result shown as an Audit Decision card.
"""

import streamlit as st

from core.model_loader import predict_invoice_flag
from components.audit_card import render_audit_card


def render_invoice_view(models: dict) -> None:
    st.header("🚩 Invoice Risk Auditor")
    st.caption(
        "Predict whether a vendor invoice should be flagged for manual approval "
        "based on invoice, freight, quantity and item-value patterns."
    )

    if models["invoice_model"] is None:
        st.error(
            "Invoice flag model not found. Expected: "
            "`models/predict_flag_invoice.pkl`."
        )
        return

    with st.container(border=True):
        st.markdown("**Invoice Parameter Input**")
        st.caption("Enter vendor invoice values used by the trained invoice risk model.")

        row1 = st.columns(3)
        row2 = st.columns(2)

        with row1[0]:
            invoice_quantity = st.number_input(
                "Invoice Quantity", min_value=0.0, value=50.0, step=1.0,
                help="Invoice quantity.",
            )
        with row1[1]:
            invoice_dollars = st.number_input(
                "Invoice Dollars", min_value=0.0, value=352.95, step=0.01,
                format="%.2f", help="Dollar value of the invoice.",
            )
        with row1[2]:
            total_item_dollars = st.number_input(
                "Total Item Dollars", min_value=0.0, value=2476.00, step=0.01,
                format="%.2f", help="Total item-dollar value.",
            )
        with row2[0]:
            freight = st.number_input(
                "Freight Cost", min_value=0.0, value=1.73, step=0.01,
                format="%.2f", help="Freight amount associated with the invoice.",
            )
        with row2[1]:
            total_item_quantity = st.number_input(
                "Total Item Quantity", min_value=0.0, value=162.0, step=1.0,
                help="Total item quantity.",
            )

        predict = st.button(
            "🧠 Evaluate Invoice Risk",
            key="invoice_predict",
            use_container_width=True,
            type="primary",
        )

    if predict:
        try:
            flag = predict_invoice_flag(
                models["invoice_model"],
                invoice_quantity,
                invoice_dollars,
                freight,
                total_item_quantity,
                total_item_dollars,
            )
            render_audit_card(flag)
        except Exception as e:
            st.error(f"Invoice flag prediction failed: {e}")

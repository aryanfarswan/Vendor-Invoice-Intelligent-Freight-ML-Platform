"""
views/freight_view.py
-----------------------
The "Freight Cost Estimator" module: a single quantity input feeding
the trained freight regression model, with the result shown in a
styled card next to it.
"""

import streamlit as st

from core.model_loader import predict_freight_for_quantity
from components.predicted_card import render_empty_predicted_card, render_predicted_card


def render_freight_view(models: dict) -> None:
    st.header("🚚 Freight Cost Prediction Engine")
    st.caption(
        "Predict expected shipping & freight expenditures based on order "
        "volume and unit quantities."
    )

    if models["freight_model"] is None:
        st.error(
            "Freight model not found. Expected: "
            "`models/predict_freight_model.pkl` "
            "(or `Freight_cost_prediction/models/predict_freight_model.pkl`)."
        )
        return

    (tab_single,) = st.tabs(["🎯 Order Estimation"])

    with tab_single:
        left_col, right_col = st.columns([1.1, 1], gap="large")

        with left_col:
            with st.container(border=True):
                st.markdown("**Shipment Parameter Input**")
                st.caption("Adjust quantity to calculate real-time estimated freight cost.")

                quantity = st.number_input(
                    "Order Quantity (Units):",
                    min_value=0.0,
                    value=1200.0,
                    step=1.0,
                    help="Invoice quantity used by the supplied freight inference model.",
                )

                predict = st.button(
                    "🧠 Estimate Freight Cost",
                    key="freight_predict",
                    use_container_width=True,
                    type="primary",
                )

        with right_col:
            if predict:
                try:
                    predicted_freight = predict_freight_for_quantity(
                        models["freight_model"], quantity
                    )
                    render_predicted_card(predicted_freight, quantity)
                except Exception as e:
                    st.error(f"Freight prediction failed: {e}")
            else:
                render_empty_predicted_card()

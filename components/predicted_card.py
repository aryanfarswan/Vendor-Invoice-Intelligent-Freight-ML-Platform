"""
components/predicted_card.py
------------------------------
Renders the blue-bordered "Predicted Freight Cost" card, in either
its empty/idle state or its filled state after a prediction runs.
Only numeric model output and user-entered quantity are inserted
into the markup; both are formatted numbers, not free text.
"""

import streamlit as st


def render_empty_predicted_card() -> None:
    st.markdown(
        """
        <div class="predicted-card">
            <div class="label">Predicted Freight Cost</div>
            <div class="value">—</div>
            <div class="sub">Run an estimate to see the predicted freight cost here.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_predicted_card(predicted_freight: float, quantity: float) -> None:
    unit_rate = predicted_freight / quantity if quantity else 0.0

    st.markdown(
        f"""
        <div class="predicted-card">
            <div class="label">Predicted Freight Cost</div>
            <div class="value">${predicted_freight:,.2f}</div>
            <div class="sub">Expected shipping charge for <b>{quantity:,.0f}</b> units</div>
            <hr />
            <div class="rate-row">
                <span>Unit Freight Rate:</span>
                <span class="rate-value">${unit_rate:,.4f} / unit</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

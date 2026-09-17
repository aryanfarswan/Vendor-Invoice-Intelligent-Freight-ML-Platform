"""
components/sidebar.py
----------------------
Renders the left navigation sidebar and returns the selected module.
"""

import streamlit as st

from config import FREIGHT_MODULE_LABEL, INVOICE_MODULE_LABEL


def render_sidebar() -> str:
    """Render the sidebar and return the currently selected module label."""
    with st.sidebar:
        st.title("🔍 Navigation")
        st.caption("Choose Module")

        module = st.radio(
            "Navigation",
            [FREIGHT_MODULE_LABEL, INVOICE_MODULE_LABEL],
            label_visibility="collapsed",
        )

        st.divider()

        st.subheader("Business Impact")
        st.write("📉 Improved cost forecasting")
        st.write("🧾 Reduced invoice fraud & anomalies")
        st.write("⚙️ Faster finance operations")

        st.divider()

        st.subheader("⚙️ Engine Status")
        engine_col1, engine_col2 = st.columns(2)
        with engine_col1:
            st.caption("Freight ML")
            st.success("● Active")
        with engine_col2:
            st.caption("Audit ML")
            st.success("● Active")

    return module

"""
components/hero_banner.py
---------------------------
Renders the top gradient banner. Content here is static (no user
input is ever interpolated), so unsafe_allow_html is safe to use.
"""

import streamlit as st


def render_hero_banner() -> None:
    st.markdown(
        """
        <div class="hero-banner">
            <h1>📦 Vendor Invoice Intelligence &amp; Freight ML Platform</h1>
            <div class="hero-subtitle">
                Automated freight cost prediction and intelligent risk auditing for vendor invoices.
            </div>
            <p class="hero-body">
                This internal analytics portal leverages machine learning to support freight cost
                estimation, invoice anomaly and risk detection, and automated financial control
                workflows through data-driven predictive analytics.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

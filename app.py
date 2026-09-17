

import streamlit as st

from config import PAGE_TITLE, PAGE_ICON, FREIGHT_MODULE_LABEL, INVOICE_MODULE_LABEL
from styles import inject_global_css
from core.model_loader import get_models
from components.sidebar import render_sidebar
from components.hero_banner import render_hero_banner
from views.freight_view import render_freight_view
from views.invoice_view import render_invoice_view

# ------------------------------------------------------------------
# Page configuration (must be the first Streamlit call)
# ------------------------------------------------------------------
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------
# Global CSS
# ------------------------------------------------------------------
inject_global_css()

# ------------------------------------------------------------------
# Sidebar (returns the selected module)
# ------------------------------------------------------------------
selected_module = render_sidebar()

# ------------------------------------------------------------------
# Hero banner
# ------------------------------------------------------------------
render_hero_banner()

# ------------------------------------------------------------------
# Load models once per session (cached)
# ------------------------------------------------------------------
models = get_models()

# ------------------------------------------------------------------
# Route to the selected module's view
# ------------------------------------------------------------------
if selected_module == FREIGHT_MODULE_LABEL:
    render_freight_view(models)
elif selected_module == INVOICE_MODULE_LABEL:
    render_invoice_view(models)

# ------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------
st.divider()
st.caption(
    "Vendor Invoice Intelligence Portal • Streamlit UI • "
    "Predictions are generated from the supplied trained inference models."
)

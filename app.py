"""Africa Leapfrog Toolkit — Main Streamlit App
AI-powered infrastructure intelligence for Kenya and East Africa.
"""
import streamlit as st

st.set_page_config(page_title="Africa Leapfrog Toolkit", page_icon="🌍", layout="wide")

st.sidebar.title("🌍 Africa Leapfrog")
st.sidebar.caption("AI-powered infrastructure intelligence")

module = st.sidebar.selectbox("Select Module", [
    "🗺️ Infrastructure Gap Mapper",
    "🌾 NDVI Crop Stress Monitor",
    "⚠️ Early Warning System",
    "🤝 Chama/SACCO Trust Engine",
    "🔍 Procurement Watchdog (coming soon)",
    "📊 County Dashboard (coming soon)",
])

st.sidebar.markdown("---")
st.sidebar.info("**DEMO MODE** — All data is synthetic or from open public sources.")

if "Gap Mapper" in module:
    from modules.gap_mapper import render; render()
elif "NDVI" in module:
    from modules.ndvi_monitor import render; render()
elif "Early Warning" in module:
    from modules.early_warning import render; render()
elif "Chama" in module:
    from modules.chama_trust import render; render()
else:
    st.title("🌍 Africa Leapfrog Toolkit")
    st.markdown("Select a module from the sidebar.")
    st.info("Part of the AI-KungFU East Africa coordination infrastructure stack.")

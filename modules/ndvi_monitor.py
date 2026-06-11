"""NDVI Crop Stress Monitor — Packt Geospatial Ch.8 NDVI pattern."""
import streamlit as st
import pandas as pd

MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
NDVI_PROFILES = {
    "Arid North (ASAL)":  [0.12,0.10,0.09,0.15,0.20,0.18,0.16,0.14,0.12,0.18,0.22,0.15],
    "Semi-Arid Eastern":  [0.20,0.18,0.17,0.28,0.35,0.32,0.28,0.25,0.22,0.30,0.38,0.25],
    "Central Highlands":  [0.45,0.42,0.40,0.55,0.65,0.62,0.58,0.55,0.52,0.60,0.68,0.52],
    "Western Kenya":      [0.50,0.48,0.46,0.58,0.68,0.65,0.62,0.60,0.55,0.62,0.70,0.55],
    "Coastal Strip":      [0.35,0.33,0.32,0.45,0.55,0.52,0.48,0.45,0.40,0.48,0.58,0.42],
}
def classify_ndvi(ndvi):
    if ndvi < 0.15: return "Severe Drought Stress"
    if ndvi < 0.28: return "Moderate Stress"
    if ndvi < 0.40: return "Mild Stress"
    if ndvi < 0.60: return "Normal Vegetation"
    return "Good Vegetation"

def anomaly_score(current, baseline):
    return round((current - baseline) / max(baseline, 0.01) * 100, 1)

def render():
    st.title("🌾 NDVI Crop Stress Monitor")
    st.caption("DEMO — synthetic NDVI. Production: NASA MODIS / Sentinel-2")
    st.info("**NDVI = (NIR - Red)/(NIR + Red)** — from *Learning Geospatial Analysis with Python* (Packt, Ch.8)")
    
    col1, col2 = st.columns([1,2])
    with col1:
        region = st.selectbox("Region", list(NDVI_PROFILES.keys()))
        month = st.selectbox("Month", MONTHS, index=5)
    
    with col2:
        profile = NDVI_PROFILES[region]
        idx = MONTHS.index(month)
        cur = profile[idx]
        base = sum(profile)/len(profile)
        anom = anomaly_score(cur, base)
        label = classify_ndvi(cur)
        
        c1,c2,c3 = st.columns(3)
        c1.metric("NDVI", f"{cur:.2f}", delta=f"{anom:+.1f}% vs baseline")
        c2.metric("Baseline", f"{base:.2f}")
        c3.metric("Status", label[:18])
        
        df = pd.DataFrame({"NDVI": profile, "Baseline": [base]*12}, index=MONTHS)
        st.line_chart(df)
        
        if cur < 0.15: st.error("🚨 SEVERE DROUGHT STRESS — activate NDMA emergency response.")
        elif cur < 0.28: st.warning("⚠️ Moderate crop stress — increase county monitoring.")
        else: st.success(f"✅ Vegetation {label.lower()} for {month}.")
        
        st.markdown("**Production data:** NASA MODIS (earthdata.nasa.gov) · Sentinel-2 (scihub.copernicus.eu) · NDMA (ndma.go.ke)")

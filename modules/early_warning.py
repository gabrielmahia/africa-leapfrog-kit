"""County Early Warning System."""
import streamlit as st
from datetime import date

RISKS = {
    "Turkana":    {"phase":3,"rain":-35,"maize":45,"ndvi":-28},
    "Mandera":    {"phase":3,"rain":-30,"maize":40,"ndvi":-22},
    "Marsabit":   {"phase":3,"rain":-28,"maize":38,"ndvi":-20},
    "Wajir":      {"phase":2,"rain":-20,"maize":30,"ndvi":-15},
    "Garissa":    {"phase":2,"rain":-18,"maize":28,"ndvi":-12},
    "Tana River": {"phase":2,"rain":-15,"maize":25,"ndvi":-10},
    "West Pokot": {"phase":2,"rain":-12,"maize":20,"ndvi":-8},
    "Baringo":    {"phase":1,"rain":-8,"maize":12,"ndvi":-5},
    "Narok":      {"phase":1,"rain":-5,"maize":8,"ndvi":-3},
    "Nakuru":     {"phase":0,"rain":5,"maize":-2,"ndvi":3},
    "Nairobi":    {"phase":0,"rain":8,"maize":-3,"ndvi":5},
}
PHASES = {0:"Normal",1:"Watch",2:"Alert",3:"Emergency",4:"Crisis"}
COLORS = {0:"🟢",1:"🟡",2:"🟠",3:"🔴",4:"🆘"}

def render():
    st.title("⚠️ County Early Warning System")
    st.caption("DEMO — simulating Kenya NDMA drought monitoring. Integrates with wapimaji-mcp.")
    
    county = st.selectbox("Select County", list(RISKS.keys()))
    d = RISKS[county]
    phase = d["phase"]
    
    st.header(f"{COLORS[phase]} {county} — Phase {phase}: {PHASES[phase]}")
    st.caption(f"Brief: {date.today().strftime('%B %d, %Y')} | DEMO")
    
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Drought Phase", f"{phase}: {PHASES[phase]}")
    c2.metric("Rainfall Anomaly", f"{d['rain']:+d}%", delta_color="inverse")
    c3.metric("Maize Price Change", f"{d['maize']:+d}%", delta_color="inverse")
    c4.metric("NDVI Anomaly", f"{d['ndvi']:+d}%", delta_color="inverse")
    
    if phase >= 3:
        st.error("**EMERGENCY** — Activate NDMA EOC · Request Red Cross food assistance · Enable cash transfers · Monitor child malnutrition")
    elif phase == 2:
        st.warning("**ALERT** — Pre-position food stocks · Activate county contingency plan · Monitor markets weekly")
    elif phase == 1:
        st.info("**WATCH** — Continue NDMA reporting · Brief county agriculture · Verify food reserves")
    else:
        st.success("**NORMAL** — Continue regular monitoring.")
    
    st.markdown("---")
    st.markdown("**Production data sources:** NDMA ndma.go.ke · CHIRPS chc.ucsb.edu · WFP VAM vam.wfp.org · NASA MODIS earthdata.nasa.gov")
    st.markdown("**Connects to:** [wapimaji-mcp](https://github.com/gabrielmahia/wapimaji-mcp)")

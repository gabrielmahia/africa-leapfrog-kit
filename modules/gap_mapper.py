"""Infrastructure Gap Mapper — Packt SimpleGIS pattern adapted for Kenya."""
import streamlit as st

COUNTY_DATA = {
    "Turkana":      {"water": 18, "health": 22, "education": 31, "energy": 12, "population": 926976},
    "Marsabit":     {"water": 20, "health": 25, "education": 35, "energy": 14, "population": 459785},
    "Wajir":        {"water": 22, "health": 28, "education": 38, "energy": 15, "population": 661941},
    "Mandera":      {"water": 25, "health": 30, "education": 40, "energy": 16, "population": 867457},
    "Garissa":      {"water": 30, "health": 35, "education": 45, "energy": 20, "population": 841353},
    "West Pokot":   {"water": 28, "health": 32, "education": 42, "energy": 18, "population": 512690},
    "Tana River":   {"water": 35, "health": 40, "education": 50, "energy": 24, "population": 315943},
    "Kitui":        {"water": 38, "health": 45, "education": 52, "energy": 38, "population": 1136187},
    "Kwale":        {"water": 40, "health": 48, "education": 55, "energy": 42, "population": 866820},
    "Kilifi":       {"water": 42, "health": 50, "education": 58, "energy": 45, "population": 1453787},
    "Homabay":      {"water": 42, "health": 50, "education": 55, "energy": 45, "population": 1131950},
    "Migori":       {"water": 45, "health": 52, "education": 58, "energy": 48, "population": 1116436},
    "Kakamega":     {"water": 50, "health": 58, "education": 65, "energy": 55, "population": 1867579},
    "Makueni":      {"water": 42, "health": 50, "education": 58, "energy": 45, "population": 987653},
    "Machakos":     {"water": 62, "health": 68, "education": 72, "energy": 65, "population": 1421932},
    "Kisumu":       {"water": 72, "health": 78, "education": 82, "energy": 80, "population": 1155574},
    "Nakuru":       {"water": 70, "health": 75, "education": 80, "energy": 78, "population": 2162202},
    "Kiambu":       {"water": 78, "health": 82, "education": 85, "energy": 85, "population": 2417735},
    "Mombasa":      {"water": 82, "health": 85, "education": 88, "energy": 90, "population": 1208333},
    "Nairobi":      {"water": 85, "health": 88, "education": 90, "energy": 92, "population": 4397073},
}

def gap_score(county_data, sector):
    return max(0, 100 - county_data.get(sector, 50))

def priority_score(county_data, sectors):
    pop = county_data.get("population", 500000)
    avg_gap = sum(gap_score(county_data, s) for s in sectors) / len(sectors)
    return round((pop / 1_000_000) * avg_gap, 1)

def render():
    st.title("🗺️ Infrastructure Gap Mapper")
    st.caption("DEMO — synthetic coverage data. Source: KNBS 2019 / AI-KungFU estimates")
    st.info("""
    **Pattern from:** *Learning Geospatial Analysis with Python* (Packt, Ch.1+5).
    SimpleGIS spatial data model → layer-based gap scoring → priority ranking.
    """)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        sectors = st.multiselect("Sectors", ["water", "health", "education", "energy"],
                                 default=["water", "health"])
        top_n = st.slider("Top N counties", 5, 20, 10)
    
    with col2:
        rows = sorted(
            [{"County": c, "Pop": f"{d['population']:,}", "Priority": priority_score(d, sectors or ['water']),
              "Water Gap": gap_score(d,"water"), "Health Gap": gap_score(d,"health"),
              "Education Gap": gap_score(d,"education"), "Energy Gap": gap_score(d,"energy")}
             for c, d in COUNTY_DATA.items()],
            key=lambda x: x["Priority"], reverse=True
        )[:top_n]
        
        for r in rows:
            emoji = "🔴" if r["Priority"] > 30 else "🟡" if r["Priority"] > 15 else "🟢"
            with st.expander(f"{emoji} **{r['County']}** — Priority: {r['Priority']} | Pop: {r['Pop']}"):
                c1,c2,c3,c4 = st.columns(4)
                c1.metric("💧 Water Gap", f"{r['Water Gap']}%")
                c2.metric("🏥 Health Gap", f"{r['Health Gap']}%")
                c3.metric("🎓 Edu Gap", f"{r['Education Gap']}%")
                c4.metric("⚡ Energy Gap", f"{r['Energy Gap']}%")
        
        st.info("Northern ASAL counties show compound multi-sector deficits.")

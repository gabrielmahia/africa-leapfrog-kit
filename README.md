# Africa Leapfrog Toolkit 🌍

> **Decision infrastructure for East Africa** — AI-powered gap analysis, NDVI crop stress
> monitoring, county early warning, and chama/SACCO trust scoring.

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](LICENSE)

## What This Is

Africa doesn't need to wait for full institutional maturity to get institutional-grade
decision support. This toolkit approximates the functions of expensive planning systems
using open data, geospatial analysis, and AI — making them available in under 2 minutes
for any county, ward, or community in Kenya and East Africa.

**Built on patterns from:**
- *Learning Geospatial Analysis with Python 3rd Ed.* (Packt) — Ch.1 SimpleGIS, Ch.8 NDVI
- *Python Data Analysis 3rd Ed.* (Packt) — group statistics and trend analysis
- *ML for Algorithmic Trading 2nd Ed.* (Packt/Stefan Jansen) — Kelly Criterion sizing

## Modules

| Module | Function |
|--------|----------|
| `gap_mapper.py` | Infrastructure gap scoring (water, health, education, energy) across 20+ Kenya counties |
| `ndvi_monitor.py` | Crop stress / vegetation health — NDVI pattern, open satellite data |
| `early_warning.py` | County food security brief — drought phase, rainfall, NDVI, price anomaly |
| `chama_trust.py` | SACCO/chama group health scoring + Kelly Criterion lending capacity |
| `county_dashboard.py` | County statistics (coming soon) |
| `procurement_watch.py` | Tender anomaly detection (coming soon) |

## MCP Integration

This toolkit connects to the full coordination infrastructure stack:
- **wapimaji-mcp** → drought/NDMA data
- **afya-mcp** → health facility gaps
- **elimu-mcp** → school access
- **ardhi-mcp** → land/infrastructure
- **soko-mcp** → market access

## Running Locally

```bash
git clone https://github.com/gabrielmahia/africa-leapfrog-kit
cd africa-leapfrog-kit
pip install -r requirements.txt
streamlit run app.py
```

## Data Sources (Production)

| Data | Source | Cost |
|------|--------|------|
| NDVI (250m, 16-day) | NASA MODIS TERRA | Free — earthdata.nasa.gov |
| Rainfall anomaly | CHIRPS | Free — chc.ucsb.edu |
| Drought phase | NDMA Kenya | Free — ndma.go.ke |
| County statistics | KNBS | Free — knbs.or.ke |
| Food prices | WFP VAM Market Monitor | Free — vam.wfp.org |

All demo data is clearly labelled `DEMO — synthetic`.

## License

Creative Commons Attribution–NonCommercial–NoDerivatives 4.0 (CC BY-NC-ND 4.0)
© 2026 Gabriel Mahia / AI-KungFU. contact@aikungfu.dev

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

def test_gap_mapper():
    from modules.gap_mapper import gap_score, priority_score, COUNTY_DATA
    assert len(COUNTY_DATA) >= 20
    t = COUNTY_DATA["Turkana"]
    assert gap_score(t, "water") > 50
    print("gap_mapper OK")

def test_ndvi():
    from modules.ndvi_monitor import classify_ndvi, anomaly_score
    label, _, _ = classify_ndvi(0.10)
    assert "Severe" in label or "Drought" in label or "Stress" in label
    print("ndvi OK")

def test_chama():
    from modules.chama_trust import risk_score, kelly_group_lending
    r = risk_score(0.90, 0.05, 24, 20)
    assert r["grade"] in ("A", "B")
    print("chama OK")

if __name__ == "__main__":
    test_gap_mapper(); test_ndvi(); test_chama()
    print("All smoke tests passed.")

"""Chama/SACCO Trust Engine — Kelly Criterion + group scoring."""
import streamlit as st

def risk_score(consistency, default_rate, months_active, group_size):
    total = consistency*40 + max(0,1-default_rate*2)*30 + min(months_active/24,1)*20 + min(group_size/20,1)*10
    grade = "A" if total>=80 else "B" if total>=65 else "C" if total>=50 else "D"
    rec = ("Eligible for external credit" if total>=80 else "Eligible for small top-up loans"
           if total>=65 else "Strengthen contribution discipline" if total>=50 else "Needs governance review")
    return {"total": round(total,1), "grade": grade, "recommendation": rec}

def kelly_group_lending(win_prob, avg_recovery, loss_on_default):
    p,q = max(0.01,min(0.99,win_prob)), 1-max(0.01,min(0.99,win_prob))
    b = avg_recovery/max(loss_on_default,0.01)
    f = max(0,(p*b-q)/b)
    return {"kelly_fraction": round(f,3), "safe_pct": round(f*0.5*100,1)}

def render():
    st.title("🤝 Chama / SACCO Trust Engine")
    st.caption("DEMO — group health scoring + Kelly Criterion lending capacity")
    st.info("Pattern: *Python Data Analysis* (Packt) + ML4T Ch.5 Kelly Criterion")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Group Profile")
        group_size = st.slider("Active Members", 5, 50, 15)
        months_active = st.slider("Months Active", 1, 120, 18)
        kitty = st.number_input("Total Kitty (KES)", 10000, 5000000, 150000, step=10000)
        consistency = st.slider("Contribution Consistency %", 0, 100, 75)/100
        default_rate = st.slider("Loan Default Rate %", 0, 50, 8)/100
    
    with col2:
        r = risk_score(consistency, default_rate, months_active, group_size)
        k = kelly_group_lending(1-default_rate, 0.85, 0.40)
        
        g_color = {"A":"🟢","B":"🟡","C":"🟠","D":"🔴"}.get(r["grade"],"⚪")
        st.metric("Trust Score", f"{r['total']}/100", delta=f"Grade {r['grade']} {g_color}")
        st.info(f"**Recommendation:** {r['recommendation']}")
        
        max_loan = int(kitty * k["safe_pct"] / 100)
        st.metric("Max Safe Loan per Member (half-Kelly)", f"KES {max_loan:,}")
        st.caption(f"Kelly fraction: {k['kelly_fraction']:.3f} → safe lending: {k['safe_pct']}% of kitty")

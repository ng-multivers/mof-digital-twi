import streamlit as st
import datetime

# Apply consistent government styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=RijksOverheid+Sans:wght@400;500;600;700&display=swap');
    
    .gov-page-header {
        background: #01689b;
        color: white;
        padding: 1.5rem;
        margin: -1rem -1rem 2rem -1rem;
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
    }
    
    .gov-page-header h1 {
        color: white;
        font-size: 2rem;
        margin: 0;
    }
    
    .metric-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-left: 4px solid #01689b;
        padding: 1rem;
        border-radius: 3px;
        margin-bottom: 1rem;
    }
    
    .gov-button {
        background-color: #01689b !important;
        color: white !important;
        border: none !important;
        border-radius: 3px !important;
        padding: 0.75rem 1.5rem !important;
        font-family: 'RijksOverheid Sans', Arial, sans-serif !important;
        font-weight: 500 !important;
        width: 100% !important;
        margin-bottom: 0.5rem !important;
    }
    
    .gov-section {
        border-left: 4px solid #01689b;
        padding-left: 1rem;
        margin: 1rem 0;
    }
             [data-testid="stSidebarNav"]{
    display:none;    
    }
    
</style>
""", unsafe_allow_html=True)

# Navigation links with official ministry structure
st.sidebar.page_link("pages/2_Create_Digital_Twin.py", label="📋 Digital Twin")
st.sidebar.page_link("pages/3_Knowledge_Library.py", label="📚 Knowledge Library")
st.sidebar.page_link("pages/4_AI_Coach.py", label="🧠 AI Coach")
st.sidebar.page_link("pages/5_Recognition_Stories.py", label="🏆 Recognition & Impact")

st.markdown("""
<div class="gov-page-header">
    <h1>🏛️Ministry of Finance Dashboard</h1>
</div>
""", unsafe_allow_html=True)

# Welcome message with ministry context
st.markdown("""
<div class="gov-section">
<strong>Welcome, Ministry of Finance employee!</strong> <br/>
This dashboard shows your progress in knowledge sharing and expertise development within the ministry.
</div>
""", unsafe_allow_html=True)



# Personal stats with ministry-specific metrics
st.subheader("📊 Your Ministry Performance")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Policy Documents", "12", "3")
with col2:
    st.metric("Expertise Modules", "7", "2")
with col3:
    st.metric("Simulations Completed", "15", "5")
with col4:
    st.metric("Colleagues Helped", "23", "8")

# Ministry-specific popular links
st.subheader("🔗 Popular Links")
colA, colB = st.columns(2)
with colA:
    st.markdown("**📋 Expertise & Documentation**")
    if st.button("📝 Digital Twin"):
        st.switch_page("pages/2_Create_Digital_Twin.py")
    if st.button("📚 Explore Knowledge Library"):
        st.switch_page("pages/3_Knowledge_Library.py")
        
with colB:
    st.markdown("**🧠 Training & Simulation**")
    if st.button("🧠 AI Policy Coach"):
        st.switch_page("pages/4_AI_Coach.py")
    # Scenario training is now integrated into AI Coach



# Ministry news and updates
st.markdown("---")
st.subheader("📰 Ministry Updates")
col_news1, col_news2 = st.columns(2)
with col_news1:
    st.markdown("""
    **🔥 Trending Expertise Areas:**
    - 💰 2025 Tax Plan Implementation  
    - 📊 Budget Day 2024 Follow-up
    - 🌱 Sustainable Finance Transition
    """)
with col_news2:
    st.markdown("""
    **🏆 This Week's Top Contributors:**
    - 🥇 Cara Antione (Tax Administration)
    - 🥈 Mirjam van Kuilenberg (State Debt)
    - 🥉 Thijs Geurts (EU Finance)
    """)

# Current ministry priorities based on government.nl news
st.warning("⚠️ **Important**: 2025 Tax Plan implementation - new training modules available in Scenario Learning")


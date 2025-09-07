import streamlit as st

# Apply consistent government styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=RijksOverheid+Sans:wght@400;500;600;700&display=swap');
    
    /* Main background styling */
    .main .block-container {
        background-color: #f8f9fa;
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
    }
             [data-testid="stSidebarNav"]{
    display:none;    
    }
    
    
    .gov-page-header {
        background: #01689b;
        color: white;
        padding: 1.5rem;
        margin: -1rem -1rem 2rem -1rem;
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
        border-radius: 0 0 8px 8px;
    }
    
    .gov-page-header h1 {
        color: white;
        font-size: 2rem;
        margin: 0;
        font-weight: 700;
    }
    
    /* Impact cards */
    .impact-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-left: 4px solid #01689b;
        padding: 1.5rem;
        border-radius: 3px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Champion cards */
    .champion-card {
        background: linear-gradient(135deg, #01689b, #014d73);
        color: white;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Government buttons */
    .stButton > button {
        background-color: #01689b !important;
        color: white !important;
        border: none !important;
        border-radius: 3px !important;
        padding: 0.75rem 1.5rem !important;
        font-family: 'RijksOverheid Sans', Arial, sans-serif !important;
        font-weight: 500 !important;
        transition: background-color 0.3s !important;
    }
    
    .stButton > button:hover {
        background-color: #014d73 !important;
        color: white !important;
    }
    
    /* Form styling */
    .stSelectbox, .stTextInput, .stTextArea {
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
    }
    
    /* Metrics styling */
    .metric-container {
        background: white;
        border: 1px solid #e0e0e0;
        border-left: 4px solid #01689b;
        padding: 1rem;
        border-radius: 3px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Awards section */
    .awards-section {
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        border: 2px solid #01689b;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
        color: #01689b;
    }
    
    /* Alert boxes */
    .stAlert {
        border-left: 4px solid #01689b;
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="gov-page-header">
    <h1>🏆 Ministry Recognition & Impact</h1>
</div>
""", unsafe_allow_html=True)


# Navigation links with official ministry structure
st.sidebar.page_link("pages/1_Home.py", label="🏠 Dashboard")
st.sidebar.page_link("pages/2_Create_Digital_Twin.py", label="📋 Create Digital Twin")
st.sidebar.page_link("pages/3_Knowledge_Library.py", label="📚 Knowledge Library")
st.sidebar.page_link("pages/4_AI_Coach.py", label="🧠 AI Coach")
st.sidebar.page_link("pages/5_Recognition_Stories.py", label="🏆 Recognition & Impact")

st.markdown("""
**Recognize and share the impact of knowledge sharing within the Ministry of Finance** 🏛️  
Celebrate successes, share experiences and inspire colleagues to continue sharing their expertise.
""")

# Ministry recognition levels
st.subheader("🥇 Ministry Knowledge Champions")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **🏅 Q3 2025 Impact Champions:**
    
    **🥇 Cara Antione** - *EU Legislation Specialist*  
    📍 *Tax Administration*  
    💫 *"Her Brexit compliance module helped 47 colleagues and prevented €2.3M in fines"*
    """)
    
with col2:
    st.markdown("""
    **🥈 Mirjam van Kuilenberg** - *State Debt Analyst*  
    📍 *Treasury & State Debt*  
    💫 *"His digital euro scenario training was downloaded 156x by other ministries"*
    """)

# Impact metrics for ministry
st.markdown("---")
st.subheader("📈 Ministry Knowledge Sharing Impact")
col_metric1, col_metric2, col_metric3, col_metric4 = st.columns(4)
with col_metric1:
    st.metric("Active Experts", "127", "23")
with col_metric2:
    st.metric("Expertise Modules", "89", "15")
with col_metric3:
    st.metric("Cross-Department Collaboration", "234", "45")
with col_metric4:
    st.metric("Saved Training Costs", "€450K", "€75K")

# Success stories specific to ministry work
st.markdown("---")
st.subheader("💼 Recent Impact Stories")

with st.expander("🚀 **EU Taxonomy Crisis Response** - *By Cara Antione*"):
    st.markdown("""
    **Situation:** When EU taxonomy changes were announced, the ministry had a complete response strategy within 4 hours.
    
    **Impact:** 
    - ✅ 23 Dutch financial institutions received direct guidance
    - ✅ €15M in compliance costs saved for the sector  
    - ✅ Netherlands was first EU country with official position
    
    **Feedback:** *"Emma's expertise module on EU legislation processes made the difference. We could respond quickly and accurately."* - **Minister of Finance**
    """)

with st.expander("💱 **Digital Euro Pilot Success** - *By Mirjam van Kuilenberg*"):
    st.markdown("""
    **Situation:** Netherlands was selected as pilot for digital euro implementation.
    
    **Impact:**
    - ✅ 5 other EU countries now use our implementation strategy
    - ✅ 67% faster startup thanks to documented processes
    - ✅ DNB partnership model becomes EU-wide standard
    
    **Feedback:** *"Pieter's scenario planning module was essential for our pilot success."* - **DNB Director**
    """)

# Recognition submission form
st.markdown("---")
st.subheader("📝 Share Your Impact Story")
st.markdown("*Help other colleagues by sharing your successes and lessons learned*")

story_category = st.selectbox("Impact Category", [
    "EU Legislation & Compliance",
    "Tax Reform",
    "Digital Finance Innovation",
    "International Tax Cooperation",
    "Crisis Management & Response",
    "Stakeholder Management",
    "Cross-Department Collaboration"
])

department = st.selectbox("Your Department", [
    "Tax Administration",
    "EU & International Finance", 
    "Financial Markets",
    "State Debt Management",
    "Budget Affairs",
    "Fiscal Policy",
    "Customs",
    "Benefits"
])

impact_story = st.text_area(
    "Describe how knowledge sharing had impact:", 
    placeholder="E.g. Thanks to colleague X's expertise module, we were able to develop an EU compliance strategy within 24 hours that prevented €2M in fines..."
)

quantified_impact = st.text_input(
    "Quantifiable impact (optional):", 
    placeholder="E.g. €500K saved, 50 colleagues helped, 3 days faster process"
)

if st.button("🏛️ Submit Impact Story"):
    if impact_story:
        st.success("✅ **Thank you!** Your impact story has been submitted and will be reviewed by the Knowledge Management team within 48 hours.")
        st.info("🎯 **Next steps:** Successful stories will be shared in the ministry newsletter and may lead to formal recognition during team meetings.")
    else:
        st.error("⚠️ Please fill in your impact story.")

# Ministry awards program
st.markdown("---")
st.subheader("🏅 Ministry Awards Program")
col_award1, col_award2 = st.columns(2)
with col_award1:
    st.markdown("""
    **🏆 Annual Awards:**
    - 🥇 **Innovation Excellence Award** (€2,500 + week training Brussels)
    - 🥈 **Cross-Department Collaboration** (€1,500 + minister meeting)  
    - 🥉 **Knowledge Sharing Impact** (€1,000 + LinkedIn feature)
    """)
with col_award2:
    st.markdown("""
    **📅 Important Dates 2025:**
    - **Q2 Review:** June 15, 2025
    - **Award Nominations:** September 1, 2025
    - **Award Ceremony:** December 15, 2025 (Minister present)
    """)

st.info("💡 **Pro Tip:** The best impact stories show measurable results and help multiple colleagues. Focus on concrete examples and numbers!")

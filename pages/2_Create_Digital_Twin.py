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
    
    /* Content sections */
    .gov-section {
        background: white;
        border: 1px solid #e0e0e0;
        border-left: 4px solid #01689b;
        padding: 1.5rem;
        border-radius: 3px;
        margin: 1rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
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
        width: 100% !important;
    }
    
    .stButton > button:hover {
        background-color: #014d73 !important;
        color: white !important;
    }
    
    /* Form styling */
    .stSelectbox, .stTextInput, .stTextArea, .stMultiselect {
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
    }
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
        color: #01689b;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="gov-page-header">
    <h1>📋 Create Digital Twin</h1>
</div>
""", unsafe_allow_html=True)


# Navigation links with official ministry structure
st.sidebar.page_link("pages/1_Home.py", label="🏠 Dashboard")
st.sidebar.page_link("pages/2_Create_Digital_Twin.py", label="📋 Create Digital Twin")
st.sidebar.page_link("pages/3_Knowledge_Library.py", label="📚 Knowledge Library")
st.sidebar.page_link("pages/4_AI_Coach.py", label="🧠 AI Coach")
st.sidebar.page_link("pages/5_Recognition_Stories.py", label="🏆 Recognition & Impact")

st.markdown("""
Help colleagues and future employees by capturing your knowledge of policies, processes, and procedures.🏛️ 
""")

# Ministry department selection
dept = st.selectbox("🏢 Ministry Department", [
    "Tax Administration", 
    "State Debt Management", 
    "EU & International Finance",
    "Financial Markets",
    "Budget Affairs",
    "Fiscal Policy",
    "Customs",
    "Benefits"
])

st.markdown("---")

step = st.radio("📑 Step 1: Choose documentation type", [
    "Policy Process Video", 
    "Templates & Checklists", 
    "Expertise Profile"
])

if step == "Policy Process Video":
    st.markdown("**🎬 Video Documentation of Policy Processes**")
    st.file_uploader("Upload your screen recording", type=["mp4", "mov", "avi"])
    
    process_type = st.selectbox("Process Type", [
        "Legislative and regulatory analysis",
        "Tax revision procedure", 
        "EU directive implementation",
        "Risk assessment",
        "Stakeholder consultation",
        "Budget allocation process"
    ])
    
    st.text_area("Process Explanation", placeholder="Describe the policy process step by step...")
    st.text_area("Critical Points", placeholder="What pitfalls or important details should colleagues know?")
    
elif step == "Templates & Checklists":
    st.markdown("**📄 Ministry Templates and Procedural Documents**")
    st.file_uploader("Upload policy template", type=["pdf", "docx", "xlsx", "pptx"])
    
    template_category = st.selectbox("Template Category", [
        "Legislative and regulatory templates",
        "Policy impact assessments", 
        "EU compliance checklists",
        "Budget proposal formats",
        "Stakeholder communication templates",
        "Risk evaluation forms"
    ])
    
    st.text_area("Template Usage", placeholder="When and how do you use this template? Which steps are crucial?")
    
elif step == "Expertise Profile":
    st.markdown("**👤 Your Ministry Expertise Profile**")
    role = st.text_input("Job Title", placeholder="e.g. Senior Policy Advisor Taxation")
    
    expertise_areas = st.multiselect("Expertise Areas", [
        "Dutch Tax Legislation",
        "EU Fiscal Governance", 
        "International Tax Treaties",
        "ESG & Sustainable Finance",
        "Digital Euro Development",
        "Brexit Financial Impact",
        "State Aid Regulations",
        "Public Debt Management",
        "Financial Market Supervision",
        "Anti-Money Laundering (AML)"
    ])
    
    experience_level = st.slider("Years of Ministry Experience", 0, 30, 5)
    
    st.text_area("Critical Knowledge", placeholder="What unique knowledge do you have that is essential for the ministry?")
    
    languages = st.multiselect("Languages", ["Dutch", "English", "French", "German", "Spanish"])

# Compliance and security
st.markdown("---")
st.subheader("🔐 Compliance & Security")

security_level = st.selectbox("Classification Level", [
    "Departmentally Confidential (DC)",
    "State Secret Confidential (SC)", 
    "Not Classified (NC)"
])

st.checkbox("✅ I confirm this information contains no state secrets")
st.checkbox("✅ I confirm this documentation complies with GDPR requirements")

st.markdown("---")
if st.button("🏛️ Submit Expertise Documentation"):
    st.success("✅ Your expertise documentation has been successfully submitted and you have created your Digital Twin!")
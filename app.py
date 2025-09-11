import streamlit as st

st.set_page_config(
    page_title="FinanceGov Digital Expertise Platform", 
    layout="wide",
    page_icon="🏛️"
)

# Official Ministry of Finance styling based on government.nl
st.markdown("""
<style>
    /* Import official government fonts */
    @import url('https://fonts.googleapis.com/css2?family=RijksOverheid+Sans:wght@400;500;600;700&display=swap');
    
    /* Main header styling matching government.nl */
    .main-header {
        background: #01689b;
        padding: 2rem 1rem;
        color: white;
        text-align: left;
        margin-bottom: 2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
        margin: 0;
        color: white;
    }
    
    .main-header h2 {
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
        font-weight: 400;
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        color: white;
        opacity: 0.9;
    }
    
    /* Government badge styling */
    .ministry-badge {
        background: white;
        color: #01689b;
        padding: 0.5rem 1rem;
        border-radius: 3px;
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 1rem;
        display: inline-block;
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
    }
    
    /* Sidebar government styling */
    .sidebar .element-container {
        background-color: white;
        border-right: 3px solid #01689b;
    }
            
    [data-testid="stSidebarNav"]{
    display:none;    
    }
    
    /* Government navigation styling */
    .gov-nav-title {
        color: #01689b;
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 1rem;
    }
    
    /* Main content area */
    .main .block-container {
        padding-top: 1rem;
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
    }
    
    /* Government buttons */
    .stButton > button {
        background-color: #01689b;
        color: white;
        border: none;
        border-radius: 3px;
        padding: 0.5rem 1rem;
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
        font-weight: 500;
        transition: background-color 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #014d73;
        color: white;
    }
    
    /* Government info boxes */
    .stAlert {
        border-left: 4px solid #01689b;
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
    }
    
    /* Government links */
    a {
        color: #01689b;
        text-decoration: underline;
    }
    
    a:hover {
        color: #014d73;
    }
    
    /* Government headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
        color: #000000;
    }
    
    /* Government metrics */
    .metric-container {
        background: white;
        border: 1px solid #e0e0e0;
        border-left: 4px solid #01689b;
        padding: 1rem;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# Official Ministry Header matching government.nl design
st.markdown("""
<div class="main-header">
    <h1>Ministry of Finance</h1>
    <h2>Digital Expertise & Knowledge Transfer Platform</h2>
    <span class="ministry-badge">Government of the Netherlands</span>
</div>
""", unsafe_allow_html=True)


# Navigation links with official ministry structure
st.sidebar.page_link("app.py", label="🏠 Home")
st.sidebar.page_link("pages/2_Create_Digital_Twin.py", label="📋 Digital Twin")
st.sidebar.page_link("pages/3_Knowledge_Library.py", label="📚 Knowledge Library")
st.sidebar.page_link("pages/4_AI_Coach.py", label="🧠 AI Coach")
st.sidebar.page_link("pages/5_Recognition_Stories.py", label="🏆 Recognition & Impact")

st.sidebar.markdown("---") 
st.sidebar.info("🔒 Secure system for internal employees of the Ministry of Finance")

# Government footer reference
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="font-size: 0.8rem; color: #666;">
<a href="https://www.government.nl/ministries/ministry-of-finance" target="_blank">
Official Ministry Website
</a>
</div>
""", unsafe_allow_html=True)

st.markdown("### Welcome to the Digital Expertise Platform")
st.markdown("This platform helps Ministry of Finance employees share their expertise and transfer knowledge for more effective government operations.")
st.info("💡 **Select a module** from the sidebar to begin knowledge sharing and training.")

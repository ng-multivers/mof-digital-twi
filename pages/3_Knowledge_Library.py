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
    
    /* Search and form styling */
    .stTextInput, .stSelectbox {
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
    }
    
    /* Resource cards */
    .resource-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-left: 4px solid #01689b;
        padding: 1rem;
        border-radius: 3px;
        margin: 0.5rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'RijksOverheid Sans', Arial, sans-serif;
        color: #01689b;
    }
    
    /* Links */
    a {
        color: #01689b;
        text-decoration: underline;
    }
    
    a:hover {
        color: #014d73;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="gov-page-header">
    <h1>📚 Ministry Knowledge Library</h1>
</div>
""", unsafe_allow_html=True)


# Navigation links with official ministry structure
st.sidebar.page_link("app.py", label="🏠 Home")
st.sidebar.page_link("pages/2_Create_Digital_Twin.py", label="📋 Digital Twin")
st.sidebar.page_link("pages/3_Knowledge_Library.py", label="📚 Knowledge Library")
st.sidebar.page_link("pages/4_AI_Coach.py", label="🧠 AI Coach")
st.sidebar.page_link("pages/5_Recognition_Stories.py", label="🏆 Recognition & Impact")

st.markdown("""
**Central knowledge bank of the Ministry of Finance** 🏛️  
Access to all policy documents, procedures, training materials and colleagues' expertise.
""")

# Search functionality
st.subheader("🔍 Search Knowledge Bank")
search_query = st.text_input("Search in documents, procedures and expertise...", placeholder="e.g. EU directives, tax procedures")

if search_query:
    st.info(f"🔍 Search results for: '{search_query}'")

# Main topic categories for Finance Ministry
topics = [
    "🏦 EU & International Finance", 
    "💰 Dutch Tax Legislation", 
    "🇪🇺 Brexit Impact & Procedures",
    "💱 Digital Euro & FinTech",
    "⚖️ Compliance & Anti-Money Laundering",
    "📈 State Debt & Treasury Management",
    "🏛️ Budget Processes & Procedures"
]

selected_topic = st.selectbox("📂 Select Knowledge Area:", topics)

st.markdown("---")
st.write(f"### Available resources for: **{selected_topic}**")

# Topic-specific content
if "EU & International" in selected_topic:
    st.markdown("""
    **📋 Policy Documents:**
    - 📄 [EU State Aid Guidelines 2024](https://ec.europa.eu) *(Last updated: Jan 2024)*
    - 📄 [OECD Tax Treaty Model](https://oecd.org) *(Dutch implementation)*
    - 📄 [EU Fiscal Governance Framework](https://europa.eu) *(Post-COVID adjustments)*
    
    **🎥 Training Videos:**
    - 🎬 [EU Directive Implementation Process](#) *(45 min)*
    - 🎬 [International Tax Treaties](#) *(32 min)*
    - 🎬 [Brexit Impact on Dutch Finance](#) *(28 min)*
    
    **🧾 Procedure Guides:**
    - 📋 [EU Consultation Response Template](#)
    - 📋 [State Aid Assessment Checklist](#)
    - 📋 [International Tax Dispute Resolution](#)
    """)
    
elif "Tax Legislation" in selected_topic:
    st.markdown("""
    **📋 Laws & Regulations:**
    - ⚖️ [Income Tax Act 2001](https://wetten.nl) *(Current version)*
    - ⚖️ [Value Added Tax Act](https://wetten.nl) *(Including EU adjustments)*
    - ⚖️ [General State Taxes Act](https://wetten.nl) *(With jurisprudence)*
    
    **🎥 Masterclasses:**
    - 🎓 [Tax Avoidance Directive Implementation](#) *(2 hours)*
    - 🎓 [Digital Services Tax Overview](#) *(1.5 hours)*
    - 🎓 [International Profit Shifting Rules](#) *(3 hours)*
    
    **🔧 Practical Tools:**
    - 🧮 [Tax Impact Calculator](#)
    - 📊 [Revenue Estimation Models](#)
    - 📈 [Tax Policy Scenario Planner](#)
    """)
    
elif "Budget Processes & Procedures" in selected_topic:
    st.markdown("""
    **📋 General Resources:**
    - 📊 [Budget Allocation and Distribution](#)
    - 🧾 [Budget Monitoring and Control](#)
    - 📄 [Budget Closure and Audit](#)
    """)

else:
    st.markdown("""
    **📋 General Resources:**
    - 📄 [Ministry Procedures Handbook](#)
    - 🎥 [Onboarding Video Series](#)
    - 📋 [Template Library](#)
    - 🧾 [Best Practices Guide](#)
    """)

# Recent updates section
st.markdown("---")
st.subheader("🆕 Recent Updates")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Added This Week:**
    - 🆕 EU Anti-Tax Avoidance Directive III
    - 🆕 Digital Euro Pilot Program Guidelines  
    - 🆕 Updated Brexit Financial Services Guide
    """)
with col2:
    st.markdown("""
    **Popular Downloads:**
    - 📥 State Aid Quick Reference (623x)
    - 📥 Tax Treaty Application Forms (445x)
    """)

# Expert contacts
st.markdown("---")
st.subheader("👥 Expert Contacts")
st.markdown("""
**🎯 Subject Matter Experts:**
- **Digital Finance**: Thijs Geurts (ext. 2756)
- **International Tax**: Ronald van den Berg   (ext. 2634)
""")

st.success("💡 **Tip**: Use Ctrl+F to quickly search within documents. All resources are accessible through your ministry account.")

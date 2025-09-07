import streamlit as st
import random

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
    
    /* Scenario cards */
    .scenario-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-left: 4px solid #01689b;
        padding: 1.5rem;
        border-radius: 3px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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
    
    /* Radio buttons and form styling */
    .stRadio, .stSelectbox {
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
    <h1>🧠 AI Policy Coach & Training Platform</h1>
</div>
""", unsafe_allow_html=True)


# Navigation links with official ministry structure
st.sidebar.page_link("pages/1_Home.py", label="🏠 Dashboard")
st.sidebar.page_link("pages/2_Create_Digital_Twin.py", label="📋 Create Digital Twin")
st.sidebar.page_link("pages/3_Knowledge_Library.py", label="📚 Knowledge Library")
st.sidebar.page_link("pages/4_AI_Coach.py", label="🧠 AI Coach")
st.sidebar.page_link("pages/5_Recognition_Stories.py", label="🏆 Recognition & Impact")

st.markdown("""
**Advanced AI-powered coaching for Ministry of Finance** 🏛️  
Develop your decision-making skills through complex, realistic policy situations with personalized AI guidance specific to your ministry work based on the information provided to the digital twin by your colleagues.
""")

# Comprehensive scenario bank for Finance Ministry
scenarios = {
    "EU Directive Crisis": {
        "context": "The EU suddenly announces new Anti-Tax Avoidance directives that must be implemented within 6 months. Dutch companies are panicking.",
        "situation": "You are a Senior Policy Advisor. The minister asks for an urgent impact assessment and implementation strategy.",
        "options": [
            "Immediately start stakeholder consultation with business sector",
            "First conduct legal analysis of the directive details",
            "Set up parallel team: legal + impact assessment + communication"
        ],
        "correct": 2,
        "explanation": "With urgent EU legislation, you must work in parallel. Legal analysis, impact assessment, and stakeholder communication must run simultaneously for effective implementation."
    },
    
    "Brexit Consequences": {
        "context": "Post-Brexit: Dutch financial service providers lose access to London markets. The sector asks for state aid.",
        "situation": "You advise on state aid possibilities within EU state aid rules. What is your first step?",
        "options": [
            "Directly grant state aid - the sector is critical",
            "Consult EU Commission about state aid possibilities",
            "Wait until other EU countries take their position"
        ],
        "correct": 1,
        "explanation": "State aid rules are strictly regulated by the EU. Consultation with the Commission prevents legal problems and ensures compliant support for the financial sector."
    },
    
    "Digital Euro Decision": {
        "context": "The ECB asks member states for input on digital euro implementation. DNB and ministry must respond jointly.",
        "situation": "Different departments have conflicting visions. How do you coordinate the Dutch position?",
        "options": [
            "Let DNB take the lead - they are the experts",
            "Ministry takes the lead - policy is our responsibility", 
            "Joint working group with clear mandates per organization"
        ],
        "correct": 2,
        "explanation": "Digital euro affects both monetary policy (DNB) and fiscal/regulatory policy (Ministry). Joint approach with clear role division is essential."
    },
    
    "EU Taxonomy Crisis Management": {
        "context": "The EU suddenly publishes surprising changes to taxonomy rules for sustainable financing. Dutch banks and pension funds are panicking because their green investments suddenly no longer qualify.",
        "situation": "The media is asking for a ministry response within 2 hours.",
        "options": [
            "Immediately organize a press conference to reassure the sector",
            "First conduct legal analysis and then respond",
            "Activate crisis team: parallel legal analysis + stakeholder consultation + communication strategy",
            "Wait for reactions from other EU member states before the Netherlands responds"
        ],
        "correct": 2,
        "explanation": "In financial regulation crises, you must work in parallel: legal analysis for correct facts, stakeholder consultation for impact assessment, and communication to maintain market stability."
    },
    
    "Brexit Financial Services Escalation": {
        "context": "Post-Brexit: The UK announces that Dutch financial service providers must immediately close their London offices due to new rules.",
        "situation": "ABN AMRO, ING and other major banks threaten lawsuits and ask for Dutch government intervention.",
        "options": [
            "Direct diplomatic escalation to the UK government",
            "Support legal steps via EU mechanisms", 
            "First impact assessment + consultation with DNB + then diplomatic route",
            "Advise the sector to accept UK rules"
        ],
        "correct": 2,
        "explanation": "Financial services are crucial for the Dutch economy. Impact assessment with DNB gives you the facts, after which you can take well-informed diplomatic steps."
    },
    
    "Digital Euro Implementation Dilemma": {
        "context": "The ECB asks the Netherlands to serve as a pilot country for the digital euro. DNB is enthusiastic, but the House of Representatives is concerned about privacy and the impact on Dutch banks.",
        "situation": "You must formulate a ministerial position within 48 hours.",
        "options": [
            "Say yes - innovation is important for the Netherlands",
            "Say no - too many risks for Dutch banks",
            "Conditional yes: only with strict privacy safeguards and compensation mechanisms for banks",
            "Pass to next cabinet - too complex for quick decision"
        ],
        "correct": 2,
        "explanation": "Digital euro pilot offers opportunities but has real risks. Conditional agreement shows leadership while protecting Dutch interests through privacy rules and bank compensation."
    },
    
    "State Aid Emergency Response": {
        "context": "A large Dutch multinational threatens to move 15,000 jobs to Ireland due to better tax advantages. The company asks for Dutch state aid.",
        "situation": "The EU has strict state aid rules, but other countries also provide support. The prime minister wants a solution within 72 hours.",
        "options": [
            "Immediately offer state aid - jobs are more important than EU rules",
            "Strictly follow EU rules - no state aid",
            "Creative compliance: state aid via R&D subsidies and training programs within EU rules",
            "Bilateral consultation with Ireland to prevent 'race to the bottom'"
        ],
        "correct": 2,
        "explanation": "State aid rules are strict, but there are legal ways such as R&D and training subsidies. This protects jobs while remaining EU compliant and preventing precedent."
    },
    
    "ESG Reporting Resistance": {
        "context": "Dutch companies massively resist new EU ESG reporting rules. They claim costs are too high and threaten lawsuits.",
        "situation": "Several other EU countries are considering postponement of implementation. The Netherlands must take a position within a week.",
        "options": [
            "Go along with other countries and ask the EU for postponement",
            "Strictly implement according to EU timeline - rules are rules", 
            "Compromise: implementation on schedule but with transition period and support for companies",
            "Give Dutch companies exemption until other countries also implement"
        ],
        "correct": 2,
        "explanation": "ESG reporting is essential for climate goals. A transition period with support helps companies adapt while the Netherlands respects EU legislation."
    }
}

# Scenario selection interface
st.subheader("🎯 AI Coaching Session Setup")
scenario_choice = st.radio("Choose your coaching approach:", [
    "🎲 AI-Recommended Scenario (Adaptive coaching)",
    "📋 Choose Specific Scenario"
])

if scenario_choice == "🎲 AI-Recommended Scenario (Adaptive coaching)":
    if st.button("🎲 Start AI Coaching Session"):
        selected_scenario = random.choice(list(scenarios.keys()))
        st.session_state['current_scenario'] = selected_scenario
else:
    selected_scenario = st.selectbox("📌 Choose a Ministry Scenario:", list(scenarios.keys()))
    if st.button("▶️ Start Coaching Session"):
        st.session_state['current_scenario'] = selected_scenario

# Display active scenario
if 'current_scenario' in st.session_state:
    scenario_name = st.session_state['current_scenario']
    scenario = scenarios[scenario_name]
    
    st.markdown("---")
    st.subheader(f"🎯 AI Coaching Session: {scenario_name}")
    
    st.markdown(f"**🌍 Context:**\n{scenario['context']}")
    st.markdown(f"**⚡ Situation:**\n{scenario['situation']}")
    
    st.markdown("**🤔 How would you respond as a ministry advisor?**")
    choice = st.radio("Select your recommendation:", scenario['options'], key="scenario_choice")
    
    if st.button("📤 Get AI Coach Feedback"):
        correct_option = scenario['options'][scenario['correct']]
        
        if choice == correct_option:
            st.success("🎉 **Excellent policy analysis!** Your approach shows strategic insight and balances all ministry responsibilities.")
        else:
            st.error("⚠️ **Not the best approach.** This strategy may lead to unforeseen complications for the ministry.")
            st.info(f"**🎯 AI Coach Recommendation:** {correct_option}")
            
        st.info(f"**💡 AI Coach Insight:** {scenario['explanation']}")
        
        # Performance tracking
        st.markdown("---")
        st.subheader("📊 Your Coaching Progress")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Coaching Sessions", "42", "1")
        with col2:
            st.metric("Policy Expertise Score", "87%", "3%")
        with col3:
            st.metric("AI Coach Rating", "Advanced", "")
            
        if st.button("🔄 New Coaching Session"):
            if 'current_scenario' in st.session_state:
                del st.session_state['current_scenario']
            st.rerun()


# Ministerie van Financiën - Digital Expertise Platform 🏛️

A specialized Streamlit-based application designed exclusively for the Netherlands Ministry of Finance (Ministerie van Financiën) that enables government employees to create digital twins of their policy expertise and facilitates knowledge transfer, scenario-based training, and continuous learning within the ministry.

## 🌟 Features

- **🎥 Digital Twin Creation**: Capture role knowledge through screen recordings, templates, and structured information
- **🧠 AI Role Simulation**: Interactive scenarios to practice decision-making in realistic work situations
- **📚 Knowledge Library**: Centralized repository of resources, guides, and training materials
- **🎓 Scenario-Based Learning**: Apply knowledge through immersive, role-specific scenarios
- **🌟 Recognition & Stories**: Share success stories and recognize knowledge champions
- **🏠 Dashboard**: Track personal progress and quick access to all features

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd digital_twin_app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Streamlit server**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The application will automatically open in your default browser
   - If it doesn't open automatically, go to `http://localhost:8501`

## 📁 Project Structure

```
digital_twin_app/
├── app.py                           # Main application entry point
├── requirements.txt                 # Python dependencies
├── README.md                       # This file
├── assets/
│   └── templates/                  # Template files and assets
└── pages/
    ├── 1_Home.py                   # Dashboard and navigation
    ├── 2_Create_Digital_Twin.py    # Digital twin creation interface
    ├── 3_AI_Simulation.py          # Role simulation scenarios
    ├── 4_Knowledge_Library.py      # Resource library
    └── 5_Recognition_Stories.py    # Success stories and recognition
```

## 🎯 How to Use

### 1. Home Dashboard
- View your personal stats (recognition points, modules created, simulations completed)
- Quick access buttons to key features
- Navigation sidebar for easy movement between modules

### 2. Create Digital Twin
Choose from three options to capture your expertise:
- **Record Screen & Narration**: Upload video recordings with explanatory notes
- **Upload Templates**: Share checklists, documents, and templates with descriptions
- **Tag Role Info**: Structure your role information with departments and keywords

### 3. AI Role Simulation
- Practice decision-making in realistic work scenarios
- Receive immediate feedback on your choices
- Learn from different scenario outcomes

### 4. Knowledge Library
- Browse resources by topic (Customs Clearance, Client Onboarding, Inventory Management)
- Access checklists, training videos, and process guides
- Centralized knowledge repository

### 5. Scenario-Based Learning
- Engage with complex, multi-choice scenarios
- Apply knowledge in realistic workplace situations
- Learn from detailed feedback and explanations

### 6. Recognition & Stories
- View success stories from knowledge champions
- Submit your own impact stories
- Recognize colleagues who have helped you succeed

## 🛠️ Customization

### Adding New Scenarios
Edit `pages/5_Scenario_Learning.py` to add new learning scenarios:

```python
scenarios = {
    "Your New Scenario": {
        "description": "Scenario description...",
        "options": ["Option 1", "Option 2", "Option 3"],
        "correct": 0  # Index of correct option
    }
}
```

### Adding New Topics
Update the topics list in `pages/4_Knowledge_Library.py`:

```python
topics = ["Customs Clearance", "Client Onboarding", "Your New Topic"]
```

### Styling and Branding
- Modify the page configuration in `app.py`
- Update emojis and titles throughout the pages
- Add custom CSS using `st.markdown()` with HTML

## 🔧 Development

### Project Dependencies
- **Streamlit**: Web application framework for data science and ML applications
- Python 3.7+

### Adding New Features
1. Create new page files in the `pages/` directory
2. Update the navigation in `app.py`
3. Follow the existing naming convention (`N_Page_Name.py`)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Streamlit documentation](https://docs.streamlit.io/)
2. Review the error messages in the terminal
3. Ensure all dependencies are properly installed
4. Verify Python version compatibility

## 🚀 Deployment

### Local Deployment
Follow the installation instructions above.

### Cloud Deployment
This app can be deployed on various platforms:

- **Streamlit Cloud**: Connect your GitHub repository
- **Heroku**: Add a `Procfile` with `web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
- **AWS/GCP/Azure**: Use container services with appropriate configuration

---

**Built with ❤️ using Streamlit**

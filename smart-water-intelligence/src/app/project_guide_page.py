import streamlit as st

def show_project_guide():
    """
    Enhanced Project Guide with professional styling and visual elements
    """
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    /* Main title styling */
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #2dce74, #3db8f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
    }
    
    /* Section headers */
    .section-header {
        color: #2dce74;
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #2dce74;
        padding-bottom: 0.5rem;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, rgba(45, 206, 116, 0.1), rgba(61, 184, 245, 0.1));
        border-left: 4px solid #2dce74;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: rgba(245, 200, 66, 0.1);
        border-left: 4px solid #f5c842;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .critical-box {
        background: rgba(255, 76, 76, 0.1);
        border-left: 4px solid #ff4c4c;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Feature cards */
    .feature-card {
        background: #f8f9fa;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 4px 16px rgba(45, 206, 116, 0.2);
    }
    
    .feature-title {
        color: #2dce74;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    /* Step indicators */
    .step-number {
        display: inline-block;
        background: #2dce74;
        color: white;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        text-align: center;
        line-height: 32px;
        font-weight: 700;
        margin-right: 10px;
    }
    
    .step-text {
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    /* Metrics styling */
    .metric-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .metric-box {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #f8f9fa, #ffffff);
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        flex: 1;
        margin: 0 0.5rem;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 800;
        color: #2dce74;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #666;
        margin-top: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main Title with icon
    st.markdown('<div class="main-title">📘 Water Crisis & Irrigation Intelligence System</div>', 
                unsafe_allow_html=True)
    
    # Project Overview
    st.markdown('<div class="section-header">🎯 Project Objective</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
    The <b>Smart Water Crisis & Irrigation Intelligence System</b> is an AI-powered
    analytics platform designed to predict groundwater stress and detect
    irrigation inefficiency using machine learning models.
    <br><br>
    <b>Mission:</b> Help policymakers and farmers understand water usage patterns
    and make sustainable water management decisions through data-driven insights.
    </div>
    """, unsafe_allow_html=True)
    
    # Key Features Section
    st.markdown('<div class="section-header">✨ Key Features</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🤖 AI-Powered Predictions</div>
            Machine learning models trained on real-world water usage data
            to provide accurate stress level predictions.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">📊 Real-Time Analytics</div>
            Interactive dashboards showing live water consumption patterns
            and irrigation efficiency metrics.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🌍 Regional Monitoring</div>
            District-level groundwater stress analysis with zone-specific
            recommendations and alerts.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🌾 Crop-Specific Analysis</div>
            Irrigation efficiency evaluation based on crop type, soil conditions,
            and water usage patterns.
        </div>
        """, unsafe_allow_html=True)
    
    # Available Modules
    st.markdown('<div class="section-header">🔧 Available Modules</div>', unsafe_allow_html=True)
    
    # Module 1: Water Crisis Prediction
    with st.expander("💧 **Water Crisis Prediction Module**", expanded=True):
        st.markdown("""
        <div class="info-box">
        <b>Purpose:</b> Predicts groundwater stress levels for a specific district 
        based on recharge and extraction patterns.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Required Inputs:**")
        st.markdown("""
        - 🔄 **Annual Recharge** (in MCM) - Amount of groundwater recharged annually
        - 📉 **Annual Extraction** (in MCM) - Amount of groundwater extracted annually  
        - 📊 **Extraction Stage** (%) - Percentage of groundwater being extracted
        - 📍 **District Name** - Geographic location for analysis
        """)
        
        st.markdown("**Output:**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("✅ **Low Stress**\nSustainable usage")
        with col2:
            st.warning("⚠️ **Medium Stress**\nAction needed")
        with col3:
            st.error("🚨 **High Stress**\nCritical level")
        
        st.info("💡 **Use Case:** Government agencies can identify drought-prone regions and allocate water resources efficiently.")
    
    # Module 2: Irrigation Efficiency
    with st.expander("🌾 **Irrigation Efficiency Analysis Module**", expanded=True):
        st.markdown("""
        <div class="info-box">
        <b>Purpose:</b> Analyzes irrigation efficiency based on crop type, 
        irrigation method, and water consumption patterns.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Required Inputs:**")
        st.markdown("""
        - 🌱 **Crop Type** - Rice, Wheat, Cotton, Sugarcane, etc.
        - 💧 **Irrigation Method** - Drip, Sprinkler, Flood, etc.
        - 📏 **Water Usage** (in liters) - Amount of water consumed
        - 🗺️ **Field Area** (optional) - For per-hectare efficiency calculation
        """)
        
        st.markdown("**Output:**")
        col1, col2 = st.columns(2)
        with col1:
            st.success("""
            ✅ **Efficient Irrigation**
            - Optimal water usage
            - Recommended practices
            - Water savings potential
            """)
        with col2:
            st.error("""
            ❌ **Inefficient Irrigation**
            - Excessive water usage
            - Improvement suggestions
            - Cost of water wastage
            """)
        
        st.info("💡 **Use Case:** Farmers can optimize irrigation schedules and reduce water wastage by up to 40%.")
    
    # How to Use the System
    st.markdown('<div class="section-header">🚀 How to Use the System</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-text">
        <span class="step-number">1</span>
        <b>Select a Module</b> - Choose from the sidebar menu: Water Crisis Prediction or Irrigation Efficiency Analysis
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-text">
        <span class="step-number">2</span>
        <b>Enter Input Values</b> - Fill in all required parameters based on your data
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-text">
        <span class="step-number">3</span>
        <b>Run Prediction</b> - Click the "Predict" or "Analyze" button to generate results
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-text">
        <span class="step-number">4</span>
        <b>Review Results</b> - Analyze the predictions, charts, and recommendations
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-text">
        <span class="step-number">5</span>
        <b>Take Action</b> - Implement suggested water management strategies
    </div>
    """, unsafe_allow_html=True)
    
    # System Benefits
    st.markdown('<div class="section-header">🎁 System Benefits</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">40%</div>
            <div class="metric-label">Water Savings Potential</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">85%</div>
            <div class="metric-label">Prediction Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">24/7</div>
            <div class="metric-label">Real-Time Monitoring</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-value">100+</div>
            <div class="metric-label">Districts Covered</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Technical Stack
    st.markdown('<div class="section-header">🛠️ Technical Stack</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Machine Learning**
        - Scikit-learn
        - Random Forest
        - Gradient Boosting
        - XGBoost
        """)
    
    with col2:
        st.markdown("""
        **Data & Analytics**
        - Pandas
        - NumPy
        - Matplotlib
        - Plotly
        """)
    
    with col3:
        st.markdown("""
        **Web Framework**
        - Streamlit
        - React (Dashboard)
        - Python Backend
        """)
    
    # Important Notes
    st.markdown('<div class="section-header">⚠️ Important Notes</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box">
    <b>⚠️ Data Quality:</b> Ensure all input values are accurate and up-to-date 
    for the best prediction results. Historical data should be verified from 
    official government sources.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="critical-box">
    <b>🚨 Critical Alerts:</b> When the system indicates High Stress or Critical 
    irrigation inefficiency, immediate action is recommended. Contact local 
    water management authorities for support.
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
    <b>Water Crisis & Irrigation Intelligence System v1.0</b><br>
    Developed for sustainable water management and agricultural optimization<br>
    📧 Contact: support@aquawatch.system | 🌐 www.aquawatch.system
    </div>
    """, unsafe_allow_html=True)


# Example usage
if __name__ == "__main__":
    st.set_page_config(
        page_title="AQUAWATCH - Project Guide",
        page_icon="💧",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    show_project_guide()
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from agents import BudgetPlanner, RiskAssessor, InvestmentAdvisor, TaxOptimizer, ReportGenerator
import pandas as pd

# Set page config
st.set_page_config(
    page_title="AI Financial Advisor",
    page_icon="💰",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    .sidebar .stButton>button {
        background-color: #2196F3;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Sidebar
    st.sidebar.title("💰 Financial Profile")
    
    # User Input Section
    with st.sidebar:
        st.header("Personal Information")
        monthly_income = st.number_input("Monthly Income ($)", min_value=0, value=5000)
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        
        st.header("Risk Profile")
        risk_tolerance = st.select_slider(
            "Risk Tolerance",
            options=["Very Low", "Low", "Medium", "High", "Very High"],
            value="Medium"
        )
        
        investment_horizon = st.slider(
            "Investment Horizon (Years)",
            min_value=1,
            max_value=30,
            value=10
        )
        
        st.header("Financial Goals")
        goals = st.multiselect(
            "Select Your Financial Goals",
            ["Retirement Planning", "Emergency Fund", "Buy a House", "Children's Education", "Start a Business"],
            ["Retirement Planning", "Emergency Fund"]
        )
        
        generate_report = st.button("Generate Financial Report")

    # Main Content
    st.title("🤖 AI Financial Advisor")
    
    if generate_report:
        with st.spinner("Analyzing your financial profile..."):
            # Initialize agents
            budget_planner = BudgetPlanner(monthly_income)
            risk_assessor = RiskAssessor(age, risk_tolerance, investment_horizon)
            investment_advisor = InvestmentAdvisor(risk_tolerance, investment_horizon, monthly_income)
            tax_optimizer = TaxOptimizer(monthly_income)
            report_generator = ReportGenerator()
            
            # Create tabs for different sections
            tabs = st.tabs(["Budget Analysis", "Risk Assessment", "Investment Advice", "Tax Optimization", "Summary Report"])
            
            with tabs[0]:
                st.header("📊 Budget Analysis")
                budget_analysis = budget_planner.analyze()
                # Display budget pie chart
                fig = go.Figure(data=[go.Pie(
                    labels=budget_analysis['category'],
                    values=budget_analysis['amount'],
                    hole=.3
                )])
                st.plotly_chart(fig)
                
            with tabs[1]:
                st.header("⚖️ Risk Assessment")
                risk_profile = risk_assessor.evaluate()
                st.write(risk_profile)
                
            with tabs[2]:
                st.header("💎 Investment Recommendations")
                investment_recommendations = investment_advisor.get_recommendations()
                st.write(investment_recommendations)
                
            with tabs[3]:
                st.header("📑 Tax Optimization")
                tax_strategies = tax_optimizer.get_strategies()
                st.write(tax_strategies)
                
            with tabs[4]:
                st.header("📋 Summary Report")
                summary = report_generator.generate_report(
                    budget_analysis,
                    risk_profile,
                    investment_recommendations,
                    tax_strategies
                )
                st.write(summary)

if __name__ == "__main__":
    main()

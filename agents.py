import pandas as pd
import numpy as np
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import yfinance as yf

class BudgetPlanner:
    def __init__(self, monthly_income):
        self.monthly_income = monthly_income
        
    def analyze(self):
        """Generate a recommended budget allocation based on income."""
        # Example budget allocation (50/30/20 rule)
        budget_data = {
            'category': [
                'Essential Expenses (50%)',
                'Wants (30%)',
                'Savings & Debt (20%)'
            ],
            'amount': [
                self.monthly_income * 0.5,
                self.monthly_income * 0.3,
                self.monthly_income * 0.2
            ]
        }
        return pd.DataFrame(budget_data)

class RiskAssessor:
    def __init__(self, age, risk_tolerance, investment_horizon):
        self.age = age
        self.risk_tolerance = risk_tolerance
        self.investment_horizon = investment_horizon
        
    def evaluate(self):
        """Evaluate user's risk profile based on inputs."""
        risk_scores = {
            "Very Low": 1,
            "Low": 2,
            "Medium": 3,
            "High": 4,
            "Very High": 5
        }
        
        # Calculate risk score based on multiple factors
        risk_score = risk_scores[self.risk_tolerance]
        age_factor = (100 - self.age) / 100
        horizon_factor = self.investment_horizon / 30
        
        total_score = (risk_score + age_factor + horizon_factor) / 3
        
        risk_profile = {
            "risk_score": round(total_score, 2),
            "suggested_asset_allocation": self._get_asset_allocation(total_score),
            "risk_analysis": self._get_risk_analysis(total_score)
        }
        
        return risk_profile
    
    def _get_asset_allocation(self, risk_score):
        """Generate asset allocation based on risk score."""
        if risk_score < 1.5:
            return {"stocks": 20, "bonds": 60, "cash": 20}
        elif risk_score < 2.5:
            return {"stocks": 40, "bonds": 50, "cash": 10}
        elif risk_score < 3.5:
            return {"stocks": 60, "bonds": 30, "cash": 10}
        elif risk_score < 4.5:
            return {"stocks": 80, "bonds": 15, "cash": 5}
        else:
            return {"stocks": 90, "bonds": 5, "cash": 5}
    
    def _get_risk_analysis(self, risk_score):
        """Generate risk analysis description."""
        if risk_score < 1.5:
            return "Conservative investor focused on capital preservation"
        elif risk_score < 2.5:
            return "Moderate conservative investor seeking stable growth"
        elif risk_score < 3.5:
            return "Balanced investor looking for growth and stability"
        elif risk_score < 4.5:
            return "Growth-oriented investor comfortable with market volatility"
        else:
            return "Aggressive investor seeking maximum growth potential"

class InvestmentAdvisor:
    def __init__(self, risk_tolerance, investment_horizon, monthly_income):
        self.risk_tolerance = risk_tolerance
        self.investment_horizon = investment_horizon
        self.monthly_income = monthly_income
        
    def get_recommendations(self):
        """Generate investment recommendations based on risk profile and goals."""
        risk_levels = {
            "Very Low": self._get_conservative_portfolio(),
            "Low": self._get_moderate_conservative_portfolio(),
            "Medium": self._get_balanced_portfolio(),
            "High": self._get_growth_portfolio(),
            "Very High": self._get_aggressive_portfolio()
        }
        
        return risk_levels[self.risk_tolerance]
    
    def _get_conservative_portfolio(self):
        return {
            "recommendation": "Conservative Portfolio",
            "suggested_investments": [
                "High-yield savings accounts",
                "Government bonds",
                "Certificate of Deposits (CDs)",
                "Blue-chip dividend stocks (10-20%)"
            ],
            "monthly_investment": self.monthly_income * 0.2,
            "expected_return": "3-5% annually"
        }
    
    def _get_moderate_conservative_portfolio(self):
        return {
            "recommendation": "Moderate Conservative Portfolio",
            "suggested_investments": [
                "Government and corporate bonds (40-50%)",
                "Large-cap stocks (30-40%)",
                "Real Estate Investment Trusts (10-20%)",
                "Cash and equivalents (10%)"
            ],
            "monthly_investment": self.monthly_income * 0.2,
            "expected_return": "5-7% annually"
        }
    
    def _get_balanced_portfolio(self):
        return {
            "recommendation": "Balanced Portfolio",
            "suggested_investments": [
                "US stocks (40%)",
                "International stocks (20%)",
                "Bonds (30%)",
                "Real Estate and alternatives (10%)"
            ],
            "monthly_investment": self.monthly_income * 0.2,
            "expected_return": "7-9% annually"
        }
    
    def _get_growth_portfolio(self):
        return {
            "recommendation": "Growth Portfolio",
            "suggested_investments": [
                "US stocks (50%)",
                "International stocks (30%)",
                "Bonds (15%)",
                "Growth stocks and alternatives (5%)"
            ],
            "monthly_investment": self.monthly_income * 0.2,
            "expected_return": "9-11% annually"
        }
    
    def _get_aggressive_portfolio(self):
        return {
            "recommendation": "Aggressive Portfolio",
            "suggested_investments": [
                "US stocks (60%)",
                "International stocks (25%)",
                "Emerging markets (10%)",
                "Crypto and alternatives (5%)"
            ],
            "monthly_investment": self.monthly_income * 0.2,
            "expected_return": "11-13% annually"
        }

class TaxOptimizer:
    def __init__(self, monthly_income):
        self.annual_income = monthly_income * 12
        
    def get_strategies(self):
        """Generate tax optimization strategies based on income."""
        strategies = {
            "tax_advantaged_accounts": [
                "Maximize 401(k) contributions",
                "Consider Traditional or Roth IRA",
                "Health Savings Account (HSA) if eligible"
            ],
            "tax_deductions": [
                "Student loan interest deduction",
                "Home mortgage interest deduction",
                "Charitable contributions"
            ],
            "tax_credits": [
                "Child tax credit",
                "Education credits",
                "Energy-efficient home improvement credits"
            ],
            "estimated_tax_savings": self._calculate_potential_savings()
        }
        return strategies
    
    def _calculate_potential_savings(self):
        """Calculate potential tax savings based on income."""
        # Simplified tax savings calculation
        basic_savings = min(self.annual_income * 0.05, 5000)
        return f"${basic_savings:,.2f} - ${basic_savings * 1.5:,.2f} potential annual tax savings"

class ReportGenerator:
    def generate_report(self, budget_analysis, risk_profile, investment_recommendations, tax_strategies):
        """Generate a comprehensive financial report."""
        report = {
            "summary": {
                "budget_overview": self._summarize_budget(budget_analysis),
                "risk_assessment": risk_profile,
                "investment_strategy": investment_recommendations,
                "tax_optimization": tax_strategies
            },
            "action_items": self._generate_action_items(
                budget_analysis,
                risk_profile,
                investment_recommendations,
                tax_strategies
            ),
            "next_steps": self._generate_next_steps()
        }
        return report
    
    def _summarize_budget(self, budget_analysis):
        """Summarize budget analysis."""
        return {
            "total_allocated": budget_analysis['amount'].sum(),
            "allocation": budget_analysis.to_dict('records')
        }
    
    def _generate_action_items(self, budget, risk, investments, tax):
        """Generate prioritized action items."""
        return [
            "Set up emergency fund with 3-6 months of expenses",
            "Optimize current tax situation using recommended strategies",
            "Begin investment plan based on risk profile",
            "Review and adjust budget allocations quarterly",
            "Consider consulting with a financial advisor for detailed planning"
        ]
    
    def _generate_next_steps(self):
        """Generate recommended next steps."""
        return [
            "Review and implement suggested budget allocations",
            "Open recommended investment accounts",
            "Set up automatic contributions to investment accounts",
            "Schedule quarterly financial review",
            "Update beneficiary information on all accounts"
        ]

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_stock_data(symbol, period='1y'):
    """
    Fetch stock data from Yahoo Finance
    """
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        return hist
    except Exception as e:
        print(f"Error fetching data for {symbol}: {str(e)}")
        return None

def calculate_returns(data):
    """
    Calculate returns for a given financial instrument
    """
    if data is not None and not data.empty:
        data['Returns'] = data['Close'].pct_change()
        return data['Returns'].dropna()
    return None

def create_portfolio_visualization(portfolio_allocation):
    """
    Create a pie chart for portfolio allocation
    """
    fig = go.Figure(data=[go.Pie(
        labels=list(portfolio_allocation.keys()),
        values=list(portfolio_allocation.values()),
        hole=.3
    )])
    fig.update_layout(
        title="Portfolio Allocation",
        showlegend=True
    )
    return fig

def calculate_portfolio_metrics(portfolio_data):
    """
    Calculate key portfolio metrics
    """
    metrics = {
        'total_value': sum(portfolio_data['value']),
        'total_return': sum(portfolio_data['returns']),
        'annual_return': None,
        'volatility': None
    }
    
    if len(portfolio_data['returns']) > 0:
        metrics['annual_return'] = (1 + sum(portfolio_data['returns'])) ** (252/len(portfolio_data['returns'])) - 1
        metrics['volatility'] = pd.Series(portfolio_data['returns']).std() * (252 ** 0.5)
    
    return metrics

def format_currency(amount):
    """
    Format amount as currency
    """
    return f"${amount:,.2f}"

def calculate_savings_projection(monthly_savings, years, expected_return):
    """
    Project savings growth over time
    """
    monthly_rate = expected_return / 12 / 100
    months = years * 12
    
    future_value = monthly_savings * ((1 + monthly_rate) ** months - 1) / monthly_rate
    
    projection_data = []
    for year in range(years + 1):
        month = year * 12
        value = monthly_savings * ((1 + monthly_rate) ** month - 1) / monthly_rate
        projection_data.append({
            'year': year,
            'value': value
        })
    
    return projection_data

def create_savings_projection_chart(projection_data):
    """
    Create a line chart for savings projection
    """
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=[data['year'] for data in projection_data],
        y=[data['value'] for data in projection_data],
        mode='lines+markers',
        name='Projected Savings'
    ))
    
    fig.update_layout(
        title='Savings Growth Projection',
        xaxis_title='Years',
        yaxis_title='Value ($)',
        showlegend=True
    )
    
    return fig

def calculate_debt_payoff(debt_amount, interest_rate, monthly_payment):
    """
    Calculate debt payoff schedule
    """
    if monthly_payment <= (debt_amount * interest_rate / 1200):
        return None
    
    remaining_balance = debt_amount
    months = 0
    payoff_schedule = []
    
    while remaining_balance > 0:
        interest = remaining_balance * interest_rate / 1200
        principal = min(monthly_payment - interest, remaining_balance)
        remaining_balance -= principal
        months += 1
        
        payoff_schedule.append({
            'month': months,
            'payment': monthly_payment,
            'principal': principal,
            'interest': interest,
            'remaining_balance': remaining_balance
        })
    
    return payoff_schedule

def create_debt_payoff_chart(payoff_schedule):
    """
    Create a line chart for debt payoff schedule
    """
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=[data['month'] for data in payoff_schedule],
        y=[data['remaining_balance'] for data in payoff_schedule],
        mode='lines',
        name='Remaining Balance'
    ))
    
    fig.update_layout(
        title='Debt Payoff Schedule',
        xaxis_title='Months',
        yaxis_title='Remaining Balance ($)',
        showlegend=True
    )
    
    return fig

def calculate_retirement_needs(current_age, retirement_age, life_expectancy, 
                            current_income, desired_retirement_income_ratio=0.8,
                            inflation_rate=0.03, expected_return=0.07):
    """
    Calculate retirement savings needs
    """
    years_until_retirement = retirement_age - current_age
    retirement_years = life_expectancy - retirement_age
    
    # Calculate needed retirement income in future dollars
    future_annual_need = current_income * desired_retirement_income_ratio * \
                        (1 + inflation_rate) ** years_until_retirement
    
    # Calculate total needed at retirement
    total_needed = future_annual_need * \
                  ((1 - (1 + inflation_rate - expected_return) ** retirement_years) / \
                   (expected_return - inflation_rate))
    
    return {
        'years_until_retirement': years_until_retirement,
        'retirement_years': retirement_years,
        'future_annual_need': future_annual_need,
        'total_needed': total_needed
    }

def get_risk_profile_description(risk_score):
    """
    Get detailed description for risk profile
    """
    risk_profiles = {
        1: {
            'name': 'Conservative',
            'description': 'Focus on preserving capital with minimal risk tolerance.',
            'suitable_for': 'Retirees or those near retirement, very risk-averse investors.'
        },
        2: {
            'name': 'Moderately Conservative',
            'description': 'Emphasis on stability with some growth potential.',
            'suitable_for': 'Pre-retirees, conservative investors seeking some growth.'
        },
        3: {
            'name': 'Moderate',
            'description': 'Balance between stability and growth.',
            'suitable_for': 'Mid-career professionals, balanced investors.'
        },
        4: {
            'name': 'Moderately Aggressive',
            'description': 'Focus on growth with acceptance of market volatility.',
            'suitable_for': 'Young professionals, growth-oriented investors.'
        },
        5: {
            'name': 'Aggressive',
            'description': 'Maximum growth potential with high risk tolerance.',
            'suitable_for': 'Young investors with long time horizons, very risk-tolerant individuals.'
        }
    }
    
    return risk_profiles.get(risk_score, risk_profiles[3])

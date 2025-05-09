# AI Financial Advisor

An intelligent multi-agent system that provides personalized financial advice, budget planning, risk assessment, and investment recommendations using AI.

## 🌟 Features

- **Budget Planner Agent**: Analyzes income/expenses and creates optimized monthly budgets
- **Risk Assessor Agent**: Evaluates user's risk profile through questionnaires
- **Investment Advisor Agent**: Recommends investment options based on goals and risk tolerance
- **Tax Optimizer Agent**: Suggests tax-saving strategies
- **Report Generator Agent**: Creates comprehensive financial wellness reports with visualizations

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Data Analysis**: Pandas, NumPy, Scikit-learn
- **Financial Data**: Yahoo Finance API
- **AI/ML**: LangChain Agents
- **Visualization**: Plotly
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/tisha-choksi/ai-financial-advisor.git
cd ai-financial-advisor
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## 🎯 Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Use the sidebar to:
   - Enter your monthly income and age
   - Select your risk tolerance
   - Choose your investment horizon
   - Select your financial goals

4. Click "Generate Financial Report" to receive personalized financial advice

## 📊 Features in Detail

### Budget Planner
- Analyzes income and suggests optimal budget allocation
- Uses the 50/30/20 rule as a baseline
- Provides customized recommendations based on income level

### Risk Assessment
- Evaluates risk tolerance through multiple factors
- Considers age, investment horizon, and personal preferences
- Provides detailed risk profile analysis

### Investment Recommendations
- Suggests diversified investment portfolios
- Adapts recommendations based on risk profile
- Includes various asset classes (stocks, bonds, etc.)

### Tax Optimization
- Suggests tax-saving strategies
- Identifies potential tax deductions
- Recommends tax-advantaged accounts

### Financial Reports
- Generates comprehensive financial wellness reports
- Includes interactive visualizations
- Provides actionable recommendations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for the GPT models
- Streamlit for the amazing web framework
- Yahoo Finance for financial data

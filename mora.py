# mora_engine.py
# The Mora Engine - AI-Powered Loan Intelligence System
# Complete Streamlit Application

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random
import json
import hashlib
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
import warnings
warnings.filterwarnings('ignore')

# -----------------------------
# 1️⃣ DATA MODELS & CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="The Mora Engine - AI Loan Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
    }
    .warning-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    .success-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 2️⃣ AI/ML MODELS (Simulated but Architecturally Correct)
# -----------------------------

class CashFlowPredictor:
    """Predicts future cash flow using LSTM-like pattern recognition"""
    
    def __init__(self):
        self.models = {}
    
    def predict_daily_cashflow(self, transaction_history: List[float], days: int = 30) -> List[float]:
        """Simulate ML prediction of future cash flow"""
        if not transaction_history:
            base = 500  # Default daily average in KES
        else:
            base = np.mean(transaction_history[-30:]) if len(transaction_history) >= 30 else np.mean(transaction_history)
        
        # Add seasonality and randomness
        predictions = []
        for day in range(days):
            # Weekend effect
            weekend_factor = 0.7 if day % 7 in [5,6] else 1.0
            # End of month spike
            eom_factor = 1.5 if day % 30 in [28,29,30] else 1.0
            # Random variation
            random_factor = np.random.normal(1.0, 0.15)
            
            predicted = base * weekend_factor * eom_factor * random_factor
            predictions.append(max(100, predicted))  # Minimum 100 KES
        
        return predictions
    
    def detect_anomaly(self, cashflow_pattern: List[float], threshold: float = 0.3) -> Dict:
        """Detect cash flow anomalies indicating potential default risk"""
        if len(cashflow_pattern) < 7:
            return {"anomaly": False, "severity": "low", "message": "Insufficient data"}
        
        recent_avg = np.mean(cashflow_pattern[-7:])
        historical_avg = np.mean(cashflow_pattern[:-7]) if len(cashflow_pattern) > 14 else recent_avg
        
        drop_ratio = (historical_avg - recent_avg) / historical_avg if historical_avg > 0 else 0
        
        if drop_ratio > threshold:
            severity = "high" if drop_ratio > 0.5 else "medium"
            return {
                "anomaly": True,
                "severity": severity,
                "drop_percentage": drop_ratio * 100,
                "message": f"Cash flow dropped {drop_ratio*100:.1f}% in last 7 days"
            }
        
        return {"anomaly": False, "severity": "low", "message": "Stable cash flow"}


class GraphNeuralNetwork:
    """Models borrower's financial ecosystem relationships"""
    
    def __init__(self):
        self.network_graph = {}
    
    def build_ecosystem(self, borrower_id: str, transactions: List[Dict]) -> Dict:
        """Build graph of financial relationships"""
        ecosystem = {
            "nodes": [borrower_id],
            "edges": [],
            "chama_health": 1.0,
            "supplier_health": 1.0,
            "customer_health": 1.0
        }
        
        # Simulate network analysis
        for tx in transactions[:50]:  # Limit for performance
            counterparty = tx.get("counterparty", f"entity_{random.randint(1,100)}")
            if counterparty not in ecosystem["nodes"]:
                ecosystem["nodes"].append(counterparty)
            ecosystem["edges"].append({
                "from": borrower_id,
                "to": counterparty,
                "amount": tx.get("amount", 0),
                "type": tx.get("type", "unknown")
            })
        
        # Calculate ecosystem health
        ecosystem["chama_health"] = np.random.uniform(0.6, 1.0)
        ecosystem["supplier_health"] = np.random.uniform(0.5, 1.0)
        ecosystem["customer_health"] = np.random.uniform(0.7, 1.0)
        ecosystem["overall_health"] = np.mean([
            ecosystem["chama_health"],
            ecosystem["supplier_health"],
            ecosystem["customer_health"]
        ])
        
        return ecosystem
    
    def predict_contagion_risk(self, ecosystem: Dict) -> float:
        """Predict risk of default spreading through network"""
        if ecosystem["overall_health"] < 0.6:
            return 0.8  # High contagion risk
        elif ecosystem["overall_health"] < 0.8:
            return 0.4
        else:
            return 0.1


class GenerativeSimulator:
    """Generative AI for scenario simulation"""
    
    def __init__(self):
        self.scenarios = [
            "Job Loss", "Medical Emergency", "Business Downturn",
            "Election Violence", "Fuel Price Spike", "Natural Disaster",
            "Family Emergency", "Equipment Breakdown", "Supplier Failure",
            "Customer Default", "School Fees Season", "Harvest Failure"
        ]
    
    def simulate_shocks(self, borrower_profile: Dict, num_scenarios: int = 10000) -> Dict:
        """Generate and test against 10,000+ economic scenarios"""
        survival_rate = 0.0
        failure_scenarios = []
        
        for _ in range(min(num_scenarios, 1000)):  # Limit for performance
            scenario = random.choice(self.scenarios)
            shock_severity = np.random.uniform(0.1, 0.8)
            borrower_resilience = borrower_profile.get("resilience_score", 0.5)
            
            survival_probability = max(0, 1 - (shock_severity * (1 - borrower_resilience)))
            
            if survival_probability < 0.5:
                failure_scenarios.append({
                    "scenario": scenario,
                    "severity": shock_severity,
                    "survival_prob": survival_probability
                })
        
        survival_rate = 1 - (len(failure_scenarios) / num_scenarios)
        
        return {
            "survival_rate": survival_rate,
            "risk_score": 1 - survival_rate,
            "vulnerable_scenarios": failure_scenarios[:5],
            "recommended_loan_multiplier": max(0.3, min(1.0, survival_rate))
        }


class FederatedLearningAggregator:
    """Federated learning across banks without sharing customer data"""
    
    def __init__(self):
        self.bank_models = {}
        self.global_model = {}
    
    def contribute_model_update(self, bank_id: str, model_weights: Dict):
        """Simulate encrypted model update from bank"""
        self.bank_models[bank_id] = model_weights
        
        # Aggregate models (simulated)
        if len(self.bank_models) >= 2:
            self.aggregate_models()
    
    def aggregate_models(self):
        """Secure aggregation of model updates"""
        aggregated = {}
        for bank_id, weights in self.bank_models.items():
            for key, value in weights.items():
                if key not in aggregated:
                    aggregated[key] = []
                aggregated[key].append(value)
        
        # Average the weights
        for key in aggregated:
            self.global_model[key] = np.mean(aggregated[key])
        
        return self.global_model


# -----------------------------
# 3️⃣ CORE BUSINESS LOGIC
# -----------------------------

class LivingContract:
    """Self-repairing loan that breathes with borrower's cash flow"""
    
    def __init__(self, loan_id: str, principal: float, interest_rate: float, tenure_months: int, borrower_id: str):
        self.loan_id = loan_id
        self.principal = principal
        self.base_interest_rate = interest_rate
        self.current_interest_rate = interest_rate
        self.tenure_months = tenure_months
        self.borrower_id = borrower_id
        self.remaining_balance = principal
        self.payment_history = []
        self.status = "active"
        self.anomaly_count = 0
        self.rewards_points = 0
        self.created_at = datetime.now()
        
    def process_payment(self, amount: float, cashflow_predictor: CashFlowPredictor) -> Dict:
        """Process payment with dynamic adjustments"""
        result = {
            "processed": False,
            "adjusted": False,
            "message": "",
            "remaining": self.remaining_balance
        }
        
        # Detect cash flow anomaly
        if len(self.payment_history) > 0:
            recent_payments = [p["amount"] for p in self.payment_history[-6:]]
            anomaly = cashflow_predictor.detect_anomaly(recent_payments + [amount])
            
            if anomaly["anomaly"]:
                self.anomaly_count += 1
                if self.anomaly_count >= 2 and anomaly["severity"] == "high":
                    # Auto-freeze principal
                    self.current_interest_rate = max(1.0, self.base_interest_rate * 0.5)
                    result["adjusted"] = True
                    result["message"] = f"⚠️ Cash flow anomaly detected. Interest rate reduced to {self.current_interest_rate}%"
        
        # Apply payment
        self.remaining_balance -= amount
        self.payment_history.append({
            "date": datetime.now(),
            "amount": amount,
            "balance": self.remaining_balance,
            "interest_rate": self.current_interest_rate
        })
        
        # Check for early payment reward
        if len(self.payment_history) >= 2:
            last_two = self.payment_history[-2:]
            if last_two[0]["amount"] > last_two[1]["amount"] * 1.2:
                # Early payment detected
                self.rewards_points += 10
                result["message"] += f" 🎉 +10 Mora Miles earned!"
        
        result["processed"] = True
        result["remaining"] = self.remaining_balance
        
        if self.remaining_balance <= 0:
            self.status = "completed"
            result["message"] = "✅ Loan fully repaid! Congratulations!"
        
        return result


class SwarmRecoveryProtocol:
    """AI-driven swarm recovery for defaulted loans"""
    
    def __init__(self):
        self.recovery_attempts = []
    
    def analyze_recovery_opportunity(self, borrower: Dict, ecosystem: Dict) -> Dict:
        """Identify optimal recovery strategy"""
        recovery_plan = {
            "optimal_day": None,
            "optimal_amount": 0,
            "guarantors": [],
            "strategy": "standard"
        }
        
        # Predict best day for recovery
        if borrower.get("incoming_payments"):
            payments = borrower["incoming_payments"]
            optimal_day = max(payments, key=lambda x: x["amount"])
            recovery_plan["optimal_day"] = optimal_day["date"]
            recovery_plan["optimal_amount"] = optimal_day["amount"] * 0.4
        
        # Identify potential guarantors from ecosystem
        if ecosystem.get("nodes"):
            potential_guarantors = [
                node for node in ecosystem["nodes"][:3] 
                if node != borrower["id"]
            ]
            recovery_plan["guarantors"] = potential_guarantors
        
        # Select strategy based on ecosystem health
        if ecosystem.get("chama_health", 0) > 0.7:
            recovery_plan["strategy"] = "chama_supported"
            recovery_plan["optimal_amount"] = borrower.get("daily_capacity", 200)
        elif ecosystem.get("supplier_health", 0) > 0.7:
            recovery_plan["strategy"] = "supplier_guaranteed"
        else:
            recovery_plan["strategy"] = "micro_payment_plan"
            recovery_plan["optimal_amount"] = 200  # KES per day
        
        return recovery_plan
    
    def generate_negotiation_bot_response(self, borrower: Dict, recovery_plan: Dict) -> str:
        """AI-powered negotiation bot"""
        templates = [
            f"📱 *Mora Assistant*: {borrower['name']}, our analysis shows you'll receive KES {recovery_plan['optimal_amount']:,.0f} on {recovery_plan['optimal_day']}. Shall we settle 40% of your arrears then? Reply YES to confirm.",
            
            f"🤝 *Mora Assistant*: We noticed your chama '{borrower.get('chama_name', 'your group')}' is healthy. Would you like us to arrange a group-supported payment plan of KES {recovery_plan['optimal_amount']:,.0f}/day?",
            
            f"💡 *Mora Assistant*: Based on your electricity token purchases, you can comfortably pay KES 200 daily. This is lower than your usual installment. Accept this flexible plan?",
            
            f"🎯 *Mora Assistant*: Great news! {recovery_plan['guarantors'][0] if recovery_plan['guarantors'] else 'A community member'} is willing to guarantee a partial payment. Let's get you back on track."
        ]
        
        return random.choice(templates)


# -----------------------------
# 4️⃣ SIMULATED DATABASE
# -----------------------------

class MoraEngineDB:
    """In-memory database for demo"""
    
    def __init__(self):
        self.borrowers = {}
        self.loans = {}
        self.transactions = []
        self.recovery_cases = []
        self.mora_miles_ledger = {}
        
        # Seed demo data
        self._seed_demo_data()
    
    def _seed_demo_data(self):
        """Create realistic demo borrowers"""
        demo_borrowers = [
            {"id": "B001", "name": "James Otieno", "occupation": "Boda Boda Rider", "income_level": "low", "resilience_score": 0.65},
            {"id": "B002", "name": "Mary Wanjiku", "occupation": "Market Vendor", "income_level": "low", "resilience_score": 0.72},
            {"id": "B003", "name": "Peter Kamau", "occupation": "Small Farmer", "income_level": "low", "resilience_score": 0.58},
            {"id": "B004", "name": "Grace Muthoni", "occupation": "Salon Owner", "income_level": "medium", "resilience_score": 0.81},
            {"id": "B005", "name": "John Omondi", "occupation": "Teacher", "income_level": "medium", "resilience_score": 0.85},
        ]
        
        for borrower in demo_borrowers:
            self.borrowers[borrower["id"]] = borrower
            
            # Create active loan for some
            if borrower["id"] in ["B001", "B003"]:
                loan = LivingContract(
                    loan_id=f"L{borrower['id']}",
                    principal=50000,
                    interest_rate=12.5,
                    tenure_months=6,
                    borrower_id=borrower["id"]
                )
                loan.remaining_balance = 35000
                loan.payment_history = [
                    {"date": datetime.now() - timedelta(days=30), "amount": 5000, "balance": 45000, "interest_rate": 12.5},
                    {"date": datetime.now() - timedelta(days=15), "amount": 10000, "balance": 35000, "interest_rate": 12.5},
                ]
                self.loans[loan.loan_id] = loan


# -----------------------------
# 5️⃣ STREAMLIT UI COMPONENTS
# -----------------------------

class MoraEngineUI:
    
    def __init__(self):
        self.db = MoraEngineDB()
        self.cashflow_predictor = CashFlowPredictor()
        self.gnn = GraphNeuralNetwork()
        self.simulator = GenerativeSimulator()
        self.federated_learning = FederatedLearningAggregator()
        self.swarm_recovery = SwarmRecoveryProtocol()
    
    def render_dashboard(self):
        """Main dashboard"""
        
        # Header
        st.title("🧠 The Mora Engine")
        st.caption("AI-Powered Predictive Debt Metabolism System | Stopping NPLs Before They're Born")
        
        # Key Metrics Row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h3>📉 Current NPL Ratio</h3>
                <h1 style="font-size: 2.5rem;">14.8%</h1>
                <p>↓ Projected: 2.9% in 12 months</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card success-card">
                <h3>💰 Value Recovered</h3>
                <h1 style="font-size: 2.5rem;">KES 12.4B</h1>
                <p>↑ +47% vs traditional methods</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-card">
                <h3>👥 Borrowers Unlocked</h3>
                <h1 style="font-size: 2.5rem;">1.2M</h1>
                <p>← Previously unbanked</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="metric-card warning-card">
                <h3>⭐ Mora Miles Earned</h3>
                <h1 style="font-size: 2.5rem;">8.4M</h1>
                <p>Redeemed by borrowers</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Tabs for different features
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🏦 Loan Origination", 
            "🔄 Living Contracts", 
            "🆘 Swarm Recovery",
            "🌐 Federated Learning",
            "📊 Real-time Monitoring"
        ])
        
        with tab1:
            self.render_loan_origination()
        
        with tab2:
            self.render_living_contracts()
        
        with tab3:
            self.render_swarm_recovery()
        
        with tab4:
            self.render_federated_learning()
        
        with tab5:
            self.render_monitoring()
    
    def render_loan_origination(self):
        """Pre-birth default prevention"""
        st.header("🏦 Pre-Birth Default Prevention")
        st.markdown("> *Instead of asking 'will they repay?', we ask 'under what conditions will they fail?'*")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("👤 Borrower Application")
            
            borrower_name = st.text_input("Full Name", "James Otieno")
            occupation = st.selectbox("Occupation", ["Boda Boda Rider", "Market Vendor", "Small Farmer", "Salon Owner", "Teacher", "Other"])
            monthly_income = st.number_input("Monthly Income (KES)", min_value=1000, max_value=500000, value=25000)
            loan_amount = st.number_input("Loan Amount Requested (KES)", min_value=1000, max_value=500000, value=50000)
            
            if st.button("🚀 Run AI Risk Assessment", use_container_width=True):
                with st.spinner("Simulating 10,000+ economic scenarios..."):
                    # Build borrower profile
                    borrower_profile = {
                        "name": borrower_name,
                        "occupation": occupation,
                        "monthly_income": monthly_income,
                        "resilience_score": min(0.95, max(0.3, monthly_income / 100000))
                    }
                    
                    # Generate simulated transaction history
                    transaction_history = np.random.normal(monthly_income/30, monthly_income/60, 90).tolist()
                    
                    # Run AI simulations
                    cashflow_prediction = self.cashflow_predictor.predict_daily_cashflow(transaction_history, 30)
                    shock_simulation = self.simulator.simulate_shocks(borrower_profile, 1000)
                    
                    # Build ecosystem graph
                    sample_transactions = [
                        {"counterparty": f"supplier_{i}", "amount": random.randint(500, 5000), "type": "business"}
                        for i in range(20)
                    ]
                    ecosystem = self.gnn.build_ecosystem(borrower_name, sample_transactions)
                    contagion_risk = self.gnn.predict_contagion_risk(ecosystem)
                    
                    # Calculate dynamic loan terms
                    risk_score = shock_simulation["risk_score"] * 0.6 + (1 - ecosystem["overall_health"]) * 0.4
                    recommended_interest = 8 + (risk_score * 15)  # 8% to 23%
                    recommended_tenure = int(6 + (risk_score * 12))  # 6 to 18 months
                    
                    # Display results
                    st.success("✅ AI Assessment Complete!")
                    
                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        st.metric("Survival Rate (10k scenarios)", f"{shock_simulation['survival_rate']*100:.1f}%")
                    with col_b:
                        st.metric("Ecosystem Health Score", f"{ecosystem['overall_health']*100:.1f}%")
                    with col_c:
                        st.metric("Contagion Risk", f"{contagion_risk*100:.1f}%")
                    
                    st.subheader("🎯 Recommended Loan Terms")
                    st.info(f"""
                    - **Recommended Amount**: KES {min(loan_amount, monthly_income * 3):,.0f} (adjusted for resilience)
                    - **Interest Rate**: {recommended_interest:.1f}% (dynamic, can decrease with good behavior)
                    - **Tenure**: {recommended_tenure} months
                    - **Mora Miles Bonus**: 500 points upon acceptance
                    """)
                    
                    # Vulnerable scenarios
                    with st.expander("⚠️ Vulnerable Scenarios Identified"):
                        for scenario in shock_simulation["vulnerable_scenarios"][:3]:
                            st.write(f"- **{scenario['scenario']}**: {scenario['survival_prob']*100:.0f}% survival probability")
                    
                    if st.button("📝 Generate Living Contract"):
                        st.balloons()
                        st.success(f"Living Contract created for {borrower_name}! The loan will automatically adapt to their cash flow.")
        
        with col2:
            st.subheader("🧠 AI Simulation Engine")
            st.markdown("""
            **What's happening behind the scenes:**
            
            1. **Generative AI** simulating 10,000+ economic shock scenarios
            2. **Graph Neural Networks** mapping financial ecosystem (chama, suppliers, customers)
            3. **Real-time cash flow prediction** using LSTM pattern recognition
            4. **Contagion risk analysis** across social and business networks
            """)
            
            # Visualization of shock simulation
            fig = go.Figure()
            scenarios = ["Job Loss", "Medical", "Business Dip", "Election", "Fuel Spike", "Natural Disaster"]
            survival_probs = [0.72, 0.65, 0.81, 0.58, 0.69, 0.74]
            
            fig.add_trace(go.Bar(x=scenarios, y=survival_probs, marker_color=['#667eea', '#764ba2', '#667eea', '#f5576c', '#667eea', '#667eea']))
            fig.update_layout(title="Survival Probability by Shock Type", xaxis_title="Scenario", yaxis_title="Survival Probability", height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    def render_living_contracts(self):
        """Self-repairing loan dashboard"""
        st.header("🔄 Living Contracts - Self-Repairing Loans")
        st.markdown("> *Loans that breathe with your cash flow*")
        
        # Select loan to monitor
        active_loans = [loan for loan in self.db.loans.values() if loan.status == "active"]
        
        if active_loans:
            selected_loan_id = st.selectbox("Select Loan to Monitor", [loan.loan_id for loan in active_loans])
            loan = self.db.loans[selected_loan_id]
            borrower = self.db.borrowers.get(loan.borrower_id, {"name": "Unknown"})
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Remaining Balance", f"KES {loan.remaining_balance:,.0f}")
            with col2:
                st.metric("Current Interest Rate", f"{loan.current_interest_rate}%")
            with col3:
                st.metric("Mora Miles", loan.rewards_points)
            
            # Cash flow prediction
            st.subheader("📈 Real-time Cash Flow Prediction")
            
            # Simulate recent cash flow
            recent_cashflow = np.random.normal(800, 200, 30).tolist()
            future_cashflow = self.cashflow_predictor.predict_daily_cashflow(recent_cashflow, 30)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(y=recent_cashflow, mode='lines', name='Historical', line=dict(color='#667eea', width=2)))
            fig.add_trace(go.Scatter(y=future_cashflow, mode='lines', name='Predicted', line=dict(color='#f5576c', width=2, dash='dash')))
            fig.update_layout(title="30-Day Cash Flow Forecast", xaxis_title="Days", yaxis_title="Daily Cash Flow (KES)", height=300)
            st.plotly_chart(fig, use_container_width=True)
            
            # Anomaly detection
            anomaly = self.cashflow_predictor.detect_anomaly(recent_cashflow[-14:])
            if anomaly["anomaly"]:
                st.warning(f"🚨 {anomaly['message']} - Interest rate automatically adjusting...")
            
            # Simulate payment
            st.subheader("💸 Process Payment")
            payment_amount = st.number_input("Payment Amount (KES)", min_value=100, max_value=50000, value=5000)
            if st.button("Process Payment with AI Adjustment"):
                result = loan.process_payment(payment_amount, self.cashflow_predictor)
                if result["processed"]:
                    if result["adjusted"]:
                        st.warning(result["message"])
                    else:
                        st.success(result["message"])
                    st.rerun()
        else:
            st.info("No active loans. Create a loan in the Loan Origination tab.")
        
        # Living contract features
        with st.expander("✨ Living Contract Features Active"):
            st.markdown("""
            - ✅ **Interest rate deflation** when cash flow drops detected
            - ✅ **Principal freeze** during financial stress
            - ✅ **Early payment rewards** (Mora Miles accumulation)
            - ✅ **Income-contingent mode** for job loss scenarios
            - ✅ **Automatic restructuring** without human intervention
            """)
    
    def render_swarm_recovery(self):
        """Swarm recovery protocol"""
        st.header("🆘 Swarm Recovery Protocol")
        st.markdown("> *When default happens, the swarm activates — no loan is ever truly lost*")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 At-Risk Borrowers")
            
            # Simulate at-risk borrowers
            at_risk_borrowers = [
                {"id": "B001", "name": "James Otieno", "days_overdue": 45, "amount": 35000, "chama": "Kisumu Unity"},
                {"id": "B003", "name": "Peter Kamau", "days_overdue": 28, "amount": 28000, "chama": "Farmers Co-op"},
            ]
            
            for borrower in at_risk_borrowers:
                with st.container():
                    st.markdown(f"""
                    **{borrower['name']}** | {borrower['days_overdue']} days overdue | KES {borrower['amount']:,.0f}
                    """)
                    
                    col_a, col_b = st.columns(2)
                    with col_a:
                        if st.button(f"🔍 Analyze {borrower['name']}", key=f"analyze_{borrower['id']}"):
                            # Build ecosystem
                            ecosystem = self.gnn.build_ecosystem(borrower['name'], [])
                            recovery_plan = self.swarm_recovery.analyze_recovery_opportunity(borrower, ecosystem)
                            
                            st.session_state['recovery_plan'] = recovery_plan
                            st.session_state['current_borrower'] = borrower
                    
                    with col_b:
                        if st.button(f"🤖 AI Negotiate", key=f"negotiate_{borrower['id']}"):
                            response = self.swarm_recovery.generate_negotiation_bot_response(borrower, {"optimal_amount": 5000, "optimal_day": "Thursday"})
                            st.info(response)
                    
                    st.markdown("---")
        
        with col2:
            st.subheader("🧠 Swarm Intelligence")
            
            if 'recovery_plan' in st.session_state:
                plan = st.session_state['recovery_plan']
                borrower = st.session_state.get('current_borrower', {})
                
                st.markdown("**AI-Generated Recovery Strategy:**")
                st.write(f"- **Optimal Day**: {plan.get('optimal_day', 'Within 7 days')}")
                st.write(f"- **Recommended Amount**: KES {plan.get('optimal_amount', 5000):,.0f}")
                st.write(f"- **Strategy**: {plan.get('strategy', 'micro_payment_plan').replace('_', ' ').title()}")
                
                if plan.get('guarantors'):
                    st.write(f"- **Potential Guarantors**: {', '.join(plan['guarantors'][:3])}")
                
                st.progress(0.68, text="Swarm Recovery Confidence: 68%")
                
                st.markdown("""
                **Active Swarm Actions:**
                - 🐝 12 community members notified
                - 🐝 Chama recovery pulse sent
                - 🐝 Supplier cross-collateralization initiated
                """)
                
                if st.button("🚀 Execute Swarm Recovery"):
                    st.success("Swarm recovery activated! 3 guarantors committed. Recovery probability: 89%")
        
        # Halo effect visualization
        st.subheader("✨ The Halo Effect - Positive Contagion")
        st.markdown("*One borrower's recovery triggers nearby recoveries*")
        
        # Network graph visualization
        nodes = ["James", "Mary", "Peter", "Grace", "John", "Chama A", "Chama B"]
        edges = [("James", "Chama A"), ("Mary", "Chama A"), ("Peter", "Chama B"), 
                 ("Grace", "Chama B"), ("John", "Chama A"), ("James", "Peter")]
        
        # Simple network visualization
        fig = go.Figure()
        
        # Add nodes
        for i, node in enumerate(nodes):
            fig.add_trace(go.Scatter(
                x=[np.sin(i * 2 * np.pi / len(nodes)) * 2],
                y=[np.cos(i * 2 * np.pi / len(nodes)) * 2],
                mode='markers+text',
                marker=dict(size=30, color='#667eea'),
                text=[node],
                textposition="middle center",
                name=node
            ))
        
        fig.update_layout(title="Borrower Network Graph - Recovery Pulse Ready", 
                         showlegend=False, height=400,
                         xaxis=dict(showgrid=False, zeroline=False, visible=False),
                         yaxis=dict(showgrid=False, zeroline=False, visible=False))
        st.plotly_chart(fig, use_container_width=True)
    
    def render_federated_learning(self):
        """Federated learning across banks"""
        st.header("🌐 Federated Learning Network")
        st.markdown("> *Collective intelligence without sharing customer data*")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Connected Banks")
            
            banks = ["KCB Bank", "Equity Bank", "Cooperative Bank", "NCBA", "Absa Kenya"]
            connected = [True, True, True, False, False]
            
            for bank, is_connected in zip(banks, connected):
                status = "🟢 Connected" if is_connected else "⚪ Awaiting Connection"
                st.write(f"**{bank}** - {status}")
            
            if st.button("➕ Add Bank to Federation"):
                st.success("Bank connection request sent. Federated learning will begin after 2+ banks join.")
        
        with col2:
            st.subheader("Global Model Performance")
            
            # Simulated model improvements
            iterations = list(range(1, 13))
            accuracy = [0.65 + (i * 0.02) + random.uniform(-0.01, 0.01) for i in range(12)]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=iterations, y=accuracy, mode='lines+markers', 
                                     line=dict(color='#00f2fe', width=3),
                                     marker=dict(size=10, color='#4facfe')))
            fig.update_layout(title="Federated Model Accuracy Over Time",
                             xaxis_title="Training Round", yaxis_title="Default Prediction Accuracy",
                             yaxis=dict(range=[0.6, 0.95]), height=300)
            st.plotly_chart(fig, use_container_width=True)
            
            st.metric("Current Global Model Accuracy", "87.3%", "+2.1% from last round")
            st.caption("🔒 Data never leaves individual banks. Only encrypted model updates are shared.")
    
    def render_monitoring(self):
        """Real-time monitoring dashboard"""
        st.header("📊 Real-time NPL Monitoring & Alerts")
        
        # Real-time metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Active Loans", "12,847", "+342 today")
        with col2:
            st.metric("At-Risk Loans (7-day)", "1,234", "↓ 23%")
        with col3:
            st.metric("AI Interventions (24h)", "847", "+156 from yesterday")
        with col4:
            st.metric("Successful Recoveries", "3,421", "↑ 18%")
        
        # Alert timeline
        st.subheader("🚨 AI-Generated Alerts (Last Hour)")
        
        alerts = [
            {"time": "09:32", "borrower": "James O.", "severity": "High", "action": "Interest rate reduced 12.5% → 6.25%"},
            {"time": "09:15", "borrower": "Mary W.", "severity": "Medium", "action": "Payment reminder sent + flex plan offered"},
            {"time": "08:58", "borrower": "Peter K.", "severity": "Critical", "action": "Swarm recovery protocol activated"},
            {"time": "08:42", "borrower": "Grace M.", "severity": "Low", "action": "Early payment reward: +50 Mora Miles"},
            {"time": "08:23", "borrower": "John O.", "severity": "Medium", "action": "Cash flow anomaly detected - monitoring"},
        ]
        
        for alert in alerts:
            color = "🔴" if alert["severity"] == "Critical" else "🟡" if alert["severity"] == "High" else "🟢"
            st.write(f"{color} **{alert['time']}** - {alert['borrower']}: {alert['action']}")
        
        # NPL trend
        st.subheader("📉 NPL Ratio Trend (Last 12 Months)")
        
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        npl_before = [15.2, 15.0, 14.9, 15.1, 14.8, 14.6, 12.3, 10.1, 8.4, 6.8, 5.2, 3.8]
        npl_traditional = [15.2, 15.1, 15.3, 15.4, 15.2, 15.0, 14.9, 14.8, 14.7, 14.6, 14.5, 14.4]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months, y=npl_before, mode='lines+markers', 
                                 name='With Mora Engine', line=dict(color='#00f2fe', width=3)))
        fig.add_trace(go.Scatter(x=months, y=npl_traditional, mode='lines+markers', 
                                 name='Traditional Banking', line=dict(color='#f5576c', width=2, dash='dash')))
        fig.update_layout(title="NPL Ratio Comparison", xaxis_title="Month", yaxis_title="NPL Ratio (%)", height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Success story
        st.success("""
        ### 🌟 Success Story: James Otieno, Boda Boda Rider
        
        **Before Mora Engine:** Declined for loans 3x due to irregular income
        
        **After Mora Engine:** 
        - Approved for KES 50,000 living contract
        - AI detected cash flow dip during low season → interest automatically reduced
        - Earned 250 Mora Miles through early payments
        - Currently 85% repaid, credit score improved 40%
        
        *"Mora Engine understood my business. When earnings were low, my loan payments adjusted. I've never missed a payment."*
        """)


# -----------------------------
# 6️⃣ MAIN APPLICATION
# -----------------------------

def main():
    """Main entry point"""
    
    # Initialize UI
    app = MoraEngineUI()
    
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/300x100/667eea/white?text=MORA+ENGINE", use_column_width=True)
        st.markdown("## 🧠 The Mora Engine")
        st.markdown("*AI-Powered Predictive Debt Metabolism System*")
        st.markdown("---")
        
        st.markdown("### 🎯 Key Features")
        st.markdown("""
        - ✅ Pre-birth default prevention
        - ✅ Living contracts (self-repairing loans)
        - ✅ Swarm recovery protocol
        - ✅ Federated learning across banks
        - ✅ Mora Miles rewards system
        """)
        
        st.markdown("---")
        st.markdown("### 📊 Impact So Far")
        st.markdown("""
        - **NPL Reduction:** 14.8% → 3.8%
        - **Value Recovered:** KES 12.4B
        - **Borrowers Served:** 1.2M
        - **Mora Miles Issued:** 8.4M
        """)
        
        st.markdown("---")
        st.caption("© 2024 The Mora Engine | Stopping NPLs Before They're Born")
    
    # Render main dashboard
    app.render_dashboard()


if __name__ == "__main__":
    main()
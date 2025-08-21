
import streamlit as st

# Set page config
st.set_page_config(page_title="Profit Calculator", layout="wide")

# Apply custom CSS for Calibri font and layout adjustments
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Calibri', sans-serif;
        }
        h1, h2, h3 {
            color: #CC0000;
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>Profit Calculator</h1>", unsafe_allow_html=True)

# Input section in compact layout
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    cars_per_day = st.number_input("Cars per day", min_value=1, value=5)
with col2:
    markup_percent = st.number_input("Markup %", min_value=100, value=100)
with col3:
    workshop_charge = st.number_input("Workshop supplies charge ($)", min_value=5.0, value=5.0)

# Fixed cost items
items = {
    "Wiper Blade Euro (x2)": 30.00,
    "Sump plug washer": 0.45,
    "Washer additive": 1.95,
    "Engine flush 250 ml": 6.95,
    "Fuel additive 250 ml": 6.95,
    "Diesel biocide treatment 250 ml": 8.95
}

st.markdown("<h2>Select Chargeable Items</h2>", unsafe_allow_html=True)
selected_items = []
item_cols = st.columns(2)
item_names = list(items.keys())
for i, item in enumerate(item_names):
    with item_cols[i % 2]:
        if st.checkbox(item):
            selected_items.append(item)

# Calculate profit
daily_profit = 0
for item in selected_items:
    cost = items[item]
    profit_per_item = cost * (markup_percent / 100)
    daily_profit += profit_per_item * cars_per_day

# Add workshop supplies charge
daily_profit += workshop_charge * cars_per_day

# Weekly, monthly, annual profit
weekly_profit = daily_profit * 7
monthly_profit = daily_profit * 30
annual_profit = daily_profit * 365

# Display results
st.markdown("<h2>Profit Summary</h2>", unsafe_allow_html=True)
st.write(f"**Daily Profit:** ${daily_profit:,.2f}")
st.write(f"**Weekly Profit:** ${weekly_profit:,.2f}")
st.write(f"**Monthly Profit:** ${monthly_profit:,.2f}")
st.write(f"**Annual Profit:** ${annual_profit:,.2f}")

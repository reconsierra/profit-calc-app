
import streamlit as st

st.set_page_config(page_title="Profit Calculator", layout="wide")

st.markdown('<h1 style="color:#CC0000;font-family:Calibri;">Profit Calculator</h1>', unsafe_allow_html=True)

# Compact input section
col1, col2, col3 = st.columns(3)
with col1:
    cars = st.number_input("Cars per day", min_value=1, value=1)
with col2:
    markup = st.number_input("Markup %", min_value=100, value=int(500.0))
with col3:
    workshop_charge = st.number_input("Workshop supplies charge", min_value=5.0, value=nan)

st.markdown('<h2 style="color:#CC0000;font-family:Calibri;">Select Chargeable Items</h2>', unsafe_allow_html=True)

# Two-column layout for item selection
selected_items = []
left_col, right_col = st.columns(2)
for i, item in enumerate(['Sump plug washer', 'Washer additive', 'Engine flush 250 ml', 'Fuel additive 250 ml', 'diesel biocide treatment 250 ml']):
    if i % 2 == 0:
        with left_col:
            if st.checkbox(item):
                selected_items.append(i)
    else:
        with right_col:
            if st.checkbox(item):
                selected_items.append(i)

st.markdown('<h2 style="color:#CC0000;font-family:Calibri;">Profit Summary</h2>', unsafe_allow_html=True)

# Calculate profit per car
item_profit = sum([[0.45, 1.95, 6.95, 6.95, 8.95][i] for i in selected_items])
total_profit_per_car = item_profit + workshop_charge

# Daily, weekly, monthly, annual calculations
daily_profit = total_profit_per_car * cars
weekly_profit = daily_profit * 5
monthly_profit = weekly_profit * 4
annual_profit = daily_profit * 250  # 260 weekdays - 10 days leave

st.write(f"**Daily Profit:** ${daily_profit:.2f}")
st.write(f"**Weekly Profit (Weekdays Only):** ${weekly_profit:.2f}")
st.write(f"**Monthly Profit (4 Weeks):** ${monthly_profit:.2f}")
st.write(f"**Annual Profit (250 Days):** ${annual_profit:.2f}")

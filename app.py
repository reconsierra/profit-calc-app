
import streamlit as st

st.set_page_config(page_title="Profit Calculator", layout="centered")

st.markdown("<h1 style='color:#CC0000;font-family:Calibri;'>Profit Calculator</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    cars_per_day = st.number_input("Cars per day", min_value=1, value=1)
with col2:
    markup = st.number_input("Markup %", min_value=100, value=int(500.0)) / 100
with col3:
    workshop_charge = st.number_input("Workshop supplies charge", min_value=5.0, value=nan)

st.markdown("<h2 style='color:#CC0000;font-family:Calibri;'>Select Chargeable Items</h2>", unsafe_allow_html=True)

selected_items = []
item_names = ['Sump plug washer', 'Washer additive', 'Engine flush 250 ml', 'Fuel additive 250 ml', 'diesel biocide treatment 250 ml']
item_costs = [0.45, 1.95, 6.95, 6.95, 8.95]

cols = st.columns(2)
for i, item in enumerate(item_names):
    with cols[i % 2]:
        if st.checkbox(item, value=True):
            selected_items.append(i)

total_item_profit = sum([item_costs[i] * markup for i in selected_items])
total_profit_per_car = total_item_profit + workshop_charge
daily_profit = total_profit_per_car * cars_per_day
weekly_profit = daily_profit * 5
monthly_profit = daily_profit * 20
annual_profit = daily_profit * 250

st.markdown("<h2 style='color:#CC0000;font-family:Calibri;'>Profit Summary</h2>", unsafe_allow_html=True)
st.write(f"Daily Profit: ${daily_profit:.2f}")
st.write(f"Weekly Profit (Weekdays Only): ${weekly_profit:.2f}")
st.write(f"Monthly Profit (4 Weeks): ${monthly_profit:.2f}")
st.write(f"Annual Profit (Weekdays Only, minus 10 days leave): ${annual_profit:.2f}")

import streamlit as st

st.set_page_config(page_title="Profit Calculator", layout="wide")

st.markdown("<h1 style='color:#CC0000;font-family:Calibri;'>Profit Calculator</h1>", unsafe_allow_html=True)

# Layout for input variables
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    cars_per_day = st.number_input("Cars per day", min_value=1, value=1)
with col2:
    markup = st.number_input("Markup %", min_value=100.0, value=5.00)
with col3:
    workshop_charge = st.number_input("Workshop supplies charge", min_value=5.0, value=nan)

st.markdown("<h2 style='color:#CC0000;font-family:Calibri;'>Select Chargeable Items</h2>", unsafe_allow_html=True)

# Item selection
selected_items = []
cols = st.columns(2)
items = ['Sump plug washer', 'Washer additive', 'Engine flush 250 ml', 'Fuel additive 250 ml', 'diesel biocide treatment 250 ml']
for i, item in enumerate(items):
    with cols[i % 2]:
        if st.checkbox(item):
            selected_items.append(item)

st.markdown("<h2 style='color:#CC0000;font-family:Calibri;'>Profit Summary</h2>", unsafe_allow_html=True)

# Calculate profit
item_data = {'Sump plug washer': 0.45, 'Washer additive': 1.95, 'Engine flush 250 ml': 6.95, 'Fuel additive 250 ml': 6.95, 'diesel biocide treatment 250 ml': 8.95}
total_item_profit = sum([(item_data[item] * (markup / 100)) for item in selected_items])
total_profit_per_car = total_item_profit + workshop_charge
daily_profit = total_profit_per_car * cars_per_day
weekly_profit = daily_profit * 5
monthly_profit = weekly_profit * 4
annual_profit = daily_profit * 250  # 260 weekdays - 10 days leave

st.write(f"**Daily Profit:** AUD {daily_profit:.2f}")
st.write(f"**Weekly Profit:** AUD {weekly_profit:.2f}")
st.write(f"**Monthly Profit:** AUD {monthly_profit:.2f}")
st.write(f"**Annual Profit:** AUD {annual_profit:.2f}")

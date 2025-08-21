
import streamlit as st

# Set page config
st.set_page_config(page_title="Profit Calculator", layout="centered")

# Apply custom CSS for colors and font
st.markdown("""
    <style>
        body {
            font-family: 'Calibri', sans-serif;
            background-color: #FFFFFF;
            color: #000000;
        }
        .stButton>button {
            background-color: #CC0000;
            color: #FFFFFF;
        }
        .stCheckbox {
            color: #737373;
        }
        .stTextInput>div>input {
            background-color: #BFBFBF;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Profit Calculator")

# Input fields
cars_per_day = st.number_input("Cars per day", min_value=1, value=5)
markup_percent = st.number_input("Markup (%)", min_value=100, value=100)
workshop_charge = st.number_input("Workshop supplies charge per vehicle (AUD)", min_value=5.0, value=5.0)

# Fixed cost items
items = {
    "Wiper Blade Euro (x2)": 30.00,
    "Sump plug washer": 0.45,
    "Washer additive": 1.95,
    "Engine flush 250 ml": 6.95,
    "Fuel additive 250 ml": 6.95,
    "Diesel biocide treatment 250 ml": 8.95
}

st.subheader("Select Chargeable Items")
selected_items = []
for item, cost in items.items():
    if st.checkbox(item):
        selected_items.append((item, cost))

# Calculate profit
daily_profit = 0
for item, cost in selected_items:
    profit_per_item = cost * (markup_percent / 100)
    daily_profit += profit_per_item * cars_per_day

# Add workshop supplies charge
daily_profit += workshop_charge * cars_per_day

weekly_profit = daily_profit * 7
monthly_profit = daily_profit * 30
annual_profit = daily_profit * 365

# Display results
st.subheader("Profit Summary")
st.write(f"**Daily Profit:** AUD {daily_profit:.2f}")
st.write(f"**Weekly Profit:** AUD {weekly_profit:.2f}")
st.write(f"**Monthly Profit:** AUD {monthly_profit:.2f}")
st.write(f"**Annual Profit:** AUD {annual_profit:.2f}")

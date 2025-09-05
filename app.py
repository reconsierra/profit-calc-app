
import streamlit as st

# Set page config
st.set_page_config(page_title="Profit Calculator", layout="wide")

# Apply custom CSS for Calibri font and layout adjustments
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Calibri', sans-serif;
            background-color: #FFFFFF;
        }
        h1 {
            color: #CC0000;
            margin-top: -40px;
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        .stTextInput > div > div > input {
            background-color: #BFBFBF;
            color: #000000;
        }
        .stCheckbox > label {
            color: #737373;
        }
    </style>
""", unsafe_allow_html=True)


# Header
st.markdown("<h1>Profit Calculator</h1>", unsafe_allow_html=True)

# Cars per day and Markup % on the same row
col1, col2 = st.columns(2)
with col1:
    cars_per_day = st.number_input("Service Cars per day", min_value=1, value=5, step=1, format="%d")
with col2:
    markup = st.number_input("Markup % (2 x cost)", min_value=100, value=100, step=10, format="%d")

# Workshop charge input
workshop_charge = st.number_input("Workshop supplies charge ($ per vehicle)", min_value=5.00, value=5.00, step=0.50, format="%.2f")

# Fixed cost items
st.markdown("### Select Chargeable Items")
items = {
    "Sump plug washer": 0.45,
    "Washer additive": 1.95,
    "Wiper Blade Metal (x2)": 19.96,
    "Wiper Flat Blade Euro (x2)": 30.00,
    "Engine flush 250 ml": 6.95,
    "Petrol/Diesel fuel additive 250 ml": 6.95,
    #"Diesel biocide treatment 250 ml": 8.95
}

selected_items = {}
for item, cost in items.items():
    if st.checkbox(item):
        selected_items[item] = cost

# Calculate profit
daily_profit = 0
for item, cost in selected_items.items():
    profit_per_item = cost * (markup / 100)
    daily_profit += profit_per_item * cars_per_day

# Add workshop supplies charge
daily_profit += workshop_charge * cars_per_day

weekly_profit = daily_profit * 5
monthly_profit = daily_profit * 20
annual_profit = daily_profit * 250

# Display results
st.markdown("### Profit Summary")
#st.write(f"**Daily Profit:** ${daily_profit:.2f}")
st.write(f"**Weekly Profit:** ${weekly_profit:.2f}")
st.write(f"**Monthly Profit:** ${monthly_profit:.2f}")
st.write(f"**Annual Profit:** ${annual_profit:.2f}")

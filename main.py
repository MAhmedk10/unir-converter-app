import streamlit as st

# Function to convert units
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9,
        "seconds_minutes": 1/60,
        "minutes_seconds": 60,
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        conversion = conversions[key]
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return "Conversion not supported"

# Streamlit UI Setup
st.set_page_config(page_title="Unit Converter", layout="centered")

# Styled Title Using Streamlit Markdown
st.markdown("## Unit Converter")
st.write("Easily convert between different units like length, weight, temperature, and time.")

# Input Section
st.markdown("### Enter Value to Convert")
value = st.number_input("Enter value:", min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

# Available units
units = ["meters", "kilometers", "grams", "kilograms", "celsius", "fahrenheit", "seconds", "minutes"]

# Select Boxes for Units
with col1:
    unit_from = st.selectbox("Convert from:", units)

with col2:
    unit_to = st.selectbox("Convert to:", units)

# Prevent converting to the same unit
if unit_from == unit_to:
    st.warning("Please select different units for conversion.")
else:
    # Convert Button with Styling
    if st.button("Convert", use_container_width=True):
        result = convert_units(value, unit_from, unit_to)
        st.success(f"Converted Value: {result:.2f} {unit_to}")

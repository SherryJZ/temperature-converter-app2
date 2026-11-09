
# ==========================================
# TEMPERATURE CONVERTER WEB APP
# Built with Python and Streamlit
# ==========================================

# Step 1: Import the Streamlit library
import streamlit as st

# Step 2: Configure the web page
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered"
)

# Step 3: Display the app title
st.title("🌡️ Temperature Converter")

# Add a short description
st.write("Convert temperatures between Celsius and Fahrenheit.")

# Add a divider for a clean interface
st.divider()

# Step 4: Ask the user to enter a temperature
temperature = st.number_input(
    "Enter the temperature:",
    value=0.0,
    step=0.1,
    format="%.2f"
)

# Step 5: Let the user select a conversion type
conversion_type = st.radio(
    "Select conversion type:",
    [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius"
    ]
)

# Step 6: Perform the temperature conversion
if conversion_type == "Celsius to Fahrenheit":

    # Formula: F = (C * 9/5) + 32
    result = (temperature * 9/5) + 32

    # Set the correct temperature units
    input_unit = "°C"
    output_unit = "°F"

    # Store the formula to display later
    formula = "°F = (°C × 9/5) + 32"

else:

    # Formula: C = (F - 32) * 5/9
    result = (temperature - 32) * 5/9

    # Set the correct temperature units
    input_unit = "°F"
    output_unit = "°C"

    # Store the formula to display later
    formula = "°C = (°F - 32) × 5/9"

# Step 7: Display the converted temperature
st.divider()

st.subheader("✅ Conversion Result")

st.success(
    f"{temperature:.2f} {input_unit} = "
    f"{result:.2f} {output_unit}"
)

# Step 8: Display the conversion formula
st.subheader("📘 Formula Used")

st.info(formula)

# Step 9: Add a friendly footer
st.divider()

st.caption("Made with ❤️ using Python and Streamlit")

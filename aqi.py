import streamlit as st

def calculate_aqi(concentration, pollutant):
    """
    Calculate AQI for a given pollutant concentration.

    Parameters:
        concentration (float): Pollutant concentration in µg/m³ or ppm.
        pollutant (str): Pollutant name ('PM2.5', 'PM10', 'O3', 'NO2', 'SO2', 'CO').

    Returns:
        int: AQI value.
    """
    # Define AQI breakpoints for each pollutant
    aqi_breakpoints = {
        'PM2.5': [
            (0.0, 12.0, 0, 50),
            (12.1, 35.4, 51, 100),
            (35.5, 55.4, 101, 150),
            (55.5, 150.4, 151, 200),
            (150.5, 250.4, 201, 300),
            (250.5, 350.4, 301, 400),
            (350.5, 500.4, 401, 500),
        ],
        'PM10': [
            (0, 54, 0, 50),
            (55, 154, 51, 100),
            (155, 254, 101, 150),
            (255, 354, 151, 200),
            (355, 424, 201, 300),
            (425, 504, 301, 400),
            (505, 604, 401, 500),
        ],
        'O3': [
            (0.000, 0.054, 0, 50),
            (0.055, 0.070, 51, 100),
            (0.071, 0.085, 101, 150),
            (0.086, 0.105, 151, 200),
            (0.106, 0.200, 201, 300),
        ],
        'CO': [
            (0.0, 4.4, 0, 50),
            (4.5, 9.4, 51, 100),
            (9.5, 12.4, 101, 150),
            (12.5, 15.4, 151, 200),
            (15.5, 30.4, 201, 300),
            (30.5, 40.4, 301, 400),
            (40.5, 50.4, 401, 500),
        ],
        'SO2': [
            (0.0, 35, 0, 50),
            (36, 75, 51, 100),
            (76, 185, 101, 150),
            (186, 304, 151, 200),
            (305, 604, 201, 300),
            (605, 804, 301, 400),
            (805, 1004, 401, 500),
        ],
        'NO2': [
            (0, 53, 0, 50),
            (54, 100, 51, 100),
            (101, 360, 101, 150),
            (361, 649, 151, 200),
            (650, 1249, 201, 300),
            (1250, 1649, 301, 400),
            (1650, 2049, 401, 500),
        ],
    }

    if pollutant not in aqi_breakpoints:
        raise ValueError(f"Invalid pollutant: {pollutant}")

    for bp in aqi_breakpoints[pollutant]:
        c_low, c_high, aqi_low, aqi_high = bp
        if c_low <= concentration <= c_high:
            # Calculate AQI using linear interpolation
            aqi = ((aqi_high - aqi_low) / (c_high - c_low)) * (concentration - c_low) + aqi_low
            return round(aqi)

    raise ValueError("Concentration out of range for AQI calculation")

# Streamlit UI
st.title("AQI Calculator")
st.write("Calculate the Air Quality Index (AQI) for a given pollutant concentration.")

# User inputs
pollutant = st.selectbox("Select the pollutant", ["PM2.5", "PM10", "O3", "NO2", "SO2", "CO"])
concentration = st.number_input(f"Enter the concentration of {pollutant} (in µg/m³ or ppm):", min_value=0.0, format="%.2f")

if st.button("Calculate AQI"):
    try:
        aqi = calculate_aqi(concentration, pollutant)
        st.success(f"The AQI for {pollutant} with a concentration of {concentration} is {aqi}.")
    except ValueError as e:
        st.error(f"Error: {e}")

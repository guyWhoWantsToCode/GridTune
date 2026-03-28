import copy
import streamlit as st
import os
from PIL import Image
import pillow_avif

# ============================
# PAGE CONFIG
# ============================
st.set_page_config(page_title="F1 2025 Setup Generator", layout="wide")

# ============================
# DATA
# ============================
F1_CARS = {
    "redbull_rb21": {
        "car_name": "Red Bull RB21",
        "front_wing": 7,
        "rear_wing": 9,
        "diff_on": 55,
        "diff_off": 50,
        "camber_front": -3.50,
        "camber_rear": -2.00,
        "toe_front": 0.05,
        "toe_rear": 0.20,
        "suspension_front": 35,
        "suspension_rear": 15,
        "arb_front": 15,
        "arb_rear": 10,
        "ride_height_front": 20,
        "ride_height_rear": 45,
        "brake_bias": 56.0,
        "tire_pressure_fl": 23.0,
        "tire_pressure_fr": 23.0,
        "tire_pressure_rl": 21.5,
        "tire_pressure_rr": 21.5
    },

    "ferrari_sf25": {
        "car_name": "Ferrari SF-25",
        "front_wing": 8,
        "rear_wing": 10,
        "diff_on": 57,
        "diff_off": 52,
        "camber_front": -3.40,
        "camber_rear": -2.00,
        "toe_front": 0.05,
        "toe_rear": 0.20,
        "suspension_front": 34,
        "suspension_rear": 16,
        "arb_front": 14,
        "arb_rear": 10,
        "ride_height_front": 20,
        "ride_height_rear": 45,
        "brake_bias": 55.5,
        "tire_pressure_fl": 23.2,
        "tire_pressure_fr": 23.2,
        "tire_pressure_rl": 21.6,
        "tire_pressure_rr": 21.6
    },

    "mercedes_w16": {
        "car_name": "Mercedes W16",
        "front_wing": 6,
        "rear_wing": 8,
        "diff_on": 54,
        "diff_off": 50,
        "camber_front": -3.50,
        "camber_rear": -2.10,
        "toe_front": 0.05,
        "toe_rear": 0.20,
        "suspension_front": 33,
        "suspension_rear": 15,
        "arb_front": 13,
        "arb_rear": 9,
        "ride_height_front": 20,
        "ride_height_rear": 45,
        "brake_bias": 55.5,
        "tire_pressure_fl": 23.1,
        "tire_pressure_fr": 23.1,
        "tire_pressure_rl": 21.5,
        "tire_pressure_rr": 21.5
    },

    "mclaren_mcl39": {
        "car_name": "McLaren MCL39",
        "front_wing": 7,
        "rear_wing": 9,
        "diff_on": 56,
        "diff_off": 51,
        "camber_front": -3.45,
        "camber_rear": -2.05,
        "toe_front": 0.05,
        "toe_rear": 0.20,
        "suspension_front": 34,
        "suspension_rear": 15,
        "arb_front": 14,
        "arb_rear": 10,
        "ride_height_front": 20,
        "ride_height_rear": 45,
        "brake_bias": 55.0,
        "tire_pressure_fl": 23.1,
        "tire_pressure_fr": 23.1,
        "tire_pressure_rl": 21.6,
        "tire_pressure_rr": 21.6
    },

    "aston_martin_amr25": {
        "car_name": "Aston Martin AMR25",
        "front_wing": 6,
        "rear_wing": 8,
        "diff_on": 55,
        "diff_off": 50,
        "camber_front": -3.45,
        "camber_rear": -2.00,
        "toe_front": 0.05,
        "toe_rear": 0.20,
        "suspension_front": 33,
        "suspension_rear": 15,
        "arb_front": 13,
        "arb_rear": 9,
        "ride_height_front": 20,
        "ride_height_rear": 45,
        "brake_bias": 55.5,
        "tire_pressure_fl": 23.0,
        "tire_pressure_fr": 23.0,
        "tire_pressure_rl": 21.5,
        "tire_pressure_rr": 21.5
    },

    "alpine_a525": {
        "car_name": "Alpine A525",
        "front_wing": 7,
        "rear_wing": 9,
        "diff_on": 55,
        "diff_off": 50,
        "camber_front": -3.45,
        "camber_rear": -2.05,
        "toe_front": 0.05,
        "toe_rear": 0.20,
        "suspension_front": 34,
        "suspension_rear": 15,
        "arb_front": 14,
        "arb_rear": 10,
        "ride_height_front": 20,
        "ride_height_rear": 45,
        "brake_bias": 55.0,
        "tire_pressure_fl": 23.0,
        "tire_pressure_fr": 23.0,
        "tire_pressure_rl": 21.5,
        "tire_pressure_rr": 21.5
    },

    "williams_fw47": {
        "car_name": "Williams FW47",
        "front_wing": 6,
        "rear_wing": 8,
        "diff_on": 54,
        "diff_off": 49,
        "camber_front": -3.40,
        "camber_rear": -2.00,
        "toe_front": 0.05,
        "toe_rear": 0.20,
        "suspension_front": 32,
        "suspension_rear": 14,
        "arb_front": 13,
        "arb_rear": 9,
        "ride_height_front": 20,
        "ride_height_rear": 45,
        "brake_bias": 55.5,
        "tire_pressure_fl": 23.0,
        "tire_pressure_fr": 23.0,
        "tire_pressure_rl": 21.4,
        "tire_pressure_rr": 21.4
    },

    "rb_vcarb02": {
        "car_name": "RB VCARB 02",
        "front_wing": 7,
        "rear_wing": 9,
        "diff_on": 55,
        "diff_off": 50,
        "camber_front": -3.45,
        "camber_rear": -2.05,
        "toe_front": 0.05,
        "toe_rear": 0.20,
        "suspension_front": 34,
        "suspension_rear": 15,
        "arb_front": 14,
        "arb_rear": 10,
        "ride_height_front": 20,
        "ride_height_rear": 45,
        "brake_bias": 55.0,
        "tire_pressure_fl": 23.0,
        "tire_pressure_fr": 23.0,
        "tire_pressure_rl": 21.5,
        "tire_pressure_rr": 21.5
    },

    "sauber_c45": {
        "car_name": "Sauber C45",
        "front_wing": 6,
        "rear_wing": 8,
        "diff_on": 54,
        "diff_off": 49,
        "camber_front": -3.40,
        "camber_rear": -2.00,
        "toe_front": 0.05,
        "toe_rear": 0.20,
        "suspension_front": 32,
        "suspension_rear": 14,
        "arb_front": 13,
        "arb_rear": 9,
        "ride_height_front": 20,
        "ride_height_rear": 45,
        "brake_bias": 55.5,
        "tire_pressure_fl": 23.0,
        "tire_pressure_fr": 23.0,
        "tire_pressure_rl": 21.4,
        "tire_pressure_rr": 21.4
    },

    "haas_vf25": {
        "car_name": "Haas VF-25",
        "front_wing": 6,
        "rear_wing": 8,
        "diff_on": 54,
        "diff_off": 49,
        "camber_front": -3.40,
        "camber_rear": -2.00,
        "toe_front": 0.05,
        "toe_rear": 0.20,
        "suspension_front": 32,
        "suspension_rear": 14,
        "arb_front": 13,
        "arb_rear": 9,
        "ride_height_front": 20,
        "ride_height_rear": 45,
        "brake_bias": 55.5,
        "tire_pressure_fl": 23.0,
        "tire_pressure_fr": 23.0,
        "tire_pressure_rl": 21.4,
        "tire_pressure_rr": 21.4
    }
}

TRACKS = {
    "bahrain": 0.60,
    "jeddah": 0.45,
    "australia": 0.65,
    "suzuka": 0.75,
    "china": 0.60,
    "miami": 0.55,
    "imola": 0.70,
    "monaco": 0.95,
    "canada": 0.50,
    "spain": 0.75,
    "austria": 0.60,
    "silverstone": 0.70,
    "hungary": 0.85,
    "spa": 0.50,
    "zandvoort": 0.85,
    "monza": 0.20,
    "singapore": 0.90,
    "austin": 0.65,
    "mexico": 0.55,
    "brazil": 0.65,
    "las_vegas": 0.35,
    "qatar": 0.75,
    "abu_dhabi": 0.60
}

# ============================
# SETUP ENGINE
# ============================
def generate_setup(base, track, balance, aggression, weather, session_type):
    setup = copy.deepcopy(base)
    df = TRACKS[track]

    setup["front_wing"] = int(10 * df) + balance * 2
    setup["rear_wing"] = int(12 * df) - balance * 2
    setup["diff_on"] += aggression * 8
    setup["diff_off"] += balance * 3
    setup["arb_front"] -= balance * 2
    setup["arb_rear"] += balance * 2

    pressure_delta_front = aggression * 0.2
    pressure_delta_rear = aggression * 0.15

    if session_type == "race":
        setup["rear_wing"] += 1
        pressure_delta_front -= 0.1
        pressure_delta_rear -= 0.1
    elif session_type == "quali":
        setup["front_wing"] += 1
        setup["diff_on"] += 2
    elif session_type == "time_trial":
        setup["front_wing"] += 1
        setup["diff_on"] += 3
        setup["diff_off"] += 2
        pressure_delta_front += 0.1
        pressure_delta_rear += 0.1

    setup["tire_pressure_fl"] += pressure_delta_front
    setup["tire_pressure_fr"] += pressure_delta_front
    setup["tire_pressure_rl"] += pressure_delta_rear
    setup["tire_pressure_rr"] += pressure_delta_rear

    if weather == "wet":
        setup["rear_wing"] += 2
        setup["ride_height_front"] += 5
        setup["ride_height_rear"] += 5

    return setup


# ============================
# UI
# ============================
st.image(
    "Untitled design (3).png",
    width=350
)
st.markdown(
    """
    <div class="main-title"></div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@400&display=swap');

    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 52px;
        font-weight: 700;
        margin-bottom: 0;
    }

    .sub-title {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        margin-top: -10px;
    }
    </style>

    <div class="main-title">GridTune</div>
    <div class="sub-title">Smart F1 2025 Setup Generator</div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    car_key = st.selectbox("Choose Car", list(F1_CARS.keys()))
    track = st.selectbox("Choose Track", list(TRACKS.keys()))
    session_type = st.selectbox("Session Type", ["race", "quali", "time_trial"])

with col2:
    weather = st.selectbox("Weather", ["dry", "wet"])
    balance = st.slider(
    "Balance",
    -1.0,
    1.0,
    0.0,
    0.1,
    help="""
    -1 = Understeer: the car resists turning and pushes wide through corners.
    
    +1 = Oversteer: the rear of the car rotates more aggressively and may step out.
    
    0 = Neutral balance.
    """
)
    aggression = st.slider(
    "Aggression",
    0.0,
    1.0,
    0.5,
    0.1,
    help="""
    Lower values = safer and more stable setup.

    Higher values = more aggressive setup with sharper turn-in and faster lap-time potential.
    """
)

if st.button("Generate Setup", use_container_width=True):
    setup = generate_setup(F1_CARS[car_key], track, balance, aggression, weather, session_type)

    st.subheader(setup["car_name"])

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Front Wing",
            round(setup["front_wing"], 1),
            help="Controls front-end downforce and turn-in response. Higher values improve cornering grip but reduce top speed."
        )
        st.metric(
            "Rear Wing",
            round(setup["rear_wing"], 1),
            help="Controls rear stability and traction. Higher values improve corner exits but add drag."
        )
        st.metric(
            "Brake Bias",
            round(setup["brake_bias"], 1),
            help="Percentage of braking force sent to the front axle. Higher values increase braking stability."
        )

    with c2:
        st.metric(
            "Diff On",
            round(setup["diff_on"], 1),
            help="Differential lock while accelerating. Higher = more traction, less rotation."
        )
        st.metric(
            "Diff Off",
            round(setup["diff_off"], 1),
            help="Differential behavior while off-throttle and on corner entry. Lower = better rotation."
        )
        st.metric(
            "Front ARB",
            round(setup["arb_front"], 1),
            help="Front anti-roll bar stiffness. Higher values sharpen response but may reduce front grip."
        )
        st.metric(
            "Rear ARB",
            round(setup["arb_rear"], 1),
            help="Rear anti-roll bar stiffness. Higher values increase rotation and oversteer tendency."
        )

    with c3:
        st.metric(
            "FL Pressure",
            round(setup["tire_pressure_fl"], 2),
            help="Front-left tyre pressure. Affects temperature, wear, and grip."
        )
        st.metric(
            "FR Pressure",
            round(setup["tire_pressure_fr"], 2),
            help="Front-right tyre pressure. Higher pressure improves speed, lower improves grip."
        )
        st.metric(
            "RL Pressure",
            round(setup["tire_pressure_rl"], 2),
            help="Rear-left tyre pressure. Impacts traction and tyre temps."
        )
        st.metric(
            "RR Pressure",
            round(setup["tire_pressure_rr"], 2),
            help="Rear-right tyre pressure. Important for rear stability and traction."
        )
st.divider()
st.subheader("Track Map")

base_dir = os.path.dirname(__file__)
image_path = os.path.join("track_maps", f"{track}.avif")

if os.path.exists(image_path):
    img = Image.open(image_path)

    st.image(
        img,
        caption=f"{track.replace('_', ' ').title()} Circuit Map",
        use_container_width=True
    )
else:
    st.warning("Track map image not found.")

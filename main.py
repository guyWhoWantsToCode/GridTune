import copy

# ============================
# F1 2025 CAR DATABASE
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

def generate_setup(base, track, balance, aggression, weather, session_type):
    setup = copy.deepcopy(base)

    df = TRACKS[track]

    # Base aero from track
    setup["front_wing"] = int(10 * df) + balance * 2
    setup["rear_wing"] = int(12 * df) - balance * 2

    # Transmission
    setup["diff_on"] += aggression * 8
    setup["diff_off"] += balance * 3

    # Suspension
    setup["arb_front"] -= balance * 2
    setup["arb_rear"] += balance * 2

    # Tyres
    setup["tire_pressure_fl"] += aggression * 0.2
    setup["tire_pressure_fr"] += aggression * 0.2
    setup["tire_pressure_rl"] += aggression * 0.15
    setup["tire_pressure_rr"] += aggression * 0.15

    # Weather
    if weather == "wet":
        setup["rear_wing"] += 2
        setup["ride_height_front"] += 5
        setup["ride_height_rear"] += 5

    # Session Type
    if session_type == "race":
        setup["rear_wing"] += 1
        setup["diff_on"] -= 2
        setup["tire_pressure_fl"] -= 0.1
        setup["tire_pressure_fr"] -= 0.1
        setup["tire_pressure_rl"] -= 0.1
        setup["tire_pressure_rr"] -= 0.1

    elif session_type == "quali":
        setup["front_wing"] += 1
        setup["diff_on"] += 2
        setup["tire_pressure_fl"] += 0.1
        setup["tire_pressure_fr"] += 0.1

    elif session_type == "time_trial":
        setup["front_wing"] += 1
        setup["diff_on"] += 3
        setup["diff_off"] += 2
        setup["tire_pressure_fl"] += 0.15
        setup["tire_pressure_fr"] += 0.15
        setup["tire_pressure_rl"] += 0.15
        setup["tire_pressure_rr"] += 0.15

    return setup

def print_setup(setup):
    print(f"\n=== {setup['car_name']} SETUP ===\n")

    print("AERO")
    print(f"Front Wing: {round(setup['front_wing'],1)}")
    print(f"Rear Wing: {round(setup['rear_wing'],1)}")

    print("\nTRANSMISSION")
    print(f"Diff On Throttle: {round(setup['diff_on'],1)}")
    print(f"Diff Off Throttle: {round(setup['diff_off'],1)}")

    print("\nSUSPENSION")
    print(f"Front ARB: {round(setup['arb_front'],1)}")
    print(f"Rear ARB: {round(setup['arb_rear'],1)}")

    print("\nBRAKES")
    print(f"Brake Bias: {round(setup['brake_bias'],1)}")

    print("\nTYRES")
    print(f"FL: {round(setup['tire_pressure_fl'],2)}")
    print(f"FR: {round(setup['tire_pressure_fr'],2)}")
    print(f"RL: {round(setup['tire_pressure_rl'],2)}")
    print(f"RR: {round(setup['tire_pressure_rr'],2)}")

def main():
    print("=== F1 2025 Setup Generator ===")

    print("\nAvailable Cars:")
    for car in F1_CARS:
        print("-", car)

    car = input("\nChoose car: ").lower()

    print("\nAvailable Tracks:")
    for track_name in TRACKS:
        print("-", track_name)

    track = input("\nChoose track: ").lower()

    print("\nSession Types:")
    print("- race")
    print("- quali")
    print("- time_trial")

    session_type = input("\nChoose session type: ").lower()

    balance = float(input("Balance (-1 to 1): "))
    aggression = float(input("Aggression (0 to 1): "))
    weather = input("Weather (dry/wet): ").lower()

    setup = generate_setup(
        F1_CARS[car],
        track,
        balance,
        aggression,
        weather,
        session_type
    )

    print_setup(setup)


if __name__ == "__main__":
    main()
import random
import math

# Weights extracted from: https://www.reddit.com/r/pesmobile/comments/14xov22/here_is_how_overall_rating_works_mimos_post/
position_weights = {
    "CF": {
        "OffensiveAwareness": 0.21, 
        "BallControl": 0.11, 
        "Dribbling": 0.062, "TightPossession": 0.041, "LowPass": 0.035, "LoftedPass": 0.013, 
        "Finishing": 0.36, "Heading": 0.067, "PlaceKicking": 0.012, "Curl": 0.016, 
        "DefensiveAwareness": 0.0, "BallWinning": 0.016, "Aggression": 0.013, "Speed": 0.098, 
        "Acceleration": 0.13, "KickingPower": 0.12, "Jump": 0.063, "PhysicalContact": 0.085, 
        "Balance": 0.088, "Stamina": 0.043
    },
    "SS": {"OffensiveAwareness": 0.18, "BallControl": 0.22, "Dribbling": 0.13, "TightPossession": 0.084, "LowPass": 0.088, "LoftedPass": 0.084, "Finishing": 0.28, "Heading": 0.014, "PlaceKicking": 0.028, "Curl": 0.013, "DefensiveAwareness": 0.01, "BallWinning": 0.017, "Aggression": 0.006, "Speed": 0.07, "Acceleration": 0.11, "KickingPower": 0.092, "Jump": 0.042, "PhysicalContact": 0.034, "Balance": 0.075, "Stamina": 0.057},
    "LWF": {"OffensiveAwareness": 0.17, "BallControl": 0.17, "Dribbling": 0.16, "TightPossession": 0.091, "LowPass": 0.067, "LoftedPass": 0.11, "Finishing": 0.16, "Heading": 0.021, "PlaceKicking": 0.01, "Curl": 0.013, "DefensiveAwareness": 0.016, "BallWinning": 0.006, "Aggression": 0.013, "Speed": 0.23, "Acceleration": 0.16, "KickingPower": 0.059, "Jump": 0.029, "PhysicalContact": 0.036, "Balance": 0.07, "Stamina": 0.044},
    "RWF": {"OffensiveAwareness": 0.17, "BallControl": 0.17, "Dribbling": 0.16, "TightPossession": 0.091, "LowPass": 0.067, "LoftedPass": 0.11, "Finishing": 0.16, "Heading": 0.021, "PlaceKicking": 0.01, "Curl": 0.013, "DefensiveAwareness": 0.016, "BallWinning": 0.006, "Aggression": 0.013, "Speed": 0.23, "Acceleration": 0.16, "KickingPower": 0.059, "Jump": 0.029, "PhysicalContact": 0.036, "Balance": 0.07, "Stamina": 0.044},
    "AMF": {"OffensiveAwareness": 0.17, "BallControl": 0.21, "Dribbling": 0.12, "TightPossession": 0.085, "LowPass": 0.19, "LoftedPass": 0.14, "Finishing": 0.15, "Heading": 0.025, "PlaceKicking": 0.015, "Curl": 0.025, "DefensiveAwareness": 0.03, "BallWinning": 0.005, "Aggression": 0.005, "Speed": 0.12, "Acceleration": 0.12, "KickingPower": 0.08, "Jump": 0.015, "PhysicalContact": 0.015, "Balance": 0.04, "Stamina": 0.095},
    "LMF": {"OffensiveAwareness": 0.095, "BallControl": 0.16, "Dribbling": 0.12, "TightPossession": 0.076, "LowPass": 0.14, "LoftedPass": 0.2, "Finishing": 0.093, "Heading": 0.005, "PlaceKicking": 0.018, "Curl": 0.025, "DefensiveAwareness": 0.057, "BallWinning": 0.012, "Aggression": 0.015, "Speed": 0.19, "Acceleration": 0.16, "KickingPower": 0.032, "Jump": 0.022, "PhysicalContact": 0.019, "Balance": 0.056, "Stamina": 0.15},
    "RMF": {"OffensiveAwareness": 0.095, "BallControl": 0.16, "Dribbling": 0.12, "TightPossession": 0.076, "LowPass": 0.14, "LoftedPass": 0.2, "Finishing": 0.093, "Heading": 0.005, "PlaceKicking": 0.018, "Curl": 0.025, "DefensiveAwareness": 0.057, "BallWinning": 0.012, "Aggression": 0.015, "Speed": 0.19, "Acceleration": 0.16, "KickingPower": 0.032, "Jump": 0.022, "PhysicalContact": 0.019, "Balance": 0.056, "Stamina": 0.15},
    "CMF": {"OffensiveAwareness": 0.096, "BallControl": 0.18, "Dribbling": 0.096, "TightPossession": 0.052, "LowPass": 0.21, "LoftedPass": 0.16, "Finishing": 0.077, "Heading": 0.023, "PlaceKicking": 0.009, "Curl": 0.01, "DefensiveAwareness": 0.079, "BallWinning": 0.091, "Aggression": 0.04, "Speed": 0.057, "Acceleration": 0.089, "KickingPower": 0.073, "Jump": 0.01, "PhysicalContact": 0.052, "Balance": 0.017, "Stamina": 0.19},
    "DMF": {"OffensiveAwareness": 0.072, "BallControl": 0.14, "Dribbling": 0.043, "TightPossession": 0.011, "LowPass": 0.11, "LoftedPass": 0.12, "Finishing": 0.027, "Heading": 0.056, "PlaceKicking": 0.008, "Curl": 0.019, "DefensiveAwareness": 0.22, "BallWinning": 0.13, "Aggression": 0.11, "Speed": 0.048, "Acceleration": 0.072, "KickingPower": 0.056, "Jump": 0.035, "PhysicalContact": 0.12, "Balance": 0.008, "Stamina": 0.2},
    "LB": {"OffensiveAwareness": 0.055, "BallControl": 0.08, "Dribbling": 0.069, "TightPossession": 0.034, "LowPass": 0.078, "LoftedPass": 0.14, "Finishing": 0.023, "Heading": 0.03, "PlaceKicking": 0.024, "Curl": 0.034, "DefensiveAwareness": 0.14, "BallWinning": 0.088, "Aggression": 0.032, "Speed": 0.23, "Acceleration": 0.18, "KickingPower": 0.016, "Jump": 0.039, "PhysicalContact": 0.1, "Balance": 0.033, "Stamina": 0.2},
    "RB": {"OffensiveAwareness": 0.055, "BallControl": 0.08, "Dribbling": 0.069, "TightPossession": 0.034, "LowPass": 0.078, "LoftedPass": 0.14, "Finishing": 0.023, "Heading": 0.03, "PlaceKicking": 0.024, "Curl": 0.034, "DefensiveAwareness": 0.14, "BallWinning": 0.088, "Aggression": 0.032, "Speed": 0.23, "Acceleration": 0.18, "KickingPower": 0.016, "Jump": 0.039, "PhysicalContact": 0.1, "Balance": 0.033, "Stamina": 0.2},
    "CB": {"OffensiveAwareness": 0.01, "BallControl": 0.025, "Dribbling": 0.019, "TightPossession": 0.004, "LoftedPass": 0.067, "Finishing": 0.028, "Heading": 0.049, "PlaceKicking": 0.016, "Curl": 0.009, "DefensiveAwareness": 0.29, "BallWinning": 0.2, "Aggression": 0.078, "Speed": 0.14, "Acceleration": 0.14, "KickingPower": 0.033, "Jump": 0.11, "PhysicalContact": 0.2, "Balance": 0.004, "Stamina": 0.064, "LowPass": 0.043},
    "GK": {"OffensiveAwareness": 0.0, "BallControl": 0.0, "Dribbling": 0.0, "TightPossession": 0.0, "LowPass": 0.025, "LoftedPass": 0.044, "Finishing": 0.005, "Heading": 0.004, "PlaceKicking": 0.008, "Curl": 0.001, "DefensiveAwareness": 0.007, "BallWinning": 0.0, "Aggression": 0.0, "Speed": 0.013, "Acceleration": 0.039, "KickingPower": 0.051, "Jump": 0.14, "PhysicalContact": 0.078, "Balance": 0.0, "Stamina": 0.002, "GKAwareness": 0.29, "GKCatching": 0.23, "GKClearing": 0.18, "GKReflexes": 0.16, "GKReach": 0.23 }
}

style_bias = {
    1: {  # Goal Poacher
        "Finishing": 1.25, "OffensiveAwareness": 1.2, "Acceleration": 1.1
    },
    2: {  # Dummy Runner
        "OffensiveAwareness": 1.2, "Speed": 1.15, "LowPass": 1.1
    },
    3: {  # Fox in the Box
        "Finishing": 1.3, "Balance": 1.15, "PhysicalContact": 1.1
    },
    4: {  # Prolific Winger
        "Speed": 1.3, "Acceleration": 1.25, "Dribbling": 1.15
    },
    5: {  # Classic No.10
        "BallControl": 1.3, "LowPass": 1.3, "TightPossession": 1.2
    },
    6: {  # Hole Player
        "OffensiveAwareness": 1.25, "Acceleration": 1.2, "Finishing": 1.1
    },
    7: {  # Box-to-Box
        "Stamina": 1.35, "Aggression": 1.2, "BallWinning": 1.15
    },
    8: {  # Anchor Man
        "DefensiveAwareness": 1.35, "BallWinning": 1.25, "PhysicalContact": 1.1
    },
    9: {  # The Destroyer
        "Aggression": 1.35, "BallWinning": 1.3, "PhysicalContact": 1.2
    },
    10: {  # Extra Frontman
        "OffensiveAwareness": 1.25, "PhysicalContact": 1.2, "Heading": 1.15
    },
    11: {  # Offensive Full-back
        "Speed": 1.3, "Acceleration": 1.25, "LoftedPass": 1.15
    },
    12: {  # Defensive Full-back
        "DefensiveAwareness": 1.3, "BallWinning": 1.25, "PhysicalContact": 1.1
    },
    13: {  # Target Man
        "PhysicalContact": 1.35, "Heading": 1.3, "Balance": 1.15
    },
    14: {  # Creative Playmaker
        "LowPass": 1.35, "TightPossession": 1.25, "Balance": 1.15
    },
    15: {  # Build Up
        "LowPass": 1.25, "DefensiveAwareness": 1.2, "BallControl": 1.15
    },
    16: {  # Offensive Goalkeeper
        "GKAwareness": 1.2, "GKClearing": 1.15, "LowPass": 1.1
    },
    17: {  # Defensive Goalkeeper
        "GKAwareness": 1.3, "GKReflexes": 1.25, "GKReach": 1.15
    },
    18: {  # Roaming Flank
        "Speed": 1.25, "BallControl": 1.2, "Stamina": 1.15
    },
    19: {  # Cross Specialist
        "LoftedPass": 1.35, "Curl": 1.25, "Stamina": 1.1
    },
    20: {  # Orchestrator
        "LowPass": 1.3, "BallControl": 1.25, "DefensiveAwareness": 1.1
    },
    21: {  # Full-back Finisher
        "OffensiveAwareness": 1.25, "Finishing": 1.2, "Acceleration": 1.15
    }
}

all_abilities = [
    "OffensiveAwareness", "BallControl", "Dribbling", "TightPossession", "LowPass",
    "LoftedPass", "Finishing", "Heading", "PlaceKicking", "Curl", "Speed",
    "Acceleration", "KickingPower", "Jump", "PhysicalContact", "Balance", "Stamina",
    "DefensiveAwareness", "BallWinning", "Aggression", "GKAwareness", "GKCatching",
    "GKClearing", "GKReflexes", "GKReach"
]

gk_abilities = ["GKAwareness", "GKCatching", "GKClearing", "GKReflexes", "GKReach"]

def generate_abilities_dice_system(position, rating=75, style=None):
    weights = position_weights.get(position, {})
    bias_map = style_bias.get(style, {})
    abilities = {}

    BASE_MIN = 40
    BASE_MAX = 99

    # This list is to order them by weight, for testing using the MAIN in this file
    ability_weights = []

    for ability in all_abilities:
        if position != "GK" and ability in gk_abilities:
            abilities[ability] = "40"
            continue
        if position == "GK" and ability not in weights:
            abilities[ability] = "40"
            continue

        w = weights.get(ability, 0.0)
        adjusted_weight = w * bias_map.get(ability, 1.0)
        ability_weights.append((ability, w, adjusted_weight))

    ability_weights.sort(key=lambda x: x[2], reverse=True)

    max_weight = ability_weights[0][2] if ability_weights else 0.0

    # For each ability, calculate the ranges and roll the dice
    for ability, w, adjusted_weight in ability_weights:
        print(f"{ability:20} ({w:.4f}) {adjusted_weight:.4f}", end=" ")
        # Uses the max weight to normalize the others
        ranges = calculate_ranges(rating, adjusted_weight, max_weight)

        final_value = None
        for attempt, (range_name, range_limits) in enumerate(ranges.items()):
            # In case the range limits are out of bounds, this prevents multiple rolls in extreme ranges
            roll_min = min(range_limits['min'], BASE_MIN)
            roll_max = max(range_limits['max'], BASE_MAX)
            roll = random.randint(roll_min, roll_max)

            if range_limits['min'] <= roll <= range_limits['max']:
                final_value = roll
                print(f"{attempt}: {roll}")
                break

            if attempt == len(ranges) - 1:
                print(f"{attempt}: {roll}")
                final_value = max(range_limits['min'], min(range_limits['max'], roll))

        # Clamps the value
        final_value = max(BASE_MIN, min(BASE_MAX, final_value))
        abilities[ability] = str(final_value)

    return abilities

def calculate_ranges(rating, weight, MAX_WEIGHT=0.36):
    # CENTER: it is a combination of the rating and the weight of the ability
    # weight_factor is a curve that goes from 0 to 1, where 0 means "no weight" and 1 means "max weight"
    
    BASE_MIN = 40 # minimum ability value
    BASE_MAX = 99 # maximum ability value

    # This prevents high weights from being exponential
    limit = 2000

    # Here I used 0.02 as a "reference weight" to make the curve threshold, but using the max weight works better
    # weight_factor = (math.log(1 + limit * weight) / math.log(1 + limit * 0.02))  
    weight_factor = (math.log(1 + limit * weight) / math.log(1 + limit * MAX_WEIGHT))
    
    # UNUSED ALGORITHMS
    # RATINGS FAR AWAY = EXPONENTIAL, LOW RATINGS = GOOD
    # center: interpolates between BASE_MIN and rating according to weight
    # center = BASE_MIN + (rating - BASE_MIN) * weight_factor
    # center = min(BASE_MAX, center)
    
    # RATING LINEAR
    # center: the rating displaces the full range linearly
    # weight_factor defines HOW MUCH of the total range is used
    # rating defines FROM WHERE that range starts
    # center = rating - RATING_RANGE * (1 - weight_factor) * 0.5
    # center = max(BASE_MIN, min(BASE_MAX, center))

    # LOGARITHMIC RATING
    # Normalize the rating so that it is between 0 and 1
    # normalized_rating = (rating - BASE_MIN) / RATING_RANGE

    # dampened_rating = normalized_rating ** 0.5

    # # Center: interpolates between BASE_MIN and rating, but using the inverse factor
    # center = BASE_MIN + (rating - BASE_MIN) * dampened_rating

    # # Adjust by weight
    # center = center - RATING_RANGE * (1 - weight_factor) * 0.5
    # center = min(BASE_MAX, max(BASE_MIN, center)) 

    # LINEAR RATING WITH THRESHOLD (EQUILIBRIUM POINT)
    # Define the threshold where Rating == Center APROX
    THRESHOLD = 69
    
    # Define the "strength" of the growth (Slope)
    # 0.8 means that for each rating point, the center increases by 0.8
    # This makes the center greater below the threshold and smaller above it.
    growth_factor = 0.8
    
    # linear formula
    center = THRESHOLD + (rating - THRESHOLD) * growth_factor
    
    # weight_impact = 15
    # Apply a weight_factor adjustment so that the weight still influences the calculation
    # This shifts the center based on how weighted the calculation is
    # center = center - RATING_RANGE * (1 - weight_factor) * 0.5
    # center = center - weight_impact * (1 - weight_factor) # BRUTALLL but 0.0 doesn't give 40
    center = BASE_MIN + (center - BASE_MIN) * weight_factor

    # OFFSET: The results always end up being 6-7 points less than they should be for the given ratings
    # OFFSET = 2
    # center = center + OFFSET

    center = max(BASE_MIN, min(BASE_MAX, center))

    print(f"WF: {weight_factor:.4f} Center: {center:6.2f}", end=" ")
    
    range_definitions = [
        ('A', 3),
        ('B', 6),
        ('C', 9),
        ('D', 12),
        ('E', 16),
        ('F', 20),
        ('G', 24),
        ('H', 28),
    ]

    ranges = {}

    # Dynamic range calculator
    for range_name, amplitude in range_definitions:
        ranges[range_name] = {
            'min': int(center - amplitude), # Removed the min and max because it
            'max': int(center + amplitude)  # caused multiple rolls in the extreme ranges
        }

    # FOR TESTING
    for range_name, amplitude in range_definitions:
        print(f"{range_name}:{ranges[range_name]['min']:3}-{ranges[range_name]['max']:2}", end=" ")
    # print()

    return ranges

# Exported Function
def generate_abilities(position, rating=75, style=None):
    return generate_abilities_dice_system(position, rating, style)

# TESTS
if __name__ == "__main__":
    rating = 65
    position = "CF"
    print("\n" + "="*50)
    print("GENERATING A ", position, "WITH", rating, "RATING:")
    print("="*50)
    
    cf_abilities = generate_abilities(position, rating=rating, style=None)  # Goal Poacher
    print("{")
    for i, (ab, value) in enumerate(cf_abilities.items()):
        comma = "," if i < len(cf_abilities) - 1 else ""
        print(f'  "{ab}": "{value}"{comma}')
    print("}")

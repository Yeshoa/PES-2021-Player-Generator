import random
import numpy as np
import string
from config import COUNTRY_CODES 

def generate_id():
    return str(random.randint(100000, 999999))

def generate_shirt_name(name):
    parts = name.split()
    if len(parts) >= 2:
        return parts[-1] 
    else:
        return name 


def generate_country_code():
    return str(random.choice(list(COUNTRY_CODES.values())))

def generate_height(position):
    print(f"Generating height for position: {position}")
    position_heights = {
        "GK": {"mean": 188, "std": 5, "min": 160, "max": 210},
        "0": {"mean": 188, "std": 5, "min": 160, "max": 210},  # GK
        "CB": {"mean": 186, "std": 4, "min": 160, "max": 210},
        "1": {"mean": 186, "std": 4, "min": 160, "max": 210},  # CB
        "LB": {"mean": 180, "std": 4, "min": 160, "max": 210},
        "2": {"mean": 180, "std": 4, "min": 160, "max": 210},  # LB
        "RB": {"mean": 180, "std": 4, "min": 160, "max": 210},
        "3": {"mean": 180, "std": 4, "min": 160, "max": 210},  # RB
        "DMF": {"mean": 180, "std": 4, "min": 160, "max": 210},
        "4": {"mean": 180, "std": 4, "min": 160, "max": 210},  # DMF
        "CMF": {"mean": 180, "std": 4, "min": 160, "max": 210},
        "5": {"mean": 180, "std": 4, "min": 160, "max": 210},  # CMF
        "LMF": {"mean": 179, "std": 4, "min": 160, "max": 210},
        "6": {"mean": 179, "std": 4, "min": 160, "max": 210},  # LMF
        "RMF": {"mean": 179, "std": 4, "min": 160, "max": 210},
        "7": {"mean": 179, "std": 4, "min": 160, "max": 210},  # RMF
        "AMF": {"mean": 179, "std": 4, "min": 160, "max": 210},
        "8": {"mean": 179, "std": 4, "min": 160, "max": 210},  # AMF
        "LWF": {"mean": 177, "std": 4, "min": 160, "max": 210},
        "9": {"mean": 177, "std": 4, "min": 160, "max": 210},  # LWF
        "RWF": {"mean": 177, "std": 4, "min": 160, "max": 210},
        "10": {"mean": 177, "std": 4, "min": 160, "max": 210}, # RWF
        "SS": {"mean": 180, "std": 4, "min": 160, "max": 210},
        "11": {"mean": 180, "std": 4, "min": 160, "max": 210}, # SS
        "CF": {"mean": 183, "std": 4, "min": 160, "max": 210},
        "12": {"mean": 183, "std": 4, "min": 160, "max": 210}, # CF
    }
    
    params = position_heights.get(position, {"mean": 180, "std": 4, "min": 130, "max": 210})
    height = np.random.normal(params["mean"], params["std"])
    height = max(params["min"], min(params["max"], int(round(height))))
    return height

def generate_weight(height):
    imc = random.uniform(20.5, 23.5)
    height_m = height / 100
    weight = int(imc * (height_m ** 2))
    weight = max(30, min(129, weight))
    return weight

def generate_foot():
    # False = right foot, True = left foot
    return random.choices([False, True], weights=[0.85, 0.15])[0]

def generate_age():
    age = int(np.random.normal(28, 6))
    age = max(15, min(50, age))
    return age

def generate_weak_foot_stats():
    # 1-4 Weak Foot Usage and Weak Foot Accuracy
    weak_foot_usage = random.randint(1, 4)
    weak_foot_accuracy = random.randint(1, 4)
    return weak_foot_usage, weak_foot_accuracy

def generate_form():
    forms = [1, 2, 3, 4, 5, 6, 7, 8]
    weights = [0.01, 0.04, 0.20, 0.25, 0.25, 0.20, 0.04, 0.01] # Gaussian distribution
    return random.choices(forms, weights=weights)[0]

def generate_injury_resistance():
    resistances = [1, 2, 3]
    weights = [0.1, 0.3, 0.7] # Previous calculated by real player data
    return random.choices(resistances, weights=weights)[0]

def generate_position_code(position_str):
    position_map = {
        "GK": "0", "CB": "1", "LB": "2", "RB": "3", "DMF": "4",
        "CMF": "5", "LMF": "6", "RMF": "7", "AMF": "8", "LWF": "9",
        "RWF": "10", "SS": "11", "CF": "12"
    }
    return position_map.get(position_str, "0")  # GK default

# def generate_position_aptitudes(position_str):
#     # Genera las aptitudes por posición (solo 1 en la posición principal)
#     position_code = generate_position_code(position_str)
#     positions = ["GK", "CB", "LB", "RB", "DMF", "CMF", "LMF", "RMF", "AMF", "LWF", "RWF", "SS", "CF"]
    
#     aptitudes = {}
#     for pos in positions:
#         aptitudes[pos] = "1" if pos == position_str else "0"
    
#     return aptitudes
def generate_position_aptitudes(position_str):
    # Generates the position aptitudes with realistic chances based on proximity. The main position is always 1
    position_compatibility = {
        "GK": {},  # Goalkeepers don't have more positions
        
        "CB": {
            "LB": 0.25, "RB": 0.25, 
            "DMF": 0.20, 
            "CMF": 0.05,  
        },
        
        "LB": {
            "CB": 0.30, "RB": 0.30, 
            "LMF": 0.35, "LWF": 0.15, 
            "DMF": 0.10, "CMF": 0.05,  
        },
        "RB": {
            "CB": 0.30, "LB": 0.30, 
            "RMF": 0.35, "RWF": 0.15,
            "DMF": 0.10, "CMF": 0.05,
        },
        
        "DMF": {
            "CB": 0.25, 
            "LB": 0.10, "RB": 0.10, 
            "CMF": 0.40, 
            "LMF": 0.15, "RMF": 0.15,  
            "AMF": 0.05, 
        },
        
        "CMF": {
            "DMF": 0.35,
            "LMF": 0.25, "RMF": 0.25, 
            "AMF": 0.30,  
            "LB": 0.05, "RB": 0.05,  
            "SS": 0.03, "CF": 0.02,  
        },
        
        "LMF": {
            "LB": 0.30, 
            "CMF": 0.35, "DMF": 0.15,  
            "LWF": 0.35,  
            "AMF": 0.20,  
            "RMF": 0.30,  
        },
        "RMF": {
            "RB": 0.30,
            "CMF": 0.35, "DMF": 0.15,
            "RWF": 0.35,
            "AMF": 0.20,
            "LMF": 0.30,  
        },
        
        "AMF": {
            "CMF": 0.35,  
            "LMF": 0.20, "RMF": 0.20,  
            "SS": 0.40,  
            "LWF": 0.20, "RWF": 0.20,  
            "CF": 0.15,  
            "DMF": 0.05,  
        },
        
        "LWF": {
            "LMF": 0.40, 
            "AMF": 0.25,  
            "SS": 0.30,  
            "CF": 0.20,  
            "RWF": 0.25,  
            "LB": 0.10,  
        },
        "RWF": {
            "RMF": 0.40,
            "AMF": 0.25,
            "SS": 0.30,
            "CF": 0.20,
            "LWF": 0.25,  
            "RB": 0.10,
        },
        
        "SS": {
            "CF": 0.45,  
            "AMF": 0.40,  
            "LWF": 0.25, "RWF": 0.25,  
            "CMF": 0.10,  
        },
        
        "CF": {
            "SS": 0.50, 
            "LWF": 0.20, "RWF": 0.20, 
            "AMF": 0.15,  
            "CMF": 0.03,  
        },
    }
    
    positions = ["GK", "CB", "LB", "RB", "DMF", "CMF", "LMF", "RMF", "AMF", "LWF", "RWF", "SS", "CF"]
    aptitudes = {pos: "0" for pos in positions}
    
    aptitudes[position_str] = "1" # Main positino
    
    if position_str == "GK":
        return aptitudes
    
    # How many additional positions
    num_additional = random.choices(
        [0, 1, 2, 3, 4], 
        weights=[0.30, 0.40, 0.20, 0.08, 0.02]
    )[0]
    
    # Get compatible positions and their probabilities
    compatible_positions = position_compatibility.get(position_str, {})
    
    if compatible_positions:
        for _ in range(num_additional):
            # Select from compatible positions that are not yet assigned
            available = [pos for pos in compatible_positions.keys() if aptitudes[pos] == "0"]
            
            if not available:
                break
            
            # Normalize probabilities
            probs = [compatible_positions[pos] for pos in available]
            total = sum(probs)
            normalized_probs = [p/total for p in probs]
            
            selected = random.choices(available, weights=normalized_probs)[0]
            aptitudes[selected] = "1"
    
    return aptitudes

# Styles per position
styles_by_position = {
    "GK": [16, 17],  # Offensive/Defensive Goalkeeper
    "CB": [9, 10, 15],  # The Destroyer, Extra Frontman, Build Up
    "LB": [11, 12, 21],  # Offensive/Defensive Full-back, Full-Back Finisher
    "RB": [11, 12, 21],  # Offensive/Defensive Full-back, Full-Back Finisher
    "DMF": [8, 9, 20],  # Anchor Man, The Destroyer, Orchestrator
    "CMF": [5, 7, 20],  # Classic No. 10, Box-to-Box, Orchestrator
    "LMF": [6, 7, 14, 18, 19],  # Hole Player, Box-to-Box, Creative Playmaker, Roaming Flank, Cross Specialist
    "RMF": [6, 7, 14, 18, 19],  # Hole Player, Box-to-Box, Creative Playmaker, Roaming Flank, Cross Specialist
    "AMF": [5, 6, 14],  # Classic No. 10, Hole Player, Creative Playmaker
    "LWF": [4, 14, 18, 19],  # Prolific Winger, Creative Playmaker, Roaming Flank, Cross Specialist
    "RWF": [4, 14, 18, 19],  # Prolific Winger, Creative Playmaker, Roaming Flank, Cross Specialist
    "SS": [1, 2, 5, 6, 14],  # Goal Poacher, Dummy Runner, Classic No. 10, Hole Player, Creative Playmaker
    "CF": [1, 3, 13],  # Goal Poacher, Fox in the Box, Target Man
}

def generate_playing_style(position):
    styles = styles_by_position.get(position, [0])
    return str(random.choice(styles)) # ALWAYS STR

def detect_playing_style(position, abilities):
    a = {k: int(v) for k, v in abilities.items()}
    scores = {}

    scores[1]  = a["Finishing"]*1.3 + a["OffensiveAwareness"]*1.2 + a["Acceleration"]*1.1
    scores[2]  = a["OffensiveAwareness"]*1.3 + a["Speed"]*1.2 + a["LowPass"]*1.1
    scores[3]  = a["Finishing"]*1.4 + a["Balance"]*1.2 + a["PhysicalContact"]*1.1
    scores[4]  = a["Speed"]*1.4 + a["Acceleration"]*1.3 + a["Dribbling"]*1.2
    scores[5]  = a["BallControl"]*1.4 + a["LowPass"]*1.4 + a["TightPossession"]*1.3
    scores[6]  = a["OffensiveAwareness"]*1.3 + a["Acceleration"]*1.2 + a["Finishing"]*1.1
    scores[7]  = a["Stamina"]*1.4 + a["Aggression"]*1.3 + a["BallWinning"]*1.2
    scores[8]  = a["DefensiveAwareness"]*1.4 + a["BallWinning"]*1.3 + a["PhysicalContact"]*1.1
    scores[9]  = a["Aggression"]*1.4 + a["BallWinning"]*1.35 + a["PhysicalContact"]*1.2
    scores[10] = a["OffensiveAwareness"]*1.3 + a["Heading"]*1.2 + a["PhysicalContact"]*1.1
    scores[11] = a["Speed"]*1.3 + a["Acceleration"]*1.3 + a["LoftedPass"]*1.2
    scores[12] = a["DefensiveAwareness"]*1.4 + a["BallWinning"]*1.3 + a["PhysicalContact"]*1.1
    scores[13] = a["PhysicalContact"]*1.4 + a["Heading"]*1.35 + a["Balance"]*1.2
    scores[14] = a["LowPass"]*1.4 + a["TightPossession"]*1.3 + a["Balance"]*1.2
    scores[15] = a["LowPass"]*1.3 + a["DefensiveAwareness"]*1.2 + a["BallControl"]*1.1
    scores[16] = a.get("GKAwareness",0)*1.2 + a.get("GKClearing",0)*1.15 + a["LowPass"]*1.05
    scores[17] = a.get("GKAwareness",0)*1.3 + a.get("GKReflexes",0)*1.25 + a.get("GKReach",0)*1.15
    scores[18] = a["Speed"]*1.3 + a["BallControl"]*1.2 + a["Stamina"]*1.15
    scores[19] = a["LoftedPass"]*1.4 + a["Curl"]*1.3 + a["Stamina"]*1.1
    scores[20] = a["LowPass"]*1.35 + a["BallControl"]*1.25 + a["DefensiveAwareness"]*1.1
    scores[21] = a["OffensiveAwareness"]*1.3 + a["Finishing"]*1.2 + a["Acceleration"]*1.15

    valid = styles_by_position.get(position, [])
    scores = {k: v for k, v in scores.items() if k in valid}

    return max(scores, key=scores.get)


import random
import numpy as np

RACE_GROUPS = {
    1: {
        "name": "Nordic / Northern European",
        "skin_range": (1, 2),
        "prob": 8,
        "iris_light_prob": 0.55,
        "eye_mongoloid_factor": 0.05,
        "nose_height": 2.0,
        "nose_width": -1.8,
        "nostril_width": -2.0,
        "lips_full": -1.5,
        "lip_thickness": -1.2,
        "cheekbones": 1.5,
        "chin_projection": 1.8,
        "jaw_square": 0.8,
        "eyebrow_density": -0.5,
        "eye_depth": -1.0,
    },
    2: {
        "name": "Mediterranean / Southern European",
        "skin_range": (2, 3),
        "prob": 12,
        "iris_light_prob": 0.25,
        "eye_mongoloid_factor": 0.10,
        "nose_height": 1.2,
        "nose_width": -0.8,
        "nostril_width": -0.5,
        "lips_full": -0.5,
        "lip_thickness": -0.3,
        "cheekbones": 1.0,
        "chin_projection": 1.0,
        "jaw_square": 1.2,
        "eyebrow_density": 0.3,
        "eye_depth": -0.5,
    },
    3: {
        "name": "East European / Slavic",
        "skin_range": (2, 3),
        "prob": 7,
        "iris_light_prob": 0.15,
        "eye_mongoloid_factor": 0.15,
        "nose_height": 0.8,
        "nose_width": 0.0,
        "nostril_width": 0.2,
        "lips_full": 0.0,
        "lip_thickness": 0.2,
        "cheekbones": 1.2,
        "chin_projection": 0.5,
        "jaw_square": 1.8,
        "eyebrow_density": 1.0,
        "eye_depth": 0.0,
    },
    4: {
        "name": "Mestizo / Latin American mixed",
        "skin_range": (3, 4),
        "prob": 12,
        "iris_light_prob": 0.08,
        "eye_mongoloid_factor": 0.25,
        "nose_height": 0.0,
        "nose_width": 0.8,
        "nostril_width": 1.0,
        "lips_full": 1.2,
        "lip_thickness": 1.0,
        "cheekbones": 0.5,
        "chin_projection": 0.0,
        "jaw_square": 0.5,
        "eyebrow_density": 0.4,
        "eye_depth": 0.2,
    },
    5: {
        "name": "Middle Eastern / North African",
        "skin_range": (3, 4),
        "prob": 8,
        "iris_light_prob": 0.05,
        "eye_mongoloid_factor": 0.45,
        "nose_height": 1.8,
        "nose_width": 0.5,
        "nostril_width": 0.3,
        "lips_full": 0.5,
        "lip_thickness": 0.4,
        "cheekbones": 0.8,
        "chin_projection": 0.8,
        "jaw_square": 1.0,
        "eyebrow_density": 1.5,
        "eye_depth": 0.3,
    },
    6: {
        "name": "South Asian",
        "skin_range": (4, 5),
        "prob": 15,
        "iris_light_prob": 0.01,
        "eye_mongoloid_factor": 0.10,
        "nose_height": -0.5,
        "nose_width": 1.2,
        "nostril_width": 1.5,
        "lips_full": 0.8,
        "lip_thickness": 0.6,
        "cheekbones": 0.0,
        "chin_projection": -0.3,
        "jaw_square": 0.4,
        "eyebrow_density": 1.2,
        "eye_depth": 0.5,
    },
    7: {
        "name": "East Asian",
        "skin_range": (3, 4),
        "prob": 18,
        "iris_light_prob": 0.01,
        "eye_mongoloid_factor": 0.95,
        "nose_height": -1.8,
        "nose_width": -0.5,
        "nostril_width": -0.8,
        "lips_full": -1.0,
        "lip_thickness": -1.2,
        "cheekbones": 0.8,
        "chin_projection": -0.8,
        "jaw_square": -0.5,
        "eyebrow_density": -0.3,
        "eye_depth": 1.0,
    },
    8: {
        "name": "Southeast Asian",
        "skin_range": (4, 5),
        "prob": 10,
        "iris_light_prob": 0.01,
        "eye_mongoloid_factor": 0.85,
        "nose_height": -1.2,
        "nose_width": 0.5,
        "nostril_width": 0.8,
        "lips_full": -0.5,
        "lip_thickness": -0.6,
        "cheekbones": 0.6,
        "chin_projection": -0.5,
        "jaw_square": -0.3,
        "eyebrow_density": 0.2,
        "eye_depth": 0.8,
    },
    9: {
        "name": "Sub-Saharan African",
        "skin_range": (5, 6),
        "prob": 12,
        "iris_light_prob": 0.00,
        "eye_mongoloid_factor": 0.05,
        "nose_height": -2.2,
        "nose_width": 2.5,
        "nostril_width": 3.0,
        "lips_full": 2.5,
        "lip_thickness": 2.2,
        "cheekbones": -1.2,
        "chin_projection": 0.5,
        "jaw_square": 0.3,
        "eyebrow_density": 0.8,
        "eye_depth": 1.5,           
    },
    10: {
        "name": "Oceanic / Indigenous mixed",
        "skin_range": (4, 6),
        "prob": 5,
        "iris_light_prob": 0.02,
        "eye_mongoloid_factor": 0.30,
        "nose_height": -1.0,
        "nose_width": 1.8,
        "nostril_width": 2.0,
        "lips_full": 1.5,
        "lip_thickness": 1.3,
        "cheekbones": 1.0,
        "chin_projection": 0.0,
        "jaw_square": 0.6,
        "eyebrow_density": 0.7,
        "eye_depth": 0.7,
    },
    11: {
        "name": "Random",
        "skin_range": (1, 6),
        "prob": 3,
        "iris_light_prob": 0.30,
        "eye_mongoloid_factor": 0.20,
        "nose_height": 0.0,
        "nose_width": 0.0,
        "nostril_width": 0.0,
        "lips_full": 0.0,
        "lip_thickness": 0.0,
        "cheekbones": 0.0,
        "chin_projection": 0.0,
        "jaw_square": 0.0,
        "eyebrow_density": 0.0,
        "eye_depth": 0.0,
    }
}

RACE_WEIGHTS = [g["prob"] for g in RACE_GROUPS.values()]

def clipped_gaussian(mean, std_dev, min_val, max_val):
    while True:
        val = random.gauss(mean, std_dev)
        if min_val <= val <= max_val:
            return int(round(val))
        val = max(min_val, min(val, max_val))
        return int(round(val))

def generate_eye_features(skin_colour):
    features = {}

    if skin_colour in [1, 2]:
        features["UpperEyelidType"] = clipped_gaussian(3, 1.5, 1, 8)
        features["BottomEyelidType"] = clipped_gaussian(3, 1.5, 1, 7)
    elif skin_colour in [3, 4]:
        features["UpperEyelidType"] = clipped_gaussian(4, 1.5, 1, 8)
        features["BottomEyelidType"] = clipped_gaussian(4, 1.2, 1, 7)
    else:  # 5, 6
        features["UpperEyelidType"] = clipped_gaussian(6, 1.2, 1, 8)
        features["BottomEyelidType"] = clipped_gaussian(5, 1.2, 1, 7)

    features["EyeHeight"] = clipped_gaussian(0, 2, -7, 7)
    features["HorizontalEyePosition"] = clipped_gaussian(0, 2, -7, 7)

    if skin_colour == 1:  # Pale
        iris_weights = [5, 15, 20, 15, 12, 8, 8, 7, 3, 5, 2]
    elif skin_colour == 2:  # White
        iris_weights = [5, 18, 22, 15, 10, 7, 7, 6, 3, 5, 2]
    elif skin_colour == 3:  # Medium
        iris_weights = [10, 30, 35, 15, 4, 2, 2, 1, 0, 1, 0]
    elif skin_colour == 4:  # Brown
        iris_weights = [20, 40, 30, 7, 1, 1, 1, 0, 0, 0, 0]
    elif skin_colour == 5:  # Dark
        iris_weights = [40, 45, 12, 2, 0, 0, 1, 0, 0, 0, 0]
    else:  # 6 - Black
        iris_weights = [60, 35, 4, 1, 0, 0, 0, 0, 0, 0, 0]

    features["IrisColour"] = random.choices(range(1, 12), weights=iris_weights)[0]

    features["PupilSize"] = clipped_gaussian(0, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["UpperEyelidHt.(Inner)"] = clipped_gaussian(-1, 2, -7, 7)
        features["UpperEyelidWd.(Inner)"] = clipped_gaussian(-1, 2, -7, 7)
        features["UpperEyelidHt.(Outer)"] = clipped_gaussian(-1, 2, -7, 7)
        features["UpperEyelidWd.(Outer)"] = clipped_gaussian(-1, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["UpperEyelidHt.(Inner)"] = clipped_gaussian(0, 2, -7, 7)
        features["UpperEyelidWd.(Inner)"] = clipped_gaussian(0, 2, -7, 7)
        features["UpperEyelidHt.(Outer)"] = clipped_gaussian(0, 2, -7, 7)
        features["UpperEyelidWd.(Outer)"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["UpperEyelidHt.(Inner)"] = clipped_gaussian(1, 2, -7, 7)
        features["UpperEyelidWd.(Inner)"] = clipped_gaussian(1, 2, -7, 7)
        features["UpperEyelidHt.(Outer)"] = clipped_gaussian(1, 2, -7, 7)
        features["UpperEyelidWd.(Outer)"] = clipped_gaussian(1, 2, -7, 7)

    features["InnerEyeHeight"] = clipped_gaussian(0, 2, -7, 7)
    features["InnerEyePosition"] = clipped_gaussian(0, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["EyeCornerHeight"] = clipped_gaussian(-1, 2, -7, 7)
    else:
        features["EyeCornerHeight"] = clipped_gaussian(0, 2, -7, 7)

    features["OuterEyePosition"] = clipped_gaussian(0, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["BottomEyelidHeight"] = clipped_gaussian(-1, 2, -7, 7)
    else:
        features["BottomEyelidHeight"] = clipped_gaussian(1, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["EyeDepth"] = clipped_gaussian(-2, 2, -7, 7) 
    elif skin_colour in [3, 4]:
        features["EyeDepth"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["EyeDepth"] = clipped_gaussian(2, 1.5, -7, 7) 

    return {k: str(v) for k, v in features.items()}

def generate_eyebrow_features(skin_colour):
    features = {}

    features["Forehead"] = random.randint(1, 7)
    features["EyebrowType"] = random.randint(1, 8)

    if skin_colour in [1, 2]:
        features["EyebrowThickness"] = clipped_gaussian(0.5, 0.6, 0, 2)
    elif skin_colour in [3, 4]:
        features["EyebrowThickness"] = clipped_gaussian(1, 0.6, 0, 2)
    else:
        features["EyebrowThickness"] = clipped_gaussian(1.5, 0.6, 0, 2)

    if skin_colour in [1, 2]:
        features["EyebrowStyle"] = random.choices([0, 1, 2], weights=[25, 50, 25])[0]
    else:
        features["EyebrowStyle"] = random.choices([0, 1, 2], weights=[40, 35, 25])[0]

    if skin_colour in [1, 2]:
        features["EyebrowDensity"] = clipped_gaussian(1, 0.8, 0, 3)
    elif skin_colour in [3, 4]:
        features["EyebrowDensity"] = clipped_gaussian(2, 0.8, 0, 3)
    else:
        features["EyebrowDensity"] = clipped_gaussian(2.5, 0.6, 0, 3)

    if skin_colour == 1:  # Pale
        r = clipped_gaussian(45, 8, 0, 63)
        g = clipped_gaussian(32, 8, 0, 63)
        b = clipped_gaussian(18, 6, 0, 63)
    elif skin_colour == 2:  # White
        r = clipped_gaussian(38, 8, 0, 63)
        g = clipped_gaussian(24, 7, 0, 63)
        b = clipped_gaussian(12, 5, 0, 63)
    elif skin_colour == 3:  # Medium
        r = clipped_gaussian(28, 6, 0, 63)
        g = clipped_gaussian(16, 5, 0, 63)
        b = clipped_gaussian(8, 4, 0, 63)
    elif skin_colour == 4:  # Brown
        r = clipped_gaussian(20, 5, 0, 63)
        g = clipped_gaussian(10, 4, 0, 63)
        b = clipped_gaussian(5, 3, 0, 63)
    else:  # 5, 6: Dark
        r = clipped_gaussian(10, 4, 0, 63)
        g = clipped_gaussian(6, 3, 0, 63)
        b = clipped_gaussian(3, 2, 0, 63)

    features["EyebrowColourR"] = r
    features["EyebrowColourG"] = g
    features["EyebrowColourB"] = b

    if skin_colour in [1, 2]:
        features["InnerEyebrowHeight"] = clipped_gaussian(1, 2, -7, 7)  
        features["OuterEdyebrowHeight"] = clipped_gaussian(-1, 2, -7, 7) 
    elif skin_colour in [3, 4]:
        features["InnerEyebrowHeight"] = clipped_gaussian(0, 2, -7, 7)
        features["OuterEdyebrowHeight"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["InnerEyebrowHeight"] = clipped_gaussian(-1, 2, -7, 7) 
        features["OuterEdyebrowHeight"] = clipped_gaussian(1, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["BrowWidth"] = clipped_gaussian(-1, 2, -7, 7) 
    elif skin_colour in [3, 4]:
        features["BrowWidth"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["BrowWidth"] = clipped_gaussian(2, 1.5, -7, 7) 

    features["TempleWidth"] = clipped_gaussian(0, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["EyebrowDepth"] = clipped_gaussian(-2, 2, -7, 7) 
    elif skin_colour in [3, 4]:
        features["EyebrowDepth"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["EyebrowDepth"] = clipped_gaussian(1, 2, -7, 7)  

    return {k: str(v) for k, v in features.items()}

def generate_nose_features(skin_colour):
    features = {}

    features["NoseType"] = random.randint(1, 8)

    features["LaughterLines"] = random.randint(1, 5)

    if skin_colour in [1, 2]:
        features["NoseHeight"] = clipped_gaussian(2, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["NoseHeight"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["NoseHeight"] = clipped_gaussian(-2, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["NostrilWidth"] = clipped_gaussian(-2, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["NostrilWidth"] = clipped_gaussian(1, 2, -7, 7)
    else:
        features["NostrilWidth"] = clipped_gaussian(3, 1.5, -7, 7)

    if skin_colour in [1, 2]:
        features["NoseWidth"] = clipped_gaussian(-2, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["NoseWidth"] = clipped_gaussian(1, 2, -7, 7)
    else:
        features["NoseWidth"] = clipped_gaussian(3, 1.5, -7, 7)

    if skin_colour in [1, 2]:
        features["NoseTipDepth"] = clipped_gaussian(2, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["NoseTipDepth"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["NoseTipDepth"] = clipped_gaussian(-2, 1.5, -7, 7)

    if skin_colour in [1, 2]:
        features["NoseDepth"] = clipped_gaussian(2, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["NoseDepth"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["NoseDepth"] = clipped_gaussian(-1, 2, -7, 7)

    return {k: str(v) for k, v in features.items()}


def generate_mouth_features(skin_colour):
    features = {}

    features["UpperLipType"] = random.randint(1, 5)
    features["LowerLipType"] = random.randint(1, 5)

    features["MouthPosition"] = clipped_gaussian(0, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["LipSize"] = clipped_gaussian(-2, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["LipSize"] = clipped_gaussian(1, 2, -7, 7)
    else:
        features["LipSize"] = clipped_gaussian(3, 1.5, -7, 7)

    if skin_colour in [1, 2]:
        features["LipWidth"] = clipped_gaussian(-1, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["LipWidth"] = clipped_gaussian(1, 2, -7, 7)
    else:
        features["LipWidth"] = clipped_gaussian(2, 1.5, -7, 7)

    features["MouthCornerHeight"] = clipped_gaussian(0, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["MouthDepth"] = clipped_gaussian(-1, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["MouthDepth"] = clipped_gaussian(1, 2, -7, 7)
    else:
        features["MouthDepth"] = clipped_gaussian(2, 1.5, -7, 7)

    return {k: str(v) for k, v in features.items()}

def generate_jaw_features(skin_colour):
    features = {}

    features["CheekType"] = random.randint(0, 4)
    features["NeckLineType"] = random.randint(0, 4)

    if skin_colour in [1, 2]:
        features["Cheekbones"] = clipped_gaussian(1, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["Cheekbones"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["Cheekbones"] = clipped_gaussian(-1, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["ChinHeight"] = clipped_gaussian(1, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["ChinHeight"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["ChinHeight"] = clipped_gaussian(-1, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["ChinWidth"] = clipped_gaussian(-1, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["ChinWidth"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["ChinWidth"] = clipped_gaussian(1, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["JawHeight"] = clipped_gaussian(0, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["JawHeight"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["JawHeight"] = clipped_gaussian(1, 2, -7, 7)

    features["Jawline"] = clipped_gaussian(0, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["ChinDepth"] = clipped_gaussian(2, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["ChinDepth"] = clipped_gaussian(0, 2, -7, 7)
    else:
        features["ChinDepth"] = clipped_gaussian(-1, 2, -7, 7)

    return {k: str(v) for k, v in features.items()}


def generate_ear_features(skin_colour):
    features = {}

    if skin_colour in [1, 2]:
        features["EarLength"] = clipped_gaussian(0, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["EarLength"] = clipped_gaussian(1, 2, -7, 7)
    else:
        features["EarLength"] = clipped_gaussian(1, 2, -7, 7)

    if skin_colour in [1, 2]:
        features["EarWidth"] = clipped_gaussian(0, 2, -7, 7)
    elif skin_colour in [3, 4]:
        features["EarWidth"] = clipped_gaussian(1, 2, -7, 7)
    else:
        features["EarWidth"] = clipped_gaussian(1, 2, -7, 7)

    features["EarAngle"] = clipped_gaussian(0, 2, -7, 7)

    return {k: str(v) for k, v in features.items()}

HAIR_COLOUR_RGB = {
    1: {"r": (38, 6), "g": (32, 5), "b": (22, 4)},   # Brown
    2: {"r": (48, 6), "g": (42, 5), "b": (28, 4)},   # Dark Blond
    3: {"r": (58, 4), "g": (52, 4), "b": (35, 5)},   # Blond
    4: {"r": (8,  3), "g": (5,  2), "b": (3,  2)},   # Dark
    5: {"r": (32, 5), "g": (22, 4), "b": (10, 3)},   # Brown
    6: {"r": (14, 4), "g": (9,  3), "b": (5,  2)},   # Dark Brown
    7: {"r": (52, 5), "g": (50, 5), "b": (48, 5)},   # White
    8: {"r": (55, 5), "g": (22, 5), "b": (5,  3)},   # Red
}

# Weights by skin colour
HAIR_COLOUR_WEIGHTS = {
    1: [10, 15, 20, 10, 20, 10, 10, 5],  # Pale
    2: [12, 12, 10, 15, 25, 15, 8,  3],  # White
    3: [5,  5,  2,  25, 30, 25, 5,  3],  # Medium
    4: [1,  1,  0,  40, 25, 28, 3,  2],  # Brown
    5: [0,  0,  0,  55, 15, 25, 3,  2],  # Dark
    6: [0,  0,  0,  65, 10, 20, 3,  2],  # Black
}

def pick_hair_colour(skin_colour):
    weights = HAIR_COLOUR_WEIGHTS.get(skin_colour, HAIR_COLOUR_WEIGHTS[3])
    return random.choices(range(1, 9), weights=weights)[0]

def rgb_from_hair_colour(hair_colour):
    palette = HAIR_COLOUR_RGB[hair_colour]
    r = clipped_gaussian(palette["r"][0], palette["r"][1], 0, 63)
    g = clipped_gaussian(palette["g"][0], palette["g"][1], 0, 63)
    b = clipped_gaussian(palette["b"][0], palette["b"][1], 0, 63)
    return r, g, b


def generate_facial_hair_features(skin_colour):
    features = {}

    features["FacialHairType"] = str(
        0 if random.random() < 0.65 else random.randint(1, 18)
    )
    features["Thickness"] = random.randint(0, 3)

    facial_hair_colour = pick_hair_colour(skin_colour)
    r, g, b = rgb_from_hair_colour(facial_hair_colour)

    features["FacialHairColourR"] = r
    features["FacialHairColourG"] = g
    features["FacialHairColourB"] = b

    return {k: str(v) for k, v in features.items()}


def generate_hair_features(skin_colour):
    features = {}

    # Random
    features["Overall-Style"] = random.randint(0, 7)
    features["Overall-Length"] = random.randint(0, 5)
    features["Overall-WaveLevel"] = random.randint(0, 7)
    features["Overall-HairVariation"] = random.randint(0, 29)
    features["Font-Style"] = random.randint(0, 3)
    features["Font-Parted"] = random.randint(0, 6)
    features["Font-Hairline"] = random.randint(0, 3)
    features["Font-ForeheadWidth"] = random.randint(0, 3)
    features["Side/Back-Style"] = random.randint(0, 4)
    features["Side/Back-Cropped"] = random.randint(0, 6)

    # Chances of getting a custom colour
    use_custom = random.random() < 0.1

    if use_custom:
        if random.random() < 0.05: # Full random, flashy colours possible
            features["HairColourR"] = random.randint(0, 63)
            features["HairColourG"] = random.randint(0, 63)
            features["HairColourB"] = random.randint(0, 63)
        else:
            hair_colour_ref = pick_hair_colour(skin_colour)
            r, g, b = rgb_from_hair_colour(hair_colour_ref)
            features["HairColourR"] = r
            features["HairColourG"] = g
            features["HairColourB"] = b
        features["AccessoryColour"] = random.randint(1, 8)
        features["HairColour"] = 9
    else:
        hair_colour = pick_hair_colour(skin_colour)
        r, g, b = rgb_from_hair_colour(hair_colour)
        features["HairColourR"] = r
        features["HairColourG"] = g
        features["HairColourB"] = b
        features["AccessoryColour"] = random.randint(1, 8)
        features["HairColour"] = hair_colour

    features["Accessories"] = "True" if random.randint(1, 10000) == 1 else "False"
    return {k: str(v) for k, v in features.items()}


def generate_appearance(skin_colour=None):
    if skin_colour is None:
        skin_colour = random.randint(1, 6)

    appearance = {}

    # Physique
    appearance["NeckLength"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["NeckSize"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["ShoulderHeight"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["ShoulderWidth"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["ChestMeasurement"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["WaistSize"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["ArmSize"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["ThighSize"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["CalfSize"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["LegLength"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["ArmLength"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["SkinColour"] = str(skin_colour)

    # Head
    appearance["HeadLength"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["HeadWidth"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["HeadDepth"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["FaceHeight"] = str(clipped_gaussian(0, 2.5, -7, 7))
    appearance["FaceSize"] = str(clipped_gaussian(0, 2.5, -7, 7))

    # Face
    appearance.update(generate_eye_features(skin_colour))
    appearance.update(generate_eyebrow_features(skin_colour))
    appearance.update(generate_nose_features(skin_colour))
    appearance.update(generate_mouth_features(skin_colour))
    appearance.update(generate_facial_hair_features(skin_colour))
    appearance.update(generate_jaw_features(skin_colour))
    appearance.update(generate_ear_features(skin_colour))
    appearance.update(generate_hair_features(skin_colour))

    # Strip
    appearance["Wristtaping"] = str(random.randint(0, 4))
    appearance["WristTapeColour1"] = str(random.randint(0, 10))
    appearance["WristTapeColour2"] = str(random.randint(0, 10))
    appearance["AnkleTaping"] = str(random.randint(0, 4))
    appearance["PlayerGloves"] = str(random.randint(0, 5))
    appearance["Colour"] = str(random.randint(1, 6))
    appearance["Undershorts"] = str(random.randint(0, 2))
    appearance["Sleeves"] = str(random.randint(0, 2))
    appearance["Shirttail"] = str(random.randint(0, 2))
    appearance["SockLength"] = str(random.randint(0, 2))
    appearance["Long-SleevedInners"] = str(random.randint(0, 2))

    # Misc
    appearance["ValueAp1"] = "0"
    appearance["ValueAp2"] = "0"
    appearance["ValueAp3"] = "0"
    appearance["ValueAp4"] = "0"
    appearance["ValueAp5"] = "0"
    appearance["ValueAp6"] = "0"
    appearance["ValueAp7"] = "0"    
    appearance["ValueAp8"] = "0"
    appearance["ValueAp9"] = "0"
    appearance["ValueAp10"] = "0"
    appearance["ValueAp11"] = "0"
    appearance["ValueAp12"] = "0"
    appearance["ValueAp13"] = "0"    
    appearance["ValueAp14"] = "0"
    appearance["ValueAp15"] = "0"
    appearance["ValueAp16"] = "0"
    appearance["ValueAp17"] = "0"
    appearance["ValueAp18"] = "0"
    appearance["ValueAp19"] = "0"

    return appearance
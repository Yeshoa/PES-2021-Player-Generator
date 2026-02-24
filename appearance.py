import random
import numpy as np

RACE_GROUPS = {
    "nordic": {
        "skin_range": (1, 2),
        "prob": 8,
        "hair_weights": [10, 15, 20, 10, 20, 10, 10, 5],
        "iris_weights": [5, 15, 20, 15, 12, 8, 8, 7, 3, 5, 2],
        "features": {
            "NoseHeight": 2.0,
            "NoseWidth": -1.8,
            "NostrilWidth": -2.0,
            "LipsFull": -1.5,
            "LipThickness": -1.2,
            "Cheekbones": 1.5,
            "ChinProjection": 1.8,
            "JawSquare": 0.8,
            "EyebrowDensity": -0.5,
            "EyeDepth": -1.0,
        }
    },
    "mediterranean": {
        "skin_range": (2, 3),
        "prob": 12,
        "hair_weights": [12, 12, 10, 15, 25, 15, 8,  3],
        "iris_weights": [5, 18, 22, 15, 10, 7, 7, 6, 3, 5, 2],
        "features": {
            "NoseHeight": 1.2,
            "NoseWidth": -0.8,
            "NostrilWidth": -0.5,
            "LipsFull": -0.5,
            "LipThickness": -0.3,
            "Cheekbones": 1.0,
            "ChinProjection": 1.0,
            "JawSquare": 1.2,
            "EyebrowDensity": 0.3,
            "EyeDepth": -0.5,
        }
    },
    "slavic": {
        "skin_range": (2, 3),
        "prob": 7,
        "hair_weights": [12, 12, 10, 15, 25, 15, 8,  3],
        "iris_weights": [5, 18, 22, 15, 10, 7, 7, 6, 3, 5, 2],
        "features": {
            "NoseHeight": 0.8,
            "NoseWidth": 0.0,
            "NostrilWidth": 0.2,
            "LipsFull": 0.0,
            "LipThickness": 0.2,
            "Cheekbones": 1.2,
            "ChinProjection": 0.5,
            "JawSquare": 1.8,
            "EyebrowDensity": 1.0,
            "EyeDepth": 0.0,
        }
    },
    "mestizo": {
        "skin_range": (3, 4),
        "prob": 12,
        "hair_weights": [1,  1,  0,  40, 25, 28, 3,  2],
        "iris_weights": [10, 30, 35, 15, 4, 2, 2, 1, 0, 1, 0],
        "features": {
            "NoseHeight": 0.0,
            "NoseWidth": 0.8,
            "NostrilWidth": 1.0,
            "LipsFull": 1.2,
            "LipThickness": 1.0,
            "Cheekbones": 0.5,
            "ChinProjection": 0.0,
            "JawSquare": 0.5,
            "EyebrowDensity": 0.4,
            "EyeDepth": 0.2,
        }
    },
    "arab": {
        "skin_range": (3, 4),
        "prob": 8,
        "hair_weights": [1,  1,  0,  40, 25, 28, 3,  2],
        "iris_weights": [10, 30, 35, 15, 4, 2, 2, 1, 0, 1, 0],
        "features": {
            "NoseHeight": 1.8,
            "NoseWidth": 0.5,
            "NostrilWidth": 0.3,
            "LipsFull": 0.5,
            "LipThickness": 0.4,
            "Cheekbones": 0.8,
            "ChinProjection": 0.8,
            "JawSquare": 1.0,
            "EyebrowDensity": 1.5,
            "EyeDepth": 0.3,
        }
    },
    "south asian": {
        "skin_range": (4, 5),
        "prob": 15,
        "hair_weights": [0,  0,  0,  55, 15, 25, 3,  2],
        "iris_weights": [20, 40, 30, 7, 1, 1, 1, 0, 0, 0, 0],
        "features": {
            "NoseHeight": -0.5,
            "NoseWidth": 1.2,
            "NostrilWidth": 1.5,
            "LipsFull": 0.8,
            "LipThickness": 0.6,
            "Cheekbones": 0.0,
            "ChinProjection": -0.3,
            "JawSquare": 0.4,
            "EyebrowDensity": 1.2,
            "EyeDepth": 0.5,
        }
    },
    "east asian": {
        "skin_range": (3, 4),
        "prob": 18,
        "hair_weights": [0,  0,  0,  55, 15, 25, 3,  2],
        "iris_weights": [10, 30, 35, 15, 4, 2, 2, 1, 0, 1, 0],
        "features": {
            "NoseHeight": -1.8,
            "NoseWidth": -0.5,
            "NostrilWidth": -0.8,
            "LipsFull": -1.0,
            "LipThickness": -1.2,
            "Cheekbones": 0.8,
            "ChinProjection": -0.8,
            "JawSquare": -0.5,
            "EyebrowDensity": -0.3,
            "EyeDepth": 1.0,
        }
    },
    "southeast asian": {
        "skin_range": (4, 5),
        "prob": 10,
        "hair_weights": [0,  0,  0,  65, 10, 20, 3,  2],
        "iris_weights": [20, 40, 30, 7, 1, 1, 1, 0, 0, 0, 0],
        "features": {
            "NoseHeight": -1.2,
            "NoseWidth": 0.5,
            "NostrilWidth": 0.8,
            "LipsFull": -0.5,
            "LipThickness": -0.6,
            "Cheekbones": 0.6,
            "ChinProjection": -0.5,
            "JawSquare": -0.3,
            "EyebrowDensity": 0.2,
            "EyeDepth": 0.8,
        }
    },
    "sub-saharan": {
        "skin_range": (5, 6),
        "prob": 12,
        "hair_weights": [0,  0,  0,  65, 10, 20, 3,  2],
        "iris_weights": [60, 35, 4, 1, 0, 0, 0, 0, 0, 0, 0],
        "features": {
            "NoseHeight": -2.2,
            "NoseWidth": 2.5,
            "NostrilWidth": 3.0,
            "LipsFull": 2.5,
            "LipThickness": 2.2,
            "Cheekbones": -1.2,
            "ChinProjection": 0.5,
            "JawSquare": 0.3,
            "EyebrowDensity": 0.8,
            "EyeDepth": 1.5,
        }
    },
    "oceanic": {
        "skin_range": (4, 6),
        "prob": 5,
        "hair_weights": [0,  0,  0,  60, 15, 20, 3,  2],
        "iris_weights": [40, 45, 12, 2, 0, 0, 1, 0, 0, 0, 0],
        "features": {
            "NoseHeight": -1.0,
            "NoseWidth": 1.8,
            "NostrilWidth": 2.0,
            "LipsFull": 1.5,
            "LipThickness": 1.3,
            "Cheekbones": 1.0,
            "ChinProjection": 0.0,
            "JawSquare": 0.6,
            "EyebrowDensity": 0.7,
            "EyeDepth": 0.7,
        }
    },
    "random": {
        "skin_range": (1, 6),
        "prob": 3,
        "hair_weights": [10, 10, 10, 20, 20, 15, 10, 5],
        "iris_weights": [10, 30, 35, 15, 4, 2, 2, 1, 0, 1, 0],
        "features": {}
    },
    "test": {
        "skin_range": (6, 6),
        "prob": 3,
        "hair_weights": [100, 0, 0, 0, 0, 0, 0, 0],
        "iris_weights": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        "features": {}
    }
}

RACE_IDS = list(RACE_GROUPS.keys())
RACE_WEIGHTS = [g["prob"] for g in RACE_GROUPS.values()]

def clipped_gaussian(mean, std_dev, min_val, max_val):
    while True:
        val = random.gauss(mean, std_dev)
        if min_val <= val <= max_val:
            return int(round(val))
        val = max(min_val, min(val, max_val))
        return int(round(val))

def get_feature_value(race_data, feature_name, default_mean=0, std_dev=2.0, min_val=-7, max_val=7):
    # Get mean from race data or use default
    mean = race_data.get("features", {}).get(feature_name, default_mean)
    return clipped_gaussian(mean, std_dev, min_val, max_val)

def generate_eye_features(race_data, skin_colour):
    features = {}

    # Eyes: Types must be random style selections
    features["UpperEyelidType"] = random.randint(1, 7) # Style selection
    features["BottomEyelidType"] = random.randint(1, 7) # Style selection

    # Positions and gradual values from race data
    features["EyeHeight"] = get_feature_value(race_data, "EyeHeight")
    features["HorizontalEyePosition"] = get_feature_value(race_data, "HorizontalEyePosition")

    # Iris colour based on race data
    iris_weights = race_data.get("iris_weights", [10, 30, 35, 15, 4, 2, 2, 1, 0, 1, 0])
    features["IrisColour"] = random.choices(range(1, 12), weights=iris_weights)[0]
    features["PupilSize"] = get_feature_value(race_data, "PupilSize")

    # Gradual eyelid measurements
    eyelid_mean = 1 if skin_colour >= 5 else (0 if skin_colour in [3, 4] else -1)
    features["UpperEyelidHt.(Inner)"] = get_feature_value(race_data, "UpperEyelidHt.(Inner)", eyelid_mean)
    features["UpperEyelidWd.(Inner)"] = get_feature_value(race_data, "UpperEyelidWd.(Inner)", eyelid_mean)
    features["UpperEyelidHt.(Outer)"] = get_feature_value(race_data, "UpperEyelidHt.(Outer)", eyelid_mean)
    features["UpperEyelidWd.(Outer)"] = get_feature_value(race_data, "UpperEyelidWd.(Outer)", eyelid_mean)

    features["InnerEyeHeight"] = get_feature_value(race_data, "InnerEyeHeight")
    features["InnerEyePosition"] = get_feature_value(race_data, "InnerEyePosition")
    features["EyeCornerHeight"] = get_feature_value(race_data, "EyeCornerHeight", -1 if skin_colour in [1, 2] else 0)
    features["OuterEyePosition"] = get_feature_value(race_data, "OuterEyePosition")
    features["BottomEyelidHeight"] = get_feature_value(race_data, "BottomEyelidHeight", -1 if skin_colour in [1, 2] else 1)
    features["EyeDepth"] = get_feature_value(race_data, "EyeDepth", 2 if skin_colour >= 5 else (0 if skin_colour in [3, 4] else -2))

    return {k: str(v) for k, v in features.items()}

def generate_eyebrow_features(race_data, skin_colour):
    features = {}

    # Random style types
    features["Forehead"] = random.randint(1, 7)
    features["EyebrowType"] = random.randint(1, 8)
    # Eyebrow style density weight
    features["EyebrowStyle"] = random.choices([0, 1, 2], weights=[40, 35, 25])[0]

    # Gradual features
    thick_mean = 1.5 if skin_colour >= 5 else (1.0 if skin_colour in [3, 4] else 0.5)
    features["EyebrowThickness"] = get_feature_value(race_data, "EyebrowThickness", thick_mean, std_dev=0.6, min_val=0, max_val=2)

    dens_mean = 2.5 if skin_colour >= 5 else (2.0 if skin_colour in [3, 4] else 1.0)
    features["EyebrowDensity"] = get_feature_value(race_data, "EyebrowDensity", dens_mean, std_dev=0.8, min_val=0, max_val=3)

    # Base colours for eyebrows
    if skin_colour == 1:
        rgb = (45, 32, 18)
    elif skin_colour == 2:
        rgb = (38, 24, 12)
    elif skin_colour == 3:
        rgb = (28, 16, 8)
    elif skin_colour == 4:
        rgb = (20, 10, 5)
    else:
        rgb = (10, 6, 3)

    features["EyebrowColourR"] = clipped_gaussian(rgb[0], 8, 0, 63)
    features["EyebrowColourG"] = clipped_gaussian(rgb[1], 8, 0, 63)
    features["EyebrowColourB"] = clipped_gaussian(rgb[2], 6, 0, 63)

    features["InnerEyebrowHeight"] = get_feature_value(race_data, "InnerEyebrowHeight", 1 if skin_colour in [1, 2] else (-1 if skin_colour >= 5 else 0))
    features["OuterEdyebrowHeight"] = get_feature_value(race_data, "OuterEdyebrowHeight", -1 if skin_colour in [1, 2] else (1 if skin_colour >= 5 else 0))
    features["BrowWidth"] = get_feature_value(race_data, "BrowWidth", -1 if skin_colour in [1, 2] else (2 if skin_colour >= 5 else 0))
    features["TempleWidth"] = get_feature_value(race_data, "TempleWidth")
    features["EyebrowDepth"] = get_feature_value(race_data, "EyebrowDepth", -2 if skin_colour in [1, 2] else (1 if skin_colour >= 5 else 0))

    return {k: str(v) for k, v in features.items()}

def generate_nose_features(race_data, skin_colour):
    features = {}

    # Random style types
    features["NoseType"] = random.randint(1, 8)
    features["LaughterLines"] = random.randint(1, 5)

    # Nose measurements
    features["NoseHeight"] = get_feature_value(race_data, "NoseHeight", 2 if skin_colour in [1, 2] else (-2 if skin_colour >= 5 else 0))
    features["NostrilWidth"] = get_feature_value(race_data, "NostrilWidth", -2 if skin_colour in [1, 2] else (3 if skin_colour >= 5 else 1))
    features["NoseWidth"] = get_feature_value(race_data, "NoseWidth", -2 if skin_colour in [1, 2] else (3 if skin_colour >= 5 else 1))
    features["NoseTipDepth"] = get_feature_value(race_data, "NoseTipDepth", 2 if skin_colour in [1, 2] else (-2 if skin_colour >= 5 else 0))
    features["NoseDepth"] = get_feature_value(race_data, "NoseDepth", 2 if skin_colour in [1, 2] else (-1 if skin_colour >= 5 else 0))

    return {k: str(v) for k, v in features.items()}

def generate_mouth_features(race_data, skin_colour):
    features = {}

    # Random style types
    features["UpperLipType"] = random.randint(1, 5)
    features["LowerLipType"] = random.randint(1, 5)

    # Lip measurements
    features["MouthPosition"] = get_feature_value(race_data, "MouthPosition")
    features["LipSize"] = get_feature_value(race_data, "LipSize", -2 if skin_colour in [1, 2] else (3 if skin_colour >= 5 else 1))
    features["LipWidth"] = get_feature_value(race_data, "LipWidth", -1 if skin_colour in [1, 2] else (2 if skin_colour >= 5 else 1))
    features["MouthCornerHeight"] = get_feature_value(race_data, "MouthCornerHeight")
    features["MouthDepth"] = get_feature_value(race_data, "MouthDepth", -1 if skin_colour in [1, 2] else (2 if skin_colour >= 5 else 1))

    return {k: str(v) for k, v in features.items()}

def generate_jaw_features(race_data, skin_colour):
    features = {}

    # Random style types
    features["CheekType"] = random.randint(0, 4)
    features["NeckLineType"] = random.randint(0, 4)

    # Jaw and chin measurements
    features["Cheekbones"] = get_feature_value(race_data, "Cheekbones", 1 if skin_colour in [1, 2] else (-1 if skin_colour >= 5 else 0))
    features["ChinHeight"] = get_feature_value(race_data, "ChinHeight", 1 if skin_colour in [1, 2] else (-1 if skin_colour >= 5 else 0))
    features["ChinWidth"] = get_feature_value(race_data, "ChinWidth", -1 if skin_colour in [1, 2] else (1 if skin_colour >= 5 else 0))
    features["JawHeight"] = get_feature_value(race_data, "JawHeight", 1 if skin_colour >= 5 else 0)
    features["Jawline"] = get_feature_value(race_data, "Jawline")
    features["ChinDepth"] = get_feature_value(race_data, "ChinDepth", 2 if skin_colour in [1, 2] else (-1 if skin_colour >= 5 else 0))

    return {k: str(v) for k, v in features.items()}

def generate_ear_features(race_data, skin_colour):
    features = {}

    ear_mean = 0 if skin_colour in [1, 2] else 1
    features["EarLength"] = get_feature_value(race_data, "EarLength", ear_mean)
    features["EarWidth"] = get_feature_value(race_data, "EarWidth", ear_mean)
    features["EarAngle"] = get_feature_value(race_data, "EarAngle")

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

def pick_hair_colour(race_data):
    weights = race_data.get("hair_weights", [10, 10, 10, 10, 10, 10, 10, 10])
    return random.choices(range(1, 9), weights=weights)[0]

def rgb_from_hair_colour(hair_colour):
    palette = HAIR_COLOUR_RGB[hair_colour]
    r = clipped_gaussian(palette["r"][0], palette["r"][1], 0, 63)
    g = clipped_gaussian(palette["g"][0], palette["g"][1], 0, 63)
    b = clipped_gaussian(palette["b"][0], palette["b"][1], 0, 63)
    return r, g, b

def generate_facial_hair_features(race_data, skin_colour):
    features = {}

    # Random style types
    features["FacialHairType"] = str(random.randint(0, 18) if random.random() > 0.65 else 0)
    features["Thickness"] = random.randint(0, 3)

    # Hair colour is race-based
    facial_hair_colour = pick_hair_colour(race_data)
    r, g, b = rgb_from_hair_colour(facial_hair_colour)

    features["FacialHairColourR"] = r
    features["FacialHairColourG"] = g
    features["FacialHairColourB"] = b

    return {k: str(v) for k, v in features.items()}

def generate_hair_features(race_data, skin_colour):
    features = {}

    # Hair Style (Random style selections)
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

    # Hair color (10% chance of custom logic)
    use_custom = random.random() < 0.1

    if use_custom:
        if random.random() < 0.05: # Rare random colors
            features["HairColourR"] = random.randint(0, 63)
            features["HairColourG"] = random.randint(0, 63)
            features["HairColourB"] = random.randint(0, 63)
        else:
            hair_colour_ref = pick_hair_colour(race_data)
            r, g, b = rgb_from_hair_colour(hair_colour_ref)
            features["HairColourR"] = r
            features["HairColourG"] = g
            features["HairColourB"] = b
        features["AccessoryColour"] = random.randint(1, 8)
        features["HairColour"] = 9
    else:
        hair_colour = pick_hair_colour(race_data)
        r, g, b = rgb_from_hair_colour(hair_colour)
        features["HairColourR"] = r
        features["HairColourG"] = g
        features["HairColourB"] = b
        features["AccessoryColour"] = random.randint(1, 8)
        features["HairColour"] = hair_colour

    features["Accessories"] = "True" if random.randint(1, 10000) == 1 else "False"
    return {k: str(v) for k, v in features.items()}

def generate_appearance(race_id=None):
    # Race Selection
    if race_id is None:
        race_id = random.choices(RACE_IDS, weights=RACE_WEIGHTS)[0]
    
    race_data = RACE_GROUPS.get(race_id.lower(), RACE_GROUPS["random"])
    
    # Skin colour selection based on race range
    skin_min, skin_max = race_data["skin_range"]
    skin_colour = random.randint(skin_min, skin_max)

    appearance = {}

    # Physique
    appearance["NeckLength"] = str(get_feature_value(race_data, "NeckLength", 0, std_dev=2.5))
    appearance["NeckSize"] = str(get_feature_value(race_data, "NeckSize", 0, std_dev=2.5))
    appearance["ShoulderHeight"] = str(get_feature_value(race_data, "ShoulderHeight", 0, std_dev=2.5))
    appearance["ShoulderWidth"] = str(get_feature_value(race_data, "ShoulderWidth", 0, std_dev=2.5))
    appearance["ChestMeasurement"] = str(get_feature_value(race_data, "ChestMeasurement", 0, std_dev=2.5))
    appearance["WaistSize"] = str(get_feature_value(race_data, "WaistSize", 0, std_dev=2.5))
    appearance["ArmSize"] = str(get_feature_value(race_data, "ArmSize", 0, std_dev=2.5))
    appearance["ThighSize"] = str(get_feature_value(race_data, "ThighSize", 0, std_dev=2.5))
    appearance["CalfSize"] = str(get_feature_value(race_data, "CalfSize", 0, std_dev=2.5))
    appearance["LegLength"] = str(get_feature_value(race_data, "LegLength", 0, std_dev=2.5))
    appearance["ArmLength"] = str(get_feature_value(race_data, "ArmLength", 0, std_dev=2.5))
    appearance["SkinColour"] = str(skin_colour)

    # Head
    appearance["HeadLength"] = str(get_feature_value(race_data, "HeadLength", 0, std_dev=2.5))
    appearance["HeadWidth"] = str(get_feature_value(race_data, "HeadWidth", 0, std_dev=2.5))
    appearance["HeadDepth"] = str(get_feature_value(race_data, "HeadDepth", 0, std_dev=2.5))
    appearance["FaceHeight"] = str(get_feature_value(race_data, "FaceHeight", 0, std_dev=2.5))
    appearance["FaceSize"] = str(get_feature_value(race_data, "FaceSize", 0, std_dev=2.5))

    # Face Features - pass race_data to all sub-functions
    appearance.update(generate_eye_features(race_data, skin_colour))
    appearance.update(generate_eyebrow_features(race_data, skin_colour))
    appearance.update(generate_nose_features(race_data, skin_colour))
    appearance.update(generate_mouth_features(race_data, skin_colour))
    appearance.update(generate_facial_hair_features(race_data, skin_colour))
    appearance.update(generate_jaw_features(race_data, skin_colour))
    appearance.update(generate_ear_features(race_data, skin_colour))
    appearance.update(generate_hair_features(race_data, skin_colour))

    # Strip / Gear
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

    # Misc value padding
    for i in range(1, 20):
        appearance[f"ValueAp{i}"] = "0"

    return appearance

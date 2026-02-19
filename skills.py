import random

# Lista de todos los skills disponibles en PES 2021
ALL_SKILLS = [
    "Trickster", "MazingRun", "SpeedingBullet", "IncisiveRun", "LongBallExpert",
    "EarlyCross", "LongRanger", "ScissorsFeint", "DoubleTouch", "FlipFlap",
    "MarseilleTurn", "Sombrero", "CrossOverTurn", "CutBehindAndTurn", "ScotchMove",
    "StepOnSkillcontrol", "HeadingSpecial", "LongRangeDrive", "Chipshotcontrol",
    "LongRangeShot", "KnuckleShot", "DippingShots", "RisingShots", "AcrobaticFinishing",
    "HeelTrick", "FirstTimeShot", "OneTouchPass", "ThroughPassing", "WeightedPass",
    "PinpointCrossing", "OutsideCurler", "Rabona", "NoLookPass", "LowLoftedPass",
    "GKLowPunt", "GKHighPunt", "LongThrow", "GKLongThrow", "PenaltySpecialist",
    "GKPenaltySaver", "Gamesmanship", "ManMarking", "TrackBack", "Interception",
    "AcrobaticClear", "Captaincy", "SuperSub", "FightingSpirit"
]

# Probabilities of getting each skill by position
# ALL skills are in each position, only varying in probability
def get_base_probabilities(position):
    
    return {
        "GK": {
            "Trickster": 0.05, "MazingRun": 0.05, "SpeedingBullet": 0.05, "IncisiveRun": 0.05,
            "LongBallExpert": 0.15, "EarlyCross": 0.05, "LongRanger": 0.05, "ScissorsFeint": 0.05,
            "DoubleTouch": 0.05, "FlipFlap": 0.05, "MarseilleTurn": 0.05, "Sombrero": 0.05,
            "CrossOverTurn": 0.05, "CutBehindAndTurn": 0.05, "ScotchMove": 0.05, "StepOnSkillcontrol": 0.05,
            "HeadingSpecial": 0.05, "LongRangeDrive": 0.05, "Chipshotcontrol": 0.05, "LongRangeShot": 0.05,
            "KnuckleShot": 0.05, "DippingShots": 0.05, "RisingShots": 0.05, "AcrobaticFinishing": 0.05,
            "HeelTrick": 0.05, "FirstTimeShot": 0.05, "OneTouchPass": 0.10, "ThroughPassing": 0.05,
            "WeightedPass": 0.10, "PinpointCrossing": 0.05, "OutsideCurler": 0.05, "Rabona": 0.05,
            "NoLookPass": 0.05, "LowLoftedPass": 0.05, "GKLowPunt": 0.85, "GKHighPunt": 0.85,
            "LongThrow": 0.30, "GKLongThrow": 0.80, "PenaltySpecialist": 0.05, "GKPenaltySaver": 0.70,
            "Gamesmanship": 0.05, "ManMarking": 0.25, "TrackBack": 0.20, "Interception": 0.50,
            "AcrobaticClear": 0.60, "Captaincy": 0.30, "SuperSub": 0.15, "FightingSpirit": 0.35,
        },
        "CB": {
            "Trickster": 0.05, "MazingRun": 0.05, "SpeedingBullet": 0.05, "IncisiveRun": 0.05,
            "LongBallExpert": 0.15, "EarlyCross": 0.05, "LongRanger": 0.05, "ScissorsFeint": 0.05,
            "DoubleTouch": 0.10, "FlipFlap": 0.05, "MarseilleTurn": 0.05, "Sombrero": 0.05,
            "CrossOverTurn": 0.05, "CutBehindAndTurn": 0.05, "ScotchMove": 0.05, "StepOnSkillcontrol": 0.05,
            "HeadingSpecial": 0.65, "LongRangeDrive": 0.05, "Chipshotcontrol": 0.05, "LongRangeShot": 0.05,
            "KnuckleShot": 0.05, "DippingShots": 0.05, "RisingShots": 0.05, "AcrobaticFinishing": 0.05,
            "HeelTrick": 0.05, "FirstTimeShot": 0.05, "OneTouchPass": 0.10, "ThroughPassing": 0.05,
            "WeightedPass": 0.10, "PinpointCrossing": 0.05, "OutsideCurler": 0.05, "Rabona": 0.05,
            "NoLookPass": 0.05, "LowLoftedPass": 0.05, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.15, "GKLongThrow": 0.05, "PenaltySpecialist": 0.05, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.10, "ManMarking": 0.65, "TrackBack": 0.50, "Interception": 0.75,
            "AcrobaticClear": 0.55, "Captaincy": 0.35, "SuperSub": 0.15, "FightingSpirit": 0.45,
        },
        "LB": {
            "Trickster": 0.10, "MazingRun": 0.15, "SpeedingBullet": 0.45, "IncisiveRun": 0.20,
            "LongBallExpert": 0.15, "EarlyCross": 0.50, "LongRanger": 0.05, "ScissorsFeint": 0.10,
            "DoubleTouch": 0.35, "FlipFlap": 0.15, "MarseilleTurn": 0.10, "Sombrero": 0.05,
            "CrossOverTurn": 0.15, "CutBehindAndTurn": 0.15, "ScotchMove": 0.05, "StepOnSkillcontrol": 0.10,
            "HeadingSpecial": 0.15, "LongRangeDrive": 0.05, "Chipshotcontrol": 0.05, "LongRangeShot": 0.05,
            "KnuckleShot": 0.05, "DippingShots": 0.05, "RisingShots": 0.05, "AcrobaticFinishing": 0.10,
            "HeelTrick": 0.10, "FirstTimeShot": 0.15, "OneTouchPass": 0.20, "ThroughPassing": 0.15,
            "WeightedPass": 0.20, "PinpointCrossing": 0.25, "OutsideCurler": 0.15, "Rabona": 0.10,
            "NoLookPass": 0.10, "LowLoftedPass": 0.10, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.20, "GKLongThrow": 0.05, "PenaltySpecialist": 0.05, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.10, "ManMarking": 0.65, "TrackBack": 0.55, "Interception": 0.55,
            "AcrobaticClear": 0.40, "Captaincy": 0.20, "SuperSub": 0.15, "FightingSpirit": 0.35,
        },
        "RB": {
            "Trickster": 0.10, "MazingRun": 0.15, "SpeedingBullet": 0.45, "IncisiveRun": 0.20,
            "LongBallExpert": 0.15, "EarlyCross": 0.50, "LongRanger": 0.05, "ScissorsFeint": 0.10,
            "DoubleTouch": 0.35, "FlipFlap": 0.15, "MarseilleTurn": 0.10, "Sombrero": 0.05,
            "CrossOverTurn": 0.15, "CutBehindAndTurn": 0.15, "ScotchMove": 0.05, "StepOnSkillcontrol": 0.10,
            "HeadingSpecial": 0.15, "LongRangeDrive": 0.05, "Chipshotcontrol": 0.05, "LongRangeShot": 0.05,
            "KnuckleShot": 0.05, "DippingShots": 0.05, "RisingShots": 0.05, "AcrobaticFinishing": 0.10,
            "HeelTrick": 0.10, "FirstTimeShot": 0.15, "OneTouchPass": 0.20, "ThroughPassing": 0.15,
            "WeightedPass": 0.20, "PinpointCrossing": 0.25, "OutsideCurler": 0.15, "Rabona": 0.10,
            "NoLookPass": 0.10, "LowLoftedPass": 0.10, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.20, "GKLongThrow": 0.05, "PenaltySpecialist": 0.05, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.10, "ManMarking": 0.65, "TrackBack": 0.55, "Interception": 0.55,
            "AcrobaticClear": 0.40, "Captaincy": 0.20, "SuperSub": 0.15, "FightingSpirit": 0.35,
        },
        "DMF": {
            "Trickster": 0.10, "MazingRun": 0.10, "SpeedingBullet": 0.15, "IncisiveRun": 0.10,
            "LongBallExpert": 0.55, "EarlyCross": 0.10, "LongRanger": 0.15, "ScissorsFeint": 0.05,
            "DoubleTouch": 0.15, "FlipFlap": 0.05, "MarseilleTurn": 0.05, "Sombrero": 0.05,
            "CrossOverTurn": 0.05, "CutBehindAndTurn": 0.05, "ScotchMove": 0.05, "StepOnSkillcontrol": 0.05,
            "HeadingSpecial": 0.10, "LongRangeDrive": 0.10, "Chipshotcontrol": 0.05, "LongRangeShot": 0.10,
            "KnuckleShot": 0.05, "DippingShots": 0.05, "RisingShots": 0.05, "AcrobaticFinishing": 0.05,
            "HeelTrick": 0.05, "FirstTimeShot": 0.10, "OneTouchPass": 0.50, "ThroughPassing": 0.45,
            "WeightedPass": 0.45, "PinpointCrossing": 0.20, "OutsideCurler": 0.15, "Rabona": 0.15,
            "NoLookPass": 0.15, "LowLoftedPass": 0.15, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.15, "GKLongThrow": 0.05, "PenaltySpecialist": 0.05, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.15, "ManMarking": 0.55, "TrackBack": 0.55, "Interception": 0.75,
            "AcrobaticClear": 0.35, "Captaincy": 0.40, "SuperSub": 0.15, "FightingSpirit": 0.45,
        },
        "CMF": {
            "Trickster": 0.20, "MazingRun": 0.20, "SpeedingBullet": 0.20, "IncisiveRun": 0.20,
            "LongBallExpert": 0.60, "EarlyCross": 0.15, "LongRanger": 0.20, "ScissorsFeint": 0.10,
            "DoubleTouch": 0.25, "FlipFlap": 0.15, "MarseilleTurn": 0.10, "Sombrero": 0.05,
            "CrossOverTurn": 0.10, "CutBehindAndTurn": 0.10, "ScotchMove": 0.05, "StepOnSkillcontrol": 0.10,
            "HeadingSpecial": 0.15, "LongRangeDrive": 0.15, "Chipshotcontrol": 0.10, "LongRangeShot": 0.15,
            "KnuckleShot": 0.10, "DippingShots": 0.10, "RisingShots": 0.10, "AcrobaticFinishing": 0.15,
            "HeelTrick": 0.10, "FirstTimeShot": 0.25, "OneTouchPass": 0.70, "ThroughPassing": 0.60,
            "WeightedPass": 0.55, "PinpointCrossing": 0.30, "OutsideCurler": 0.25, "Rabona": 0.35,
            "NoLookPass": 0.30, "LowLoftedPass": 0.25, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.15, "GKLongThrow": 0.05, "PenaltySpecialist": 0.15, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.20, "ManMarking": 0.40, "TrackBack": 0.50, "Interception": 0.50,
            "AcrobaticClear": 0.25, "Captaincy": 0.40, "SuperSub": 0.20, "FightingSpirit": 0.40,
        },
        "LMF": {
            "Trickster": 0.60, "MazingRun": 0.55, "SpeedingBullet": 0.55, "IncisiveRun": 0.45,
            "LongBallExpert": 0.25, "EarlyCross": 0.60, "LongRanger": 0.25, "ScissorsFeint": 0.20,
            "DoubleTouch": 0.55, "FlipFlap": 0.50, "MarseilleTurn": 0.40, "Sombrero": 0.30,
            "CrossOverTurn": 0.35, "CutBehindAndTurn": 0.35, "ScotchMove": 0.20, "StepOnSkillcontrol": 0.25,
            "HeadingSpecial": 0.10, "LongRangeDrive": 0.20, "Chipshotcontrol": 0.15, "LongRangeShot": 0.20,
            "KnuckleShot": 0.15, "DippingShots": 0.15, "RisingShots": 0.15, "AcrobaticFinishing": 0.30,
            "HeelTrick": 0.20, "FirstTimeShot": 0.40, "OneTouchPass": 0.35, "ThroughPassing": 0.30,
            "WeightedPass": 0.35, "PinpointCrossing": 0.55, "OutsideCurler": 0.40, "Rabona": 0.25,
            "NoLookPass": 0.25, "LowLoftedPass": 0.20, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.15, "GKLongThrow": 0.05, "PenaltySpecialist": 0.10, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.10, "ManMarking": 0.30, "TrackBack": 0.40, "Interception": 0.35,
            "AcrobaticClear": 0.20, "Captaincy": 0.15, "SuperSub": 0.20, "FightingSpirit": 0.30,
        },
        "RMF": {
            "Trickster": 0.60, "MazingRun": 0.55, "SpeedingBullet": 0.55, "IncisiveRun": 0.45,
            "LongBallExpert": 0.25, "EarlyCross": 0.60, "LongRanger": 0.25, "ScissorsFeint": 0.20,
            "DoubleTouch": 0.55, "FlipFlap": 0.50, "MarseilleTurn": 0.40, "Sombrero": 0.30,
            "CrossOverTurn": 0.35, "CutBehindAndTurn": 0.35, "ScotchMove": 0.20, "StepOnSkillcontrol": 0.25,
            "HeadingSpecial": 0.10, "LongRangeDrive": 0.20, "Chipshotcontrol": 0.15, "LongRangeShot": 0.20,
            "KnuckleShot": 0.15, "DippingShots": 0.15, "RisingShots": 0.15, "AcrobaticFinishing": 0.30,
            "HeelTrick": 0.20, "FirstTimeShot": 0.40, "OneTouchPass": 0.35, "ThroughPassing": 0.30,
            "WeightedPass": 0.35, "PinpointCrossing": 0.55, "OutsideCurler": 0.40, "Rabona": 0.25,
            "NoLookPass": 0.25, "LowLoftedPass": 0.20, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.15, "GKLongThrow": 0.05, "PenaltySpecialist": 0.10, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.10, "ManMarking": 0.30, "TrackBack": 0.40, "Interception": 0.35,
            "AcrobaticClear": 0.20, "Captaincy": 0.15, "SuperSub": 0.20, "FightingSpirit": 0.30,
        },
        "AMF": {
            "Trickster": 0.50, "MazingRun": 0.45, "SpeedingBullet": 0.30, "IncisiveRun": 0.40,
            "LongBallExpert": 0.40, "EarlyCross": 0.25, "LongRanger": 0.30, "ScissorsFeint": 0.20,
            "DoubleTouch": 0.45, "FlipFlap": 0.35, "MarseilleTurn": 0.25, "Sombrero": 0.20,
            "CrossOverTurn": 0.25, "CutBehindAndTurn": 0.25, "ScotchMove": 0.15, "StepOnSkillcontrol": 0.20,
            "HeadingSpecial": 0.15, "LongRangeDrive": 0.25, "Chipshotcontrol": 0.20, "LongRangeShot": 0.25,
            "KnuckleShot": 0.20, "DippingShots": 0.20, "RisingShots": 0.20, "AcrobaticFinishing": 0.35,
            "HeelTrick": 0.20, "FirstTimeShot": 0.50, "OneTouchPass": 0.60, "ThroughPassing": 0.60,
            "WeightedPass": 0.50, "PinpointCrossing": 0.40, "OutsideCurler": 0.35, "Rabona": 0.40,
            "NoLookPass": 0.35, "LowLoftedPass": 0.30, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.15, "GKLongThrow": 0.05, "PenaltySpecialist": 0.20, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.20, "ManMarking": 0.30, "TrackBack": 0.35, "Interception": 0.40,
            "AcrobaticClear": 0.20, "Captaincy": 0.25, "SuperSub": 0.25, "FightingSpirit": 0.35,
        },
        "LWF": {
            "Trickster": 0.70, "MazingRun": 0.65, "SpeedingBullet": 0.65, "IncisiveRun": 0.60,
            "LongBallExpert": 0.20, "EarlyCross": 0.55, "LongRanger": 0.35, "ScissorsFeint": 0.25,
            "DoubleTouch": 0.65, "FlipFlap": 0.60, "MarseilleTurn": 0.55, "Sombrero": 0.40,
            "CrossOverTurn": 0.45, "CutBehindAndTurn": 0.45, "ScotchMove": 0.25, "StepOnSkillcontrol": 0.30,
            "HeadingSpecial": 0.20, "LongRangeDrive": 0.25, "Chipshotcontrol": 0.20, "LongRangeShot": 0.25,
            "KnuckleShot": 0.20, "DippingShots": 0.20, "RisingShots": 0.20, "AcrobaticFinishing": 0.45,
            "HeelTrick": 0.30, "FirstTimeShot": 0.55, "OneTouchPass": 0.30, "ThroughPassing": 0.25,
            "WeightedPass": 0.30, "PinpointCrossing": 0.60, "OutsideCurler": 0.45, "Rabona": 0.30,
            "NoLookPass": 0.25, "LowLoftedPass": 0.20, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.10, "GKLongThrow": 0.05, "PenaltySpecialist": 0.15, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.15, "ManMarking": 0.20, "TrackBack": 0.30, "Interception": 0.25,
            "AcrobaticClear": 0.15, "Captaincy": 0.10, "SuperSub": 0.20, "FightingSpirit": 0.25,
        },
        "RWF": {
            "Trickster": 0.70, "MazingRun": 0.65, "SpeedingBullet": 0.65, "IncisiveRun": 0.60,
            "LongBallExpert": 0.20, "EarlyCross": 0.55, "LongRanger": 0.35, "ScissorsFeint": 0.25,
            "DoubleTouch": 0.65, "FlipFlap": 0.60, "MarseilleTurn": 0.55, "Sombrero": 0.40,
            "CrossOverTurn": 0.45, "CutBehindAndTurn": 0.45, "ScotchMove": 0.25, "StepOnSkillcontrol": 0.30,
            "HeadingSpecial": 0.20, "LongRangeDrive": 0.25, "Chipshotcontrol": 0.20, "LongRangeShot": 0.25,
            "KnuckleShot": 0.20, "DippingShots": 0.20, "RisingShots": 0.20, "AcrobaticFinishing": 0.45,
            "HeelTrick": 0.30, "FirstTimeShot": 0.55, "OneTouchPass": 0.30, "ThroughPassing": 0.25,
            "WeightedPass": 0.30, "PinpointCrossing": 0.60, "OutsideCurler": 0.45, "Rabona": 0.30,
            "NoLookPass": 0.25, "LowLoftedPass": 0.20, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.10, "GKLongThrow": 0.05, "PenaltySpecialist": 0.15, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.15, "ManMarking": 0.20, "TrackBack": 0.30, "Interception": 0.25,
            "AcrobaticClear": 0.15, "Captaincy": 0.10, "SuperSub": 0.20, "FightingSpirit": 0.25,
        },
        "SS": {
            "Trickster": 0.55, "MazingRun": 0.50, "SpeedingBullet": 0.40, "IncisiveRun": 0.50,
            "LongBallExpert": 0.30, "EarlyCross": 0.20, "LongRanger": 0.40, "ScissorsFeint": 0.20,
            "DoubleTouch": 0.50, "FlipFlap": 0.40, "MarseilleTurn": 0.30, "Sombrero": 0.25,
            "CrossOverTurn": 0.30, "CutBehindAndTurn": 0.30, "ScotchMove": 0.20, "StepOnSkillcontrol": 0.25,
            "HeadingSpecial": 0.30, "LongRangeDrive": 0.30, "Chipshotcontrol": 0.25, "LongRangeShot": 0.30,
            "KnuckleShot": 0.25, "DippingShots": 0.25, "RisingShots": 0.25, "AcrobaticFinishing": 0.50,
            "HeelTrick": 0.30, "FirstTimeShot": 0.65, "OneTouchPass": 0.40, "ThroughPassing": 0.35,
            "WeightedPass": 0.40, "PinpointCrossing": 0.30, "OutsideCurler": 0.25, "Rabona": 0.35,
            "NoLookPass": 0.30, "LowLoftedPass": 0.25, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.10, "GKLongThrow": 0.05, "PenaltySpecialist": 0.25, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.15, "ManMarking": 0.20, "TrackBack": 0.25, "Interception": 0.30,
            "AcrobaticClear": 0.15, "Captaincy": 0.20, "SuperSub": 0.25, "FightingSpirit": 0.35,
        },
        "CF": {
            "Trickster": 0.40, "MazingRun": 0.35, "SpeedingBullet": 0.35, "IncisiveRun": 0.45,
            "LongBallExpert": 0.15, "EarlyCross": 0.10, "LongRanger": 0.35, "ScissorsFeint": 0.15,
            "DoubleTouch": 0.35, "FlipFlap": 0.30, "MarseilleTurn": 0.25, "Sombrero": 0.20,
            "CrossOverTurn": 0.25, "CutBehindAndTurn": 0.25, "ScotchMove": 0.15, "StepOnSkillcontrol": 0.20,
            "HeadingSpecial": 0.65, "LongRangeDrive": 0.30, "Chipshotcontrol": 0.25, "LongRangeShot": 0.30,
            "KnuckleShot": 0.25, "DippingShots": 0.25, "RisingShots": 0.25, "AcrobaticFinishing": 0.60,
            "HeelTrick": 0.35, "FirstTimeShot": 0.70, "OneTouchPass": 0.30, "ThroughPassing": 0.25,
            "WeightedPass": 0.30, "PinpointCrossing": 0.20, "OutsideCurler": 0.15, "Rabona": 0.25,
            "NoLookPass": 0.20, "LowLoftedPass": 0.15, "GKLowPunt": 0.05, "GKHighPunt": 0.05,
            "LongThrow": 0.10, "GKLongThrow": 0.05, "PenaltySpecialist": 0.35, "GKPenaltySaver": 0.05,
            "Gamesmanship": 0.10, "ManMarking": 0.15, "TrackBack": 0.20, "Interception": 0.25,
            "AcrobaticClear": 0.10, "Captaincy": 0.15, "SuperSub": 0.30, "FightingSpirit": 0.40,
        },
    }.get(position, {skill: 0.15 for skill in ALL_SKILLS})


# How many skills will it get based on the rating
def get_num_skills_by_rating(rating):
    # APROX
    # 95+: 8-10
    # 90-95: 7-10
    # 80-90: 5-8
    # 70-80: 1-4
    # 60-70: 1, 2
    # 50-60: 1
    # -50: 1
    if rating is None:
        rating = 60
    
    if rating < 50:
        skills_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        weights = [0.85, 0.10, 0.03, 0.01, 0.005, 0.003, 0.001, 0.0005, 0.0003, 0.0001, 0.0001]
    elif rating < 60:
        skills_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        weights = [0.60, 0.25, 0.10, 0.03, 0.01, 0.005, 0.003, 0.001, 0.0005, 0.0003, 0.0002]
    elif rating < 70:
        skills_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        weights = [0.35, 0.30, 0.20, 0.10, 0.03, 0.01, 0.005, 0.003, 0.001, 0.0005, 0.0005]
    elif rating < 80:
        skills_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        weights = [0.15, 0.20, 0.20, 0.20, 0.12, 0.08, 0.03, 0.01, 0.005, 0.003, 0.002]
    elif rating < 90:
        skills_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        weights = [0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.15, 0.10, 0.03, 0.01, 0.01]
    elif rating < 95:
        skills_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        weights = [0.03, 0.05, 0.07, 0.08, 0.10, 0.12, 0.15, 0.20, 0.12, 0.05, 0.03]
    else:  # 95+
        skills_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        weights = [0.01, 0.02, 0.03, 0.04, 0.05, 0.08, 0.10, 0.15, 0.22, 0.20, 0.10]

    return random.choices(skills_options, weights=weights)[0]


def generate_skills(position, rating=None):
    # Porbabilities by position
    position_probs = get_base_probabilities(position)
    
    # Number of skills gained
    target_num_skills = get_num_skills_by_rating(rating)
    
    selected_skills = []
    for skill in ALL_SKILLS:
        probability = position_probs.get(skill, 0.05)
        if random.random() < probability:
            selected_skills.append(skill)
    
    if len(selected_skills) < target_num_skills:
        remaining = target_num_skills - len(selected_skills)
        available = [s for s in ALL_SKILLS if s not in selected_skills]
        if available:
            selected_skills.extend(random.sample(available, min(remaining, len(available))))
    
    elif len(selected_skills) > target_num_skills:
        selected_skills = random.sample(selected_skills, target_num_skills)
    
    result = {}
    for skill in ALL_SKILLS:
        result[skill] = "True" if skill in selected_skills else "False"
    
    return result


import json
import os
import csv
from main import PlayerGenerator

PLAYER_COLUMNS = [
    "Id", "Name", "JapName", "Shirt", "ShirtNational", "Commentary", "Country", "Country2",
    "Height", "Weight", "Age", "Foot", "PlayingStyle", "POS", "GK", "CB", "LB", "RB", "DMF",
    "CMF", "LMF", "RMF", "AMF", "LWF", "RWF", "SS", "CF", "OffensiveAwareness", "BallControl",
    "Dribbling", "TightPossession", "LowPass", "LoftedPass", "Finishing", "Heading",
    "PlaceKicking", "Curl", "Speed", "Acceleration", "KickingPower", "Jump", "PhysicalContact",
    "Balance", "Stamina", "DefensiveAwareness", "BallWinning", "Aggression", "GKAwareness",
    "GKCatching", "GKClearing", "GKReflexes", "GKReach", "WeakFootUsage", "WeakFootAcc",
    "Form", "InjuryResistance", "Reputation", "PlayingAttitude", "Trickster", "MazingRun",
    "SpeedingBullet", "IncisiveRun", "LongBallExpert", "EarlyCross", "LongRanger",
    "ScissorsFeint", "DoubleTouch", "FlipFlap", "MarseilleTurn", "Sombrero", "CrossOverTurn",
    "CutBehindAndTurn", "ScotchMove", "StepOnSkillcontrol", "HeadingSpecial", "LongRangeDrive",
    "Chipshotcontrol", "LongRangeShot", "KnuckleShot", "DippingShots", "RisingShots",
    "AcrobaticFinishing", "HeelTrick", "FirstTimeShot", "OneTouchPass", "ThroughPassing",
    "WeightedPass", "PinpointCrossing", "OutsideCurler", "Rabona", "NoLookPass", "LowLoftedPass",
    "GKLowPunt", "GKHighPunt", "LongThrow", "GKLongThrow", "PenaltySpecialist", "GKPenaltySaver",
    "Gamesmanship", "ManMarking", "TrackBack", "Interception", "AcrobaticClear", "Captaincy",
    "SuperSub", "FightingSpirit", "Celebration1", "Celebration2", "DribblingHunching",
    "DribblingArmMove.", "RunningHunching", "RunningArmMovement", "CornerKicks", "FreeKicks",
    "PenaltyKick", "DribbleMotion", "YouthClub", "OwnerClub", "ContractUntil", "LoanUntil",
    "MarketValue", "NationalCaps", "Legend", "Hand", "WinnerGoldenBall", "EditName",
    "EditBasics", "EditPosition", "EditPositions", "EditAbilities", "EditPlayerSkills",
    "EditPlayingStyle", "EditCOMPlayingStyles", "EditMovements", "Edit1", "Edit2", "Edit3",
    "Edit4", "Edit5", "Edit6", "Edit7", "Value1", "Value2", "Value3", "Value2020_1",
    "Value2020_2", "Appearance", "ListBoots", "ListGloves", "InEditFile", "OverallStats",
    "NeckLength", "NeckSize", "ShoulderHeight", "ShoulderWidth", "ChestMeasurement", "WaistSize",
    "ArmSize", "ThighSize", "CalfSize", "LegLength", "ArmLength", "SkinColour", "HeadLength",
    "HeadWidth", "HeadDepth", "FaceHeight", "FaceSize", "UpperEyelidType", "BottomEyelidType",
    "EyeHeight", "HorizontalEyePosition", "IrisColour", "PupilSize", "UpperEyelidHt.(Inner)",
    "UpperEyelidWd.(Inner)", "UpperEyelidHt.(Outer)", "UpperEyelidWd.(Outer)", "InnerEyeHeight",
    "InnerEyePosition", "EyeCornerHeight", "OuterEyePosition", "BottomEyelidHeight", "EyeDepth",
    "Forehead", "EyebrowType", "EyebrowThickness", "EyebrowStyle", "EyebrowDensity",
    "EyebrowColourR", "EyebrowColourG", "EyebrowColourB", "InnerEyebrowHeight", "BrowWidth",
    "OuterEdyebrowHeight", "TempleWidth", "EyebrowDepth", "NoseType", "LaughterLines",
    "NoseHeight", "NostrilWidth", "NoseWidth", "NoseTipDepth", "NoseDepth", "UpperLipType",
    "LowerLipType", "MouthPosition", "LipSize", "LipWidth", "MouthCornerHeight", "MouthDepth",
    "FacialHairType", "FacialHairColourR", "FacialHairColourG", "FacialHairColourB", "Thickness",
    "CheekType", "NeckLineType", "Cheekbones", "ChinHeight", "ChinWidth", "JawHeight", "Jawline",
    "ChinDepth", "EarLength", "EarWidth", "EarAngle", "Overall-Style", "Overall-Length",
    "Overall-WaveLevel", "Overall-HairVariation", "Font-Style", "Font-Parted", "Font-Hairline",
    "Font-ForeheadWidth", "Side/Back-Style", "Side/Back-Cropped", "HairColourR", "HairColourG",
    "HairColourB", "AccessoryColour", "HairColour", "Accessories", "Wristtaping",
    "WristTapeColour1", "WristTapeColour2", "AnkleTaping", "PlayerGloves", "Colour",
    "Undershorts", "Sleeves", "Shirttail", "SockLength", "Long-SleevedInners", "ValueAp1",
    "ValueAp2", "ValueAp3", "ValueAp4", "ValueAp5", "ValueAp6", "ValueAp7", "ValueAp8",
    "ValueAp9", "ValueAp10", "ValueAp11", "ValueAp12", "ValueAp13", "ValueAp14", "ValueAp15",
    "ValueAp16", "ValueAp17", "ValueAp18", "ValueAp19", "IdFace", "Boots", "Gloves", "EditFace",
    "EditHair", "EditPhysique", "EditStrip", "ValueA"
]

# JSON: Unique for each player
def generate_team(team_name, players_list, generator):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    teams_dir = os.path.join(current_dir, "Teams")
    team_folder = os.path.join(teams_dir, team_name)
    os.makedirs(team_folder, exist_ok=True)
    
    for i, player_data in enumerate(players_list, 1):
        player = generator.generate_player(**player_data)
        
        filename = f"{i:02d}_{player_data['Name']}_{player_data['Position']}.json"
        filepath = os.path.join(team_folder, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(player, f, ensure_ascii=False, indent=2)
    
    print(f"{team_name}: {len(players_list)} players generated in {team_folder}")

# CSV: Full team
def generate_team_csv(team_name, players_list, generator):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    teams_dir = os.path.join(current_dir, "Teams")
    # team_folder = os.path.join(teams_dir, team_name)
    # os.makedirs(team_folder, exist_ok=True)
    os.makedirs(teams_dir, exist_ok=True)

    filename = f"{team_name}.csv"
    filepath = os.path.join(teams_dir, filename)

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=PLAYER_COLUMNS, extrasaction='ignore', delimiter=';')
        writer.writeheader()
        for player_data in players_list:
            player = generator.generate_player(**player_data)
            writer.writerow(player)

    print(f"{team_name}: {len(players_list)} players generated in {filename}")

# Generate CSV with multiple teams
def generate_teams_csv(teams_data, generator):
    for team_name, players_list in teams_data.items():
        generate_team_csv(team_name, players_list, generator)

# Execution
if __name__ == "__main__":
    generator = PlayerGenerator()

    # Example team: "Northern Stars FC"
    northern_stars_players = [
        {"Id": "20001", "Name": "Ethan BLACKWOOD", "Position": "GK", "Height": 192, "Country": "Germany", "Rating": 87},
        {"Id": "20002", "Name": "Liam STONEBRIDGE", "Position": "CB", "Height": 188, "Country": "Germany", "Rating": 85},
        {"Id": "20003", "Name": "Noah FROSTBORN", "Position": "CB", "Height": 185, "Country": "Germany", "Rating": 84},
        {"Id": "20004", "Name": "Lucas IRONWOOD", "Position": "RB", "Height": 180, "Country": "Germany", "Rating": 82},
        {"Id": "20005", "Name": "Oliver STORMWIND", "Position": "LB", "Height": 178, "Country": "Germany", "Rating": 83},
        {"Id": "20006", "Name": "James THUNDERCLAP", "Position": "DMF", "Height": 182, "Country": "Germany", "Rating": 86},
        {"Id": "20007", "Name": "Benjamin FLAMEHEART", "Position": "CMF", "Height": 179, "Country": "Germany", "Rating": 88},
        {"Id": "20008", "Name": "Henry STARFALL", "Position": "LMF", "Height": 176, "Country": "Germany", "Rating": 84},
        {"Id": "20009", "Name": "Alexander MOONSHADOW", "Position": "RMF", "Height": 177, "Country": "Germany", "Rating": 85},
        {"Id": "20010", "Name": "Daniel SKYWALKER", "Position": "CF", "Height": 183, "Country": "Germany", "Rating": 89},
        {"Id": "20011", "Name": "Jack FROSTBITE", "Position": "RWF", "Height": 175, "Country": "Germany", "Rating": 86},
        {"Id": "20012", "Name": "William IRONFIST", "Position": "GK", "Height": 190, "Country": "Germany", "Rating": 83},
    ]

    # Generate team in JSON format (one file per player, creates a folder)
    # generate_team("Northern Stars", northern_stars_players, generator)

    # Generate team in CSV format (single file)
    generate_team_csv("Northern Stars CSV", northern_stars_players, generator)

    all_teams = {
        "Northern Stars": northern_stars_players,
        # "Southern Stars": northern_stars_players
    }

    # Generate multiple teams in CSV format (single file)
    generate_teams_csv(all_teams, generator)
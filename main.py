import json
import random
import os
from config import COUNTRY_CODES

from basics import (
    detect_playing_style, generate_id, generate_shirt_name, generate_country_code,
    generate_height, generate_weight, generate_foot, generate_age,
    generate_weak_foot_stats, generate_form, generate_injury_resistance,
    generate_position_code, generate_position_aptitudes, generate_playing_style
)
from abilities import generate_abilities
from skills import generate_skills
from motions import generate_motions
from appearance import generate_appearance


class PlayerGenerator:
    def __init__(self):
        self.position_map = {
            "GK": "0", "CB": "1", "LB": "2", "RB": "3", "DMF": "4",
            "CMF": "5", "LMF": "6", "RMF": "7", "AMF": "8", "LWF": "9",
            "RWF": "10", "SS": "11", "CF": "12"
        }
    
    def generate_player(self, **kwargs):
        """
        Optional Parameters:
        - Name: str
        - Position: str (GK, CB, LB, RB, DMF, CMF, LMF, RMF, AMF, LWF, RWF, SS, CF)
        - Age: int
        - Height: int
        - Weight: int
        - Country: str (numeric code or country name)
        - Foot: str ("Left" o "Right")
        - Rating: int (40-109)
        - PlayingStyle: str
        - Id: str
        
        example:
        player = generator.generate_player(
            Name="Cristiano Ronaldo",
            Position="CF",
            Age=36,
            Height=187,
            Weight=84
        )
        """
        
        position = kwargs.get("Position", random.choice(
            ["GK", "CB", "LB", "RB", "DMF", "CMF", "LMF", "RMF", "AMF", "LWF", "RWF", "SS", "CF"]
        ))
        
        # Basic data
        player_id = kwargs.get("Id", generate_id())
        name = kwargs.get("Name", "UNNAMED")
        shirt_name = kwargs.get("Shirt", generate_shirt_name(name))
        shirt_national = kwargs.get("ShirtNational", generate_shirt_name(name))

        # country = kwargs.get("Country", generate_country_code())
        country_input = kwargs.get("Country", generate_country_code())
        if isinstance(country_input, str) and country_input in COUNTRY_CODES:
            country = COUNTRY_CODES[country_input]
        else:
            country = str(country_input)
        height = kwargs.get("Height", generate_height(position))
        weight = kwargs.get("Weight", generate_weight(height))
        age = kwargs.get("Age", generate_age())
        foot = kwargs.get("Foot", "False" if generate_foot() == False else "True")
        
        weak_foot_usage, weak_foot_acc = kwargs.get("WeakFootStats", generate_weak_foot_stats())
        
        form = kwargs.get("Form", generate_form())
        injury_resistance = kwargs.get("InjuryResistance", generate_injury_resistance())
        
        # Playstiles and positions
        position_code = self.position_map.get(position, "5")
        position_aptitudes = generate_position_aptitudes(position)
        playing_style = kwargs.get("PlayingStyle", generate_playing_style(position))
        
        # Rating
        rating = kwargs.get("Rating", None)
        if rating is None:
            rating = max(109, min(40, random.gauss(70, 25)))
        
        abilities = generate_abilities(position, rating, style=playing_style)

        # Detect the playing style
        detected_style = detect_playing_style(position, abilities)

        playing_style = detected_style
        
        # Skills
        skills = generate_skills(position, rating)
        
        # Motions
        motions = generate_motions()
        
        # Appearance
        appearance = generate_appearance()
        
        # Constructor
        player = {
            "Id": player_id,
            "Name": name,
            "JapName": "name",
            "Shirt": shirt_name,
            "ShirtNational": shirt_national,
            "Commentary": "-1",
            "Country": country,
            "Country2": "0",
            "Height": str(height),
            "Weight": str(weight),
            "Age": str(age),
            "Foot": foot,
            "PlayingStyle": str(playing_style),
            "POS": position_code,
        }
        
        # Add position aptitudes
        player.update(position_aptitudes)
        
        # ABILITIES
        player.update(abilities)
        
        player["WeakFootUsage"] = str(weak_foot_usage)
        player["WeakFootAcc"] = str(weak_foot_acc)
        player["Form"] = str(form)
        player["InjuryResistance"] = str(injury_resistance)
        player["Reputation"] = "4"
        player["PlayingAttitude"] = "1"
        
        player.update(skills)
        
        player.update(motions)
        
        # General data for the editor
        player["YouthClub"] = "0"
        player["OwnerClub"] = "0"
        player["ContractUntil"] = "1/1/0001 12:00:00 AM"
        player["LoanUntil"] = "1/1/0001 12:00:00 AM"
        player["MarketValue"] = "0"
        player["NationalCaps"] = "0"
        player["Legend"] = "False"
        player["Hand"] = "False"
        player["WinnerGoldenBall"] = "False"
        
        # MISC
        misc_fields = [
            "EditName", "EditBasics", "EditPosition", "EditPositions",
            "EditAbilities", "EditPlayerSkills", "EditPlayingStyle",
            "EditCOMPlayingStyles", "EditMovements", "Edit1", "Edit2", "Edit3",
            "Edit4", "Edit5", "Edit6", "Edit7"
        ]
        for field in misc_fields:
            player[field] = "False"
        
        player["Value1"] = "0"
        player["Value2"] = "False"
        player["Value3"] = "-1"
        player["Value2020_1"] = "0"
        player["Value2020_2"] = "0"
        player["Appearance"] = "0"
        player["ListBoots"] = "0"
        player["ListGloves"] = "0"
        player["InEditFile"] = "False"
        player["OverallStats"] = str(rating) if rating else "40"
        
        player.update(appearance)
        player["IdFace"] = "0"
        player["Boots"] = "0"
        player["Gloves"] = "0"
        player["EditFace"] = "False"
        player["EditHair"] = "False"
        player["EditPhysique"] = "False"
        player["EditStrip"] = "False"
        player["ValueA"] = "0"
        
        return player
    
def save_player_json(player, filename="player.json"):
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    jugadores_dir = os.path.join(current_dir, "Players")
    
    if not os.path.exists(jugadores_dir):
        os.makedirs(jugadores_dir)
    
    filepath = os.path.join(jugadores_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(player, f, ensure_ascii=False, indent=2)


def save_team_json(team, filename="team.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(team, f, ensure_ascii=False, indent=2)
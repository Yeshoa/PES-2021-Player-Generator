# PES 2021 Player Generator

Modular player generator for PES 2021 that allows creating players with specific data or automatically generating those that are not specified.

Baldur's gate 3 inspired me for the ability generation, using a dice system to determine the values.

## Structure

- **main.py** - Main generator (PlayerGenerator)
- **basics.py** - Basic data (name, position, height, weight, etc.)
- **abilities.py** - Abilities generator based on position and rating
- **skills.py** - Skill generator (based on position and rating)
- **motions.py** - Motion generator (celebrations, movements, etc.) FULL RANDOM
- **appearance.py** - Physical appearance generator FULL RANDOM (can be customized but it is too much work)

## How to use

### Generating a single player

```python
from main import PlayerGenerator

generator = PlayerGenerator()

# Full random player
player = generator.generate_player()

# Specified data
player = generator.generate_player(
    Name="Cristiano Ronaldo",
    Position="CF", 
    Age=36,
    Height=187,
    Weight=84,
    Country="Portugal"  
)
```

### Save as JSON

```python
from main import save_player_json, save_team_json

save_player_json(player, "my_player.json")
```

### Generate a team in JSON or CSV format

```python
import json
import os
import csv
from main import PlayerGenerator

northern_stars_players = [
    {"Id": "20001", "Name": "Ethan BLACKWOOD", "Position": "GK", "Height": 192, "Country": "Germany", "Rating": 87},
    {"Id": "20002", "Name": "Liam STONEBRIDGE", "Position": "CB", "Height": 188, "Country": "Germany", "Rating": 85},
    # ...
]

generator = PlayerGenerator()

# Generate team in JSON format (one file per player, creates a folder)
generate_team("Northern Stars", northern_stars_players, generator)

# Generate team in CSV format (single file)
generate_team_csv("Northern Stars CSV", northern_stars_players, generator)

# Generate multiple teams in CSV format (single file)
all_teams = {
    "Northern Stars": northern_stars_players,
    # "Southern Stars": southern_stars_players
}
generate_teams_csv(all_teams, generator)

## Available parameters for generate_player()

Actually, any parameter is available

- **Id**: this is mostly used when generating a full team
- **Name**: No idea whats the max length
- **Position**: (GK, CB, LB, RB, DMF, CMF, LMF, RMF, AMF, LWF, RWF, SS, CF)
- **Age**: (15-50)
- **Height**: centimeters (130-210)
- **Weight**: Peso en kg (30-129)
- **Country**: Name or code (see config.py for the full list)
- **Foot**: "Left" o "Right"
- **Rating**: (40-109)
- **PlayingStyle**: See basics.py (0-21)
- **Form**: (1-8)
- **InjuryResistance**: (1-3)
```
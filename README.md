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

save_player_json(player, "mi_jugador.json")
save_team_json(team, "mi_equipo.json")
```

## Available parameters for generate_player()

Actually, any parameter is available

- **Name**: No idea whats the max length
- **Position**: (GK, CB, LB, RB, DMF, CMF, LMF, RMF, AMF, LWF, RWF, SS, CF)
- **Age**: (15-50)
- **Height**: centimeters (130-210)
- **Weight**: Peso en kg (30-129)
- **Country**: Name or code (see config.py for the full list)
- **Foot**: "Left" o "Right"
- **Rating**: (40-109)
- **PlayingStyle**: See basics.py (0-21)
- **Id**: this is mostly used when generating a full team
- **Form**: (1-8)
- **InjuryResistance**: (1-3)
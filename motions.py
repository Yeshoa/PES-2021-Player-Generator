import random

def generate_motions():
    motions = {
        "Celebration1": str(random.randint(0, 152)),
        "Celebration2": str(random.randint(0, 152)),
        "DribblingHunching": str(random.randint(1, 5)),
        "DribblingArmMove.": str(random.randint(1, 10)),
        "RunningHunching": str(random.randint(1, 5)),
        "RunningArmMovement": str(random.randint(1, 10)),
        "CornerKicks": str(random.randint(1, 10)),
        "FreeKicks": str(random.randint(1, 20)),
        "PenaltyKick": str(random.randint(1, 7)),
        "DribbleMotion": str(random.randint(1, 4)),
    }
    return motions

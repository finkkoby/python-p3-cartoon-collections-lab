def roll_call_dwarves(names):
    with_numbers = list(enumerate(names, 1))
    make_strings = [f"{name[0]}. {name[1]}" for name in with_numbers]
    print("\n".join(make_strings))

def summon_captain_planet(calls):
    return [call.capitalize() + "!" for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(strings):
    for string in strings:
        if string in ["cheddar", "gouda", "camembert"]:
            return string
    return None

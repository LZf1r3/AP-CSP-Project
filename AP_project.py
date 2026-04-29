# Volleyball Practice Quest Generator
# Purpose: Create a personalized volleyball practice plan based on skill focus,
# energy level, and available practice time.

drill_names = [
    "Wall Passing Challenge",
    "Target Serving Streak",
    "Approach Footwork Circuit",
    "Block Timing Reps",
    "Pepper Control Rally",
    "Defensive Dive Simulation",
    "Serve Receive Pressure Round",
    "Hitting Accuracy Challenge",
    "Setter Release Speed Drill",
    "Free Ball Transition Drill"
]

drill_skills = [
    "passing",
    "serving",
    "hitting",
    "blocking",
    "passing",
    "defense",
    "passing",
    "hitting",
    "setting",
    "transition"
]

drill_intensity = [
    2,
    3,
    3,
    4,
    4,
    5,
    4,
    5,
    3,
    4
]

drill_time = [
    10,
    15,
    15,
    20,
    20,
    25,
    25,
    30,
    15,
    20
]

drill_points = [
    50,
    80,
    75,
    100,
    90,
    130,
    110,
    150,
    85,
    105
]


def create_practice_quest(skill_focus, energy_level, available_time):
    practice_plan = []
    total_time = 0
    total_points = 0

    for i in range(len(drill_names)):
        skill_matches = drill_skills[i] == skill_focus
        energy_matches = drill_intensity[i] <= energy_level
        time_fits = total_time + drill_time[i] <= available_time

        if skill_matches and energy_matches and time_fits:
            practice_plan.append(drill_names[i])
            total_time = total_time + drill_time[i]
            total_points = total_points + drill_points[i]

    if len(practice_plan) == 0:
        practice_plan.append("Recovery Touches")
        practice_plan.append("Light Mobility Stretch")
        total_time = 15
        total_points = 25

    return practice_plan, total_time, total_points


def get_coach_message(points):
    if points >= 250:
        return "Elite session. This is the kind of practice that actually changes your game."
    elif points >= 150:
        return "Strong session. You trained with purpose today."
    elif points >= 75:
        return "Solid work. Keep stacking these practices."
    else:
        return "Light day, but still better than doing nothing."


print("VOLLEYBALL PRACTICE QUEST GENERATOR")
print("-----------------------------------")
print("Build today's training mission and earn practice points.")

print("\nChoose your skill focus:")
print("passing")
print("serving")
print("hitting")
print("blocking")
print("defense")
print("setting")
print("transition")

focus = input("\nEnter your skill focus: ").lower()
energy = int(input("Enter your energy level from 1 to 5: "))
minutes = int(input("How many minutes do you have to practice? "))

plan, time_used, points = create_practice_quest(focus, energy, minutes)
message = get_coach_message(points)

print("\nTODAY'S PRACTICE QUEST")
print("----------------------")

for drill in plan:
    print("- " + drill)

print("\nTotal practice time: " + str(time_used) + " minutes")
print("Practice points earned: " + str(points))
print("Coach message: " + message)
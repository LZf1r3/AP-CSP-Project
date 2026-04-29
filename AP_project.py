# Volleyball Practice Quest Generator
# Purpose: Create a personalized volleyball practice plan with a warmup,
# skill-based drills, total time, intensity level, and practice points.

import random


# -----------------------------
# WARMUP LISTS
# -----------------------------

warmup_names = [
    "Dynamic Court Movement Warmup",
    "Ball Control Touch Warmup",
    "Partner Pepper Warmup",
    "Serving Rhythm Warmup",
    "Approach and Landing Warmup",
    "Blocking Footwork Warmup",
    "Rotation Walkthrough Warmup",
    "Reaction Shuffle Warmup"
]

warmup_categories = [
    "basics",
    "basics",
    "basics",
    "serving",
    "hitting",
    "blocking",
    "rotation",
    "blocking"
]

warmup_times = [
    8,
    10,
    12,
    8,
    10,
    10,
    12,
    8
]

warmup_descriptions = [
    "Jog lightly around the court, then do high knees, butt kicks, lunges, side shuffles, and arm circles. Focus on preparing your legs, shoulders, and core for volleyball movements.",

    "Start with simple ball-control touches. Pass to yourself, set to yourself, and alternate between passing and setting. Focus on clean contact, balance, and keeping the ball under control.",

    "Work with a partner and pass, set, and lightly attack the ball back and forth. The goal is not power. Focus on control, communication, and adjusting your feet before each contact.",

    "Practice your serving routine without going full power right away. Do slow tosses, shoulder circles, wrist snaps, and a few controlled serves. Focus on rhythm and consistent contact.",

    "Practice your hitting approach at medium speed. Step through your approach, jump off both feet, swing through, and land balanced. Focus on rhythm, safe landing, and arm swing timing.",

    "Start near the net and practice shuffle steps into blocking position. Jump straight up with strong hands, then land balanced. Focus on footwork, timing, and pressing over the net.",

    "Walk through base positions and rotations slowly. Practice where each player should move after serve receive, free balls, and defensive transitions. Focus on court awareness and communication.",

    "Start low in defensive position and react to a partner pointing left, right, forward, or backward. Shuffle quickly, stop balanced, and reset. Focus on fast reaction and controlled movement."
]


# -----------------------------
# DRILL LISTS
# -----------------------------

drill_names = [
    # Basics
    "Wall Passing Challenge",
    "Setter Hands Control",
    "Pass and Set Accuracy Drill",
    "Partner Control Rally",
    "Short Court Basics Game",

    # Serving
    "Target Serving Streak",
    "Deep Zone Serving",
    "Pressure Serve Challenge",
    "Serve Routine Builder",
    "Serve Accuracy Ladder",

    # Hitting
    "Approach Footwork Circuit",
    "Hitting Accuracy Challenge",
    "Line and Cross Shot Drill",
    "Tip and Roll Shot Practice",
    "Transition Attack Drill",

    # Blocking
    "Block Timing Reps",
    "Side Shuffle Block Drill",
    "Read the Hitter Drill",
    "Block and Cover Drill",
    "Double Block Movement Drill",

    # Rotation
    "Rotation Walkthrough Drill",
    "Serve Receive Rotation Drill",
    "Free Ball Transition Drill",
    "Out of System Rotation Drill",
    "Communication Rotation Game"
]

drill_categories = [
    # Basics
    "basics",
    "basics",
    "basics",
    "basics",
    "basics",

    # Serving
    "serving",
    "serving",
    "serving",
    "serving",
    "serving",

    # Hitting
    "hitting",
    "hitting",
    "hitting",
    "hitting",
    "hitting",

    # Blocking
    "blocking",
    "blocking",
    "blocking",
    "blocking",
    "blocking",

    # Rotation
    "rotation",
    "rotation",
    "rotation",
    "rotation",
    "rotation"
]

drill_intensities = [
    # Basics
    2,
    2,
    3,
    3,
    3,

    # Serving
    2,
    3,
    4,
    2,
    3,

    # Hitting
    3,
    5,
    4,
    3,
    5,

    # Blocking
    4,
    3,
    4,
    4,
    5,

    # Rotation
    2,
    3,
    4,
    4,
    5
]

drill_times = [
    # Basics
    10,
    10,
    15,
    20,
    20,

    # Serving
    15,
    15,
    20,
    10,
    15,

    # Hitting
    15,
    25,
    20,
    15,
    25,

    # Blocking
    20,
    15,
    20,
    20,
    25,

    # Rotation
    15,
    20,
    20,
    25,
    30
]

drill_points = [
    # Basics
    50,
    50,
    70,
    85,
    90,

    # Serving
    75,
    80,
    110,
    55,
    85,

    # Hitting
    75,
    150,
    110,
    80,
    150,

    # Blocking
    100,
    80,
    110,
    115,
    140,

    # Rotation
    65,
    90,
    110,
    125,
    150
]

drill_descriptions = [
    # Basics
    "Stand 2 to 3 meters away from a wall and pass the ball repeatedly against it. Keep your platform flat, bend your knees, and try to make the ball return to the same spot every time.",

    "Set the ball to yourself repeatedly while keeping your hands above your forehead. Focus on soft hands, quick release, and keeping the ball centered instead of letting it drift forward or backward.",

    "Work with a partner. One player tosses the ball, and the other must pass or set it to a target. Focus on accuracy, body angle, and making every contact playable.",

    "Play a controlled rally with a partner using only passes and sets. The goal is to keep the ball alive as long as possible while staying balanced and communicating clearly.",

    "Play in a smaller court space using only controlled passes, sets, and light attacks. Focus on placement, communication, and reading your partner instead of trying to overpower the ball.",

    # Serving
    "Choose a target zone and serve repeatedly until you hit the zone several times. Focus on a consistent toss, strong contact, and following through toward your target.",

    "Aim your serves deep into the last meter of the court. Focus on making the serve difficult to pass without serving out. Track how many deep serves land in bounds.",

    "Pretend each serve is at game point. If you miss, restart your streak. Focus on staying calm, using your routine, and serving with confidence under pressure.",

    "Build a consistent serving routine. Bounce the ball, breathe, visualize the target, toss, and serve. Repeat the same routine every time so your serve feels automatic during games.",

    "Start with an easy target, then move to harder zones after each successful serve. Try to climb the ladder by hitting short, deep, left, right, and corner targets.",

    # Hitting
    "Practice your hitting approach without needing a full set. Start in base position, take your approach steps, jump off both feet, swing through, and land balanced.",

    "Set up target zones and practice hitting toward them. Instead of only swinging hard, focus on placing the ball accurately into open areas of the court.",

    "Practice hitting both line and cross-court shots. Focus on changing your shoulder angle and hand contact so you can attack different areas instead of always hitting straight ahead.",

    "Practice controlled attacking shots such as tips, roll shots, and off-speed swings. Focus on reading open space and using smart placement when a full-power hit is not the best choice.",

    "Start in a defensive position, move off the net, transition into your approach, and attack the ball. Focus on switching quickly from defense to offense.",

    # Blocking
    "Stand near the net and practice timing your jump with a hitter or tossed ball. Focus on jumping straight up, pressing your hands over the net, and landing balanced.",

    "Shuffle along the net from one blocking position to another. Stop, square your shoulders, jump, press your hands over, and reset. Focus on fast but controlled footwork.",

    "Watch the hitter's approach and shoulder angle before jumping. Try to predict whether the attack will go line, cross, or tip. Focus on reading instead of guessing randomly.",

    "After blocking, turn around quickly and prepare to cover your hitter or defend the next ball. Focus on not stopping after the block attempt.",

    "Move with a partner as if forming a double block. Communicate the hitter's position, close the gap between blockers, jump together, and land safely.",

    # Rotation
    "Walk through all six rotation positions slowly. Practice where each player starts, where they move after the serve, and how they transition into offense or defense.",

    "Set up in serve receive and practice moving from receive positions into attacking, setting, or defensive roles. Focus on knowing where to go after the pass.",

    "Start with a free ball coming over the net. Pass to the setter area, transition to attack coverage, and reset into defensive base. Focus on team movement.",

    "Practice what happens when the setter takes the first ball or when the pass is bad. Decide who sets the second ball and where hitters should move.",

    "Play a controlled rotation game where players must call their position and responsibility before each ball. Focus on communication, spacing, and avoiding confusion."
]


# -----------------------------
# PROCEDURES
# -----------------------------

def choose_warmup(category):
    possible_warmups = []

    for i in range(len(warmup_names)):
        if warmup_categories[i] == category or warmup_categories[i] == "basics":
            possible_warmups.append(i)

    selected_index = random.choice(possible_warmups)

    return warmup_names[selected_index], warmup_descriptions[selected_index], warmup_times[selected_index]


def create_practice_plan(category, intensity_level, practice_time):
    plan_names = []
    plan_descriptions = []
    total_time = 0
    total_points = 0

    warmup_name, warmup_description, warmup_time = choose_warmup(category)

    plan_names.append(warmup_name)
    plan_descriptions.append(warmup_description)
    total_time = total_time + warmup_time

    for i in range(len(drill_names)):
        category_matches = drill_categories[i] == category
        intensity_matches = drill_intensities[i] <= intensity_level
        time_fits = total_time + drill_times[i] <= practice_time

        if category_matches and intensity_matches and time_fits:
            plan_names.append(drill_names[i])
            plan_descriptions.append(drill_descriptions[i])
            total_time = total_time + drill_times[i]
            total_points = total_points + drill_points[i]

    if len(plan_names) == 1:
        plan_names.append("Simple Technical Review")
        plan_descriptions.append(
            "Use the remaining time to review the basic movement for your chosen category. Keep the intensity low and focus on correct form, control, and consistency."
        )
        total_time = total_time + 10
        total_points = total_points + 25

    return plan_names, plan_descriptions, total_time, total_points


def get_coach_message(points):
    if points >= 350:
        return "Elite practice. This was a serious training session with strong purpose."
    elif points >= 220:
        return "Great practice. You completed a strong session that can actually improve your game."
    elif points >= 120:
        return "Solid practice. You trained with focus and built useful reps."
    else:
        return "Light practice. You still got meaningful touches and stayed consistent."


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("VOLLEYBALL PRACTICE QUEST GENERATOR")
print("-----------------------------------")
print("This program creates a volleyball practice plan with a warmup and main drills.")

print("\nChoose a practice category:")
print("basics")
print("serving")
print("hitting")
print("blocking")
print("rotation")

category_choice = input("\nEnter your category: ").lower()

print("\nChoose your intensity level:")
print("1 = very light")
print("2 = light")
print("3 = medium")
print("4 = hard")
print("5 = very hard")

intensity_choice = int(input("\nEnter intensity from 1 to 5: "))

print("\nChoose your practice length:")
print("30")
print("60")
print("90")
print("120")

time_choice = int(input("\nEnter practice time: "))

while time_choice != 30 and time_choice != 60 and time_choice != 90 and time_choice != 120:
    print("Invalid time. Please choose 30, 60, 90, or 120.")
    time_choice = int(input("Enter practice time: "))

practice_plan, descriptions, time_used, points = create_practice_plan(
    category_choice,
    intensity_choice,
    time_choice
)

coach_message = get_coach_message(points)

print("\nTODAY'S VOLLEYBALL PRACTICE QUEST")
print("---------------------------------")

print("\nINITIAL WARMUP")
print("--------------")
print(practice_plan[0])
print("What to do: " + descriptions[0])

print("\nMAIN DRILLS")
print("-----------")

for i in range(1, len(practice_plan)):
    print("\nDrill " + str(i) + ": " + practice_plan[i])
    print("What to do: " + descriptions[i])

print("\nSESSION SUMMARY")
print("---------------")
print("Practice category: " + category_choice)
print("Selected intensity: " + str(intensity_choice))
print("Selected practice length: " + str(time_choice) + " minutes")
print("Total time used: " + str(time_used) + " minutes")
print("Practice points earned: " + str(points))
print("Coach message: " + coach_message)

print("\nGood luck with practice!")
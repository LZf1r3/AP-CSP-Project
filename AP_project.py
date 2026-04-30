# Volleyball Practice Quest Generator
# This program makes a volleyball practice plan based on what the user chooses - category, intensity, and practice time.
# The user select pre determined options and the program then gives one warmup routine and multiple drills.

import random


# This list stores all the warmups.
# Each warmup has: name, category, time, and description.
warmups = [
    [
        "Dynamic Court Movement Warmup",
        "basics",
        8,
        "Jog lightly around the court, then do high knees, butt kicks, lunges, side shuffles, and arm circles. Focus on preparing your legs, shoulders, and core for volleyball movements."
    ],
    [
        "Ball Control Touch Warmup",
        "basics",
        10,
        "Start with simple ball-control touches. Pass to yourself, set to yourself, and alternate between passing and setting. Focus on clean contact, balance, and keeping the ball under control."
    ],
    [
        "Partner Pepper Warmup",
        "basics",
        12,
        "Work with a partner and pass, set, and lightly attack the ball back and forth. The goal is not power. Focus on control, communication, and adjusting your feet before each contact."
    ],
    [
        "Serving Rhythm Warmup",
        "serving",
        8,
        "Practice your serving routine without going full power right away. Do slow tosses, shoulder circles, wrist snaps, and a few controlled serves. Focus on rhythm and consistent contact."
    ],
    [
        "Approach and Landing Warmup",
        "hitting",
        10,
        "Practice your hitting approach at medium speed. Step through your approach, jump off both feet, swing through, and land balanced. Focus on rhythm, safe landing, and arm swing timing."
    ],
    [
        "Blocking Footwork Warmup",
        "blocking",
        10,
        "Start near the net and practice shuffle steps into blocking position. Jump straight up with strong hands, then land balanced. Focus on footwork, timing, and pressing over the net."
    ],
    [
        "Rotation Walkthrough Warmup",
        "rotation",
        12,
        "Walk through base positions and rotations slowly. Practice where each player should move after serve receive, free balls, and defensive transitions. Focus on court awareness and communication."
    ],
    [
        "Reaction Shuffle Warmup",
        "blocking",
        8,
        "Start low in defensive position and react to a partner pointing left, right, forward, or backward. Shuffle quickly, stop balanced, and reset. Focus on fast reaction and controlled movement."
    ]
]


# This list stores all the drills.
# Each drill has: name, category, intensity, time, points, and description.
drills = [
    [
        "Wall Passing Challenge",
        "basics",
        2,
        10,
        50,
        "Stand 2 to 3 meters away from a wall and pass the ball repeatedly against it. Keep your platform flat, bend your knees, and try to make the ball return to the same spot every time."
    ],
    [
        "Setter Hands Control",
        "basics",
        2,
        10,
        50,
        "Set the ball to yourself repeatedly while keeping your hands above your forehead. Focus on soft hands, quick release, and keeping the ball centered instead of letting it drift forward or backward."
    ],
    [
        "Pass and Set Accuracy Drill",
        "basics",
        3,
        15,
        70,
        "Work with a partner. One player tosses the ball, and the other must pass or set it to a target. Focus on accuracy, body angle, and making every contact playable."
    ],
    [
        "Partner Control Rally",
        "basics",
        3,
        20,
        85,
        "Play a controlled rally with a partner using only passes and sets. The goal is to keep the ball alive as long as possible while staying balanced and communicating clearly."
    ],
    [
        "Short Court Basics Game",
        "basics",
        3,
        20,
        90,
        "Play in a smaller court space using only controlled passes, sets, and light attacks. Focus on placement, communication, and reading your partner instead of trying to overpower the ball."
    ],
    [
        "Target Serving Streak",
        "serving",
        2,
        15,
        75,
        "Choose a target zone and serve repeatedly until you hit the zone several times. Focus on a consistent toss, strong contact, and following through toward your target."
    ],
    [
        "Deep Zone Serving",
        "serving",
        3,
        15,
        80,
        "Aim your serves deep into the last meter of the court. Focus on making the serve difficult to pass without serving out. Track how many deep serves land in bounds."
    ],
    [
        "Pressure Serve Challenge",
        "serving",
        4,
        20,
        110,
        "Pretend each serve is at game point. If you miss, restart your streak. Focus on staying calm, using your routine, and serving with confidence under pressure."
    ],
    [
        "Serve Routine Builder",
        "serving",
        2,
        10,
        55,
        "Build a consistent serving routine. Bounce the ball, breathe, visualize the target, toss, and serve. Repeat the same routine every time so your serve feels automatic during games."
    ],
    [
        "Serve Accuracy Ladder",
        "serving",
        3,
        15,
        85,
        "Start with an easy target, then move to harder zones after each successful serve. Try to climb the ladder by hitting short, deep, left, right, and corner targets."
    ],
    [
        "Approach Footwork Circuit",
        "hitting",
        3,
        15,
        75,
        "Practice your hitting approach without needing a full set. Start in base position, take your approach steps, jump off both feet, swing through, and land balanced."
    ],
    [
        "Hitting Accuracy Challenge",
        "hitting",
        5,
        25,
        150,
        "Set up target zones and practice hitting toward them. Instead of only swinging hard, focus on placing the ball accurately into open areas of the court."
    ],
    [
        "Line and Cross Shot Drill",
        "hitting",
        4,
        20,
        110,
        "Practice hitting both line and cross-court shots. Focus on changing your shoulder angle and hand contact so you can attack different areas instead of always hitting straight ahead."
    ],
    [
        "Tip and Roll Shot Practice",
        "hitting",
        3,
        15,
        80,
        "Practice controlled attacking shots such as tips, roll shots, and off-speed swings. Focus on reading open space and using smart placement when a full-power hit is not the best choice."
    ],
    [
        "Transition Attack Drill",
        "hitting",
        5,
        25,
        150,
        "Start in a defensive position, move off the net, transition into your approach, and attack the ball. Focus on switching quickly from defense to offense."
    ],
    [
        "Block Timing Reps",
        "blocking",
        4,
        20,
        100,
        "Stand near the net and practice timing your jump with a hitter or tossed ball. Focus on jumping straight up, pressing your hands over the net, and landing balanced."
    ],
    [
        "Side Shuffle Block Drill",
        "blocking",
        3,
        15,
        80,
        "Shuffle along the net from one blocking position to another. Stop, square your shoulders, jump, press your hands over, and reset. Focus on fast but controlled footwork."
    ],
    [
        "Read the Hitter Drill",
        "blocking",
        4,
        20,
        110,
        "Watch the hitter's approach and shoulder angle before jumping. Try to predict whether the attack will go line, cross, or tip. Focus on reading instead of guessing randomly."
    ],
    [
        "Block and Cover Drill",
        "blocking",
        4,
        20,
        115,
        "After blocking, turn around quickly and prepare to cover your hitter or defend the next ball. Focus on not stopping after the block attempt."
    ],
    [
        "Double Block Movement Drill",
        "blocking",
        5,
        25,
        140,
        "Move with a partner as if forming a double block. Communicate the hitter's position, close the gap between blockers, jump together, and land safely."
    ],
    [
        "Rotation Walkthrough Drill",
        "rotation",
        2,
        15,
        65,
        "Walk through all six rotation positions slowly. Practice where each player starts, where they move after the serve, and how they transition into offense or defense."
    ],
    [
        "Serve Receive Rotation Drill",
        "rotation",
        3,
        20,
        90,
        "Set up in serve receive and practice moving from receive positions into attacking, setting, or defensive roles. Focus on knowing where to go after the pass."
    ],
    [
        "Free Ball Transition Drill",
        "rotation",
        4,
        20,
        110,
        "Start with a free ball coming over the net. Pass to the setter area, transition to attack coverage, and reset into defensive base. Focus on team movement."
    ],
    [
        "Out of System Rotation Drill",
        "rotation",
        4,
        25,
        125,
        "Practice what happens when the setter takes the first ball or when the pass is bad. Decide who sets the second ball and where hitters should move."
    ],
    [
        "Communication Rotation Game",
        "rotation",
        5,
        30,
        150,
        "Play a controlled rotation game where players must call their position and responsibility before each ball. Focus on communication, spacing, and avoiding confusion."
    ]
]


# This function picks a warmup that matches the user's category.
# Basics warmups can work for any category.
def choose_warmup(category):
    possible_warmups = []

    for warmup in warmups:
        if warmup[1] == category or warmup[1] == "basics":
            possible_warmups.append(warmup)

    chosen_warmup = random.choice(possible_warmups)

    return chosen_warmup


# This function creates the full practice plan.
# It adds a warmup first and then adds drills that fit the category, intensity, and time.
def create_practice_plan(category, intensity_level, practice_time):
    practice_plan = []

    total_time = 0
    total_points = 0

    chosen_warmup = choose_warmup(category)

    practice_plan.append(chosen_warmup)
    total_time = total_time + chosen_warmup[2]

    # This makes the drill order random so the plan changes each time.
    random.shuffle(drills)

    for drill in drills:
        drill_category = drill[1]
        drill_intensity = drill[2]
        drill_time = drill[3]
        drill_points = drill[4]

        category_matches = drill_category == category
        intensity_matches = drill_intensity <= intensity_level
        time_fits = total_time + drill_time <= practice_time

        if category_matches and intensity_matches and time_fits:
            practice_plan.append(drill)
            total_time = total_time + drill_time
            total_points = total_points + drill_points

    # If no drill fits, the program adds a simple review drill.
    if len(practice_plan) == 1:
        simple_review = [
            "Simple Technical Review",
            category,
            1,
            10,
            25,
            "Use the remaining time to review the basic movement for your chosen category. Keep the intensity low and focus on correct form, control, and consistency."
        ]

        practice_plan.append(simple_review)
        total_time = total_time + simple_review[3]
        total_points = total_points + simple_review[4]

    return practice_plan, total_time, total_points


# This function gives feedback based on how many points the practice earned.
def get_coach_message(points):
    if points >= 350:
        return "Elite practice. This was a serious training session with strong purpose."
    elif points >= 220:
        return "Great practice. You completed a strong session that can actually improve your game."
    elif points >= 120:
        return "Solid practice. You trained with focus and built useful reps."
    else:
        return "Light practice. You still got meaningful touches and stayed consistent."


# This function gets a valid category from the user.
def get_category_choice():
    valid_categories = ["basics", "serving", "hitting", "blocking", "rotation"]

    print("\nChoose a practice category:")
    print("basics")
    print("serving")
    print("hitting")
    print("blocking")
    print("rotation")

    category_choice = input("\nEnter your category: ").lower()

    while category_choice not in valid_categories:
        print("Invalid category. Please choose basics, serving, hitting, blocking, or rotation.")
        category_choice = input("Enter your category: ").lower()

    return category_choice


# This function gets a valid intensity level from the user.
def get_intensity_choice():
    print("\nChoose your intensity level:")
    print("1 = very light")
    print("2 = light")
    print("3 = medium")
    print("4 = hard")
    print("5 = very hard")

    intensity_choice = int(input("\nEnter intensity from 1 to 5: "))

    while intensity_choice < 1 or intensity_choice > 5:
        print("Invalid intensity. Please choose a number from 1 to 5.")
        intensity_choice = int(input("Enter intensity from 1 to 5: "))

    return intensity_choice


# This function gets a valid practice time from the user.
def get_time_choice():
    print("\nChoose your practice length:")
    print("30")
    print("60")
    print("90")
    print("120")

    time_choice = int(input("\nEnter practice time: "))

    while time_choice != 30 and time_choice != 60 and time_choice != 90 and time_choice != 120:
        print("Invalid time. Please choose 30, 60, 90, or 120.")
        time_choice = int(input("Enter practice time: "))

    return time_choice


# Main program starts here.
print("VOLLEYBALL PRACTICE QUEST GENERATOR")
print("-----------------------------------")
print("This program creates a volleyball practice plan with an initial warmup and main drills.")

category_choice = get_category_choice()
intensity_choice = get_intensity_choice()
time_choice = get_time_choice()

practice_plan, time_used, points = create_practice_plan(
    category_choice,
    intensity_choice,
    time_choice
)

coach_message = get_coach_message(points)

print("\nTODAY'S VOLLEYBALL PRACTICE QUEST")
print("---------------------------------")

print("\nINITIAL WARMUP")
print("--------------")
print(practice_plan[0][0])
print("Time: " + str(practice_plan[0][2]) + " minutes")
print("What to do: " + practice_plan[0][3])

print("\nMAIN DRILLS")
print("-----------")

# This loop prints each drill in the final practice plan.
for i in range(1, len(practice_plan)):
    current_drill = practice_plan[i]

    print("\nDrill " + str(i) + ": " + current_drill[0])
    print("Intensity: " + str(current_drill[2]))
    print("Time: " + str(current_drill[3]) + " minutes")
    print("Points: " + str(current_drill[4]))
    print("What to do: " + current_drill[5])

print("\nSESSION SUMMARY")
print("---------------")
print("Practice category: " + category_choice)
print("Selected intensity: " + str(intensity_choice))
print("Selected practice length: " + str(time_choice) + " minutes")
print("Total time used: " + str(time_used) + " minutes")
print("Practice points earned: " + str(points))
print("Coach message: " + coach_message)

print("\nGood luck with practice!")
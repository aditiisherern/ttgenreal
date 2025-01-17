'''import random

# Define parameters
no_p_d = 10  # Total number of periods per day
f_p_w = 5    # Number of fixed periods per week
s_choice = {'maths': "murugan sir", 'chem': "divya ma'am", 'phy': "sinda ma'am", 'social': "keerthi ma'am", 'comp': "sumitha ma'am"}
sub = list(s_choice.keys())
No_fixed = len(sub)

# Initialize lists for each day
days = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

# Function to generate a schedule for a day
def generate_day_schedule():
    day = []
    remaining_periods = no_p_d - No_fixed
    
    # Ensure that each subject appears at most twice
    subjects_for_day = []
    for _ in range(remaining_periods):
        p = random.choice(sub)
        subjects_for_day.append(p)
    
    # Add fixed subjects
    day.extend(subjects_for_day)
    day.extend(sub)
    
    # Check if any subject is scheduled more than twice
    while any(day.count(subject) > 2 for subject in sub):
        day = []
        subjects_for_day = []
        for _ in range(remaining_periods):
            p = random.choice(sub)
            subjects_for_day.append(p)
        day.extend(subjects_for_day)
        day.extend(sub)
    
    return day

# Generate schedule for each day
for day_name in days:
    day_schedule = generate_day_schedule()
    days[day_name] = day_schedule

# Print the results
for day_name, day_list in days.items():
    print(f"{day_name}: {day_list}")

print("\nFinal Timetable:")
for day_name, day_list in days.items():
    print(f"{day_name}: {day_list}")
'''
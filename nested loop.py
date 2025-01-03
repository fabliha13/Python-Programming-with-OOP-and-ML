## Nested Loop
# 
for week in range(1, 5):  # Weeks in a month
    print(f"Week {week}:")
    for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
        print(f"  {day}")
    print()  # Blank line after each week

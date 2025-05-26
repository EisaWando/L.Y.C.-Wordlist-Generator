#!/usr/bin/python3
"""
Ultimate Personalized Password Generator
Generates targeted wordlists based on:
- Personal information
- Pop culture references
- Common patterns
- Hobbies/interests
- Leetspeak substitutions
"""

import itertools
from datetime import datetime

# Color formatting
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Banner
print(f"""{colors.BLUE}
 _            __    __      _________
| |           \ \  / /      | _______|
| |            \ \/ /       | |
| |             \  /        | |
| |              | |        | |
| |____   _      | |    _   | |______    _
|______| |_|     | |   |_|  |________|  |_|     

{colors.CYAN}Ultimate Personalized Password Generator{colors.END}
""")

def get_input(prompt, input_type=str):
    while True:
        try:
            user_input = input(f"{colors.YELLOW}{prompt}: {colors.END}").strip()
            if input_type == bool:
                return user_input.lower() in ('y', 'yes')
            return input_type(user_input) if user_input else None
        except ValueError:
            print(f"{colors.RED}Invalid input. Please try again.{colors.END}")

# ===== DATA COLLECTION =====
personal_info = {}
pop_culture = {}
common_patterns = {}
hobbies = {}
leetspeak = {}

print(f"{colors.HEADER}\n=== Personal Information ==={colors.END}")
personal_info['names'] = get_input("Enter names (comma separated: self, partner, kids, etc.)").split(',')
personal_info['pet_names'] = get_input("Pet names (comma separated)").split(',')
personal_info['birthdays'] = get_input("Important dates (YYYY-MM-DD, comma separated)").split(',')
personal_info['phone'] = get_input("Phone numbers (comma separated)").split(',')
personal_info['address_parts'] = get_input("Address parts (street, city, zip, comma separated)").split(',')

print(f"\n{colors.HEADER}=== Pop Culture & Interests ==={colors.END}")
pop_culture['teams'] = get_input("Sports teams (comma separated)").split(',')
pop_culture['celebrities'] = get_input("Celebrities/characters (comma separated)").split(',')
pop_culture['movies_shows'] = get_input("Movies/TV shows (comma separated)").split(',')
pop_culture['music'] = get_input("Bands/singers (comma separated)").split(',')

print(f"\n{colors.HEADER}=== Common Patterns ==={colors.END}")
common_patterns['basic_words'] = get_input("Common words (password, admin, etc.)").split(',')
common_patterns['keyboard_patterns'] = get_input("Keyboard patterns (qwerty, 123456)").split(',')

print(f"\n{colors.HEADER}=== Hobbies & Interests ==={colors.END}")
hobbies['gaming'] = get_input("Gaming usernames").split(',')
hobbies['food_drinks'] = get_input("Favorite foods/drinks").split(',')
hobbies['places'] = get_input("Favorite places/visited locations").split(',')

# ===== PASSWORD GENERATION =====
separators = ['', '_', '-', '.', '/', '!', '@', '#', '$']
years = range(datetime.now().year-150, datetime.now().year+150)
leet_map = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 's':'5', 't':'7'}

def apply_leet(text):
    """Convert text to leetspeak"""
    return ''.join(leet_map.get(c.lower(), c) for c in text)

def generate_variations(base_words):
    variations = set()
    
    for word in base_words:
        if not word:
            continue
            
        # Case variations
        variations.add(word.lower())
        variations.add(word.capitalize())
        variations.add(word.upper())
        
        # Leetspeak
        variations.add(apply_leet(word))
        
        # Add common suffixes
        for year in years:
            variations.add(f"{word}{year}")
            variations.add(f"{word.capitalize()}{year}")
            
        # Add separators
        for sep in separators:
            variations.add(f"{word}{sep}")
            variations.add(f"{sep}{word}")
            
    return variations

# Generate all password candidates
all_passwords = set()

# Personal info passwords
all_passwords.update(generate_variations(personal_info['names']))
all_passwords.update(generate_variations(personal_info['pet_names']))
all_passwords.update(generate_variations(personal_info['birthdays']))
all_passwords.update(generate_variations(personal_info['phone']))
all_passwords.update(generate_variations(personal_info['address_parts']))

# Pop culture passwords
all_passwords.update(generate_variations(pop_culture['teams']))
all_passwords.update(generate_variations(pop_culture['celebrities']))
all_passwords.update(generate_variations(pop_culture['movies_shows']))
all_passwords.update(generate_variations(pop_culture['music']))

# Common patterns
all_passwords.update(generate_variations(common_patterns['basic_words']))
all_passwords.update(generate_variations(common_patterns['keyboard_patterns']))

# Hobbies passwords
all_passwords.update(generate_variations(hobbies['gaming']))
all_passwords.update(generate_variations(hobbies['food_drinks']))
all_passwords.update(generate_variations(hobbies['places']))

# Combination passwords (name + year + special char)
for name in personal_info['names']:
    if not name:
        continue
    for year in years:
        for sep in separators:
            all_passwords.add(f"{name}{sep}{year}")
            all_passwords.add(f"{name.capitalize()}{sep}{year}")
            all_passwords.add(f"{year}{sep}{name}")
            all_passwords.add(f"{apply_leet(name)}{sep}{year}")

# ===== SAVE RESULTS =====
output_file = "ultimate_wordlist.txt"
with open(output_file, 'w') as f:
    for pwd in sorted(all_passwords):
        if 6 <= len(pwd) <= 32:  # Reasonable password length limits
            f.write(f"{pwd}\n")

print(f"\n{colors.GREEN}Generated {len(all_passwords)} passwords in {output_file}{colors.END}")
print(f"{colors.YELLOW}Remember: Only use this for authorized security testing!{colors.END}")

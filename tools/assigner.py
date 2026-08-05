import csv
import random

def load_performers(filename):
    performers = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields to integers
            row['Availability'] = int(row['Availability'])
            row['Overall'] = int(row['Overall'])
            row['English Fluency'] = int(row['English Fluency'])
            row['Japanese Fluency'] = int(row['Japanese Fluency'])
            row['Singing Skill'] = int(row['Singing Skill'])
            row['Guessing Skill'] = int(row['Guessing Skill'])
            row['Assigned Count'] = int(row['Assigned Count'])
            
            # Convert comma-separated disliked games to a set
            row['Disliked Games'] = set(g.strip() for g in row['Disliked Games'].split(','))
            # Convert comma-separated preferred games to a set
            row['Preferred Games'] = set(g.strip() for g in row['Preferred Games'].split(','))
            
            performers.append(row)
    return performers

def load_games(filename):
    games = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['Japanese'] = int(row['Japanese'])
            row['English'] = int(row['English'])
            row['Both'] = int(row['Both'])
            row['# of Players Needed'] = int(row['# of Players Needed'])
            
            # Example: row['Avg Frequency'] = float(row['Avg Frequency'])  # if needed
            games.append(row)
    return games

def language_for_slot(slot_number):
    """Define a rule for what language is used in each slot."""
    # Example: slot 1, 6, 7, 11 => Both, otherwise alternate English/Japanese
    if slot_number in [1, 6, 7, 11]:
        return 'Both'
    else:
        # odd => Japanese, even => English
        return 'English' if (slot_number % 2) == 0 else 'Japanese'

def find_games_for_language(games, lang):
    """Return a list of games that support the given language."""
    # If lang == "English", we want games where row['English'] == 1 or row['Both'] == 1
    # If lang == "Japanese", we want row['Japanese'] == 1 or row['Both'] == 1
    # If lang == "Both", we want row['Both'] == 1
    valid_games = []
    for g in games:
        if lang == 'English':
            if g['English'] == 1 or g['Both'] == 1:
                valid_games.append(g)
        elif lang == 'Japanese':
            if g['Japanese'] == 1 or g['Both'] == 1:
                valid_games.append(g)
        elif lang == 'Both':
            if g['Both'] == 1:
                valid_games.append(g)
        else:
            # fallback: all?
            valid_games.append(g)
    return valid_games

def pick_game_for_slot(slot, games):
    """Randomly pick a game from the valid set for this slot's language."""
    lang = language_for_slot(slot)
    valid = find_games_for_language(games, lang)
    # pick any game at random
    if valid:
        return random.choice(valid)
    else:
        return None

def can_perform(performer, game, lang):
    """Check if the performer is eligible for the game based on:
       - Availability > 0
       - Assigned Count < 5 (for example)
       - Language skill if needed
       - Dislike check
    """
    if performer['Availability'] <= 0:
        return False
    if performer['Assigned Count'] >= 5:
        return False
    
    # Language checks
    if lang == 'English' and performer['English Fluency'] < 3:
        return False
    if lang == 'Japanese' and performer['Japanese Fluency'] < 3:
        return False
    if lang == 'Both':
        if performer['English Fluency'] < 3 or performer['Japanese Fluency'] < 3:
            return False
    
    # Dislike check
    if game['Game Name'] in performer['Disliked Games']:
        return False
    
    return True

def assign_players_for_game(game, performers, slot):
    """Pick as many players as needed for the game, updating their Assigned Count."""
    lang = language_for_slot(slot)
    needed = game['# of Players Needed']
    
    # Get all performers who CAN do this game
    eligible = [p for p in performers if can_perform(p, game, lang)]
    
    # Sort them by (Overall desc) or name asc, or random shuffle
    # For example, let's sort by name ascending:
    eligible.sort(key=lambda p: p['Performer Name'])
    
    # If you want random picks from that sorted list, do random.sample
    # Or if you want to prioritize 'Overall' skill, do something else
    if len(eligible) < needed:
        # Not enough performers to fill the game
        chosen = eligible  # We'll just take them all, though it's short
    else:
        chosen = random.sample(eligible, needed)
    
    # Update each chosen performer’s Assigned Count
    for c in chosen:
        c['Assigned Count'] += 1
    
    # Return the chosen list
    return chosen

def main():
    # 1) Load data
    performers = load_performers('PerformerProfile.csv')
    games = load_games('GameCatalogue.csv')
    
    # 2) Generate an 11-game show
    show_slots = list(range(1, 12))  # 1..11
    set_list = []
    
    # We'll keep track of used games so we don't repeat if that's desired
    # or we can let repeats happen. Let's store used game names in a set:
    used_game_names = set()
    
    for slot in show_slots:
        # pick the game
        picked_game = pick_game_for_slot(slot, games)
        
        # If we don't want duplicates, ensure it's not already used
        # We'll loop until we find a unique game (or run out):
        attempt_count = 0
        while picked_game and picked_game['Game Name'] in used_game_names:
            picked_game = pick_game_for_slot(slot, games)
            attempt_count += 1
            if attempt_count > 10:
                # fallback
                break
        
        if not picked_game:
            # none found
            set_list.append({
                'Slot': slot,
                'Language': language_for_slot(slot),
                'Game Name': 'NO VALID GAME!',
                'Players': []
            })
            continue
        
        used_game_names.add(picked_game['Game Name'])
        
        # pick the players
        chosen_players = assign_players_for_game(picked_game, performers, slot)
        
        # Build a record
        set_list.append({
            'Slot': slot,
            'Language': language_for_slot(slot),
            'Game Name': picked_game['Game Name'],
            'Players': [p['Performer Name'] for p in chosen_players]
        })
    
    # 3) Print the result
    print("DRAFT SET LIST")
    for item in set_list:
        print(f"Game {item['Slot']}: {item['Game Name']} ({item['Language']}) -> {', '.join(item['Players'])}")
    
    # 4) (Optional) Print final assigned counts
    print("\nFINAL ASSIGNED COUNTS:")
    for p in performers:
        print(f"{p['Performer Name']}: {p['Assigned Count']}")

if __name__ == "__main__":
    main()

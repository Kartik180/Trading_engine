# Function to calculate the probability of a team winning a match
def calculate_probability():
    return 0.5

# Function to calculate the points table
def calculate_points_table():
    # Sample points table (update with actual points)
    points_table = {
        'GT': 16,
        'CSK': 13,
        'MI': 12,
        'LSG': 11,
        'RR': 10,
        'KKR': 10,
        'RCB': 10,
        'PBKS': 10,
        'SRH': 8,
        'DC': 8
    }
    return points_table

# Function to calculate the probability of a team winning the tournament
def calculate_team_probabilities(teams, fixtures):
    team_probabilities = {}
    for team in teams:
        team_probabilities[team] = 0

    for match in fixtures:
        team1 = match[0]
        team2 = match[1]

        # Calculate the probability of team1 winning the match
        probability = calculate_probability()

        # Update the team probabilities based on the match result
        if probability >= 0.5:
            team_probabilities[team1] += 2
        else:
            team_probabilities[team2] += 2

    return team_probabilities

# Function to get the four most probable teams
def get_most_probable_teams(team_probabilities):
    sorted_teams = sorted(team_probabilities.items(), key=lambda x: x[1], reverse=True)
    return [team[0] for team in sorted_teams[:4]]

def main():
    teams = ['GT', 'MI', 'CSK', 'LSG', 'KKR', 'RCB', 'PBKS', 'SRH', 'DC', 'RR']
    
    # Sample fixtures (update with actual fixtures)
    fixtures = [
        ('CSK', 'DC'),
        ('KKR', 'RR'),
        ('MI', 'GT'),
        ('SRH', 'LSG'),
        ('DC', 'PBKS'),
        ('RR', 'RCB'),
        ('CSK', 'KKR'),
        ('GT', 'SRH'),
        ('LSG', 'MI'),
        ('PBKS', 'DC'),
        ('SRH', 'RCB'),
        ('PBKS', 'RR'),
        ('DC', 'CSK'),
        ('KKR', 'LSG'),
        ('MI','SRH'),
        ('RCB','GT')
    ]

    team_probabilities = calculate_team_probabilities(teams, fixtures)
    most_probable_teams = get_most_probable_teams(team_probabilities)

    print("Most Probable Teams:")
    for team in most_probable_teams:
        print(team)

if __name__ == '__main__':
    main()

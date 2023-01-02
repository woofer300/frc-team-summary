import team_summary

# Paste your TBA API key as a string on the line below
auth_key = ""
if not auth_key:
    auth_key = input("Please paste your TBA API key.\n")
if team_summary.is_valid_api_key(auth_key):
    try:
        team_number = int(input("What is the team number of the team you would like a summary of?\n"))
        year = int(input("What year would you like a summary for?\n"))
    except ValueError:
        print("Please enter a valid number!")
    else:
        print("Contacting The Blue Alliance API...\n")
        print(team_summary.summarize_team(team_number, year, auth_key))
else:
    print("Please enter a valid TBA API key!")

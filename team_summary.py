import requests


def summarize_team(team_number, year, auth_key):
    message = ""

    headers = {"X-TBA-Auth-Key": auth_key}
    tba_base_url = "https://www.thebluealliance.com/api/v3"
    team_key = f"frc{team_number}"

    basic = requests.get(f"{tba_base_url}/team/{team_key}", headers=headers).json()
    nickname = basic.get("nickname")

    message += f"\nTeam {team_number} - {nickname}:\n\n"

    city = basic.get("city")
    state_prov = basic.get("state_prov")
    country = basic.get("country")

    message += f"Location: {city}, {state_prov}, {country}\n"

    rookie_year = basic.get("rookie_year")

    message += f"Rookie Year: {rookie_year}\n"

    events = requests.get(f"{tba_base_url}/team/{team_key}/events/{year}", headers=headers).json()
    event_names = [event.get("name")
                   for event
                   in sorted(events, key=lambda event: (event.get("week") is None, event.get("week")))]

    if event_names:
        message += f"Events in {year}: " + ", ".join(event_names) + "\n"

        awards_count = {}
        for event in events:
            awards_at_event = requests.get(f"{tba_base_url}/team/{team_key}/event/{event.get('key')}/awards",
                                           headers=headers).json()
            for award_at_event in awards_at_event:
                award_name = award_at_event.get("name")
                if award_name in awards_count:
                    awards_count.update({award_name: awards_count.get(award_name) + 1})
                else:
                    awards_count.update({award_name: 1})

        if awards_count:
            awards_count_array = []
            for award_name, times_won in awards_count.items():
                awards_count_array.append(f"{award_name} x{times_won}")
            message += f"Awards in {year}: " + ", ".join(awards_count_array) + "\n"
        else:
            message += f"Team {team_number} did not win any awards in {year}!\n"

        wins = 0
        losses = 0
        ties = 0
        ranks = []
        num_teams = []
        for event in events:
            status_at_event = requests.get(f"{tba_base_url}/team/{team_key}/event/{event.get('key')}/status",
                                           headers=headers).json()
            qual_status_at_event = status_at_event.get("qual")
            playoff_status_at_event = status_at_event.get("playoff")
            if qual_status_at_event is not None:
                num_teams.append(qual_status_at_event.get("num_teams"))
                rank = qual_status_at_event.get("ranking").get("rank")
                if rank is not None:
                    ranks.append(rank)
                qual_record = qual_status_at_event.get("ranking").get("record")
                wins += qual_record.get("wins")
                losses += qual_record.get("losses")
                ties += qual_record.get("ties")
            if playoff_status_at_event is not None:
                playoff_record = playoff_status_at_event.get("record")
                wins += playoff_record.get("wins")
                losses += playoff_record.get("losses")
                ties += playoff_record.get("ties")
        message += f"Record in {year}: {wins}-{losses}-{ties}\n"
        message += f"Average Ranking: {round(sum(ranks) / len(ranks))}/{round(sum(num_teams) / len(num_teams))}"
    else:
        message += f"Team {team_number} did not compete in {year}!"
    return message


def is_valid_api_key(auth_key):
    headers = {"X-TBA-Auth-Key": auth_key}
    status = requests.get("https://www.thebluealliance.com/api/v3/status", headers=headers).json()
    return "Error" not in status

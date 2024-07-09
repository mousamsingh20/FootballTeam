import streamlit as st

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def list_players(self):
        player_list = ""
        for player in self.players:
            player_list += f"{player.name} - {player.position}\n"
        return player_list

# Function to display the app interface
def main():
    st.title("Football Team Management")

    team_name = st.text_input("Enter Team Name:")
    coach_name = st.text_input("Enter Coach Name:")

    team = FootballTeam(team_name, coach_name)

    st.header("Add a Player")
    player_name = st.text_input("Player Name:")
    player_position = st.text_input("Player Position:")

    if st.button("Add Player"):
        new_player = Player(player_name, player_position)
        team.add_player(new_player)
        st.success(f"Added {player_name} - {player_position} to {team_name}")

    st.header("Current Players")
    if team.players:
        st.write(team.list_players())
    else:
        st.write("No players added yet.")

if __name__ == "__main__":
    main()

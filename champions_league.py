class Football:

    def __init__(self):
        self.teams = list(["chelsea fc", "barcelona fc", "real madrid fc", "bayern munich fc",
                      "paris saint germain fc", "ajax fc", "sevilla fc", "as monaco fc"])
        self.winners = []
        self.final_team = []

    def team_list(self):
        print(f"Welcome to Champions League here is the list of teams: ")
        print(f"{self.teams}".title())
        play_game = input("Please type 'start' to play the game or 'exit': ")
        if play_game == "start":
            team = ["chelsea fc", "barcelona fc", "real madrid fc", "bayern munich fc",
                    "paris saint germain fc", "ajax fc", "sevilla fc", "as monaco fc"]
            print("Results of last 8 are as follows: ")
            print("\n")
            print(f"{team[0]} vs {team[7]}".title())
            print(f"{team[1]} vs {team[6]}".title())
            print(f"{team[2]} vs {team[5]}".title())
            print(f"{team[3]} vs {team[4]}".title())
            print("\n")
            score_team1 = int(input(f"Please enter the score of {team[0]}: "))
            score_team2 = int(input(f"Enter the score of {team[7]}: "))
            if score_team1 > score_team2:
                print(f"{team[0]}..You are through to champions league, semi final stage..".title())
                self.winners.append(team[0].title())
            else:
                print(f"{team[7]}, You are through to champions league semi finals..".title())
                self.winners.append(team[7].title())
            score_team3 = int(input(f"Enter a score of {team[1]}: "))
            score_team4 = int(input(f"Enter a score of {team[6]}: "))
            if score_team3 > score_team4:
                print(f"{team[1]}, you are through to the semi finals..".title())
                self.winners.append(team[1].title())
            else:
                print(f"{team[6]}, you are through to the semi finals..".title())
                self.winners.append(team[6].title())
            score_team5 = int(input(f"Enter a score of {team[2]}: "))
            score_team6 = int(input(f"Enter a score of {team[5]}: "))
            if score_team5 > score_team6:
                print(f"{team[2]}, you are through to the semi finals..".title())
                self.winners.append(team[2].title())
            else:
                print(f"{team[5]}, you are through to the semi finals..")
                self.winners.append(team[5].title())
            score_team7 = int(input(f"Enter a score of {team[3]}: "))
            score_team8 = int(input(f"Enter a score of {team[4]}: "))
            if score_team7 > score_team8:
                print(f"{team[3]}, you are through to the semi finals..")
                self.winners.append(team[3].title())
            else:
                print(f"{team[4]}, you are through to the semi finals..")
                self.winners.append(team[4].title())

            print(f"Following teams has gone through the next stage: ")
            print(self.winners)

        if play_game == "exit":
            print("Goodbye")

    def semi_final(self):
        print("\n")
        print(f"Welcome to the stage of Semi finals...")
        print(f"Team's of the semi finals are: ")
        semi_draw = self.winners
        print(f"{semi_draw}".upper())
        print("Draw of the semi finals are as follows: ")
        semi_1 = (f"{self.winners[0]} vs {self.winners[1]}")
        semi_2 = (f"{self.winners[2]} vs {self.winners[3]}")
        print(semi_1)
        print(semi_2)
        semi_score = int(input(f"Please enter the score of {self.winners[0]}: "))
        semi_score_1 = int(input(f"Please enter the score of {self.winners[1]}: "))
        if semi_score > semi_score_1:
            print(f"{self.winners[0]}, Congratulation you are in the final")
            self.final_team.append(self.winners[0])
        else:
            print(f"{self.winners[1]}, Congratulations you are going through to the final")
            self.final_team.append(self.winners[1])
        semi_final_team_2 = int(input(f"Enter the score of {self.winners[2]}: "))
        semi_final_team_2_1 = int(input(f"Enter the score of {self.winners[3]}: "))
        if semi_final_team_2 > semi_final_team_2_1:
            print(f"{self.winners[2]}, congrats you are in the final")
            self.final_team.append(self.winners[2])
        else:
            print(f"{self.winners[3]}, congrats you are in the final")
            self.final_team.append(self.winners[3])
        print("Teams for the final of champions league is: ")
        for team in self.final_team:
            print(team)


    def final(self):
        print("\n")
        print("Welcome to Munich, for the final's of Champions League 2020")
        final_team_1 = int(input(f"Enter the score of {self.final_team[0]}: "))
        final_team_2 = int(input(f"Enter the score of {self.final_team[1]}: "))
        if final_team_1 > final_team_2:
            print(f"Massive Congratualtions to {self.final_team[0]} for winning it..")
        else:
            print(f"Huge Congratulations to {self.final_team[1]} for winning it first time..")

champions_league = Football()
champions_league.team_list()
champions_league.semi_final()
champions_league.final()
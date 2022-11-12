from unittest import TestCase, main
from project.f1_season_app import F1SeasonApp


class TestF1SeasonAppClass(TestCase):
    def test_practice(self):
        self.f1_season_app = F1SeasonApp()

        red_bull_register = self.f1_season_app.register_team_for_season("Red Bull", 2000000)
        mercedes_register = self.f1_season_app.register_team_for_season("Mercedes", 2500000)

        nurburgring_race = self.f1_season_app.new_race_results("Nurburgring", 1, 7)
        silverstone_race = self.f1_season_app.new_race_results("Silverstone", 10, 1)

        self.assertEqual(red_bull_register, "Red Bull has joined the new F1 season.")
        self.assertEqual(mercedes_register, "Mercedes has joined the new F1 season.")

        self.assertEqual(
            nurburgring_race,
            "Red Bull: The revenue after the race is 1270000$. "
            "Current budget 3270000$. "
            "Mercedes: The revenue after the race is -150000$. "
            "Current budget 2350000$. "
            "Red Bull is ahead at the Nurburgring race."
        )

        self.assertEqual(
            silverstone_race,
            "Red Bull: The revenue after the race is -240000$. "
            "Current budget 3030000$. "
            "Mercedes: The revenue after the race is 900000$. "
            "Current budget 3250000$. "
            "Mercedes is ahead at the Silverstone race."
        )


if __name__ == '__main__':
    main()
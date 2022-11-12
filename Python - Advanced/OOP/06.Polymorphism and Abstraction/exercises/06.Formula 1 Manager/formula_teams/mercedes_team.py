from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def __init__(self, budget: int):
        super().__init__(budget)
    
    @property
    def sponsors(self):

        return [
            {1: 1_000_000, 3: 500_000},
            {5: 100_000, 7: 50_000}
        ]
    
    @property
    def expenses_for_one_race(self):
        return 200_000

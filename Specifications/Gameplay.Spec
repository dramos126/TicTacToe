#--------------------
#Story: Gameplay
#--------------------
#Players P = {X | O}
#------------------------------------------------
Scenario: Run game
#------------------------------------------------
Given:  Game is not started

When:   Game is started

Then:   => Board Update
        => Determine Winner
        => Determine Next Action
        # This implies ALL these stories are implemented (true)
#--------------------
#Story: Gameplay
#--------------------
#Players P = {X | O}
#------------------------------------------------
Scenario: Run game
#------------------------------------------------
Then:   => Board Update
        => Determine Winner
        => Determine Next Action
        # This implies ALL these stories are implemented (true)

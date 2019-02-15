#--------------------
#Story: Gameplay
#--------------------

#------------------------------------------------
Scenario: Run game
#------------------------------------------------
Given:  Game is not started

When:   Game is started

Then:   {Start Game & Player Turn & Determine Winner & Determine Next Action}
        # This means all these stories are implemented
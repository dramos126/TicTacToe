------------------------
Scenario: Determine Endgame
------------------------

------------
Scenario 0
------------
Given:  Game is not started

When:   Game is started

Then:   player X can select a position

------------
Scenario 1
------------
Given:  Some Board B
        position S
        B has less than 8 filled positions
        S is an empty position
        Player P does not win with the selection of S
        Player Q is the other player

When:   Player P selects S

Then:   player Q can select a position

------------
Scenario 2
------------
Given:  Some Board B
        position S
        S is an empty position
        Player P wins with the selection of S

When:   Player P selects S

Then:   Announce End of Game

------------
Scenario 3
------------

Given:  Some Board B
        B has 8 filled positions
        position S is the empty position in B

When:   Player P selects S

Then:   Announce End of Game

------------
UI Scenario:
------------
Then:
    Announce End of Game = "Game Over"
    player Q can select a position = "Player Q turn, please select - "
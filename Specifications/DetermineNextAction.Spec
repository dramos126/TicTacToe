#----------------------------
#Story: Determine next action
#----------------------------

#-------------------
Scenario: Start Game
#-------------------
Given:  Game is not started

When:   Game is started

Then:   player X can select a position

#---------------------------------------------
Scenario: Player does not win & board not full
#---------------------------------------------
Given:  Some Board B
        position S
        B has less than 8 filled positions
        S is an empty position
        Player P does not win with the selection of S
        Player Q is the other player

When:   Player P selects S

Then:   player Q's turn

#------------------
#UI Implementation:
#------------------
#Then:
#    player Q's turn = "Player Q turn, please select - "

#--------------------
Scenario: Player wins
#--------------------
Given:  Some Board B
        position S
        S is an empty position
        Player P wins with the selection of S

When:   Player P selects S

Then:   Announce End of Game

#-------------------
Scenario: Board full
#-------------------
Given:  Some Board B
        B has 8 filled positions
        position S is the empty position in B

When:   Player P selects S

Then:   Announce End of Game

#------------------
#UI Implementation:
#------------------
#Then:
#    Announce End of Game = "Game Over"
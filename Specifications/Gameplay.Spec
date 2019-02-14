#--------------------
#Story: Gameplay
#--------------------

#------------------------------------------------
Scenario: Player turn when selection is not empty
#------------------------------------------------
Given:  Game is started
        Board is {b1, b2, b3, b4, b5, b6, b7, b8, b9}
        Player P's turn
        position S is not empty #

When:   When player selects position S

Then:   Board is {b1, b2, b3, b4, b5, b6, b7, b8, b9}
        notify P that S is full
        Determine Winner
        Accept selection from P

#------------------
#UI Implementation:
#------------------
#Then:
#        notify P that the position is full = "Position is full, try again"

#--------------------------------------------
Scenario: Player turn when selection is empty
#--------------------------------------------
Given:  Game is started
        Board is {b1, b2, b3, b4, b5, b6, b7, b8, b9}
        Player P's turn
*       S = Ø

When:   When player selects position S

Then:   Board is {b1', b2', b3', b4', b5', b6', b7', b8', b9'}
            Where bi' = bi EXCEPT bS = P
        Determine Winner
        Determine Next Action

#------------------
#UI Implementation:
#------------------
#Then:      {b1', b2', b3', b4', b5', b6', b7', b8', b9'} =
#                         +..-+..-+..-+
#                         |b1'|b2'|b3'|
#                         +..-+..-+..-+
#                         |b4'|b5'|b6'|
#                         +..-+..-+..-+
#                         |b7'|b8'|b9'|
#                         +..-+..-+..-+
#
#          ".." = should be ignored
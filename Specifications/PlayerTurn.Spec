#--------------------
#Story: Player Turn
#--------------------
# Board B = {b1, b2, b3, b4, b5, b6, b7, b8, b9}
#      Bi = {Ø|X|O|
#------------------------------------------------
Scenario: Player turn when selection is not empty
#------------------------------------------------
Given:  Game is started
        Board is B with position S not empty
        Player P's turn

When:   P selects S

Then:   Board is B
        Notify P that S is full

#------------------
#UI Implementation:
#------------------
#Then:
#        Player P's turn = "Position S is full, try again"

#--------------------------------------------
Scenario: Player turn when selection is empty
#--------------------------------------------
Given:  Game is started
        Board is B with position S empty
        Player P's turn

When:   P selects S

Then:   Board is B with position S containing P

#------------------
#UI Implementation:
#------------------
# bi' = bi except bS' = P
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
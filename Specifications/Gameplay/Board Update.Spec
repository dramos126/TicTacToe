#-----------------------
#Story: Board Update
#-----------------------
------------------------
Scenario: Start the game
------------------------
Given:  Game is not started

When:   Game is started

Then:   Board is EMPTY
#EMPTY Board = {Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø}
#------------------
#UI Implementation:
#------------------
#Given:      Command Prompt is shown
#
#When:      Start the game from command line
#
#Then:      Board is Empty =
#                    +-+-+-+
#                    |1|2|3|
#                    +-+-+-+
#                    |4|5|6|
#                    +-+-+-+
#                    |7|8|9|
#                    +-+-+-+

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
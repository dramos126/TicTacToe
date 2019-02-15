#-----------------
#Story: Start Game
#-----------------

#Players P = {X | O}
#EMPTY Board = {Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø}
------------------------
Scenario: Start the game
------------------------
Given:  Game is not started

When:   Game is started

Then:   Board is EMPTY

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


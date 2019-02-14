#-----------------
#Story: Start Game
#-----------------

#Players = {X | O}
#EMPTY Board = {Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø}
------------------------
Scenario: Start the game
------------------------
Given:  Game is not started

When:   Game is started

Then:   Board is EMPTY
        Determine Winner
        Determine Next Action

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


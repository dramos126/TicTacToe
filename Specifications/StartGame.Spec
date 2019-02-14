------------------------
Scenario: Start the game
------------------------
Players = {X | O}
Empty Board = {Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø}

Given:  Game is not started

When:   Game is started

Then:   Board is Empty
        announce Winner
        determine end of game

------------
UI Scenario:
------------
Given:  Command Prompt is shown

When:   Start the game from command line

Then:
        Board is Empty =
                    +-+-+-+
                    |1|2|3|
                    +-+-+-+
                    |4|5|6|
                    +-+-+-+
                    |7|8|9|
                    +-+-+-+

No Winner = "No winner"

player X can select position = "Player X selection - "


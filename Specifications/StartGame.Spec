------------------------
Scenario: Start the game
------------------------
Description: Start the game

Given:  Game is not started

When:   Game is started

Then:   Board is Empty
        No Winner
        Accept selection from X

Empty Board = {Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø}

------------
UI Scenario:
------------
Given:  Command Prompt is shown

When:   Start the game from command line

Then:
        Empty board =
                    +-+-+-+
                    |1|2|3|
                    +-+-+-+
                    |4|5|6|
                    +-+-+-+
                    |7|8|9|
                    +-+-+-+

No Winner = "No winner"

Accept selection from X = "Player X selection - "
P = {X | O}

------------------------
Scenario: Player turn when selection is empty
------------------------
Description: A successful move

Given:  Game is started
        Board is {b1, b2, b3, b4, b5, b6, b7, b8, b9}
        Player P's turn
*       S = Ø

When:   When player selects position S

Then:   Board is {b1', b2', b3', b4', b5', b6', b7', b8', b9'}
            Where bi' = bi EXCEPT bS = P
        announce Winner
        determine end of game

------------
UI Scenario:
------------
Then:
    {b1', b2', b3', b4', b5', b6', b7', b8', b9'} =
                         +..-+..-+..-+
                         |b1'|b2'|b3'|
                         +..-+..-+..-+
                         |b4'|b5'|b6'|
                         +..-+..-+..-+
                         |b7'|b8'|b9'|
                         +..-+..-+..-+

        ".." = should be ignored

        End of Game = "Game is Over"
        Announce Winner = No winner
                        = "P is the winner"
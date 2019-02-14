------------------------
Scenario: Player turn when selection is empty
------------------------
Description: A successful move

Given:  Game is started
        Board is {b1, b2, b3, b4, b5, b6, b7, b8, b9}
        Player P's turn
        b1 = Ø
        board has at most 7 full positions

When:   When player selects position C (ex 1)

Then:   Board is {P, b2, b3, b4, b5, b6, b7, b8, b9}
        announce Winner
        Accpet selection from other player



------------------------
Scenario: Player turn when selection is empty full board
------------------------
Description: A successful move

Given:  Game is started
        Board is {b1, b2, b3, b4, b5, b6, b7, b8, b9}
        Player P's turn
        b1 = Ø
        board has 8 full positions

When:   When player selects position C (ex 1)

Then:   Board is {P, b2, b3, b4, b5, b6, b7, b8, b9}
        announce Winner
        announce End of Game

------------
UI Scenario:
------------

Then:
    {P, b2, b3, b4, b5, b6, b7, b8, b9} =
                         +-+-+-+
                         |P|b2|b3|
                         +-+-+-+
                         |b4|b5|b6|
                         +-+-+-+
                         |b7|b8|b9|
                         +-+-+-+
        End of Game = "Game is Over"
        Announce Winner = No winner
                        = "P is the winner"
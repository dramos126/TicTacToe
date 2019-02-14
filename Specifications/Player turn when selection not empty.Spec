------------------------
Scenario: Player turn when selection is not empty
------------------------
Description: A unsuccessful move

Given:  Game is started
        Board is {b1, b2, b3, b4, b5, b6, b7, b8, b9}
        Player P's turn
 *      position S = not empty

When:   When player selects position S

Then:   Board is {b1, b2, b3, b4, b5, b6, b7, b8, b9}
        notify P that S is full
        announce Winner
        Accpet selection from P

------------
UI Scenario:
------------
Then:
        notify P that the position is full = "Postion is full, try again"
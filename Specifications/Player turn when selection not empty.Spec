------------------------
Scenario: Player turn when selection is not empty
------------------------
Description: A unsuccessful move

Given:  Game is started
        Board is {b1, b2, b3, b4, b5, b6, b7, b8, b9}
        Player P's turn
        b1 = Any P

When:   When player selects position C (ex 1)

Then:   Board is {P, b2, b3, b4, b5, b6, b7, b8, b9}
        notify P that the position is full
        announce Winner
        Accpet selection from P

------------
UI Scenario:
------------
Then:
        notify P that the position is full = "Postion is full, try again"
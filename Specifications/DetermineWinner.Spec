------------------------
Scenario: Determine Winner
------------------------
Description: Duh

Given:  Some Board B
        selecting X will result in 3 in a line

When:   Player P selects position X

Then:   P won

Empty Board = {Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø,Ø}

------------
UI Scenario:
------------
Then:
    P won = "Player P won"

Given:  Some Board B
        selecting X will not result in 3 in a line

When:   Player P selects position X

Then:   No winner
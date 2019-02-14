------------------------
Scenario: Determine Winner
------------------------

------------
Scenario 0
------------
Given:  Game is not started

When:   Game is started

Then:   No Winner

------------
Scenario 1
------------
Given:  Some Board B
        position S
        selecting S will result in 3 P in a line

When:   Player selects S

Then:   P won

------------
UI Scenario:
------------
Then:
    P won = "Player P won"

Given:  Some Board B
        position S
        selecting S will not result in 3 P in a line

When:   Player P selects S

Then:   No winner

------------
UI Scenario:
------------
Then:
    No winner = "No Winner"
    P won = "Player P Won"
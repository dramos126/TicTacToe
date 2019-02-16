#-----------------------
#Story: Determine Winner
#-----------------------
#-------------------
Scenario: Start Game
#-------------------
Given:  Game is not started

When:   Game is started

Then:   No winner

-------------------
Scenario: No Winner
-------------------
Given:  Some Board B
        Position S
        Player P's turn
        Selecting S will put 3 P's in a line on B

When:   P selects S

Then:   No winner

#------------------
#UI Implementation:
#------------------
#Then:
#    No winner = "No Winner"

---------------------
Scenario: Player Wins
---------------------
Given:  Some Board B
        Position S
        Player P turn
        Selecting S will 3 P's in a line on B

When:   P selects S

Then:   P won

#------------------
#UI Implementation:
#------------------
#Then:
#    P won = "Player P Won"
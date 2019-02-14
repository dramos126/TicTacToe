#-----------------------
#Story: Determine Winner
#-----------------------

-------------------
Scenario: No Winner
-------------------
Given:  Some Board B
        S does not have 3 P's in a line

When:   Check for winner

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
        S has 3 P's in a line

When:   Check for winner

Then:   P won

#------------------
#UI Implementation:
#------------------
#Then:
#    P won = "Player P Won"
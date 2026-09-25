Problem Statement
Organizing bodies that run multi-country sporting events such as the Olympics need to track
a large number of athletes, the countries they represent, the events they compete in, and the
medals they win. Doing this manually — on paper or in scattered spreadsheets — is slow, hard
to update consistently, and makes it difficult to answer simple but important questions such
as "who currently has the most points?" or "which country is leading the medal table?" in
real time.
The Olympics Player Management System solves this by providing a lightweight,
menu-driven console application that stores every player's record in a single structured CSV
file and offers instant operations to add, search, update, and remove players, along with
automatically generated leaderboards for both individual players and countries.
Scope of the Project
In scope:
Managing individual player records: player ID, name, country, event/item, and medal counts.
CRUD-style operations: create (add), read (search/view), update (prize update), delete
(remove).
Automatic points calculation from medal counts using a fixed weighting formula.
Two ranking/reporting views: top players by points, and top countries by aggregated medals
and points.
Persistent storage using a CSV file, requiring no external database server.
Out of scope (possible future work):
Multi-user concurrent access / networked deployment.
A graphical or web-based user interface.
Authentication, authorization, or role-based access control.
Support for team events or multi-athlete events beyond one row per player.
Target Users
Event administrators / officials who need to register athletes, record medal results
as events conclude, and correct entries when needed.
Data entry operators at a sporting event who add and update player records during the
competition.
Analysts or organizers who need a quick, ranked view of top-performing players and
countries without manually tallying a spreadsheet.
Students / learners studying Python file handling, CSV-based data storage, and modular
program design, for whom this project also serves as a practical learning example.
High-Level Features
Add Player — register a new athlete with country, event, and medal counts; duplicate
player IDs are rejected; points are computed automatically.
Search Player — retrieve and display a single player's full record by ID.
Update Prize — add newly won medals to an existing player and automatically
recalculate their total points.
Remove Player — delete a player's record from the system.
View Top Players — display all players ranked from highest to lowest points.
View Top Countries — aggregate medals and points by country and display a ranked
country-wise medal table.
Points Formula
```
points = (gold_medals × 5) + (silver_medals × 3) + (bronze_medals × 1)
```
This weighting reflects the relative value of each medal type while remaining simple enough
to compute and verify by hand.

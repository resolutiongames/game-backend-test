# game-backend-test

Welcome to Resolution Games game backend test.

## Preparations

The very first thing you should do is read through these instructions.
After that, send an e-mail to the email mentioned in the invite, with your suggested deadline for submission.

This means you choose your own deadline. There is no need to ask us if the deadline is OK.
After that, start working on the game and submit it no later than the deadline.

## Assignment
Your task is to implement the game of the lowest unique number. The game works by players choosing a number, and the one with the lowest unique number wins.
For each player, only their lowest value is considered. 
We provide a server to handle storing and retrieving of choices (see [server/README.md](server/README.md) for details).

### Example of play
`Player A choose 5`

Game displays:
- A 5

`Player B choose 9`

Game Displays:
- A 5
- B 9

`Player C choose 5`

Game Displays:
- B 9

`Player B choose 4`

Game Displays:
- B 4

`Player C choose 3`

Game Displays:
- C 3
- A 5
- B 4

`Player A choose 6`

Game displays:
- C 3
- B 4
- A 5

### Things to consider
- You chose the user interface. Keep the initial, or make your own. Do what you need to show that the mechanics are working.
- Imagine the game is multiplayer over the internet.
- Make it simple, but write the code to a quality that's good enough for professional developers to continue working on.
- You should not need to change the server, but you are wellcome to if you need to do so.

### Version control

Start with cloning this repository. Keep it local. Do not create a public repository!
Work with Git locally as usual. Do not push, as you have no write permissions.
If you haven't worked with Git before, this is an opportunity to learn it.

## Submission

Make sure you have committed the final version.

Then create a zip file of the .git directory.
The zip file should only contain the `.git` directory, nothing else.

Send the zip file to the suggested email (see your invite to the test).

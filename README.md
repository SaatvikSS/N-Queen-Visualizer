# N-Queen-Visualizer
Hi This is a N Queen Visualizer program using python.

Here is the explaination of the project:




Logic and Concept
Backtracking Algorithm:

The problem is solved using a backtracking algorithm, which tries to place a queen in each column of the board one by one, starting from the leftmost column.
For each column, the algorithm attempts to place the queen in each row and checks if it’s a safe position.
Safety Check:

A position is considered safe if there are no queens in the same row, no queens in the upper left diagonal, and no queens in the lower left diagonal.
Recursive Solution:

If placing the queen in a particular row and column is safe, the algorithm places the queen and moves to the next column.
If it’s not possible to place a queen in any row of the current column, the algorithm backtracks and removes the queen from the previous column, then tries the next possible position in the previous column.
Visualization with Pygame:

Pygame is used to visualize the board and the process of placing queens.
The board is drawn, and the queen’s position is updated in each step.
A delay is introduced to make the visualization observable.





Detailed Steps
Initialize the Board:

An empty board of size N×N is initialized with all positions set to 0.
Check Safety:

Before placing a queen, the algorithm checks if the position is safe by iterating over the rows and diagonals.
Recursive Backtracking:

The algorithm recursively attempts to place queens in each column, using a loop to try each row in the column.
If a solution is found (i.e., all queens are placed without conflicts), the algorithm returns true.
If no valid position is found in a column, the algorithm backtracks to the previous column and tries the next possible position.
Visualization:

After each successful or unsuccessful placement of a queen, the board is drawn, and the display is updated.
A delay (time.sleep) is used to slow down the visualization, so the placement process is visible step-by-step.

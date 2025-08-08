# qlearning-maze-solver
An agent is trained using tabular Q-learning to navigate and solve a grid based maze

- The environment consists of a 50X50 grid with a start cell at one corner and a goal cell at the opposite corner and some cells in-between taken as the obstacles.
- The agent should use tabular Q-learning and learn Q-values corresponding to all the cells in the grid i.e, we learn a table of Q-values tabulated against the corresponding states and actions.
- The agent uses epsilon greedy policy while learning and will finally extract the path using a greedy policy.
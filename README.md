# qlearning-maze-solver
An agent is trained using tabular Q-learning to navigate and solve a grid-based maze

- The environment consists of a 30X30 grid with a start cell at one corner, a goal cell at the opposite corner and a maze layout to navigate.
- The agent learn Q-values corresponding to all the cells(states) in the grid and populates the table of Q-values tabulated against the corresponding states and actions.
- The agent uses an epsilon-greedy policy while learning and will finally extract the path using a greedy policy.

<div align="center">
  <img src="assets/sim.gif" alt="App Demo" width="600"/>
</div>

### How to run this code

1. Clone the repository - In terminal(vs code or any other) navigate to location where you want to clone the repository(using cd) and use,   
```
git clone https://github.com/rakshith-6/qlearning-maze-solver.git
``` 

2. Create a virtual environment,

In Debian-based OSs to install python virtual environment, run in terminal the following command

```
sudo apt-get install python3-venv
```
Navigate to the cloned repo folder and use the following commands to create and activate the virtual environment (Sometimes may need to select the interpreter manually even after activating in VS Code. Just select path to python.exe in .venv folder)
```
# In Ubuntu
python3 -m venv .venv
source venv/bin/activate
# In Windows
python -m venv .venv
.\.venv\Scripts\activate
```
3. To install all the required libraries run,

```
pip install -r requirements.txt
# or run
python3 -m pip install -r requirements.txt
```
4. Run main.py

# Maze Solver Django Project

This Django project contains a maze solver code. It is built using Python 3.8.10, so ensure that this specific version of Python is installed before running the project. Some parts of the code rely on features available only in Python 3.8.10, and using a different version may cause the project to fail.

## Project Explanation

The project utilizes an ASCII representation of a maze stored in the `maze.txt` file. The `maze.txt` file serves as input for the `maze.py` code, which employs the Breadth-First Search (BFS) algorithm to find the shortest path within the maze. BFS is chosen over Depth-First Search (DFS) because it provides better efficiency in finding the shortest path and does not explore larger paths before discovering the solution.

The project includes a `tests.py` file, which contains unit tests. You can run the tests using the command `python3 tests.py`. Make sure the `unittest` package is installed.

The `templates` directory contains HTML templates that facilitate passing the context from views to the frontend. The templates utilize loops and conditional statements to render the maze appropriately, replicating how it would appear in the terminal.

## Steps to Run the Project

Follow these steps to run the project:

1. Install `virtualenv` and create a new virtual environment. Activate the environment located in the `labyrinth_project` folder.
2. Install the project requirements by running the command `pip install -r requirements.txt` (ensure you are in the `labyrinth_project` folder).
3. Start the Django development server by executing `python manage.py runserver`.
4. Visit the following URL in your web browser: [http://127.0.0.1:8000/solve-labyrinth/](http://127.0.0.1:8000/solve-labyrinth/)





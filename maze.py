import copy

class Labyrinth:
    def __init__(self, maze_file):
        self.maze = self._load_maze(maze_file)
        self._solution = None

    def _load_maze(self, maze_file):
        with open(maze_file, 'r') as file:
            return [list(line.strip()) for line in file]

    @property
    def solution(self):
        return self._solution

    def show(self):
        for row in self.maze:
            print(''.join(row))
        
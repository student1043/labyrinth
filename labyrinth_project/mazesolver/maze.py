from collections import deque

class Labyrinth:
    def __init__(self, filename):
        self.maze = self.load_maze(filename)
        self.solution = []

    def load_maze(self, filename):
        with open(filename, 'r') as file:
            maze = [list(line.strip()) for line in file]
        return maze

    def show(self, show_solution=False):
        if show_solution:
            maze_copy = [row.copy() for row in self.maze]
            for x, y in self.solution:
                maze_copy[y][x] = '*'
            for row in maze_copy:
                print(''.join(row))
        else:
            for row in self.maze:
                print(''.join(row))

    def solve(self):
        start = self.find_start()
        end = self.find_end()
        visited = set()
        parents = {}
        queue = deque([start])
        found = False

        while queue:
            current = queue.popleft()
            if current == end:
                found = True
                break

            visited.add(current)
            x, y = current

            for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x = x + move[0]
                new_y = y + move[1]

                if (
                    0 <= new_x < len(self.maze[0])
                    and 0 <= new_y < len(self.maze)
                    and self.maze[new_y][new_x] != '#'
                    and (new_x, new_y) not in visited
                ):
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
                    parents[(new_x, new_y)] = current

        if found:
            self.solution = self.build_path(parents, start, end)
        else:
            self.solution = []

        return self.solution




    def find_start(self):
        for y, row in enumerate(self.maze):
            for x, box in enumerate(row):
                if box == 'S':
                    return (x, y)

    def find_end(self):
        for y, row in enumerate(self.maze):
            for x, box in enumerate(row):
                if box == 'E':
                    return (x, y)

    def build_path(self, parents, start, end):
        path = []
        current = end

        while current != start:
            path.append(current)
            current = parents[current]

        path.append(start)
        return path[::-1]

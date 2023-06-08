import unittest
from maze import Labyrinth

class LabyrinthTests(unittest.TestCase):
    def test_constructor(self):
        labyrinth = Labyrinth("maze.txt")
        self.assertIsNotNone(labyrinth.maze)
        self.assertEqual(len(labyrinth.maze) + 1, 10)

        with self.assertRaises(FileNotFoundError):
            Labyrinth("non_existing_maze.txt")

    def test_show(self):
        labyrinth = Labyrinth("maze.txt")
        labyrinth.show()

        labyrinth.solve()
        labyrinth.show(show_solution=True)

    def test_solve(self):
        labyrinth = Labyrinth("maze.txt")
        solution = labyrinth.solve()
        self.assertIsNotNone(solution)
        self.assertIsInstance(solution, list)

        labyrinth_no_path = Labyrinth("maze_with_no_path.txt")
        solution_not_found = labyrinth_no_path.solve()
        self.assertEqual(solution_not_found, [])

if __name__ == '__main__':
    unittest.main()

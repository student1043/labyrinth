from rest_framework.decorators import api_view
from rest_framework.response import Response
from .maze import Labyrinth
import os
from django.shortcuts import render

current_dir = os.path.dirname(os.path.abspath(__file__))

maze_file = os.path.join(current_dir, "maze.txt")

@api_view(['GET'])
def solve_labyrinth(request):
    labyrinth = Labyrinth(maze_file)
    solution = labyrinth.solve()

    for x, y in solution:
        labyrinth.maze[y][x] = '*'

    context = {
        'maze': labyrinth.maze,
    }
    return render(request, 'mazesolver/maze.html', context)

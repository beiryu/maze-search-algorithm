import matplotlib.pyplot as plt
from timeit import timeit
import sys


def visualize_maze(matrix, bonus, start, end, route=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    # 1. Define walls and array of direction based on the route
    walls = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 'x']

    if route:
        direction = []
        for i in range(1, len(route)):
            if route[i][0] - route[i - 1][0] > 0:
                direction.append('v')  # ^
            elif route[i][0] - route[i - 1][0] < 0:
                direction.append('^')  # v
            elif route[i][1] - route[i - 1][1] > 0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    # 2. Drawing the map
    ax = plt.figure(dpi=100).add_subplot(111)

    for i in ['top', 'bottom', 'right', 'left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls], [-i[0] for i in walls],
                marker='X', s=100, color='black')

    plt.scatter([i[1] for i in bonus], [-i[0] for i in bonus],
                marker='P', s=100, color='green')

    plt.scatter(start[1], -start[0], marker='*',
                s=100, color='gold')

    if route:
        for i in range(len(route) - 2):
            plt.scatter(route[i + 1][1], -route[i + 1][0],
                        marker=direction[i], color='silver')

    plt.text(end[1], -end[0], 'EXIT', color='red',
             horizontalalignment='center',
             verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')

    for _, point in enumerate(bonus):
        print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')


def read_file(file_name: str = 'maze.txt'):
    f = open(file_name, 'r')
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    if n_bonus_points != 0:
        for i in range(n_bonus_points):
            x, y, reward = map(int, next(f)[:-1].split(' '))
            bonus_points.append((x, y, reward))
    text = f.read()
    matrix = [list(i) for i in text.splitlines()]
    f.close()
    return bonus_points, matrix

def maze_map_render(grid):
    """
    render 1 mảng lưới các điểm trên bản đồ thành các key => value, với key là 1 điểm trên lưới và value là {W: 0, N: 1. E: 1, S: 0}
    với 0 là tường, 1 là có thể đi
    :param grid: là 1 mảng các điểm tọa đọ
    :return:
    """
    maze_map = {cell: {'E': 0, 'W': 0, 'N': 0, 'S': 0} for cell in grid}
    for cell in maze_map:

        if cell[0] != 0 and cell[0] != len(matrix) - 1:
            if cell[1] != 0 and cell[1] != len(matrix[0]) - 1:
                if matrix[cell[0]][cell[1] + 1] != 'x':
                    maze_map[cell]['E'] = 1
                if matrix[cell[0]][cell[1] - 1] != 'x':
                    maze_map[cell]['W'] = 1
                if matrix[cell[0] - 1][cell[1]] != 'x':
                    maze_map[cell]['N'] = 1
                if matrix[cell[0] + 1][cell[1]] != 'x':
                    maze_map[cell]['S'] = 1
    return maze_map



def dfs(matrix, start, end):
    grid = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
    maze_map = maze_map_render(grid)

    explored = [start]
    frontier = [start]

    dfsPath = {}
    while len(frontier) > 0:
        currCell = frontier.pop()
        if currCell == end:
            break
        for d in 'ESNW':
            if maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currCell
    fwdPath = {}
    cell = end
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath, dfsPath


if __name__=='__main__':

    file_name = sys.argv[1]
    bonus_points, matrix = read_file(file_name)

    print(bonus_points)
    print(f'The height of the matrix: {len(matrix)}')
    print(f'The width of the matrix: {len(matrix[0])}')

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)

            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
            else:
                pass

    fwdPath, aPath = dfs(matrix, start, end)
    route = [end, *fwdPath][::-1]
    t = timeit(stmt='dfs(matrix, start, end)', number=1000, globals=globals())
    print(f'DFS time: {t}')
    print(f'DFS search length: {len(aPath)}')
    print(f'DFS path length: {len(fwdPath)}')
    print(f'The way to the destination: {route}')
    visualize_maze(matrix,bonus_points,start,end, route)
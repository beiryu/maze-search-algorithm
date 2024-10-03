# Maze Search Algorithm

This project implements various search algorithms to find the optimal path through a maze with bonus points.

![Maze Example](https://github.com/beiryu/maze-search-algorithm/blob/main/map-view.png?raw=true)

## Overview

The maze is represented as a 2D grid where:
- `S`: Starting position
- `x`: Walls (impassable)
- `+`: Bonus points (reduce path cost)
- `exit`: Goal position (unique)

The agent can move up, down, left, or right with equal cost.

## Implemented Algorithms

### Uninformed Search
- Depth First Search (DFS)
- Breadth First Search (BFS)

### Informed Search
- Greedy Best First Search
- A* Search

## Maze File Format

Each maze file follows this structure:
1. First line: Number of bonus points (n)
2. Next n lines: `x y z` (x,y coordinates and z value of bonus point)
3. Remaining lines: Maze layout
   - `S`: Start position
   - `x`: Walls
   - `+`: Bonus points
   - The exit is implicitly defined (e.g., position [2,0] in the example image)

## Usage

Run the algorithms using the following command structure:
- For algorithms with heuristics:
  ```bash
  python3 [algorithm].py [map].txt [heuristic]
  ```

- For algorithms without heuristics:
  ```bash
  python3 [algorithm].py [map].txt
  ```

- For algorithms with heuristics:
  ```bash
  python3 [algorithm].py [map].txt [heuristic]
  ```

- For maps with bonus points:
  ```bash
  python3 [algorithm].py [map].txt
  ```

Replace `[algorithm]`, `[map]`, and `[heuristic]` with appropriate filenames.

## Installation

[Add installation instructions here]

## Requirements

[List any dependencies or system requirements]

## Contributing

[Add contribution guidelines here]

## License

[Add license information here]

## Acknowledgements

[Add any acknowledgements or credits here]

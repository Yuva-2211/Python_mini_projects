import time

class Node: #creates a class for node
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier: #creates a class which has all StackFrontier actions 
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):#creates a class which has all QueueFrontier actions
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Maze: #class defines the processing of maze
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:#checks for maze's starting point does it have only one or not 
            raise Exception("Maze must have exactly one starting point")
        if contents.count("B") != 1:#checks for maze's goal point does it have only one or not
            raise Exception("Maze must have exactly one goal")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None
        self.exploration_history = []

    def print(self, show_solution=False):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("#", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                elif (i, j) in self.exploration_history:
                    print(".", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row-1, col)),
            ("down", (row+1, col)),
            ("left", (row, col-1)),
            ("right", (row, col+1))
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self, algorithm="dfs"):
        self.num_explored = 0
        self.exploration_history = []

        start = Node(state=self.start, parent=None, action=None)

        if algorithm == "dfs":
            frontier = StackFrontier()
        elif algorithm == "bfs":
            frontier = QueueFrontier()
        else:
            raise ValueError("Algorithm must be 'dfs' or 'bfs'")

        frontier.add(start)
        self.explored = set()

        while True:
            if frontier.empty():
                print("Frontier is empty, no solution found!")
                raise Exception("No solution")
            
            node = frontier.remove()
            self.num_explored += 1

            # Print current node state for debugging
            print(f"Exploring node at state: {node.state}")

            # Record state for visualization
            self.exploration_history.append(node.state)

            # Visualize after each step
            self.print()

            if node.state == self.goal:
                actions = []
                cells = []

                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent

                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                print("Solution found!")
                return

            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

# Running the maze solver with visualization
if __name__ == "__main__":
    maze = Maze("maze1.txt")  
    maze.solve("dfs")  # Use "bfs" for Breadth-First Search or "dfs" for Depth-First Search

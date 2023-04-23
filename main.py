import numpy as np
import heapq
from collections import deque


# Task 1

# Request 1. Data structure to represent and construct the treasure map
treasure_map = {"starting_point": [("stormy_ocean", 4), ("forest", 7)],
                "stormy_ocean": [("stormy_ocean", 20), ("desert", 4)],
                "forest": [("treasure", 4)],
                "desert": [("treasure", 10)],
                "treasure": []}

heuristic = {"starting_point": 1, "stormy_ocean": 2, "forest": 3, "desert": 3, "treasure": 0}



# Request 2a. Apply Uniform cost search find the cheapest path to the treasure.
def uniform_cost_search(graph, start, goal):
    print("Applying UCS:")

    # Priority queue of (priority, node, path).
    # Initially, it only includes the start state <=> starting point.
    frontier = [(0, start, [])]
    # explored will keep track of the explored nodes
    explored = set()

    print("Starting point: Cost is 0")

    # The while loop continues until the frontier queue becomes empty
    # (i.e., there are no more nodes to explore). Or, it is also possible
    # to end the loop if we already reached our goal.
    while frontier:
        # we pop the first element of the frontier list because it is the one with
        # minimum cost. Next, we will explore its neighbors.
        (priority, current, path) = heapq.heappop(frontier)

        # check if we got to the goal. if so, end the loop and return the path to the goal
        if current == goal:
            print("Solution Path:  ", "-> ".join(str(state) for state in path+[current]), " with total cost", priority)
            return path + [current]

        # if it is already explored, it means that we already added its
        # neighbors to the heap, so we can continue.
        if current in explored:
            continue

        explored.add(current)

        # remember to add the neighbors of the recently explored node.
        # check the treasure_map to find the neighbors and their respective costs
        for neighbor, cost in graph[current]:
            if neighbor not in explored:
                print(current, "-", neighbor, ": Cost is", priority+cost)
                heapq.heappush(frontier, (priority + cost, neighbor, path + [current]))

    # note the Completeness property: if there is a solution, the algorithm finds it, otherwise
    # it reports failure, which is returning none.
    return None

#solution = uniform_cost_search(treasure_map, "starting_point", "treasure")

# Request 2b. Apply A* to find the cheapest path to the treasure.
def a_star_search(graph, start, goal):

    # unlike uniform cost search, where the cost of the starting_point is zero,
    # in a* search, the cost of the starting_point should take its heuristic into account.
    frontier = [(heuristic[start], start, [])]
    # explored will keep track of the explored nodes
    explored = set()

    print("Applying A* search: ")

    while frontier:
        # we pop the first element of the frontier list because it is the one with
        # minimum cost. Next, we will explore its neighbors.
        (priority, current, path) = heapq.heappop(frontier)

        # check if we got to the goal. if so, end the loop and return the path to the goal
        if current == goal:
            print("Solution Path:  ", "-> ".join(str(state) for state in path+[current]), " with total cost", priority)
            return path + [current]

        # if it is already explored, it means that we already added its
        # neighbors to the heap, so we can continue.
        if current in explored:
            continue

        explored.add(current)

        # remember to add the neighbors of the recently explored node.
        # check the treasure_map to find the neighbors and their respective costs
      
        for neighbor, cost in graph[current]:
            if neighbor not in explored:

                # the total cost equals the cost to get to the node from the start plus its own heuristic
                print(current, "-", neighbor, ": Cost is", priority+cost - heuristic[current])
                heapq.heappush(frontier, (priority + cost - heuristic[current] + heuristic[neighbor], neighbor, path + [current]))

            print(frontier)

    return None

# path = a_star_search(treasure_map, "starting_point", "treasure")

# Task 2

# For creating the maze, take the coordinates of the start and finish from the user
# assume that indeces start from (0,0) => top left  &  (n,n) => bottom right.
# First, make sure that start and finish coordinates are valid and are within the maze.



# Request 2 - Breadth First Search:
def bfs(graph, start, finish):
    # Keep track of visited nodes to avoid infinite loops and duplicate visits
    visited = set()
    # Use a queue to implement BFS. deque => double-ended queue
    queue = deque([(start, [start])]) # tuple contains current node and its path
    # Mark the start node as visited
    visited.add(start)

    # Iterate over the queue until it is empty
    while queue:
        # Dequeue the node at the front of the queue and its path
        vertex, path = queue.popleft()
        # If we have reached the finish node, return the path to it
        if vertex == finish:
            return path
        # Otherwise, explore the neighbors of the current node
        for neighbor in graph[vertex]:
            # If we haven't visited the neighbor yet, mark it as visited and add it to the queue
            if neighbor not in visited:
                visited.add(neighbor)
                # Append the neighbor to the current path to get the path to the neighbor
                queue.append((neighbor, path + [neighbor]))

    # If we have explored the entire graph and haven't found the finish node, return None
    return None


# Define the Manhattan distance heuristic function to be used for the A* Search algorithm.
def manhattan_distance(point1, point2):
    # It calculates the absolute difference between the x
    # and y coordinates of the two points and returns their sum.
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)


def extract_coordinates(str1):

    start_index = str1.find("(")
    end_index = str1.find(")")

    # Extract the substring containing the tuple values
    tuple_str = str1[start_index:end_index+1]
    # Split the tuple string into individual values
    tuple_values = tuple_str.strip("()").split(",")
    # Convert the tuple values to integers and return the tuple
    return tuple(map(int, tuple_values))


def graph_from_file(filename):
    
   # Open the file
   with open(filename, 'r') as file:
    # Read the lines of the file
    lines = [line.strip() for line in file.readlines()]

    # Extract the start and end points as strings from the last two lines
    start_str = lines[-2]
    end_str = lines[-1]
    
    start = extract_coordinates(start_str)
    end = extract_coordinates(end_str)
    print(lines[:-2])
    maze = {}
    heuristic = {}

    for line_num in range(len(lines[:-3])):
        # represents either a wall or a pathway so just ignore it while creating the graph
        if line_num % 2 == 1:
            continue

        for char_num in range(len(lines[line_num])):
            if char_num % 2 == 1:
                continue
            # we divide the manhattan distance by 2 because the walls and pathways shouldn't be counted
            # while calculating the distance
            heuristic[(line_num, char_num)] = manhattan_distance((line_num, char_num), end) / 2
            maze[(line_num, char_num)] = []

            # if it is the right-most, don't check for the neighbors to the right
            if char_num != (len(lines[line_num]) - 1):
                if lines[line_num][char_num + 1] == '*':
                    maze[(line_num, char_num)].append(((line_num, char_num+2), int(lines[line_num][char_num + 2])))

            # if it is the left-most, don't check for the neighbors to the left
            if char_num != 0:
                if lines[line_num][char_num - 1] == '*':
                    maze[(line_num, char_num)].append(((line_num, char_num-2), int(lines[line_num][char_num - 2])))

            # if it is the bottom-most, don't check for the neighbors to the bottom
            if line_num != (len(lines[:-3]) - 1):
                if lines[line_num+1][char_num] == '*':
                    maze[(line_num, char_num)].append(((line_num+2, char_num), int(lines[line_num+2][char_num])))

            # if it is the top-most, don't check for the neighbors to the top
            if line_num != 0:
                if lines[line_num-1][char_num] == '*':
                    maze[(line_num, char_num)].append(((line_num-2, char_num), int(lines[line_num-2][char_num])))

    return maze, heuristic, start, end

# Version 2 of A* search
def a_star_updated(filename):
    graph, heuristic, start, goal = graph_from_file(filename)
    print(graph)
    print(heuristic)
    print(start)
    print(goal)

    # unlike uniform cost search, where the cost of the starting_point is zero,
    # in a* search, the cost of the starting_point should take its heuristic into account.
    frontier = [(heuristic[start], start, [])]
    # explored will keep track of the explored nodes
    explored = set()

    print("Applying A* search: ")

    while frontier:
        # we pop the first element of the frontier list because it is the one with
        # minimum cost. Next, we will explore its neighbors.
        (priority, current, path) = heapq.heappop(frontier)

        # check if we got to the goal. if so, end the loop and return the path to the goal
        if current == goal:
            print("Solution Path:  ", "-> ".join(str(state) for state in path + [current]), " with total cost",
                  priority)
            return path + [current]

        # if it is already explored, it means that we already added its
        # neighbors to the heap, so we can continue.
        if current in explored:
            continue

        explored.add(current)

        # remember to add the neighbors of the recently explored node.
        # check the treasure_map to find the neighbors and their respective costs

        for neighbor, cost in graph[current]:
            if neighbor not in explored:
                # the total cost equals the cost to get to the node from the start plus its own heuristic
                print(current, "-", neighbor, ": Cost is", priority + cost - heuristic[current])
                heapq.heappush(frontier,
                               (priority + cost - heuristic[current] + heuristic[neighbor], neighbor, path + [current]))

            print(frontier)

    return None


a_star_updated("maze.txt")
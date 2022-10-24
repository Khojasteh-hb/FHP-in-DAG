# Python program to create a labeled directed acyclic graph (DAG)
# In this DAG edge labels represent scores and range from zero to one.
# Finding the highest of all possible paths.

# Import required libraries
import sys
import math

class edge(object):
    def __init__(self, from_vertex, to_vertex, weight):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    def __str__(self):
        return str(self.to_vertex)

    def __repr__(self):
        return str(self.to_vertex)


class vertex(object):
    def __init__(self, name):
        self.name = name
        self.color = "white"
        self.discovery = 0
        self.finish = None
        self.distance = math.inf
        self.num_of_paths = 0

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class adjacency_list(dict):
    # initialize all the edgelists to len 0
    def __init__(self, num_of_vertices, num_of_edges):
        self.num_of_vertices = num_of_vertices
        self.num_of_edges = num_of_edges
        for i in range(1, num_of_vertices + 1):
            self[i] = []

    def add_edge(self, an_edge_object):
        self[an_edge_object.from_vertex].append(an_edge_object)


class paths_list(object):
    def __init__(self, a_graph, vertex_of_interest):
        self.distance = []
        self.vertices = []
        self.vertex_of_interest = vertex_of_interest
        self.topo_sort = []

        for i in range(a_graph.num_of_vertices):
            self.distance.append(math.inf)
            self.vertices.append(vertex(i + 1))


############# end class definitions #########################################################

############# begin function definitions ####################################################

def dfs_visit(a_graph, a_path_list, a_vertex, time):
    time += 1
    a_vertex.color = "grey"
    a_vertex.discovery = time
    for a_edge in a_graph[a_vertex.name]:
        new_vertex = a_edge.to_vertex
        new_vertex = a_path_list.vertices[new_vertex - 1]
        if new_vertex.color == "white":
            dfs_visit(a_graph, a_path_list, new_vertex, time)
    a_vertex.color = "black"
    a_vertex.finish = time
    a_path_list.topo_sort.insert(0, a_vertex)


def dfs_toposort(a_graph, a_path_list):
    time = 0

    for i in range(len(a_path_list.vertices)):

        a_vertex = a_path_list.vertices[i]

        if a_vertex.color == "white":
            dfs_visit(a_graph, a_path_list, a_vertex, time)


def longest_or_shortest_path(a_graph, a_path_list, node_n, longest=True):

    start_vertex = a_path_list.vertex_of_interest

    index_counter = 0
    for item in a_path_list.topo_sort:
        if item.name == start_vertex:
            break
        index_counter += 1

    index_of_start = index_counter

    a_path_list.topo_sort[index_of_start].distance = 0
    a_path_list.topo_sort[index_of_start].num_of_paths = 1

    if longest:
        x = -1
    else:
        x = 1

    change_occured = True

    while change_occured:
        change_occured = False

        for i in range(0, len(a_path_list.topo_sort)):
            for edge in a_graph[a_path_list.topo_sort[i].name]:
                if a_path_list.vertices[edge.to_vertex - 1].distance > edge.weight * x + a_path_list.topo_sort[i].distance:

                    a_path_list.vertices[edge.to_vertex - 1].distance = edge.weight * x + a_path_list.topo_sort[i].distance

                    change_occured = True

    value_of_longest_path = a_path_list.topo_sort[-1].distance * x

    #### now try to determine the amount of longest paths ####

    for i in range(0, len(a_path_list.topo_sort)):

        for a_edge in a_graph[a_path_list.topo_sort[i].name]:
            if a_path_list.vertices[a_edge.from_vertex - 1].distance * x == a_path_list.vertices[
                a_edge.to_vertex - 1].distance * x - a_edge.weight:
                a_path_list.vertices[a_edge.to_vertex - 1].num_of_paths += a_path_list.vertices[
                    a_edge.from_vertex - 1].num_of_paths

    number_of_longest_paths = a_path_list.topo_sort[-1].num_of_paths

    return value_of_longest_path, number_of_longest_paths


def collect_graph(file_pointer):
    first_line = file_pointer.readline()
    first_line = first_line.split()
    num_of_vertices, num_of_edges = int(first_line[0]), int(first_line[1])

    if (num_of_vertices <=0):
        # exits the program
        print("The number of vertices less than or equal zero, is not allowed")
        return False

    elif (num_of_edges <= 0):
        # exits the program
        print("The number of edges less than or equal zero, is not allowed")
        return False

    else:
        the_graph = adjacency_list(num_of_vertices, num_of_edges)

        for i in range(num_of_edges):
            split_line = file_pointer.readline().split()
            from_vertex, to_vertex, weight = int(split_line[0]), int(split_line[1]), float(split_line[2])

            if (from_vertex not in range(1, num_of_vertices + 1)):
                # exits the program
                print("The source vertex is not in range")
                return False

            elif (to_vertex not in range(1, num_of_vertices + 1)):
                # exits the program
                print("The destination vertex is not in range")
                return False

            elif ((weight<=0) or (weight>=1)):
                # exits the program
                print("The weight is not in range")
                return False

            else:
                the_edge = edge(from_vertex, to_vertex, weight)
                the_graph.add_edge(the_edge)

    return the_graph

def main():

    file = sys.stdin

    the_graph = collect_graph(file)

    if(not(the_graph)):
        sys.exit()

    node_n = len(the_graph)

    the_paths_list = paths_list(the_graph, 1)

    dfs_toposort(the_graph, the_paths_list)

    value_of_longest_path, number_of_longest_paths = longest_or_shortest_path(the_graph, the_paths_list, node_n)

    distances = []

    num_of_paths = []

    for i in range(len(the_paths_list.topo_sort)):
        distances.append(the_paths_list.topo_sort[i].distance)

    print("The value of longest path is:", value_of_longest_path)

    print("The longest path is:", the_paths_list.topo_sort)


if __name__ == "__main__":
    main()
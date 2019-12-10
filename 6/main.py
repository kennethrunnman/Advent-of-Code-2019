def read_file():
    f = open("input.txt","r")
    contents = f.readlines()
    return contents

def create_graph(contents):
    graph = {}
    for line in contents:
        relation = line.split(")")
        a = relation[0].strip()
        b = relation[1].strip()
        if b in graph.keys():
            graph[b].append(a)
        else:
            graph[b] = []
            graph[b].append(a)
    return graph

def create_graph2(contents):
    graph = {}
    for line in contents:
        relation = line.split(")")
        a = relation[0].strip()
        b = relation[1].strip()
        if b in graph.keys():
            graph[b].append(a)
        else:
            graph[b] = []
            graph[b].append(a)
        if a in graph.keys():
            graph[a].append(b)
        else:
            graph[a] = []
            graph[a].append(b)
    return graph

def calculate_orbits(graph):
    counter = 0
    stack = []
    for o in graph:
        stack.append(o)
        while(len(stack) > 0):
            current = stack.pop()
            if not current in graph.keys():
                continue
            else:
                counter += 1
                for n in graph[current]:
                    stack.append(n)
    print(counter)

def find_san(graph):
    visited = []
    counter = 0
    stack = []
    o = "YOU"
    stack.append(o)
    counter_dict = {}
    counter_dict[o] = 0
    while(len(stack) > 0):
        current = stack.pop()
        counter = counter_dict[current]
        print("current", current)
        print("counter", counter)
        if "SAN" in current:
            break
        elif current not in graph.keys() or current in visited:
            continue
        else:
            visited.append(current)
            counter += 1
            for n in graph[current]:
                if n not in visited:
                    stack.append(n)
                    counter_dict[n] = counter
    print(counter-2)


def main():
    contents = read_file()
    graph = create_graph(contents)
    #calculate_orbits(graph)
    graph2 = create_graph2(contents)
    find_san(graph2)
main()

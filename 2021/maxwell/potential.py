import random

from manim import *


import networkx as nx


def generate_link(number):
    a = random.randint(1,number)
    b = random.randint(1,number)
    if a == b:
        return generate_link(number)
    else: return (a, b)

def go_through_the_edge(edge, a):
    if edge.index(a) == 0:
        return edge[1]
    else: return edge[0]

def go_through_the_graph(edges, a, b):
    for x in edges:
        if a in x and b not in x:
            return x

def generate_random_path(edges, selected_edges, selected):
    random_path = []
    initial = selected_edges[0]
    finish = random.choice(random.choice(edges))
    random_path.append(initial)
    print(finish, initial)

    start = go_through_the_graph(edges, go_through_the_edge(initial, selected), selected)
    if start == None or finish == go_through_the_edge(initial, selected):
        return random_path

    x = initial
    step = 0

    while step < 5:
        start = x
        x = go_through_the_graph(edges, go_through_the_edge(start, selected), selected)
        selected = go_through_the_edge(start, selected)
        if (x is None):
            break
        print('step:', x)
        random_path.append(x)
        step += 1
    return random_path

class brain1(Scene):
    def construct(self):
        brain4 = SVGMobject('/Users/isaigordeev/Desktop/УЧЕБА/lll/ПОСТЕР/brain4.svg').scale(2.5)
        brain4inner = SVGMobject('/Users/isaigordeev/Desktop/УЧЕБА/lll/ПОСТЕР/brainnet.svg').scale(0.8)
        # self.add(brain4inner.set_color(BLUE))

        self.add(brain4)
        number_vertex = 15

        nxgraph = nx.erdos_renyi_graph(number_vertex, 0.5)
        G = Graph.from_networkx(nxgraph, layout="spring")
        # vertices = [x+1 for x in range(number_vertex)]
        # edges = [generate_link(number_vertex) for x in range(random.randint(number_vertex, number_vertex*3))]


        autolayouts = "spring"

        # random_path = generate_random_path(G.edges, selected_edges, selected)
        # print(random_path)



        # edge_config = {x: {"stroke_color": BLUE} for x in selected_edges}

        # graph1 = Graph(vertices, edges,
        #                 layout=autolayouts,
        #                 layout_scale= 3,
        #                 # labels=True,
        #                 vertex_config={selected: {"fill_color": BLUE}},
        #                 edge_config=edge_config)



        for x,dot in enumerate(G.vertices):
            G[dot].move_to(random.choice(brain4inner.get_points_defining_boundary()))

        to_delete = []
        for x in G.edges:
            if not Exclusion(G.edges[x],brain4):
                to_delete.append(x)

        G.remove_edges(*to_delete)
        edges_existing = []
        for x in G.edges:
            if x[0] not in edges_existing:
                edges_existing.append(x[0])
            if x[1] not in edges_existing:
                edges_existing.append(x[1])

        to_delete_vertices = []
        for x in G.vertices:
            if x not in edges_existing:
                to_delete_vertices.append(x)

        G.remove_vertices(*to_delete_vertices)

        selected = random.choice(edges_existing)
        selected_edges = []


        for x in G.edges:
            if selected in x:
                selected_edges.append(x)

        selected_lines = []
        for x in G.edges:
            if selected in x:
                selected_lines.append(G.edges[x])


        self.play(Create(G))
        self.wait()
        self.play(G.vertices[selected].animate.set_color(RED))
        self.play(*[x.animate.set_color(RED) for x in selected_lines])

        self.wait()

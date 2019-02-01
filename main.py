import csv
import networkx
import matplotlib.pyplot


def prepareEdges(input_files):
    edges = []

    for input_file in input_files:
        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            parsed_list = list(reader)
            for item in parsed_list:
                edge_name = input_file.replace('.csv', '')
                edges.append((edge_name, item[1], int(item[0])))

    return edges


def saveGraphToFile(graph, filename):
    matplotlib.pyplot.figure(figsize=(25, 25))
    options = {'edge_color': '#BBBBBB', 'width': 1, 'with_labels': True, 'node_color': 'blue'}

    sizes = [sum(c[2]['weight'] for c in graph.edges(node, data=True)) for node in graph]
    positions = networkx.spring_layout(graph, k=0.2, iterations=500)

    networkx.draw(graph, pos=positions, node_size=sizes, **options)
    matplotlib.pyplot.savefig(filename)


def main():
    input_files = [
        'data/tluszcz/jedzenie.csv',
        'data/tluszcz/maslo.csv',
        'data/tluszcz/mieso.csv',
        'data/tluszcz/tluszcz.csv'
    ]

    edge_list = prepareEdges(input_files)

    G = networkx.Graph()
    G.add_weighted_edges_from(edge_list)

    print(G.edges)

    saveGraphToFile(G, "tluszcz_graph.png")


if __name__ == '__main__':
    main()

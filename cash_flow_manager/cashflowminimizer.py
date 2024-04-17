from flask import request, render_template, Blueprint, jsonify
from cash_flow_manager.transaction_minimizer import cash_flow_minimizer
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import base64
matplotlib.use('Agg')
import os


cashflowminimizer = Blueprint("cashflowminimizer", __name__,static_folder="static", template_folder="templates")


def add_edge(graph, source, target, weight):
    graph.add_edge(source, target, weight=weight)


def generate_graph_image(edges):
    fig, ax = plt.subplots()

    # Create a directed graph
    G = nx.DiGraph()

    added_edges = set()  # To keep track of added edges

    for edge in edges:
        if edge[0] != edge[1]:  # Avoid self-loops
            add_edge(G, *edge)
            added_edges.add((edge[0], edge[1]))  # Add edge to set


    # Draw the weighted graph onto the Matplotlib figure
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='#135c66', node_size=1500, font_size=12, font_color='white', font_weight='bold')

    # Draw edge labels
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Save the generated graph image
    cwd = os.getcwd()
    image_path = os.path.join(cwd, 'cash_flow_manager', 'static', 'graph.png')
    plt.savefig(image_path)

    # Close the Matplotlib figure
    plt.close(fig)

    return image_path


@cashflowminimizer.route('/')
def home():
    return render_template('index2.html')

@cashflowminimizer.route('/min-flow', methods=['POST'])
def getminFlow():
    if request.method == 'POST':
        data = request.json
        print(data)
        transactions = []

        for transaction in data['transactions']:
            curr_trans = []
            curr_trans.append(transaction['payer'])
            curr_trans.append(transaction['payee'])
            curr_trans.append(transaction['amount'])
            transactions.append(curr_trans)

        print(transactions)
        # output_data = [(item[0], item[1], item[2]) for item in transactions]
        result = cash_flow_minimizer(transactions)
        result_tuples = [(item.split()[0], item.split()[-1], float(item.split()[2])) for item in result]  # Convert amount to float
        print(result_tuples)
        image_path = generate_graph_image(result_tuples)


        with open(image_path, "rb") as img_file:
            image_data = img_file.read()
            base64_encoded_image = base64.b64encode(image_data).decode('utf-8')

        # Prepare JSON response
        response_data = {
            'result': result,
            'image_base64': base64_encoded_image
        }



    print(response_data)
    return jsonify(response_data)

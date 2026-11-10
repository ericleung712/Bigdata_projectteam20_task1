from graphviz import Digraph


def visualize_tree(node, graph, feature_names=None, label_mapping=None, parent=None, edge_label=None):
    node_id = str(id(node))
    if node.is_leaf_node():
        leaf_text = label_mapping.get(node.value, node.value) if label_mapping else node.value
        graph.node(node_id, label=str(leaf_text), fillcolor="#dcfce7")
    else:
        feature_name = feature_names[node.feature_index] if feature_names is not None else f"X[{node.feature_index}]"
        graph.node(node_id, label=f"{feature_name} <= {node.threshold:.2f}", fillcolor="#dbeafe")

    if parent is not None:
        graph.edge(str(id(parent)), node_id, label=edge_label)

    if not node.is_leaf_node():
        visualize_tree(node.left, graph, feature_names, label_mapping, node, "yes")
        visualize_tree(node.right, graph, feature_names, label_mapping, node, "no")
    return graph


def visualize_decision_tree(tree_model, feature_names=None, label_mapping=None):
    if tree_model.root is None:
        raise ValueError("The decision tree must be fitted before it can be visualized.")

    graph = Digraph(
        graph_attr={"rankdir": "TB"},
        node_attr={"shape": "box", "style": "rounded,filled", "fontname": "Arial"},
        edge_attr={"fontname": "Arial"},
    )
    visualize_tree(tree_model.root, graph, feature_names, label_mapping)
    return graph

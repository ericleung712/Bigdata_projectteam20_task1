import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def visualize_decision_tree(tree_model, feature_names=None, label_mapping=None):
    if tree_model.root is None:
        raise ValueError("The decision tree must be fitted before it can be visualized.")

    positions = {}
    nodes = []
    edges = []
    next_leaf_position = [0]
    max_depth = [0]

    def layout(node, depth):
        max_depth[0] = max(max_depth[0], depth)
        nodes.append(node)
        if node.is_leaf_node():
            x_position = next_leaf_position[0]
            next_leaf_position[0] += 1
        else:
            left_position = layout(node.left, depth + 1)
            right_position = layout(node.right, depth + 1)
            x_position = (left_position + right_position) / 2
            edges.extend([(node, node.left), (node, node.right)])
        positions[id(node)] = (x_position, -depth)
        return x_position

    layout(tree_model.root, 0)
    leaf_count = max(next_leaf_position[0], 1)
    figure_width = min(24, max(8, leaf_count * 0.55))
    figure_height = min(16, max(4, (max_depth[0] + 1) * 1.1))
    figure, axis = plt.subplots(figsize=(figure_width, figure_height))

    for parent, child in edges:
        parent_x, parent_y = positions[id(parent)]
        child_x, child_y = positions[id(child)]
        axis.annotate(
            "",
            xy=(child_x, child_y + 0.12),
            xytext=(parent_x, parent_y - 0.12),
            arrowprops={"arrowstyle": "->", "color": "#64748b", "linewidth": 0.8},
        )

    for node in nodes:
        x_position, y_position = positions[id(node)]
        if node.is_leaf_node():
            label = label_mapping.get(node.value, node.value) if label_mapping else node.value
            text = str(label)
            facecolor = "#dcfce7"
        else:
            if feature_names is None:
                feature_name = f"X[{node.feature_index}]"
            else:
                feature_name = feature_names[node.feature_index]
            text = f"{feature_name} <= {node.threshold:.2f}"
            facecolor = "#dbeafe"
        axis.text(
            x_position,
            y_position,
            text,
            ha="center",
            va="center",
            fontsize=7,
            bbox={"boxstyle": "round,pad=0.3", "facecolor": facecolor, "edgecolor": "#475569"},
        )

    axis.set_xlim(-1, leaf_count)
    axis.set_ylim(-max_depth[0] - 1, 1)
    axis.axis("off")
    figure.tight_layout()
    return figure

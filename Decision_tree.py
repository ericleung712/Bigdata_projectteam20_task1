import numpy as np

def entropy(Y):
    p = np.bincount(Y, minlength=4) / len(Y)
    p = p[p > 0]
    return -np.sum(p * np.log2(p))

def gini(Y):
    p = np.bincount(Y, minlength=4) / len(Y)
    return 1.0 - np.sum(p ** 2)

def information_gain(X, Y, f, t, impurity=entropy):
    left = X[:, f] <= t
    right = ~left
    if left.sum() == 0 or right.sum() == 0:
        return 0.0
    n = len(Y)
    children = (left.sum() / n) * impurity(Y[left]) + (right.sum() / n) * impurity(Y[right])
    return impurity(Y) - children

def best_split(X, Y, impurity=entropy, n_thresholds=10, min_samples_leaf=1):
    if n_thresholds < 1:
        raise ValueError("n_thresholds must be at least 1")
    if min_samples_leaf < 1:
        raise ValueError("min_samples_leaf must be at least 1")

    best_gain, best_f, best_t = -1.0, None, None
    # Keep the original quantile range, but make the number of candidate cut points tunable.
    quantiles = np.linspace(0.05, 0.95, n_thresholds)
    for f in range(X.shape[1]):
        for t in np.unique(np.quantile(X[:, f], quantiles)):
            left = X[:, f] <= t
            right = ~left
            # Reject splits that would create a child smaller than the requested minimum.
            if left.sum() < min_samples_leaf or right.sum() < min_samples_leaf:
                continue
            gain = information_gain(X, Y, f, t, impurity=impurity)
            if gain > best_gain:
                best_gain, best_f, best_t = gain, f, t
    return best_f, best_t, best_gain

class Node:
    def __init__(self, feature_index=None, threshold=None, left=None, right=None, value=None):
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    # Fixed naming from is_left_node to is_leaf_node
    def is_leaf_node(self):
        return self.value is not None

class Decision_Tree:
    def __init__(self, max_depth=10, min_samples_split=2, min_samples_leaf=5, n_thresholds=10):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.n_thresholds = n_thresholds
        self.root = None

    def fit(self, X, Y):
        # Convert inputs to numpy arrays for easier indexing
        self.root = self.build_tree(np.array(X), np.array(Y), depth=0)

    def build_tree(self, X, Y, depth):
        samples, features = X.shape
        labels = np.unique(Y)
        #labels, counts = np.unique(Y, return_counts=True)
        #majority_label = labels[np.argmax(counts)]

        # 1. Stopping criteria (also stop if all labels are the same)
        if (depth >= self.max_depth or samples < self.min_samples_split
                or samples < 2 * self.min_samples_leaf or len(labels) == 1):
            return Node(value=np.argmax(np.bincount(Y)))
            #return Node(value=majority_label)

        # 2. Find the best split
        best_f, best_t, best_gain = best_split(
            X, Y, n_thresholds=self.n_thresholds, min_samples_leaf=self.min_samples_leaf
        )

        # 3. If we can't improve, stop and return a leaf
        if best_f is None or best_gain <= 0:
            return Node(value=np.argmax(np.bincount(Y)))
            #return Node(value=majority_label)

        # 4. Split the data
        left_idxs = X[:, best_f] <= best_t
        right_idxs = ~left_idxs

        # 5. Recurse down the left and right branches
        left_child = self.build_tree(X[left_idxs, :], Y[left_idxs], depth + 1)
        right_child = self.build_tree(X[right_idxs, :], Y[right_idxs], depth + 1)

        # 6. Return the decision node
        return Node(feature_index=best_f, threshold=best_t, left=left_child, right=right_child)

    def predict(self, X):

        X_arr = np.array(X)
        return np.array([self.traverse_tree(x, self.root) for x in X_arr])

    def traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        if x[node.feature_index] <= node.threshold:
            return self.traverse_tree(x, node.left)
        return self.traverse_tree(x, node.right)

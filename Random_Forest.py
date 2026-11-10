import numpy as np
from Decision_tree import Decision_Tree

class Random_Forest:
    def __init__(self, n_trees=20, max_depth=10, min_samples_split=10,
           min_samples_leaf=1, n_thresholds=25, random_state=None):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.n_thresholds = n_thresholds
        self.random_state = random_state
        self._rng = np.random if random_state is None else np.random.RandomState(random_state)
        self.trees = []

    def fit(self, X, Y):
        self.trees = []
        # Reset a seeded generator for reproducible fits; keep NumPy's global RNG by default.
        if self.random_state is not None:
            self._rng = np.random.RandomState(self.random_state)
        X_arr = np.array(X)
        Y_arr = np.array(Y)
        for _ in range(self.n_trees):
            tree = Decision_Tree(
                max_depth=self.max_depth,
                min_samples_split=self.min_samples_split,
                min_samples_leaf=self.min_samples_leaf,
                n_thresholds=self.n_thresholds,
            )
            X_sample, Y_sample = self.bootstrap(X_arr, Y_arr)
            tree.fit(X_sample, Y_sample)
            self.trees.append(tree)

    def predict(self, X):
        if not self.trees:
            raise RuntimeError("The random forest must be fitted before prediction.")

        # Get predictions from all trees
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        # Swap axes to iterate over samples
        tree_preds = np.swapaxes(tree_preds, 0, 1)
        # Majority vote for each sample
        predictions = np.array([np.bincount(pred).argmax() for pred in tree_preds])
        return predictions
        #predictions = []
        #for votes in tree_preds:
        #    labels, counts = np.unique(votes, return_counts=True)
        #    predictions.append(labels[np.argmax(counts)])
       # return np.asarray(predictions)

    def bootstrap(self, X, Y):
        n_samples = X.shape[0]
        idxs = self._rng.choice(n_samples, n_samples, replace=True)
        return X[idxs], Y[idxs]
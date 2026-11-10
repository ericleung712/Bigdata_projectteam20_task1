# Weather Classification: Decision Tree and Random Forest

This project prepares weather data, trains custom decision-tree and
random-forest classifiers, evaluates them, and generates predictions with the
provided sample-submission columns.

## Project structure

| File or folder | Purpose |
|---|---|
| `Training Data/train.csv` | Labeled data used for tuning and training. |
| `Test Data/test.csv` | Unlabeled data to classify. |
| `Test Data/sample_submission.csv` | Reference submission columns and row order. |
| `requirement.txt` | Python package dependencies. |
| `Data_preparation.py` | Shared feature preparation for training and test rows; can also create EDA plots and a prepared training CSV when run directly. |
| `train_model.py` | Loads and prepares training data and provides the stratified train/validation split. |
| `Decision_tree.py` | Custom decision-tree implementation. |
| `Random_Forest.py` | Custom bootstrap random-forest implementation built from the decision tree. |
| `Decision_tree_tuning.py` | Decision-tree cross-validation search function. |
| `Random_forest_tuning.py` | Random-forest cross-validation search function. |
| `tune_hyperparameters.py` | Runs both searches and writes the best parameters to `Result/best_hyperparameters.txt`. |
| `task 1.py` | Trains and evaluates both models using its configured parameters; it does not run tuning. |
| `confusion_matrix.py` | Prints classification reports and saves confusion-matrix CSV and PNG files. |
| `timing_report.py` | Measures and records training, offline, and test-inference timings. |
| `Test_data_preparation.py` | Prepares test features using the same transformations as training. |
| `Run_test.py` | Loads saved models, predicts test labels, writes submissions, and saves tree diagrams. |
| `Print_tree.py` | Builds a Graphviz diagram of a custom decision tree. |
| `model_weights/` | Created by training; stores serialized model artifacts and their feature metadata. |
| `Result/` | Stores tuning results and generated submission files. |
| `Graph/` | Stores confusion-matrix and decision-tree visualizations. |

## Environment setup (Windows PowerShell)

Open PowerShell in the project directory:

```powershell
cd C:\Users\user\BigData_task1
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, allow scripts for the current terminal and
activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirement.txt
```

The Python `graphviz` package does not include the Graphviz application.
Install it separately using Windows Package Manager:

```powershell
winget install --id Graphviz.Graphviz -e
```

Alternatively, install it from [graphviz.org/download](https://graphviz.org/download/).
Check that the Graphviz executable is available:

```powershell
dot -V
```

If PowerShell cannot find `dot`, add Graphviz's `bin` folder to `PATH`. The
following examples assume it is installed in `C:\Program Files\Graphviz`; use
the actual installation path if yours differs.

For the current terminal only:

```powershell
$env:PATH += ";C:\Program Files\Graphviz\bin"
dot -V
```

To make the change persistent for your Windows user account instead:

```powershell
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable(
    "Path",
    "$userPath;C:\Program Files\Graphviz\bin",
    "User"
)
```

Restart VS Code or open a new PowerShell window after the persistent change,
then run `dot -V` again. This adds Graphviz to your user's PATH, not the
system-wide PATH. Applications started afterward can find Graphviz; if another
program named `dot` is already earlier on PATH, it generally takes precedence.

Run subsequent commands from the project directory with the virtual environment
activated.

## Environment setup (Linux)

Install Python 3, virtual-environment support, and the Graphviz system
application using your distribution's package manager. For Ubuntu or Debian:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip graphviz
```

For Fedora:

```bash
sudo dnf install python3 python3-pip graphviz
```

For other distributions, install the equivalent packages using their package
manager. The Python `graphviz` package alone does not include the Graphviz
executable.

Open a terminal and navigate to the project directory, replacing the example
path with its actual location:

```bash
cd /path/to/BigData_task1
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirement.txt
```

Verify that Graphviz is available:

```bash
dot -V
```

If the command is not found, confirm the Graphviz system package is installed
and its `bin` directory is on `PATH`. If Graphviz was installed in a
nonstandard location, add its `bin` directory for the current terminal:

```bash
export PATH="$PATH:/path/to/graphviz/bin"
dot -V
```

Replace `/path/to/graphviz/bin` with the actual directory containing `dot`.
For a persistent change, add the `export` line to your shell's startup file
(for example, `~/.bashrc` for Bash), then open a new terminal.

Run subsequent commands from the project directory with the virtual environment
activated. The commands in the following sections work in both Linux and
Windows PowerShell.

## Reproduce the training and evaluation

Run the training pipeline:

```powershell
python "task 1.py"
```

The script prepares the labeled data, reserves a stratified 20% validation
partition, trains both models with the settings in `task 1.py`, and reports
validation classification reports and confusion matrices. It then refits each
model on all labeled rows and saves:

- `model_weights/decision_tree.pkl`
- `model_weights/random_forest.pkl`
- Confusion-matrix CSV and PNG files under `Graph/`
- Training and offline timings in `Result/timing_report.txt`

The configured parameters are explicit in `TREE_PARAMETERS` and
`FOREST_PARAMETERS` in `task 1.py`. Tuning results are not applied automatically.

## Optional: tune hyperparameters

Tuning is a separate, optional, and computationally intensive step. It uses
stratified 5-fold cross-validation on the training partition and does not
modify the training script:

```powershell
python tune_hyperparameters.py
```

The script prints the best settings for each model and saves them to
`Result/best_hyperparameters.txt`. It also prints separate tuning times and
updates `Result/timing_report.txt`. To use the settings:

1. Open [`task 1.py`](./task%201.py) and find `TREE_PARAMETERS` and
   `FOREST_PARAMETERS` near the top of the file, immediately below
   `LABEL_MAPPING`.
2. Copy the decision-tree values from the results file into `TREE_PARAMETERS`
   and the random-forest values into `FOREST_PARAMETERS`. Match each parameter
   name to its value. Decision-tree tuning keeps `min_samples_split` fixed at
   `10`, so retain that value unless you intentionally change it.
   `FOREST_PARAMETERS` also contains `random_state`, which is not tuned; retain
   it for reproducible forest training.
3. Retrain and then generate test predictions:

   ```powershell
   python "task 1.py"
   python Run_test.py
   ```

`Run_test.py` loads the newly saved models from `model_weights/`; it has no
separate hyperparameters to update. Editing the dictionaries alone does not
change existing model files or predictions: rerun training before testing.

## Generate test predictions

After training has created the model files, run:

```powershell
python Run_test.py
```

This writes:

- `Result/submission_decision_tree.csv`
- `Result/submission_random_forest.csv`
- `Graph/decision_tree.png`
- `Graph/random_forest.png`
- `Graph/decision_tree.svg`
- `Graph/random_forest.svg`
- Test-inference timings in `Result/timing_report.txt`

Each submission has the `id,label` columns and uses the original numeric
predictions (`1`, `2`, `3`, `4`) rather than the class names shown in the sample
submission. The test IDs and row order are checked against
`Test Data/sample_submission.csv`. Tree diagrams still show class names.
The random-forest diagrams show its first tree. SVG diagrams can be zoomed
without losing clarity; branches labeled `yes` satisfy the displayed split
condition, and `no` branches do not.

### Timing definitions

The training, tuning, and test scripts print elapsed wall-clock times in seconds and write them to
`Result/timing_report.txt`. Training time is the sum of the four model fits:
one validation fit and one final fit for each model. Offline time adds the
shared training-data loading, feature preparation, and train/validation split
to that training time. Validation prediction, plotting, tuning, and file saving
are excluded.

Inference time is measured separately for each model's prediction over all
test records; the report also gives their sum and the number of records per
model. Test-data preparation, model loading, CSV output, and graph rendering are
excluded. Tuning times measure each model's entire cross-validation search,
including its progress output, but exclude data loading and preprocessing.
Tuning is not included in the offline total.

Each script updates its own section of the report. Training clears previous
inference timings because the models have changed, but preserves tuning
timings; rerunning tuning or inference replaces only that section. If test
prediction is run before a timing report exists, the report states that
training timings are unavailable.

## Optional data-preparation commands

The main training and test scripts call the shared feature preparation
automatically. To run the standalone preparation utilities:

```powershell
python Data_preparation.py
python Test_data_preparation.py
```

These commands create prepared CSVs under the data folders and EDA plots under
`Graph/`.

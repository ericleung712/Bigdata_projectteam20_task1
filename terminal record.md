## No tuned cap features Random state 0 (train+test)
(.venv) PS C:\Users\user\BigData_task1> & 'c:\Users\user\BigData_task1\.venv\Scripts\python.exe' '"c:/Users/user/BigData_task1/task 1.py"'

decision_tree classification report:
              precision    recall  f1-score   support

       Sunny       0.95      0.91      0.93       495
      Cloudy       0.85      0.91      0.88       495
       Rainy       0.90      0.90      0.90       495
       Snowy       0.94      0.92      0.93       495

    accuracy                           0.91      1980
   macro avg       0.91      0.91      0.91      1980
weighted avg       0.91      0.91      0.91      1980


random_forest classification report:
              precision    recall  f1-score   support

       Sunny       0.89      0.93      0.91       495
      Cloudy       0.88      0.90      0.89       495
       Rainy       0.92      0.89      0.91       495
       Snowy       0.96      0.92      0.94       495

    accuracy                           0.91      1980
   macro avg       0.91      0.91      0.91      1980
weighted avg       0.91      0.91      0.91      1980

Saved decision_tree weights to: C:\Users\user\BigData_task1\model_weights\decision_tree.pkl
Saved random_forest weights to: C:\Users\user\BigData_task1\model_weights\random_forest.pkl
Training timing
Data loading, preprocessing and split: 0.015403 seconds
Decision tree validation fit: 0.453952 seconds
Decision tree final fit: 0.492068 seconds
Random forest validation fit: 4.205705 seconds
Random forest final fit: 4.774852 seconds
Total training time (all four fits): 9.926576 seconds
Total offline time (preprocessing + training): 9.941979 seconds
Timing report saved to: C:\Users\user\BigData_task1\Result\timing_report.txt
Training and evaluation complete.

(.venv) PS C:\Users\user\BigData_task1> & 'c:\Users\user\BigData_task1\.venv\Scripts\python.exe' 'c:/Users/user/BigData_task1/Run_test.py'
Saved decision_tree submission to: C:\Users\user\BigData_task1\Result\submission_decision_tree.csv
Saved random_forest submission to: C:\Users\user\BigData_task1\Result\submission_random_forest.csv
Inference timing
Test records per model: 3300
Decision tree inference: 0.002828 seconds
Random forest inference: 0.049636 seconds
Total inference time (both models): 0.052464 seconds
Timing report saved to: C:\Users\user\BigData_task1\Result\timing_report.txt

## No tuned uncleaned Random state 0 (train+test)
(.venv) PS C:\Users\user\BigData_task1> & 'c:\Users\user\BigData_task1\.venv\Scripts\python.exe' '"c:/Users/user/BigData_task1/task 1.py"'

decision_tree classification report:
              precision    recall  f1-score   support

       Sunny       0.91      0.93      0.92       495
      Cloudy       0.87      0.90      0.88       495
       Rainy       0.90      0.90      0.90       495
       Snowy       0.95      0.91      0.93       495

    accuracy                           0.91      1980
   macro avg       0.91      0.91      0.91      1980
weighted avg       0.91      0.91      0.91      1980


random_forest classification report:
              precision    recall  f1-score   support

       Sunny       0.89      0.93      0.91       495
      Cloudy       0.86      0.91      0.88       495
       Rainy       0.93      0.89      0.91       495
       Snowy       0.97      0.93      0.95       495

    accuracy                           0.91      1980
   macro avg       0.91      0.91      0.91      1980
weighted avg       0.91      0.91      0.91      1980

Saved decision_tree weights to: C:\Users\user\BigData_task1\model_weights\decision_tree.pkl
Saved random_forest weights to: C:\Users\user\BigData_task1\model_weights\random_forest.pkl
Training timing
Data loading, preprocessing and split: 0.011085 seconds
Decision tree validation fit: 0.403833 seconds
Decision tree final fit: 0.441227 seconds
Random forest validation fit: 3.795165 seconds
Random forest final fit: 4.353545 seconds
Total training time (all four fits): 8.993769 seconds
Total offline time (preprocessing + training): 9.004855 seconds
Timing report saved to: C:\Users\user\BigData_task1\Result\timing_report.txt
Training and evaluation complete.

## No tuned modified Random state 0 (train+test)
(.venv) PS C:\Users\user\BigData_task1> & 'c:\Users\user\BigData_task1\.venv\Scripts\python.exe' '"c:/Users/user/BigData_task1/task 1.py"'

decision_tree classification report:
              precision    recall  f1-score   support

       Sunny       0.91      0.92      0.91       495
      Cloudy       0.86      0.88      0.87       495
       Rainy       0.91      0.87      0.89       495
       Snowy       0.92      0.92      0.92       495

    accuracy                           0.90      1980
   macro avg       0.90      0.90      0.90      1980
weighted avg       0.90      0.90      0.90      1980


random_forest classification report:
              precision    recall  f1-score   support

       Sunny       0.88      0.93      0.90       495
      Cloudy       0.87      0.90      0.89       495
       Rainy       0.91      0.87      0.89       495
       Snowy       0.97      0.92      0.94       495

    accuracy                           0.90      1980
   macro avg       0.91      0.90      0.90      1980
weighted avg       0.91      0.90      0.90      1980

Saved decision_tree weights to: C:\Users\user\BigData_task1\model_weights\decision_tree.pkl
Saved random_forest weights to: C:\Users\user\BigData_task1\model_weights\random_forest.pkl
Training timing
Data loading, preprocessing and split: 0.016844 seconds
Decision tree validation fit: 0.645357 seconds
Decision tree final fit: 0.683634 seconds
Random forest validation fit: 5.674193 seconds
Random forest final fit: 6.449940 seconds
Total training time (all four fits): 13.453124 seconds
Total offline time (preprocessing + training): 13.469968 seconds
Timing report saved to: C:\Users\user\BigData_task1\Result\timing_report.txt
Training and evaluation complete.

(.venv) PS C:\Users\user\BigData_task1> & 'c:\Users\user\BigData_task1\.venv\Scripts\python.exe' 'c:/Users/user/BigData_task1/Run_test.py'
Saved decision_tree submission to: C:\Users\user\BigData_task1\Result\submission_decision_tree.csv
Saved random_forest submission to: C:\Users\user\BigData_task1\Result\submission_random_forest.csv
Inference timing
Test records per model: 3300
Decision tree inference: 0.002904 seconds
Random forest inference: 0.047940 seconds
Total inference time (both models): 0.050845 seconds
Timing report saved to: C:\Users\user\BigData_task1\Result\timing_report.txt

## tuning hyperparameter
(.venv) PS C:\Users\user\BigData_task1> & 'c:\Users\user\BigData_task1\.venv\Scripts\python.exe' 'c:/Users/user/BigData_task1/tune_hyperparameters.py'
Best decision-tree parameters: {'max_depth': 10, 'min_samples_leaf': 2, 'n_thresholds': 50}
Best mean 5-fold CV macro F1: 0.908
Completed 1/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.886
Completed 2/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.902
Completed 3/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.885
Completed 4/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.902
Completed 5/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.885
Completed 6/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.902
Completed 7/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.885
Completed 8/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.902
Completed 9/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.885
Completed 10/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.902
Completed 11/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.885
Completed 12/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.902
Completed 13/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.885
Completed 14/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.902
Completed 15/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.885
Completed 16/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.902
Completed 17/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.885
Completed 18/162: {'n_trees': 5, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.902
Completed 19/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 20/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.912
Completed 21/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.905
Completed 22/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.909
Completed 23/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 24/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.910
Completed 25/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.905
Completed 26/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 27/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.905
Completed 28/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.909
Completed 29/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 30/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.910
Completed 31/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 32/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.912
Completed 33/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.906
Completed 34/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 35/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 36/162: {'n_trees': 5, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.910
Completed 37/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.908
Completed 38/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 39/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.906
Completed 40/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 41/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.908
Completed 42/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.909
Completed 43/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.906
Completed 44/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 45/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.906
Completed 46/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 47/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.908
Completed 48/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.909
Completed 49/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 50/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.912
Completed 51/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 52/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 53/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.908
Completed 54/162: {'n_trees': 5, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.909
Completed 55/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.888
Completed 56/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 57/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.888
Completed 58/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 59/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.887
Completed 60/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 61/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.888
Completed 62/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 63/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.888
Completed 64/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 65/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.887
Completed 66/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 67/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.888
Completed 68/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 69/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.888
Completed 70/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 71/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.887
Completed 72/162: {'n_trees': 10, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 73/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 74/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.913
Completed 75/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 76/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 77/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 78/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.910
Completed 79/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 80/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.912
Completed 81/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 82/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 83/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 84/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.910
Completed 85/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 86/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 87/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.905
Completed 88/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.909
Completed 89/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 90/162: {'n_trees': 10, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.910
Completed 91/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.906
Completed 92/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.913
Completed 93/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.908
Completed 94/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 95/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 96/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.910
Completed 97/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 98/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 99/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.908
Completed 100/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 101/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 102/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.910
Completed 103/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.908
Completed 104/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 105/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 106/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.910
Completed 107/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 108/162: {'n_trees': 10, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.910
Completed 109/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.889
Completed 110/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.899
Completed 111/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.889
Completed 112/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.899
Completed 113/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.889
Completed 114/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.899
Completed 115/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.889
Completed 116/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.899
Completed 117/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.889
Completed 118/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.899
Completed 119/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.889
Completed 120/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.899
Completed 121/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.889
Completed 122/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 123/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.889
Completed 124/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.900
Completed 125/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.889
Completed 126/162: {'n_trees': 20, 'max_depth': 4, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.899
Completed 127/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.912
Completed 128/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.914
Completed 129/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 130/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.912
Completed 131/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 132/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 133/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.910
Completed 134/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.913
Completed 135/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.907
Completed 136/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.912
Completed 137/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 138/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 139/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.911
Completed 140/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.912
Completed 141/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.912
Completed 142/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 143/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 144/162: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 145/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.911
Completed 146/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.914
Completed 147/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 148/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 149/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 150/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 151/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.908
Completed 152/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.914
Completed 153/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 154/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 155/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 156/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 10, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.911
Completed 157/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 10}, mean CV macro F1=0.910
Completed 158/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 1, 'n_thresholds': 25}, mean CV macro F1=0.913
Completed 159/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 10}, mean CV macro F1=0.910
Completed 160/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 5, 'n_thresholds': 25}, mean CV macro F1=0.913
Completed 161/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 10}, mean CV macro F1=0.909
Completed 162/162: {'n_trees': 20, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 10, 'n_thresholds': 25}, mean CV macro F1=0.911
Best random-forest parameters: {'n_trees': 20, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}
Best mean 5-fold CV macro F1: 0.914
Tuning timing
Decision tree tuning: 83.624672 seconds
Random forest tuning: 4127.284717 seconds
Timing report saved to: C:\Users\user\BigData_task1\Result\timing_report.txt
Best hyperparameters from 5-fold stratified cross-validation
These values are informational and are not automatically applied to task 1.py.

Decision tree (mean macro F1: 0.908)
{'max_depth': 10, 'min_samples_leaf': 2, 'n_thresholds': 50}

Random forest (mean macro F1: 0.914)
{'n_trees': 20, 'max_depth': 10, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_thresholds': 25}

Saved best hyperparameters to: C:\Users\user\BigData_task1\Result\best_hyperparameters.txt

## Tuned Modified Ran 0 (Train + Test)
(.venv) PS C:\Users\user\BigData_task1> & 'c:\Users\user\BigData_task1\.venv\Scripts\python.exe' '"c:/Users/user/BigData_task1/task 1.py"'

decision_tree classification report:
              precision    recall  f1-score   support

       Sunny       0.92      0.92      0.92       495
      Cloudy       0.86      0.91      0.88       495
       Rainy       0.92      0.88      0.90       495
       Snowy       0.95      0.93      0.94       495

    accuracy                           0.91      1980
   macro avg       0.91      0.91      0.91      1980
weighted avg       0.91      0.91      0.91      1980


random_forest classification report:
              precision    recall  f1-score   support

       Sunny       0.92      0.93      0.92       495
      Cloudy       0.86      0.91      0.89       495
       Rainy       0.93      0.89      0.91       495
       Snowy       0.95      0.93      0.94       495

    accuracy                           0.91      1980
   macro avg       0.91      0.91      0.91      1980
weighted avg       0.91      0.91      0.91      1980

Saved decision_tree weights to: C:\Users\user\BigData_task1\model_weights\decision_tree.pkl
Saved random_forest weights to: C:\Users\user\BigData_task1\model_weights\random_forest.pkl
Training timing
Data loading, preprocessing and split: 0.018191 seconds
Decision tree validation fit: 1.577503 seconds
Decision tree final fit: 1.854537 seconds
Random forest validation fit: 24.851501 seconds
Random forest final fit: 27.571755 seconds
Total training time (all four fits): 55.855296 seconds
Total offline time (preprocessing + training): 55.873487 seconds
Timing report saved to: C:\Users\user\BigData_task1\Result\timing_report.txt
Training and evaluation complete.
(.venv) PS C:\Users\user\BigData_task1> & 'c:\Users\user\BigData_task1\.venv\Scripts\python.exe' 'c:/Users/user/BigData_task1/Run_test.py'
Saved decision_tree submission to: C:\Users\user\BigData_task1\Result\submission_decision_tree.csv
Saved random_forest submission to: C:\Users\user\BigData_task1\Result\submission_random_forest.csv
Inference timing
Test records per model: 3300
Decision tree inference: 0.003022 seconds
Random forest inference: 0.079201 seconds
Total inference time (both models): 0.082222 seconds
Timing report saved to: C:\Users\user\BigData_task1\Result\timing_report.txt
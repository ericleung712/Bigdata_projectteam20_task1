Results of CSV file generated on test data evaluated by external platform (with correct labels) using Macro-F1 score
| Feature engineering strategy | Submission file | Macro F1 score |
| Binned feature + One-hot encoding + outlier | NoTune_capfeature_ran0_submission_random_forest.csv | 0.90652 |
| Binned feature + One-hot encoding + outlier | NoTune_capfeature_ran0_submission_decision_tree.csv | 0.90685 |
| Uncleaned | NoTune_unclean_ran0_submission_random_forest.csv | 0.90527|
| Uncleaned | NoTune_unclean_ran0_submission_decision_tree.csv | 0.90956 |
| Interactive feature + Binned feature + One-hot encoding + outlier | NoTune_modified_ran0_submission_random_forest.csv | 0.91102 |
| Interactive feature + Binned feature + One-hot encoding + outlier | NoTune_modified_ran0_submission_decision_tree.csv | 0.90689 |
| Tuned parameter + Interactive feature + Binned feature + One-hot encoding + outlier | NoTune_modified_ran0_submission_decision_tree.csv | 0.91628|



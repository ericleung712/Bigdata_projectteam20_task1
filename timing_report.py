from pathlib import Path
from time import perf_counter


TIMING_REPORT_PATH = Path(__file__).resolve().parent / "Result" / "timing_report.txt"
TRAINING_HEADING = "Training timing"
TUNING_HEADING = "Tuning timing"
INFERENCE_HEADING = "Inference timing"
TRAINING_UNAVAILABLE = (
    "Training timing unavailable: run task 1.py to record training and offline time."
)


def fit_with_timing(model, features, labels):
    start = perf_counter()
    model.fit(features, labels)
    return perf_counter() - start


def update_timing_section(heading, report, remove_headings=()):
    sections = []
    if TIMING_REPORT_PATH.exists():
        sections = TIMING_REPORT_PATH.read_text(encoding="utf-8").strip().split("\n\n")

    replaced = False
    updated = []
    for section in sections:
        section_heading = section.split("\n", 1)[0]
        if heading == TRAINING_HEADING and section == TRAINING_UNAVAILABLE:
            section_heading = TRAINING_HEADING
        if section_heading in remove_headings:
            continue
        if section_heading == heading:
            if not replaced:
                updated.append(report.rstrip())
                replaced = True
        elif section:
            updated.append(section)
    if not replaced:
        updated.append(report.rstrip())

    TIMING_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    TIMING_REPORT_PATH.write_text("\n\n".join(updated) + "\n", encoding="utf-8")
    print(report, end="")
    print(f"Timing report saved to: {TIMING_REPORT_PATH}")


def write_training_timing(preprocessing_seconds, model_fit_times):
    training_seconds = sum(model_fit_times.values())
    report = (
        f"{TRAINING_HEADING}\n"
        f"Data loading, preprocessing and split: {preprocessing_seconds:.6f} seconds\n"
        f"Decision tree validation fit: {model_fit_times['decision_tree_validation']:.6f} seconds\n"
        f"Decision tree final fit: {model_fit_times['decision_tree_final']:.6f} seconds\n"
        f"Random forest validation fit: {model_fit_times['random_forest_validation']:.6f} seconds\n"
        f"Random forest final fit: {model_fit_times['random_forest_final']:.6f} seconds\n"
        f"Total training time (all four fits): {training_seconds:.6f} seconds\n"
        f"Total offline time (preprocessing + training): "
        f"{preprocessing_seconds + training_seconds:.6f} seconds\n"
    )
    update_timing_section(TRAINING_HEADING, report, remove_headings=(INFERENCE_HEADING,))


def write_tuning_timing(tree_seconds, forest_seconds):
    report = (
        f"{TUNING_HEADING}\n"
        f"Decision tree tuning: {tree_seconds:.6f} seconds\n"
        f"Random forest tuning: {forest_seconds:.6f} seconds\n"
    )
    update_timing_section(TUNING_HEADING, report)


def write_inference_timing(model_inference_times, record_count):
    report = (
        f"{INFERENCE_HEADING}\n"
        f"Test records per model: {record_count}\n"
        f"Decision tree inference: {model_inference_times['decision_tree']:.6f} seconds\n"
        f"Random forest inference: {model_inference_times['random_forest']:.6f} seconds\n"
        f"Total inference time (both models): {sum(model_inference_times.values()):.6f} seconds\n"
    )
    if not TIMING_REPORT_PATH.exists():
        TIMING_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        TIMING_REPORT_PATH.write_text(f"{TRAINING_UNAVAILABLE}\n", encoding="utf-8")
    update_timing_section(INFERENCE_HEADING, report)

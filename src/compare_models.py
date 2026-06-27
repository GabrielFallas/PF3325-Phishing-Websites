"""
Compare all trained classifiers (Random Forest, SVM, MLP) on the held-out test
set and export the numbers + figures used in the Entrega 5 presentation and the
Entrega 6 IEEE paper.

Outputs:
    reports/metrics.json          all metrics + inference timing for every model
    reports/roc_comparison.png    combined ROC curve
    reports/confusion_mlp.png     MLP confusion matrix
"""

import json
import pickle
import time
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, confusion_matrix,
)
import tensorflow as tf

from preprocess import preprocess_data

_BENCHMARK_RUNS = 50  # repetitions for stable timing estimates


def metrics_for(y_true, y_pred, y_proba):
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred)),
        "recall": float(recall_score(y_true, y_pred)),
        "specificity": float(tn / (tn + fp)),
        "f1": float(f1_score(y_true, y_pred)),
        "auc_roc": float(roc_auc_score(y_true, y_proba)),
        "tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp),
    }


def benchmark_inference(predict_fn, X, n_runs=_BENCHMARK_RUNS):
    """Return avg/min/max/std inference time in milliseconds per sample.

    Each run calls predict_fn(X) on the full test set; per-sample time is
    computed by dividing the run duration by len(X).  The first run is
    discarded as a warm-up.
    """
    n_samples = len(X)
    times_ms = []
    for i in range(n_runs + 1):
        t0 = time.perf_counter()
        predict_fn(X)
        elapsed = (time.perf_counter() - t0) * 1000  # ms
        if i > 0:  # skip warm-up
            times_ms.append(elapsed / n_samples)
    arr = np.array(times_ms)
    return {
        "avg_ms": float(arr.mean()),
        "min_ms": float(arr.min()),
        "max_ms": float(arr.max()),
        "std_ms": float(arr.std()),
        "n_runs": n_runs,
        "n_samples": n_samples,
    }


def main():
    _, _, X_test, _, _, y_test, _, _ = preprocess_data()
    Path("reports").mkdir(exist_ok=True)

    rf = pickle.load(open("models/random_forest_model.pkl", "rb"))
    svm = pickle.load(open("models/svm_model.pkl", "rb"))
    mlp = tf.keras.models.load_model("models/best_model.keras")

    results = {}
    rocs = {}

    # Random Forest
    rf_proba = rf.predict_proba(X_test)[:, 1]
    results["Random Forest"] = metrics_for(y_test, rf.predict(X_test), rf_proba)
    results["Random Forest"]["inference"] = benchmark_inference(
        rf.predict, X_test)
    rocs["Random Forest"] = roc_curve(y_test, rf_proba)

    # SVM
    svm_proba = svm.predict_proba(X_test)[:, 1]
    results["SVM (RBF)"] = metrics_for(y_test, svm.predict(X_test), svm_proba)
    results["SVM (RBF)"]["inference"] = benchmark_inference(
        svm.predict, X_test)
    rocs["SVM (RBF)"] = roc_curve(y_test, svm_proba)

    # MLP
    mlp_proba = mlp.predict(X_test, verbose=0).flatten()
    mlp_pred = (mlp_proba >= 0.5).astype(int)
    results["MLP (proposed)"] = metrics_for(y_test, mlp_pred, mlp_proba)
    results["MLP (proposed)"]["inference"] = benchmark_inference(
        lambda X: mlp.predict(X, verbose=0), X_test)
    rocs["MLP (proposed)"] = roc_curve(y_test, mlp_proba)

    with open("reports/metrics.json", "w") as fh:
        json.dump(results, fh, indent=2)

    # Print classification metrics
    print("\n{:<18s} {:>8s} {:>8s} {:>8s} {:>8s} {:>8s}".format(
        "Model", "Acc", "Prec", "Recall", "F1", "AUC"))
    print("-" * 62)
    for name, m in results.items():
        print("{:<18s} {:>8.4f} {:>8.4f} {:>8.4f} {:>8.4f} {:>8.4f}".format(
            name, m["accuracy"], m["precision"], m["recall"], m["f1"], m["auc_roc"]))

    # Print inference timing
    print("\n{:<18s} {:>10s} {:>10s} {:>10s} {:>10s}".format(
        "Model", "Avg (ms)", "Min (ms)", "Max (ms)", "Std (ms)"))
    print("-" * 62)
    for name, m in results.items():
        t = m["inference"]
        print("{:<18s} {:>10.4f} {:>10.4f} {:>10.4f} {:>10.4f}".format(
            name, t["avg_ms"], t["min_ms"], t["max_ms"], t["std_ms"]))

    # Combined ROC
    plt.figure(figsize=(7, 6))
    colors = {"Random Forest": "#2ca02c", "SVM (RBF)": "#ff7f0e",
              "MLP (proposed)": "#1f77b4"}
    for name, (fpr, tpr, _) in rocs.items():
        plt.plot(fpr, tpr, linewidth=2.2, color=colors[name],
                 label=f"{name} (AUC={results[name]['auc_roc']:.4f})")
    plt.plot([0, 1], [0, 1], "k--", linewidth=1, label="Random")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve Comparison — Phishing Detection")
    plt.legend(loc="lower right")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("reports/roc_comparison.png", dpi=150)
    plt.close()
    print("\n✓ reports/roc_comparison.png")

    # MLP confusion matrix
    cm = confusion_matrix(y_test, mlp_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Phishing", "Legitimate"],
                yticklabels=["Phishing", "Legitimate"])
    plt.ylabel("True Label")
    plt.xlabel("Predicted Label")
    plt.title("Confusion Matrix — MLP")
    plt.tight_layout()
    plt.savefig("reports/confusion_mlp.png", dpi=150)
    plt.close()
    print("✓ reports/confusion_mlp.png")
    print("✓ reports/metrics.json")


if __name__ == "__main__":
    main()

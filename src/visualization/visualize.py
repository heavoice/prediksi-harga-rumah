# src/visualization/visualize.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_predictions_vs_actual(y_test, y_pred):
    """Menampilkan scatter plot prediksi vs aktual"""
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=y_test, y=y_pred, color='blue', alpha=0.6)
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
    plt.title("Prediksi vs Aktual Harga Rumah")
    plt.xlabel('Harga Aktual')
    plt.ylabel('Harga Prediksi')
    plt.show()

def plot_residuals(y_test, y_pred):
    """Menampilkan distribusi residuals"""
    residuals = y_test - y_pred
    plt.figure(figsize=(8,6))
    sns.histplot(residuals, kde=True, color='purple', bins=30)
    plt.title("Distribusi Residuals")
    plt.xlabel('Residuals')
    plt.ylabel('Frekuensi')
    plt.show()

    
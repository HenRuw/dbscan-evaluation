import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles, make_blobs
from sklearn.cluster import KMeans, DBSCAN

# Automatisch einen Ordner für die Ausgabe erstellen
os.makedirs('plots', exist_ok=True)

# ==========================================
# 1. DATEN GENERIEREN
# ==========================================
X_ringe, _ = make_circles(n_samples=600, factor=0.4, noise=0.05, random_state=42)

X_blob, _ = make_blobs(n_samples=150, centers=[[0, 0]], cluster_std=0.6, random_state=42)
np.random.seed(42) 
X_noise = np.random.uniform(low=-7, high=7, size=(25, 2))
X_rauschen = np.vstack((X_blob, X_noise)) 

# ==========================================
# 2. ALGORITHMEN AUSFÜHREN
# ==========================================
kmeans_ringe = KMeans(n_clusters=2, random_state=42, n_init=10).fit(X_ringe)
dbscan_ringe = DBSCAN(eps=0.15, min_samples=4).fit(X_ringe)

kmeans_rauschen = KMeans(n_clusters=1, random_state=42, n_init=10).fit(X_rauschen)
dbscan_rauschen = DBSCAN(eps=0.4, min_samples=4).fit(X_rauschen)

# ==========================================
# 3. PLOTTING-HILFSFUNKTION FÜR DBSCAN
# ==========================================
def plot_dbscan(ax, X, dbscan_model, title):
    core_mask = dbscan_model.labels_ != -1
    noise_mask = dbscan_model.labels_ == -1
    ax.scatter(X[noise_mask, 0], X[noise_mask, 1], c='black', s=15, alpha=0.5, label='Rauschen')
    ax.scatter(X[core_mask, 0], X[core_mask, 1], c=dbscan_model.labels_[core_mask], cmap='viridis', s=30)
    ax.set_title(title, pad=15)
    ax.set_xticks([]); ax.set_yticks([])

# ==========================================
# 4. BILDER GENERIEREN & SPEICHERN
# ==========================================
plt.style.use('default')

# --- BILD 1: RINGE ---
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
fig1.suptitle('Vergleich bei nicht-konvexen Strukturen (Ringe)', fontsize=14)
ax1.scatter(X_ringe[:, 0], X_ringe[:, 1], c=kmeans_ringe.labels_, cmap='viridis', s=30)
ax1.set_title('K-Means (k=2)', pad=15)
ax1.set_xticks([]); ax1.set_yticks([])
plot_dbscan(ax2, X_ringe, dbscan_ringe, r'DBSCAN ($\epsilon=0.15$, MinPts=4)')
plt.tight_layout()
plt.savefig('plots/ringe_vergleich.png', dpi=300, bbox_inches='tight')
plt.close(fig1)

# --- BILD 2: RAUSCHEN ---
fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(10, 4.5))
fig2.suptitle('Umgang mit einem dichten Kern und Hintergrundrauschen', fontsize=14)
ax3.scatter(X_rauschen[:, 0], X_rauschen[:, 1], c=kmeans_rauschen.labels_, cmap='viridis', s=30)
ax3.set_title('K-Means (k=1)', pad=15)
ax3.set_xticks([]); ax3.set_yticks([])
plot_dbscan(ax4, X_rauschen, dbscan_rauschen, r'DBSCAN ($\epsilon=0.4$, MinPts=4)')
plt.tight_layout()
plt.savefig('plots/rauschen_vergleich.png', dpi=300, bbox_inches='tight')
plt.close(fig2)

print("Plots wurden erfolgreich im Ordner '/plots' gespeichert.")
import numpy as np
import matplotlib.pyplot as plt

# Parameter
eps = 1.5
min_pts = 4

# Punktkoordinaten
core_points = np.array([
    [4.0, 3.5], [3.7, 3.9], [4.3, 3.2], 
    [4.1, 4.2], [3.5, 3.1], [3.8, 2.8]
])
border_points = np.array([[5.4, 3.0]])
noise_points = np.array([
    [6.6, 2.6],  # In Rand-Umgebung, aber > 1.5 von Kernpunkten
    [1.5, 4.5]   # Isoliertes Rauschen
])

fig, ax = plt.subplots(figsize=(8, 6))

# 1. Epsilon-Umgebungen der Kernpunkte (nur leicht angedeutet)
for pt in core_points:
    circle = plt.Circle((pt[0], pt[1]), eps, color='#800080', fill=True, alpha=0.05, linestyle=':', linewidth=1.0)
    ax.add_patch(circle)

# 2. Epsilon-Umgebung für Randpunkte (deutlich)
for pt in border_points:
    circle = plt.Circle((pt[0], pt[1]), eps, color='#FFD700', fill=True, alpha=0.15, linestyle='--', linewidth=1.5)
    ax.add_patch(circle)

# 3. Epsilon-Umgebungen für Rauschpunkte (deutlich)
for pt in noise_points:
    circle = plt.Circle((pt[0], pt[1]), eps, color='#A9A9A9', fill=True, alpha=0.15, linestyle='--', linewidth=1.5)
    ax.add_patch(circle)

# Punkte zeichnen (zorder=4 stellt sie in den Vordergrund)
ax.scatter(core_points[:, 0], core_points[:, 1], c='#800080', s=120, label='Kernpunkte', edgecolors='k', zorder=4)
ax.scatter(border_points[:, 0], border_points[:, 1], c='#FFD700', s=120, label='Randpunkte', edgecolors='k', zorder=4)
ax.scatter(noise_points[:, 0], noise_points[:, 1], c='#A9A9A9', s=120, label='Rauschen', edgecolors='k', zorder=4)

# Plot formatieren
ax.set_aspect('equal')
ax.set_xlim(0, 8)
ax.set_ylim(1, 6)
ax.set_title(r"DBSCAN Punktklassifizierung ($\varepsilon=1.5, MinPts=4$)", fontsize=14, pad=15)
ax.legend(loc='upper left', fontsize=11)
ax.grid(True, linestyle=':', alpha=0.7)

# Speichern
plt.savefig("dbscan_klassifizierung.png", dpi=300, bbox_inches='tight')
plt.close()

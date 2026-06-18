import matplotlib.pyplot as plt

# Koordinaten der zwei Punkte
A = (1, 1)
B = (5, 4)

fig, ax = plt.subplots(figsize=(6, 4))

# 1. Euklidische Distanz (Direkte Luftlinie)
ax.plot([A[0], B[0]], [A[1], B[1]], color='blue', linewidth=2.5, label='Euklidische Distanz')

# 2. Manhattan-Distanz (Gitterförmig / treppenartig)
# Variante als "Treppe" zur Verdeutlichung des Gitters
ax.plot([A[0], 2, 2, 3, 3, 4, 4, B[0], B[0]], 
        [A[1], A[1], 2, 2, 3, 3, 4, 4, B[1]], 
        color='red', linewidth=2.5, linestyle='--', label='Manhattan-Distanz')

# Punkte einzeichnen
ax.scatter([A[0], B[0]], [A[1], B[1]], color='black', s=100, zorder=5)

# Beschriftung der Punkte
ax.text(A[0] - 0.2, A[1] + 0.2, 'p', fontsize=14, fontweight='bold')
ax.text(B[0] + 0.2, B[1] - 0.2, 'q', fontsize=14, fontweight='bold')

# Achsen und Layout formatieren
ax.set_xlim(0, 6)
ax.set_ylim(0, 5)
ax.set_xticks(range(7))
ax.set_yticks(range(6))
ax.grid(True, linestyle=':', alpha=0.7)
ax.set_aspect('equal')
ax.legend(loc='upper left')
ax.set_title("Vergleich der Distanzmaße", fontsize=14, pad=15)

# Bild speichern
plt.savefig("distanzmasse.png", dpi=300, bbox_inches='tight')
plt.close()

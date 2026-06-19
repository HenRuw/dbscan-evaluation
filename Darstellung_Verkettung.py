import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Plot Setup
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('equal')
ax.set_xlim(0, 6.5)
ax.set_ylim(0, 5) 
ax.grid(True, linestyle=':', alpha=0.6)

# Parameter
epsilon = 1.5
min_pts = 4
u_size = 10  # Einheitliche Größe für alle Punkte

# Punkte definieren (Mittelweg: y=2.0)
p = (2.0, 2.0) # Kernpunkt
q = (3.4, 2.0) # Randpunkt

# Zusätzliche Punkte, damit p ein Kernpunkt ist
p_neighbors = [(1.3, 2.5), (1.1, 1.5), (2.3, 0.9)]

# Epsilon-Umgebungen zeichnen
circle_p = patches.Circle(p, epsilon, color='purple', alpha=0.2, ec='purple', ls='--')
circle_q = patches.Circle(q, epsilon, color='gold', alpha=0.2, ec='orange', ls='--')
ax.add_patch(circle_p)
ax.add_patch(circle_q)

# Alle Punkte plotten (einheitliche Größe u_size)
for nx, ny in p_neighbors:
    ax.plot(nx, ny, 'o', markersize=u_size, color='purple', markeredgecolor='black')

ax.plot(p[0], p[1], 'o', markersize=u_size, color='purple', markeredgecolor='black', label='Kernpunkt')
ax.plot(q[0], q[1], 'o', markersize=u_size, color='gold', markeredgecolor='black', label='Randpunkt')

# Beschriftungen
ax.text(p[0] - 0.2, p[1] + 0.2, '$p$', fontsize=14, fontweight='bold')
ax.text(q[0] + 0.1, q[1] + 0.2, '$q$', fontsize=14, fontweight='bold')

# --- Pfeile für die Asymmetrie ---
ax.annotate('', xy=(q[0]-0.15, q[1]+0.05), xytext=(p[0]+0.15, p[1]+0.05),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
ax.text(2.7, 2.15, r'$p \Rightarrow q$', fontsize=12, ha='center', color='black')

ax.annotate('', xy=(p[0]+0.15, p[1]-0.05), xytext=(q[0]-0.15, q[1]-0.05),
            arrowprops=dict(edgecolor='red', arrowstyle='->', ls='--', lw=1.5))
ax.text(2.7, 1.75, r'$q \nRightarrow p$', fontsize=12, ha='center', color='red')

# --- Erklärungs-Textfeld ---
erklaerung = (
    r"$\mathbf{p \Rightarrow q}$: $q$ liegt in der $\varepsilon$-Umgebung von $p$." "\n"
    r"$\rightarrow q$ ist direkt dichte-erreichbar von $p$." "\n\n"
    r"$\mathbf{q \nRightarrow p}$: $q$ ist kein Kernpunkt ($< \mathit{MinPts}$)." "\n"
    r"$\rightarrow p$ ist nicht dichte-erreichbar von $q$."
)

props = dict(boxstyle='round,pad=0.6', facecolor='white', alpha=0.9, edgecolor='gray')
ax.text(0.2, 4.8, erklaerung, fontsize=11, verticalalignment='top', bbox=props)

# Legende und Titel
ax.legend(loc='lower right', fontsize=12, framealpha=1.0)
plt.title("Asymmetrie der direkten Dichte-Erreichbarkeit", fontsize=14, pad=15)

# Speichern
plt.tight_layout()
plt.savefig('dbscan_asymmetrie.png', dpi=300, bbox_inches='tight') 
print("Grafik mit einheitlicher Punktgröße erfolgreich gespeichert.")

#Base hecha con Claude

"""
Región factible del Símplex
Óptimo LP (rojo) vs Solución Segura P(sob) <= 2,5% (verde)
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# ---------------------------------------------------------------
# Datos del problema
# ---------------------------------------------------------------
P1, P0 = 0.80, 0.70

# Colores
C_NAVY   = "#1F3864"
C_ORANGE = "#E8762C"
C_GREEN  = "#2E8B3D"
C_FILL   = "#CCE0F5"
RED_STAR   = "#E8521E"
GREEN_STAR = "#2CA25F"
GRAY_BOX   = "#7A7A7A"

fig, ax = plt.subplots(figsize=(12, 9))

# ---------------------------------------------------------------
# Región factible
# ---------------------------------------------------------------
verts = [(0, 0), (58, 0), (58, 10), (0, 68)]
ax.add_patch(Polygon(verts, closed=True, facecolor=C_FILL,
                     alpha=0.55, edgecolor="none", zorder=0))

x = np.linspace(0, 80, 400)

# C1
ax.plot(x, 68 - x, color=C_NAVY, lw=2.6,
        label="C1: θ₁ + θ₀ ≤ 68  (máx. citas/día)")

# C2
ax.axvline(58, color=C_ORANGE, lw=2.4,
           label="C2: θ₁ ≤ 58")

# C3
ax.plot(x, (55 - 0.80 * x) / 0.70, color=C_GREEN, lw=2.4,
        label="C3: 0,80 θ₁ + 0,70 θ₀ ≤ 55  (E[X] ≤ C_max)")

# ---------------------------------------------------------------
# Recta iso-z paralela a C3 por (53, 10)
# ---------------------------------------------------------------
z_safe = P1 * 53 + P0 * 10        # = 49.40
ax.plot(x, (z_safe - P1 * x) / P0,
        color=GREEN_STAR, lw=1.8, ls="--", alpha=0.9,
        label=f"iso-z paralela a C3:  z = {z_safe:.2f}",
        zorder=4)

# ---------------------------------------------------------------
# Estrellas (óptimos)
# ---------------------------------------------------------------
ax.scatter([58], [10], marker="*", s=700, color=RED_STAR, zorder=6,
           edgecolor="white", linewidth=0.8,
           label="Óptimo LP (C1 ∩ C2):  z=53.40")
ax.scatter([53], [10], marker="*", s=700, color=GREEN_STAR, zorder=6,
           edgecolor="white", linewidth=0.8,
           label="Solución P(sob.)≤2,5%:  z=49.40")

# Vértices visibles en el nuevo rango
ax.scatter([58, 58], [0, 10], color="black", s=20, zorder=5)

# ---------------------------------------------------------------
# Cajas de anotación  (reposicionadas para el rango 30-80)
# ---------------------------------------------------------------
# Caja roja - óptimo LP  (arriba a la derecha)
ax.annotate("ÓPTIMO LP\nθ₁=58, θ₀=10\nz = E[X] = 53.40\nC3 holgura: 1,60",
            xy=(58, 10), xytext=(64, 18),
            color=RED_STAR, fontsize=10.5, va="center",
            bbox=dict(boxstyle="round", fc="white", ec=RED_STAR, lw=1.4),
            arrowprops=dict(arrowstyle="->", color=RED_STAR, lw=1.4))

# Caja verde - solución segura  (a la izquierda de la estrella verde)
ax.annotate("Solución P(sobrecarga)≤2,5%\nθ₁=53, θ₀=10\n"
            "z = E[X] = 49.40\nDE = 3,25 · P(X>55) = 2,43%",
            xy=(53, 10), xytext=(34, 4),
            color=C_GREEN, fontsize=10.5, va="center",
            bbox=dict(boxstyle="round", fc="#EAF7EA", ec=C_GREEN, lw=1.4),
            arrowprops=dict(arrowstyle="->", color=C_GREEN, lw=1.6))

# Etiquetas de vértices visibles
box_gray = dict(boxstyle="round", fc="#F2F2F2", ec=GRAY_BOX, lw=0.8)
ax.text(60.0, 11.5, "(58, 10)\nz=53.40", fontsize=8.5, color="#333", bbox=box_gray)

# ---------------------------------------------------------------
# Ejes, título y leyenda
# ---------------------------------------------------------------
ax.set_xlim(30, 80)
ax.set_ylim(0, 30)
ax.set_xlabel("θ₁, P(θ₁) = 0,80", fontsize=12)
ax.set_ylabel("θ₀, P(θ₀) = 0,70", fontsize=12)

ax.set_title("Región factible del Símplex\n"
             "Óptimo LP (Rojo) vs Solución Segura P(sob) ≤ 2,5% (Verde)",
             fontsize=14)

ax.grid(True, color="white", lw=1.0, alpha=0.9)
ax.set_axisbelow(True)
ax.legend(loc="upper right", fontsize=10, framealpha=0.95)

plt.tight_layout()
plt.show()
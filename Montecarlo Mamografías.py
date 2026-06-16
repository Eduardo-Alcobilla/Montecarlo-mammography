import random as rm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter

def Visita(prob):
    theta = rm.randrange(1,101)
    if theta <= prob:
        return 1
    
    return 0


Jor = 1000000   #Numero de Jornadas/Simulaciones
TPv = 10      #Primeras visitas TOTAL por Jornada
TSv = 53      #Segundas visitas TOTAL por Jornada
Pv_as = []  #Gente que asiste en simul de Pv
Sv_as = []  #Gente que asiste en simul de Sv
As = []     ##Gente que asiste
Prob_P = 70
Prob_S = 80


#Temporal
Pv = 0      #Primeras visitas
Sv = 0      #Segundas visitas

for i in range(1, Jor + 1):
    Pv = 0      #Primeras visitas
    Sv = 0      #Segundas visitas

    for j in range(1, TPv +1):
        Pv += Visita(Prob_P)

    for k in range(1, TSv + 1):
        Sv += Visita(Prob_S)
    
    Pv_as.append(Pv)
    Sv_as.append(Sv)
    As.append(Pv+Sv)


p05_total = np.percentile(As, 0.5)
p99_total = np.percentile(As, 99.5)

p2_total = np.percentile(As, 2.5)
p97_total = np.percentile(As, 97.5)


print(f"P2.5 Total:            {p2_total:.1f}")
print(f"P97.5 Total:            {p97_total:.1f}")
print(f"P0.5 Total:            {p05_total:.1f}")
print(f"P99.5 Total:            {p99_total:.1f}")


Sobre = (sum(x >= 56 for x in As) / Jor) * 100
Infra = (sum(x <= 49 for x in As) / Jor) * 100

print(f"Sobrecitazion: {Sobre} %")
print(f"Infracitazion: {Infra} %")

fig, ax = plt.subplots(figsize=(15, 5))


# Histograma Total
ax.hist(As, bins=range(35, 70), edgecolor='black', color='mediumseagreen', 
        align='left', weights=np.ones(len(As)) / len(As))
ax.set_title('Total Asistentes')
ax.set_xlabel('Asistentes')
ax.set_ylabel('% de simulaciones')
ax.yaxis.set_major_formatter(PercentFormatter(1))

# Líneas de percentil
ax.axvline(p2_total, color='red', linestyle='--', linewidth=1.5, label=f'P2.5 = {p2_total:.1f}')
ax.axvline(p97_total, color='red', linestyle='--', linewidth=1.5, label=f'P97.5 = {p97_total:.1f}')
ax.axvline(p05_total, color='blue', linestyle='--', linewidth=1.5, label=f'P0.5 = {p05_total:.1f}')
ax.axvline(p99_total, color='blue', linestyle='--', linewidth=1.5, label=f'P99.5 = {p99_total:.1f}')
ax.legend()

plt.suptitle(f'Simulación de Visitas ({Jor} jornadas)', fontsize=14)
plt.tight_layout()
plt.show()


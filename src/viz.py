# filen till plot-funktioner

# från uppgiften i omniway:
# Exempel: intäkt per kategori (stapeldiagram), försäljning över tid (linje/vecka eller månad).
# Tydliga rubriker, axlar och 1–2 meningar markdown som förklarar vad figuren visar.

import matplotlib.pyplot as plt

#------------PLOTTING AOV--------------

# hämtar datan från beräkningsfilen
from metrics import calculate_aov 
monthly_aov, total_aov = calculate_aov()

# Skapar ett stapeldiagram
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(monthly_aov["month"], monthly_aov["AOV"], color="blue")
ax.axhline(y=total_aov, color="orange", linestyle="--")

# lägger till etiketter (AOV värdena) ovanför stolparna
for i, v in enumerate(monthly_aov["AOV"]):
    ax.text(i, v - 100, f"{v}", ha="center", va="top", color= "white")

# anpassar utseendet
ax.set_title("Genomsnittlig orderstorlek (AOV) per månad")
ax.set_xlabel("Månad")
ax.set_ylabel("AOV i kr")
ax.set_ylim(400, 2000)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
#________________________________________

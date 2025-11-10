import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

estados = ["CDMX", "Puebla", "Veracruz", "Oaxaca", "Guerrero", "Hidalgo", "Morelos"]

conexiones = [
    ("CDMX", "Puebla", 120),
    ("CDMX", "Hidalgo", 90),
    ("CDMX", "Morelos", 70),
    ("Puebla", "Veracruz", 180),
    ("Puebla", "Oaxaca", 200),
    ("Oaxaca", "Guerrero", 250),
    ("Guerrero", "Morelos", 150),
    ("Hidalgo", "Veracruz", 210),
    ("Morelos", "Puebla", 110)
]

G.add_weighted_edges_from(conexiones)

print("Estados y sus relaciones:\n")
for estado in G.nodes():
    vecinos = list(G.neighbors(estado))
    print(f"{estado}: {vecinos}")

recorrido_sin_repetir = ["CDMX", "Puebla", "Veracruz", "Hidalgo", "CDMX", "Morelos", "Guerrero", "Oaxaca"]

recorrido_sin_repetir = ["CDMX", "Puebla", "Veracruz", "Hidalgo", "Oaxaca", "Guerrero", "Morelos"]

def calcular_costo(ruta):
    costo_total = 0
    for i in range(len(ruta) - 1):
        if G.has_edge(ruta[i], ruta[i+1]):
            costo_total += G[ruta[i]][ruta[i+1]]["weight"]
        else:
            print(f"No hay conexión entre {ruta[i]} y {ruta[i+1]}")
            return None
    return costo_total

print("\nRecorrido sin repetir:")
print(" -> ".join(recorrido_sin_repetir))
print("Costo total:", calcular_costo(recorrido_sin_repetir))

recorrido_con_repeticion = ["CDMX", "Puebla", "Veracruz", "Puebla", "Oaxaca", "Guerrero", "Morelos"]
print("\nRecorrido repitiendo al menos un estado:")
print(" -> ".join(recorrido_con_repeticion))
print("Costo total:", calcular_costo(recorrido_con_repeticion))

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=10, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo de 7 Estados de México")
plt.show()

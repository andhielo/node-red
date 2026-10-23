"""Simula el microcontrolador (ESP32): envía datos JSON al endpoint de Node-RED.
Uso:  python enviar_datos_prueba.py            (envía 20 lecturas, una cada 2 s)
      python enviar_datos_prueba.py 192.168.1.50   (IP de la PC con Node-RED)
No requiere instalar librerías.
"""
import json, random, sys, time, urllib.request

host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
url = f"http://{host}:1880/actualizar_datos"

for i in range(20):
    datos = {
        "temperatura": round(random.uniform(22, 38), 1),
        "humedad_suelo": random.randint(20, 90),
        "gas": random.randint(80, 550),
        "intrusion": random.random() > 0.85,
        "consumo": random.randint(150, 800),
    }
    req = urllib.request.Request(url, data=json.dumps(datos).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=5) as r:
        print(f"[{i+1:02d}] {datos} -> HTTP {r.status} {r.read().decode()}")
    time.sleep(2)

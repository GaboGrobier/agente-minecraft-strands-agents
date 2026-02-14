'''
librerias a utilizar 
'''


import requests 
from strands import Agent, tool
from strands.models.openai import OpenAIModel
from os import getenv
import json 
import time 

base ="http://127.0.0.1:8080"
TOKEN ="mod-gabogrobier123"
PLAYER = "Player257"


system_prompt= f"""
Eres un pro player de minecraft por lo cual controlas el jugador {PLAYER}

Objetivos:
Explorar el mundo 
no quedarte atascado 
abrirte paso rompiendo bloques si es neceario
buscar un espacio abierto para hacer una casa 

Reglas importantes : 
- anters de moverte simpre consulta el mc_can_step(dx, dz) y usa el dy  que te duvuelva 
- Si mc_raycast detecta un bloque cerca, intenta romperlo.
- Si no puedes avanzar, gira (look) y prueba otra dirección.
- Ejecuta SOLO UNA acción por ciclo.
- Para actuar, SIEMPRE usa mc_action(action_json) con JSON válido (string).

"""
''' Envio de token '''

def _headers():
    return{"X-Agent-Token":TOKEN}

#que es el yaw hotbar y que hace el raise_for_status
@tool
def mc_state() -> dict:
    '''
    Esta herramienta consulta el estado del jugador (posicion/vida/hambre/yaw/pitch/hotbar)
    '''
    response = requests.get(f"{base}/state", headers=_headers(), params={"player": PLAYER}, timeout=2)
    response.raise_for_status()
    return response.json()




@tool
def mc_raycast(distance: int = 4) -> dict:
    '''
    Esta herramienta consulta qué esta viendo el jugador al frente (bloque/entidad/miss)
    '''
    response = requests.get(
        f"{base}/raycast",
        headers=_headers(),
        params={"player": PLAYER, "distance": distance},
        timeout=2
    )
    response.raise_for_status()
    return response.json()

@tool
def mc_can_step(dx: int, dz: int) -> dict:
    '''
    Esta herramienta valida si el jugador puede moverse dx/dz y devuelve dy recomendado (0, 1, -1)
    '''
    response = requests.get(
        f"{base}/can_step",
        headers=_headers(),
        params={"player": PLAYER, "dx": dx, "dz": dz},
        timeout=2
    )
    response.raise_for_status()
    return response.json()


@tool
def mc_action(action_json: str) -> dict:
    '''
    Esta herramienta ejecuta una acción en Minecraft.
    Debes pasar un JSON como string, ejemplo:
      {"type":"look","yaw":90,"pitch":0}
      {"type":"move","dx":1,"dy":0,"dz":0}
      {"type":"break","x":10,"y":64,"z":-3}
    '''
    data = json.loads(action_json)
    data["player"] = PLAYER  # forzamos el jugador correcto
    response = requests.post(
        f"{base}/action",
        headers={**_headers(), "Content-Type": "application/json"},
        json=data,
        timeout=2
    )
    response.raise_for_status()
    return response.json()



@tool
def mc_say(text: str) -> dict:
    '''
    Esta herramienta envia texto al chat del servidor
    '''
    response = requests.post(
        f"{base}/say",
        headers={**_headers(), "Content-Type": "application/json"},
        json={"text": text},
        timeout=2
    )
    response.raise_for_status()
    return response.json()


openai = OpenAIModel(
    client_args={"api_key": getenv("API_GPT")},
    model_id="gpt-4o",
    params={"max_tokens": 600, "temperature": 0.3}
)

agent = Agent(
    model=openai,
    system_prompt=system_prompt,
    tools=[mc_state, mc_raycast, mc_can_step, mc_action, mc_say]
)

# # ====== DEMO 1: una sola interacción (igual que tu ejemplo) ======
# print(agent("Haz 1 ciclo: consulta mc_state y mc_raycast y di qué harías (sin ejecutar acciones)."))

# ====== DEMO 2: loop autónomo (opcional) ======
# Si quieres que "juegue solo", descomenta esto:

print(mc_say("🤖 Agente conectado. Voy a explorar."))

while True:
    # El agente decide y EJECUTA 1 acción por ciclo usando tools
    print(agent(
        "Ciclo: usa mc_state y mc_raycast. "
        "Si ves un bloque, rompe. Si no, intenta avanzar (dx=1,dz=0) usando mc_can_step y luego mc_action. "
        "Si no puedes avanzar, gira a la derecha (yaw+90) con mc_action."
    ))
    time.sleep(0.6)


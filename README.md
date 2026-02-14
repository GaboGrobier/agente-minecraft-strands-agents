# Agente-MC 🎮✨

Un puente simpático entre Python y Minecraft — controla tu mundo desde scripts.

**Descripción**

- **Qué es:** Un proyecto ligero que permite que scripts en Python interactúen con Minecraft usando el mod Minecraft Agent Bridge. Piensa en esto como un asistente programable que camina, coloca bloques y responde dentro del juego.


**Enlace del mod**

- Usa el mod: https://github.com/GaboGrobier/minecraft-agent-bridge

**Requisitos**

- Python 3.10+ (se recomienda 3.11)
- Una instalación de Minecraft compatible con el mod `minecraft-agent-bridge` (sigue las instrucciones en el repo del mod)
- Acceso al directorio `mods/` de tu instalación de Minecraft para poner el mod

**Instalación rápida**

- 1) Clona este repositorio o descarga los archivos en tu máquina.
- 2) Instala dependencias (si hay) — revisa `pyproject.toml` o el README del mod para detalles.

  ```bash
  # macOS / Linux - instalar uv
  curl -LsSf https://astral.sh/uv/install.sh | sh
  # o con pipx
  pipx install uv
  # (alternativa: pip install uv)

  # Windows (PowerShell) - instalar uv
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  # o con pipx (desde PowerShell/Terminal con pipx disponible)
  pipx install uv

  # Crear un entorno gestionado por uv (plataforma-agnóstico)
  uv venv

  # Activar el entorno
  # macOS / Linux (bash/zsh):
  source .venv/bin/activate
  # Windows (PowerShell):
  .\.venv\Scripts\Activate.ps1
  # Windows (cmd.exe):
  .\.venv\Scripts\activate

  # Sincronizar dependencias desde el lockfile (uv.lock / pyproject.toml)
  uv sync
  ```

- 3) Instala el mod `minecraft-agent-bridge` en tu carpeta `mods/` de Minecraft. Reinicia Minecraft con el mod activado.

**Uso básico**

- Hay un punto de entrada en este proyecto:
  - `agente-mc.py` — script principal del agente.

- Ejecuta el agente (ejemplo):

  ```bash
  python3 agente-mc.py
  ```

  Nota: Ajusta el comando según tu entorno y la forma en que `minecraft-agent-bridge` espera conectarse (puerto/host/token).

**Ejemplo rápido (conceptual)**

- Imagina un script que hace que el agente construya una torre de 5 bloques:

  - Conecta con el mod -> envía comandos de movimiento -> coloca bloques -> sale un pequeño resumen.

  (Los detalles exactos de la API vienen del repo del mod; revisa su documentación para nombres de funciones y eventos.)

**Características**

- Automatización de acciones en Minecraft desde Python
- Ideal para demos, streamings y creación de contenido
- Fácil de integrar con scripts para grabar secuencias reproducibles

**Consejos y buenas prácticas**

- Prueba primero en un mundo de pruebas o en un servidor local.
- Añade pausas y checks en tus scripts para evitar bucles infinitos o acciones no deseadas.
- Versiona tus scripts para poder repetir demos exactas.

**Contribuir**

- ¿Tienes ideas o mejoras? ¡Genial! Abre un issue o PR en este repositorio.
- Si mejoras el README o añades ejemplos concretos de uso con el mod, engánchalos aquí para ayudar a futuros creadores.

**Contacto / Créditos**

- Proyecto y mod: GaboGrobier — revisa https://github.com/GaboGrobier/minecraft-agent-bridge


¡Diviértete creando con Python dentro de Minecraft! 🚀🪄

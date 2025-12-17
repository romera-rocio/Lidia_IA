import requests
from utils.safety import safe_response

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def ia_response(user_message: str, context: dict) -> str:
    business = context.get("business", "general")

    system_prompt = f"""
    Sos un asistente de ventas y atención por WhatsApp.
    Tipo de negocio: {business}.
    Respondé claro, profesional y breve.
    Nunca digas que sos una IA.
    """

    payload = {
        "model": MODEL,
        "prompt": system_prompt + "\nCliente: " + user_message,
        "stream": False
    }

    try:
        res = requests.post(OLLAMA_URL, json=payload, timeout=30)
        text = res.json().get("response", "")
        return safe_response(text)

    except Exception:
        return safe_response("")

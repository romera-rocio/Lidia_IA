from core.ia_engine import ia_response
from admin.commands import process_admin

def route_message(phone: str, text: str) -> str:
    if not text:
        return ia_response("", {"business": "general", "intent": "empty"})

    text = text.lower().strip()

    # Comandos administrador (no IA)
    if text.startswith("#"):
        return process_admin(text)

    context = {"intent": "consulta", "business": "general"}

    if any(w in text for w in ["precio", "producto", "comprar", "stock"]):
        context["business"] = "ecommerce"

    elif any(w in text for w in ["menu", "pedido", "comida", "delivery"]):
        context["business"] = "restaurant"

    elif any(w in text for w in ["turno", "horario", "servicio"]):
        context["business"] = "services"

    return ia_response(text, context)

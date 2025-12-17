def process_admin(command: str) -> str:
    if command == "#pedidos":
        return "ADMIN: tenés pedidos pendientes."

    if command.startswith("#enviado"):
        return "ADMIN: pedido marcado como enviado."

    if command == "#ayuda":
        return "ADMIN comandos: #pedidos | #enviado | #ayuda"

    return "ADMIN: comando no reconocido."

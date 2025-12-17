def safe_response(text: str) -> str:
    if not text or len(text.strip()) < 10:
        return (
            "Claro, estoy acá para ayudarte.\n"
            "Decime qué necesitás saber y te respondo."
        )
    return text

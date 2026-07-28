import secrets

def generer_api_key() -> str:
    return secrets.token_hex(16)
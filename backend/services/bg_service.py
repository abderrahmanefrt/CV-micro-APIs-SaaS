from rembg import remove

def enlever_fond(image_bytes: bytes) -> bytes:
    resultat = remove(image_bytes)
    return resultat
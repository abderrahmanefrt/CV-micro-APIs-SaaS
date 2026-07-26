import easyocr

reader = easyocr.Reader(['fr', 'en'])

def extraire_texte(image_bytes: bytes) -> str:
    resultats = reader.readtext(image_bytes, detail=0)
    return " ".join(resultats)
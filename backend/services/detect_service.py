from ultralytics import YOLO
from PIL import Image
import io

modele = YOLO("yolov8n.pt")

def detecter_objets(image_bytes: bytes) -> list:
    image = Image.open(io.BytesIO(image_bytes))
    resultats = modele(image)
    
    detections = []
    for resultat in resultats:
        for box in resultat.boxes:
            classe = modele.names[int(box.cls[0])]
            confiance = float(box.conf[0])
            detections.append({"objet": classe, "confiance": round(confiance, 2)})
    
    return detections
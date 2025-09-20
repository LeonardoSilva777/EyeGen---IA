from ultralytics import YOLO

# Carrega o modelo
modelo = YOLO('yolov8n.pt')

# Executa a detecção, mas agora salva o resultado em uma pasta
# "runs/detect/predict"
modelo.predict(source='img/cat.jpg', save=True, name='resultados', exist_ok=True)
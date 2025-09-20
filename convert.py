from ultralytics import YOLO

# Carrega o modelo YOLOv8n (nano)
model = YOLO('yolov8n.pt')

# Exporta o modelo para o formato TFLite, com a opção de quantização
model.export(format='tflite', int8=True)


#salva o arquivo e quando for rodar ele usa o comando execute-o no terminal da Raspberry Pi python3 convert.py 
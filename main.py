from ultralytics import YOLO
import cv2


model = YOLO('yolov8n.pt')

# Otimiza o modelo para a sua placa, convertendo-o para TFLite 
model = YOLO('yolov8n_full_integer_quant.tflite')


results = model.predict(source='0', show=True)

for r in results:
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#IA. BANCO DE VOZ Reconhecimento de voz 
#reconhecimento pelo console 
#antes da IA falar pro usuario que tem um objeto ele verifica quantos metros 
#Sprint 1 tentar trazer Reconhecimento de objetos, a função de verificar metros, e avisar pro usuario. 

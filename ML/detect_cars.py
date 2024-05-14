from ultralytics import YOLO

# pretrained model for detecting cars
model = YOLO('yolov8n.pt')

#dataset will be update in yolov8 format from ultralytics , traffic signal data has been taken from roboflow , dataset creation website
# training model for traffic signal detection
results = model.train(data = '/data.yaml' ,epochs=5)

# best mode will saved with name best.pt













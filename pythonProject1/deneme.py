from ultralytics import YOLO
from PIL import Image
# resim dosyası üzerinde nesne tanıma
#best1 en iyi sonuc buluyo
model = YOLO('ti.pt')
im1 = Image.open("res.jpg")
sonuc = model.predict(source=im1, save=True)
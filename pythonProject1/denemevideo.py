from ultralytics import YOLO
import subprocess

# YOLO modelini yükle
model = YOLO('best26.pt')

# Video dosyasını aç
video_path = "2024-04-18 15-30-45 - Trim.mp4"  # Video dosyasının yolunu buraya girin
result = model.predict(source=video_path, save=True)

# AVI formatındaki dosyayı MP4 formatına dönüştür
output_avi = result.xyxy[0].export()  # AVI formatında çıktı dosyası
output_mp4 = "output.mp4"  # MP4 formatındaki çıktı dosyası adı
subprocess.run(['ffmpeg', '-i', output_avi, output_mp4])  # FFmpeg kullanarak dönüştürme işlemi

# Dönüştürülen MP4 dosyasının yolunu göster
print(f"Dönüştürülen MP4 dosyası: {output_mp4}")

from ultralytics import YOLO
import subprocess

# YOLO modelini yükle
model = YOLO('best26.pt')

# Video dosyasını aç
video_path = "test-1706604407.mp4"  # Video dosyasının yolunu buraya girin

# Tahmin işlemi ve sonuçların kaydedilmesi
results = model.predict(source=video_path, save=True)

# Kırık ve sağlam sayılarının kaydedileceği liste
data = []

# Tahmin sonuçlarını işleme
for i, result in enumerate(results):
    boxes = result.boxes  # Algılanan nesnelerin kutularını al
    if boxes is not None:
        classes = boxes.cls.cpu().numpy()  # Sınıf etiketlerini al

        # Sınıf etiketlerini kontrol ederek kırık ve sağlam sayısını hesaplayın
        num_saglam = (classes == 1).sum()  # Örnek olarak, 'saglam' sınıfının etiketi 1
        num_kirik = (classes == 0).sum()  # Örnek olarak, 'kirik' sınıfının etiketi 0

        # Çerçeve numarası, sağlam sayısı ve kırık sayısını kaydedin
        data.append((i, num_saglam, num_kirik))

# Sonuçları bir TXT dosyasına yazma
output_txt = "output_counts2.txt"
with open(output_txt, mode='w') as file:
    file.write("Frame\tSaglam\tKirik\n")  # Başlık satırı
    for frame_index, num_saglam, num_kirik in data:
        file.write(f"{frame_index}\t{num_saglam}\t{num_kirik}\n")

print(f"Kırık ve sağlam sayıları {output_txt} dosyasına kaydedildi.")

# AVI formatındaki dosyayı MP4 formatına dönüştür
output_avi = results.save_dir / 'predictions.avi'  # AVI formatında çıktı dosyası
output_mp4 = "output.mp4"  # MP4 formatındaki çıktı dosyası adı
subprocess.run(['ffmpeg', '-i', str(output_avi), output_mp4])  # FFmpeg kullanarak dönüştürme işlemi

# Dönüştürülen MP4 dosyasının yolunu göster
print(f"Dönüştürülen MP4 dosyası: {output_mp4}")

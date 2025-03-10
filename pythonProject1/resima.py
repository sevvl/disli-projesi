import cv2

cap = cv2.VideoCapture("2024-04-18 15-30-45 - TTrim.mp4")
sayac = 6200
max_kare_sayisi = 400

while sayac < 6200 + max_kare_sayisi:
    success, img = cap.read()
    if not success:
        break
    outfile = 'resimler2/resim_%s.jpg' % sayac
    cv2.imwrite(outfile, img)  # Kareyi resim dosyası olarak kaydet
    sayac += 1

cap.release()  # Video yakalama nesnesini serbest bırak

print("İşlem tamamlandı. Toplam {} kare kaydedildi.".format(max_kare_sayisi))



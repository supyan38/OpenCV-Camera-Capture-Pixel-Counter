import cv2

# Fungsi untuk menangkap gambar dari kamera, menyimpan, dan menghitung jumlah pixel
def capture_and_count_pixels():
    # Buka kamera 
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Tidak dapat membuka kamera")
        return

    # Menangkap frame dari kamera
    ret, frame = cap.read()
    if not ret:
        print("Tidak dapat menangkap gambar.")
        return

    # Menampilkan gambar yang ditangkap
    cv2.imshow("Gambar Tertangkap", frame)

    # Menyimpan file citra
    filename = "captured_image.jpg"
    cv2.imwrite(filename, frame)
    print(f"Gambar disimpan sebagai {filename}")

    # Menghitung jumlah pixel (total pixel = lebar x tinggi)
    height, width, _ = frame.shape
    total_pixels = height * width
    print(f"Ukuran citra: {width}x{height}")
    print(f"Jumlah pixel dalam citra: {total_pixels}")

    cv2.waitKey(0)

    # Melepaskan kamera dan menutup jendela
    cap.release()
    cv2.destroyAllWindows()

# Memanggil fungsi
capture_and_count_pixels()

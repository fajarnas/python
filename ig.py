import pywhatkit as kit
import time

# Daftar nomor yang akan dikirim pesan
nomor_list = ["+628567122478", "+6285882088077"]

# Pesan yang akan dikirim
pesan = (
    "Halo, ini adalah pesan otomatis yang dikirim menggunakan Python. "
    "Maaf malam-malam ganggu. PPT sudah dibuat, kalau ada tambahan boleh ditambahkan, "
    "atau kalau ada yang direvisi, silakan direvisi: "
    "https://docs.google.com/presentation/d/1GkjDG4_4gwr-9NFXieYPCILj8xweQuPwlmEIrzlm-ZY/edit?usp=sharing\n"
    "Terima kasih!"
)

# Kirim pesan ke setiap nomor
for nomor in nomor_list:
    try:
        # Kirim pesan secara instan
        kit.sendwhatmsg_instantly(nomor, pesan)

        print(f"✅ Pesan terkirim ke {nomor}")
        time.sleep(3)  # Jeda antar pesan untuk menghindari error atau spam
    except Exception as e:
        print(f"❌ Gagal mengirim ke {nomor}: {e}")

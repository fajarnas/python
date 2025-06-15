import pywhatkit as kit
import time

# Daftar nomor yang akan dikirim pesan
nomor_list = ["+62", "+62"]

# Pesan yang akan dikirim
pesan = (
    "Halo, ini adalah pesan otomatis yang dikirim menggunakan Python. "
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

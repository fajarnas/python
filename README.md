# python

## Mengirim Pesan WhatsApp Otomatis dengan pywhatkit

Repositori ini berisi contoh penggunaan **pywhatkit** untuk mengirim pesan WhatsApp secara otomatis menggunakan Python.

### Instalasi

Pastikan Anda sudah menginstall `pywhatkit`. Jika belum, jalankan perintah berikut:

```bash
pip install pywhatkit
```

### Contoh Penggunaan

Berikut adalah contoh script sederhana untuk mengirim pesan WhatsApp menggunakan pywhatkit:

```python
import pywhatkit

# Kirim pesan WhatsApp ke nomor tujuan pada jam dan menit tertentu
# Format nomor: "+62xxxxxxxxxxx"
# Contoh: "+6281234567890"
pywhatkit.sendwhatmsg(
    phone_no="+62xxxxxxxxxxx",
    message="Halo, ini pesan otomatis dari pywhatkit!",
    time_hour=15,      # Jam (24 jam)
    time_min=30        # Menit
)
```

**Catatan:**
- Pastikan komputer Anda terhubung ke internet dan WhatsApp Web.
- Script ini akan membuka tab browser secara otomatis untuk mengirim pesan.
- Anda dapat menyesuaikan nomor, pesan, jam, dan menit pengiriman sesuai kebutuhan.

### Referensi

- [Dokumentasi pywhatkit](https://github.com/Ankit404butfound/PyWhatKit)# python

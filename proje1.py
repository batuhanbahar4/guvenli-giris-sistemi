# Güvenli Kayıt ve Giriş Sistemi
# Şifre güçlülük kontrolü + 3 hakla kilitlenen giriş
# Yazan: Batuhan Bahar - Ekim 2026

def sifre_kontrol(sifre):
    yaygin_sifreler = ["123456", "password", "qwerty", "111111"]
    rakam_var = False
    buyuk_var = False
    ozel_var = False
    for harf in sifre:
        if harf.isdigit():
            rakam_var = True
        if harf.isupper():
            buyuk_var = True
        if not harf.isalnum():
            ozel_var = True
    if sifre.lower() in yaygin_sifreler:
        return "Bu şifre çok yaygın!"
    elif len(sifre) < 8:
        return "Şifre en az 8 karakter olmalı!"
    elif rakam_var == False:
        return "Şifre en az bir rakam içermeli!"
    elif buyuk_var == False:
        return "Şifre en az bir büyük harf içermeli!"
    elif ozel_var == False:
        return "Şifre en az bir özel işaret içermeli!"
    else:
        return "Şifre kabul edildi ✓"
    
# --- KAYIT --- 
print("=== KAYIT ===")
isim = input("Kullanıcı adı: ")
while True:
    sifre = input("Şifre belirle: ")
    sonuc = sifre_kontrol(sifre) 
    if sonuc == "Şifre kabul edildi ✓":
        print("Kayıt başarılı ✓")
        break    
    else:
        print(sonuc) 
        
#  --- GİRİŞ ---
print("=== GİRİŞ ===")
max_hak = 3
deneme = 0
while deneme < max_hak :
    giris_isim = input("Kullanıcı adı: ")
    giris_sifre = input("Şifre: ")
    if giris_isim == isim and giris_sifre == sifre :
        print(f"Hoş geldin {isim}!")
        break 
    else:
        deneme = deneme + 1 
        print(f"Kullanıcı adı veya şifre yanlış! Kalan hak: {max_hak - deneme}")
if deneme == max_hak:
    print("Hesap kilitlendi")
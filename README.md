# 🔐 Güvenli Kayıt ve Giriş Sistemi

Python ile yazdığım, temel güvenlik önlemleri içeren bir kayıt ve giriş sistemi.
Python ve siber güvenlik öğrenme yolculuğumun ilk projesi.

## Özellikler

- **Şifre güçlülük kontrolü:** En az 8 karakter, rakam, büyük harf ve özel işaret zorunlu
- **Sözlük saldırısı koruması:** Yaygın şifreler (123456, qwerty...) büyük/küçük harf fark etmeksizin reddedilir
- **Brute force koruması:** 3 yanlış denemede hesap kilitlenir
- **Kullanıcı adı numaralandırma koruması:** Hatalı girişte "kullanıcı adı veya şifre yanlış" denir, saldırgana hangisinin yanlış olduğu söylenmez

## Nasıl Çalıştırılır

```bash
python3 proje1.py
```

## Örnek Kullanım

```
=== KAYIT ===
Kullanıcı adı: batu
Şifre belirle: 123
Şifre en az 8 karakter olmalı!
Şifre belirle: Batu.2026
Kayıt başarılı ✓
=== GİRİŞ ===
Kullanıcı adı: batu
Şifre: Batu.2026
Hoş geldin batu!
```

## Bilinen Sınırlamalar

Bu bir öğrenme projesi. Gerçek bir sistemde şunlar eksik olurdu:

- Kayıtlar program kapanınca siliniyor (dosya/veritabanı yok)
- Şifreler bellekte düz metin olarak tutuluyor (hash'lenmiyor)
- Program yeniden başlatılınca kilit sıfırlanıyor

Bunları ilerleyen versiyonlarda geliştirmeyi planlıyorum.

## Kullandıklarım

Python · fonksiyonlar · döngüler · listeler · koşullar

---
👤 **Batuhan Bahar** — Python & Siber Güvenlik öğreniyor

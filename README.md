# AWS Tabanlı Personel Yönetim Sistemi

Bu çalışma, modern bir web uygulamasının uçtan uca bulut mimarisi üzerinde nasıl kurgulanacağını gösteren bir projedir. Sistem; veritabanı, arka yüz ve ön yüz katmanlarının tamamı **Amazon Web Services (AWS)** ekosistemi üzerinde, yüksek erişilebilirlik prensipleriyle barındırılmaktadır.

## Canlı Proje Bağlantıları

Projeyi incelemek isteyenler için sistem şu an aktif olarak AWS üzerinde çalışmaktadır:

* **🌐 Ön Yüz (Uygulama Arayüzü):** [http://blm3522-proje1-frontend.s3-website.us-east-2.amazonaws.com/](http://blm3522-proje1-frontend.s3-website.us-east-2.amazonaws.com)

---

## 🏗️ Sistem Mimarisi

Sistem, birbiriyle asenkron haberleşen üç temel katmandan oluşmaktadır:

1.  **Frontend:** React (Vite) ile geliştirilmiştir. Statik web dosyaları olarak derlenerek **AWS S3** üzerinde statik web barındırma modunda yayınlanmıştır.
2.  **Backend:** Python Flask framework'ü ile geliştirilen API. **AWS EC2 (Ubuntu)** sunucusu üzerinde `nohup` servisi ile 7/24 aktif tutulmaktadır.
3.  **Veritabanı:** **AWS RDS (MySQL)** servisi kullanılarak veri kalıcılığı ve güvenliği sağlanmıştır.

## 🛠️ Teknik Özellikler

### **Kullanılan Teknolojiler**
* **Frontend:** React, CSS3, Fetch API, Vite.
* **Backend:** Python 3, Flask, MySQL Connector.
* **Cloud:** AWS (S3, EC2, RDS, Security Groups).

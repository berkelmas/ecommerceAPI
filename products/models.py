from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Kategori(models.Model):
    kat_isim = models.CharField(('Kategori Adı'), max_length= 150)
    kat_aciklama = RichTextField(('Kategori Açıklaması'))

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

class Marka(models.Model):
    marka_isim = models.CharField(('Marka Adı'), max_length=150)
    marka_resim = models.ImageField(('Marka Resmi'))

    class Meta:
        verbose_name = "Marka"
        verbose_name_plural = "Markalar"

class Varyant(models.Model):
    varyant_isim = models.CharField(('Varyant Adı'), max_length=80)

    ## Burasi da array olarak kurulacak; front end'de array acilarak localStorage'a kaydedilecek
    ## en son da siparisde siparis_urunler alanina json objesi olarak gelecek.
    varyant_secenekleri = models.CharField(('Varyant Seçenekleri'), max_length=300)

    class Meta:
        verbose_name = "Varyant"
        verbose_name_plural = "Varyantlar"

class Urun(models.Model):
    urun_isim = models.CharField(('Ürün İsmi'), max_length= 150)
    urun_aciklama = RichTextField(('Ürün Açıklaması'))
    urun_fiyat = models.FloatField(('Ürün Fiyatı'))
    urun_eskifiyat = models.FloatField(('Ürün Eski Fiyatı'), blank= True, null=True)

    urun_onecikan = models.BooleanField(('Ürünün Öne Çıkma Durumu'))
    urun_coksatan = models.BooleanField(('Ürün Çok Satan Durumu'))
    urun_durum = models.BooleanField(('Ürün Aktiflik Durumu'))

    urun_metadescription = models.TextField(('Ürün Meta Açıklaması'))

    urun_resim1 = models.ImageField(('Ürün Resim 1'))
    urun_resim2 = models.ImageField(('Ürün Resim 2'))
    urun_resim3 = models.ImageField(('Ürün Resim 3'))
    urun_resim4 = models.ImageField(('Ürün Resim 4'))

    kategori = models.ForeignKey(Kategori, null= True, on_delete= models.SET_NULL)
    marka = models.ForeignKey(Marka, null= True, on_delete= models.SET_NULL)
    varyant = models.ManyToManyField(Varyant)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"


class Siparis(models.Model):
    SIPARIS_DURUMU = (
        ('onay', 'Sipariş Onaylandı'),
        ('hazirlik', 'Sipariş Hazırlanıyor'),
        ('kargo', 'Kargoya Verildi'),
        ('teslim', 'Teslim Edildi')
    )
    siparis_durum = models.CharField(('Sipariş Durumu'), choices=SIPARIS_DURUMU, max_length= 60 )

    # Urunler json objesi olarak gelecek.
    siparis_urunler = models.TextField()
    siparis_adres = models.TextField()
    siparis_user = models.CharField(('Siparis Verenin Adi'), max_length= 100)
    siparis_adres = models.TextField()
    siparis_useriletisim = models.CharField(('Sipariş Veren İletişim Bilgileri'), max_length= 100)
    siparis_fiyat = models.CharField(('Toplam Sipariş Bedeli'), max_length=30)

    siparis_tarih = models.DateField(auto_now_add= True)

    class Meta:
        verbose_name = "Sipariş"
        verbose_name_plural = "Siparişler"

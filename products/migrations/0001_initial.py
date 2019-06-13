# Generated by Django 2.2.2 on 2019-06-13 15:54

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kat_isim', models.CharField(max_length=150, verbose_name='Kategori Adı')),
                ('kat_aciklama', ckeditor.fields.RichTextField(verbose_name='Kategori Açıklaması')),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
            },
        ),
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka_isim', models.CharField(max_length=150, verbose_name='Marka Adı')),
                ('marka_resim', models.ImageField(upload_to='', verbose_name='Marka Resmi')),
            ],
            options={
                'verbose_name': 'Marka',
                'verbose_name_plural': 'Markalar',
            },
        ),
        migrations.CreateModel(
            name='Siparis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siparis_durum', models.CharField(choices=[('onay', 'Sipariş Onaylandı'), ('hazirlik', 'Sipariş Hazırlanıyor'), ('kargo', 'Kargoya Verildi'), ('teslim', 'Teslim Edildi')], max_length=60, verbose_name='Sipariş Durumu')),
                ('siparis_urunler', models.TextField()),
                ('siparis_user', models.CharField(max_length=100, verbose_name='Siparis Verenin Adi')),
                ('siparis_adres', models.TextField()),
                ('siparis_useriletisim', models.CharField(max_length=100, verbose_name='Sipariş Veren İletişim Bilgileri')),
                ('siparis_fiyat', models.CharField(max_length=30, verbose_name='Toplam Sipariş Bedeli')),
                ('siparis_tarih', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Sipariş',
                'verbose_name_plural': 'Siparişler',
            },
        ),
        migrations.CreateModel(
            name='Varyant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varyant_isim', models.CharField(max_length=80, verbose_name='Varyant Adı')),
                ('varyant_secenekleri', models.CharField(max_length=300, verbose_name='Varyant Seçenekleri')),
            ],
            options={
                'verbose_name': 'Varyant',
                'verbose_name_plural': 'Varyantlar',
            },
        ),
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urun_isim', models.CharField(max_length=150, verbose_name='Ürün İsmi')),
                ('urun_aciklama', ckeditor.fields.RichTextField(verbose_name='Ürün Açıklaması')),
                ('urun_fiyat', models.FloatField(verbose_name='Ürün Fiyatı')),
                ('urun_eskifiyat', models.FloatField(blank=True, null=True, verbose_name='Ürün Eski Fiyatı')),
                ('urun_onecikan', models.BooleanField(verbose_name='Ürünün Öne Çıkma Durumu')),
                ('urun_coksatan', models.BooleanField(verbose_name='Ürün Çok Satan Durumu')),
                ('urun_durum', models.BooleanField(verbose_name='Ürün Aktiflik Durumu')),
                ('urun_metadescription', models.TextField(verbose_name='Ürün Meta Açıklaması')),
                ('urun_resim1', models.ImageField(upload_to='', verbose_name='Ürün Resim 1')),
                ('urun_resim2', models.ImageField(upload_to='', verbose_name='Ürün Resim 2')),
                ('urun_resim3', models.ImageField(upload_to='', verbose_name='Ürün Resim 3')),
                ('urun_resim4', models.ImageField(upload_to='', verbose_name='Ürün Resim 4')),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Kategori')),
                ('marka', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Marka')),
                ('varyant', models.ManyToManyField(to='products.Varyant')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
            },
        ),
    ]

# My Watchlist
Deployment link : [link](https://tugas2-pbp-fajar.herokuapp.com/mywatchlist/)

# Perbedaan HTML, XML, dan JSON
*HTML: HTML (_Hyper Text Markup Language_) digunakan untuk membuat halaman web dan aplikasi web. _HTML_ adalah suatu bahasa markup. Dengan _HTML_ kita dapat membuat halaman statis kita sendiri. _HTML_ digunakan untuk menampilkan data bukan untuk mengangkut data. _HTML_ adalah kombinasi dari _Hypertext_ dan bahasa _Markup_. _Hypertext_ mendefinisikan link antara halaman web. Bahasa markup digunakan untuk mendefinisikan dokumen teks dalam tag yang mendefinisikan struktur halaman web. Bahasa ini digunakan untuk membubuhi keterangan (membuat catatan untuk komputer) teks sehingga mesin dapat memahaminya dan memanipulasi teks yang sesuai.
* XML: XML (_eXtensible Markup Language_)  markup language yang digunakan untuk menyederhanakan proses penyimpanan dan pengiriman data antarserver. XML cenderung menyimpan data dalam format teks sederhana seperti tree yang mirip dengan HTML. Format ini cenderung mudah dibaca oleh manusia dibandingkan format JSON, tetapi pertukaran data akan berlangsung lebih lama. XML cukup dinamis karena digunakan untuk mengangkut data bukan untuk menampilkan data. Tujuan desain XML fokus pada kesederhanaan, umum, dan kegunaan di Internet. Meskipun desain XML berfokus pada dokumen, bahasa XML banyak digunakan untuk representasi struktur data arbitrer seperti yang digunakan dalam layanan web.
* JSON atau JavaScript Object Notation merupakan suatu format yang dibuat di atas JavaScript untuk merepresentasikan data dalam bentuk key dan value. JSON dapat digunakan untuk melakukan penyimpanan dan pertukaran data dengan cepat dikarenakan strukturnya yang dapat menyimpan data dalam bentuk array, tetapi lebih sulit untuk dibaca oleh manusia daripada XML. 

# Alasan diperlukan data delivery dalam pengimplementasian platform
Pada suatu platform seringkali terdapat pertukaran data antara user atau clients dan juga server. Data delivery diperuntukkan untuk memudahkan suatu platform dalam melakukan pengiriman data. Data tersebut tentu memerlukan berbagai format dalam pertukarannya. Format yang seringkali  digunakan antara lain adalah HTML, JSON, dan XML. Pada umumnya data terbagi menjadi dua jenis yaitu data yang bersifat statis dan data yang bersifat dinamis. Data yang statis merujuk pada data yang jarang diakses dan kemungkinan besar tidak akan diubah. Sedangkan data dinamis adalah data yang terupdate secara periodik. Artinya data tersebut akan terus berganti apabila terdapat informasi baru yang didapatkan server. Serta dari yang kita tahu, informasi baru kemungkinan besar akan tetap datang apabila kita berbicara mengenai platform. Teknologi tidak lepas dari informasi-informasi sehingga data cenderung bersifat dinamis. Maka dari itu, kedinamisan data ini akan sangat terbantu dengan adanya data delivery (transmisi data) yang tersedia dalam bentuk XML maupun JSON.

# Langkah-langkah implementasi
1. Membuat Apps baru bernama mywatchlist lalu menambahkan path mywatchlist di direktori project_django pada file settings.py dan pada file urls.py

```shell
INSTALLED_APPS = [
    ...
    'mywatchlist',
]
```

```shell
urlpatterns = [
    ...
    path('katalog/', include('katalog.urls')),
    path('mywatchlist/', include('mywatchlist.urls')),
]

```

2. Membuka file models.py yang ada pada direktori mywatchlist dan menambahkan sebuah class MyWatchList dengan parameter models.Model yaitu:

```shell
class MyWatchList(models.Model):
    watched = models.CharField(max_length=3)
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
```

3. Membuat file bernama "initial_watchlist_data.json" lalu menambahkan data sebagai objek dari model MyWatchList

4. Buka terminal (cmd) dan jalankan perintah berikut untuk melakukan migrasi skema model ke database Django lokal:

   ```shell
   python manage.py makemigrations
   ```

5. Jalankan perintah berikut untuk menerapkan skema model diatas:

   ```shell
   python manage.py migrate
   ```

6. Jalankan perintah berikut untuk memasukkan data pada initial_watchlist_data.json pada database Django lokal:

   ```shell
   python manage.py loaddata initial_watchlist_data.json
   ```
   
7. Membuat file-file html yang ingin ditampil
8. Membuat function-function pada file views.py yang berada di folder mywatchlist
9. Membuat routing dengan cara menambahkan urlpatterns pada file urls.py di folder mywathlist
9. Menambahkan Class dan fungsi pada test.py yang berguna sebagai unit test
10. Menambahkan isi Procfile agar pada saat aplikasi sudah terdeploy di heroku akan menampilkan initial data yang sudah disiapkan
```shell
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_watchlist_data.json'
web: gunicorn project_django.wsgi --log-file -
```
11. Langkah terakhir yang saya lakukan adalah melakuka push ke GitHub dengan menjalankan
    ```shell
    git add -A
    git commit -m "Your Commit"
    git push origin main
    ```
# Postman
## HTML
![image](https://user-images.githubusercontent.com/97015801/191504278-62bdf203-1920-42f3-bcd2-7c2d096e62ce.png)

## JSON
![image](https://user-images.githubusercontent.com/97015801/191504626-ffa30173-bbb5-4d72-b5fc-d4eab1d46a6d.png)

## XML
![image](https://user-images.githubusercontent.com/97015801/191504754-9ad7e4b2-1744-4520-8398-4ce6b5708906.png)

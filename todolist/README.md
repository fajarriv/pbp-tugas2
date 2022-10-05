## TODOLIST (TUGAS 4)
Deployment link : [link](https://tugas2-pbp-fajar.herokuapp.com/todolist)
Username Account : akunpengguna1,akunpengguna2
Password  : 123pass123

### Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
CSRF (*Cross Site Request Forgery*) merupakan suatu serangan/exploit di mana suatu situs yang berbeda (domain) membuat request atau mengirim perintah atas nama pengguna pada suatu situs target. `{% csrf_token %}` berguna untuk menghindari CSRF attack yang mungkin akan digunakan oleh penyerang. `{% csrf_token %}` akan meng-generate token pada server sesaat kita melakukan rendering pada halaman/browser, serta melakukan filter request yang masuk pada browser. Apabila tidak ada potongan kode tersebut pada elemen `<form>` maka akan terjadi sebuah eror, akan terdapat HTTP Request 403 Forbidden karena verifikasi CSRF gagal dan request diabaikan.

### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat `<form>`secara manual.
Ya bisa. Hal pertama yang harus dilakukan adalah membuat form pada sebuah HTML (template) form tersebut akan mengirim sebuah request POST dan jangan lupa untuk menambahkan `{% csrf_token %}` pada form. Form yang sudah dibuat dapat diproses dengan cara membuat fungsi-fungsi pada Views.

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
  1. Request dari client akan dibaca oleh views 
  2. Parameter dan value dari form (request POST) akan diterima oleh Views
  3. Pada views akan terdapat opersai seperti CRUD untuk memanipulasi Database
  4. Views akan mengambil data terbaru setelah dimanipulasi untuk *template* lalu Views akan mengembalikan hasil *render* dengan *template* dan *context* yang diberikan.

### Langkah-langkah implementasi
1. Membuat apps baru bernama todolist, menambahkan Apps baru ke settings.py dan menambahkan path pada file urls.py (folder project_django)
    ```shell
    INSTALLED_APPS = [
          ...
          'mywatchlist',
          'todolist'
    ]
    ```
    ```shell
    urlpatterns = [
        ...
        path('katalog/', include('katalog.urls')),
        path('mywatchlist/', include('mywatchlist.urls')),
        path('todolist/', include('todolist.urls')),
    ]
    ```
2. Membuka file models.py yang ada pada direktori todolist dan menambahkan sebuah class Task dengan parameter models.Model yaitu:

    ```shell
    class Task(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      date = models.DateField()
      title = models.TextField()
      description = models.TextField()
      is_finished = models.BooleanField(default= False)
    ```
3. Buka terminal (cmd) dan jalankan perintah berikut untuk melakukan migrasi skema model ke database Django lokal:

   ```shell
   python manage.py makemigrations
   ```

4. Jalankan perintah berikut untuk menerapkan skema model diatas:

   ```shell
   python manage.py migrate
   ```
5. Membuat file-file html yang ingin ditampilkan
6. Membuat file `forms.py` lalu membuat class baru untuk membuat form yang ingin ditampilkan
  ```shell
  class TaskForm(forms.Form):
    title = forms.CharField(label="Judul Task")
    description = forms.CharField(label="Deskripsi Task", widget=forms.Textarea)
  ```
6. Membuat function-function pada file views.py yang berada di folder todolist
7. Membuat routing dengan cara menambahkan urlpatterns pada file urls.py di folder todolist
8. Melakukan push ke GitHub dengan menjalankan
    ```shell
    git add -A
    git commit -m "Your Commit"
    git push origin main
    ```

## TUGAS 5
Deployment link : [link](https://tugas2-pbp-fajar.herokuapp.com/todolist)

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
 Inline CSS dibuat di dalam sebuah elemen atau tag HTML dengan cara menambahkan atribut `style=""`. Scope dari Inline CSS hanya pada elemen yang digunakan atribut tersebut. Kelebihan dari menggunakan Inline CSS yaitu dapat menerapkan *style* hanya pada satu elemen saja. Sedangkan kekurangannya yaitu file HTML akan terlihat berantakan.

 Internal CSS dibuat di dalam sebuah elemen `<style>` pada suatu file HTML, sehingga hanya berlaku pada file tersebut saja. Internal CSS relatif lebih baik dan rapih dibandingkan dengan inline CSS, namun apabila terdapat beberapa *style* yang berulang untuk page / file HTML lainnya maka akan menjadi tidak efisien

 External CSS dibuat di sebuah file `.css` baru, lalu dimasukkan dengan menggunakan elemen atau tag `<link>` ke dalam suatu halaman / file HTML. Pada External CSS stylesheet berada pada file terpisah sehingga membuat file html lebih pendek dan mudah untuk dibaca. 

### Jelaskan tag HTML5 yang kamu ketahui.
Terdapat banyak sekali tag HTML5 yang tersedia. Berikut adalah beberapa elemen yang sering saya gunakan.
- `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`, tag untuk membuat teks judul / subjudul (*heading*).
- `<p>`, tag untuk membentuk sebuah paragraph .
- `<div>`, tag untuk mengemas beberapa elemen menjadi sebuah section atau *division*.
- `<ul>` dan `<ol>`, tag untuk daftar tak terurut (unordered) dan daftar terurut (ordered). `<li>` digunakan untuk tiap butir pada daftar.
- `<button>`, tag untuk membuat tombol yang dapat di*click*.
- `<a>`, tag untuk mendifinisikan *hyperlink* yang digunakan untuk menghubungkan dari satu halaman ke halaman lain.
- `<b>`, tag untuk menebalkan font (bold).
- `<i>`, tag untuk memiringkan font (italic).
- `<table>` (tabel keseluruhan), `<tr>` (baris/*row*), `<th>` (kepala/*head*), `<td>` (data), untuk membuat sebuah tabel.
- `<style>`, tag untuk menambahkan CSS secara internal.

### Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- *Universal selector* merupakan selector yang akan memilih semua elemen.  
  Contohnya adalah `*`,  yang akan memilih semua elemen.
- *Type selector* merupakan selector yang akan memilih semua elemen dengan tipe/nama node yang sama.  
  Contohnya adalah `input`, yang akan memilih semua elemen `<input>`.
- *Class selector* merupakan selector berdasarkan class untuk mentargetkan beberapa section dengan class yang bersesuaian.  
  Contohnya adalah `.card`, yang akan memilih semua elemen dengan kelas `card`.
- *ID selector* merupakan selector berdasarkan id yang akan mentargetkan beberapa section dengan id yang bersesuaian.
  Contohnya adalah `#header`, yang akan memilih semua elemen dengan ID `header`. Idealnya, satu ID hanya ada pada satu elemen.

### Langkah-langkah implementasi
- Instalasi Bootstrap melalui CDN yang ada di [dokumentasi Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/#cdn-links)
- Menerapkan kustomisasi style pada tags-tags html pada django template dengan bantuan [template](https://mdbootstrap.com/docs/standard/extended/login/) yang ada di internet
- Menerapkan Grid System dari Bootstrap agar website menjadi responsive
- Menambahkan potongan kode CSS berikut agar terdapat efek ketika melakukan hover pada cards todolist
  ```shell
    .card:hover{
    transform: scale(1.1);

    }
    .card{
        transition: transform .5s;
    }
    ```
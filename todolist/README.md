## TODOLIST
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
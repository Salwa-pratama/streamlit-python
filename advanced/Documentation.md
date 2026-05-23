# Advanced concepts of streamlit

Sekarang setelah Anda mengetahui cara kerja aplikasi Streamlit dan cara menangani data, mari kita bahas tentang efisiensi. Caching memungkinkan Anda menyimpan output suatu fungsi sehingga Anda dapat melewatinya saat menjalankan ulang. Session State memungkinkan Anda menyimpan informasi untuk setiap pengguna yang tetap tersimpan di antara eksekusi ulang. Ini tidak hanya memungkinkan Anda menghindari perhitungan ulang yang tidak perlu, tetapi juga memungkinkan Anda membuat halaman dinamis dan menangani proses progresif.


# Caching

Caching memungkinkan aplikasi Anda tetap berkinerja baik bahkan saat memuat data dari web, memanipulasi kumpulan data besar, atau melakukan komputasi yang mahal.

Ide dasar di balik caching adalah menyimpan hasil panggilan fungsi yang mahal dan mengembalikan hasil yang di-cache ketika input yang sama terjadi lagi. Ini menghindari eksekusi berulang dari suatu fungsi dengan nilai input yang sama.

Untuk melakukan caching pada suatu fungsi di Streamlit, Anda perlu menerapkan decorator caching padanya. Anda memiliki dua pilihan:

 - `st.cache_data` adalah cara yang direkomendasikan untuk menyimpan komputasi yang mengembalikan data dalam cache. Gunakan `st.cache_data` saat Anda menggunakan fungsi yang mengembalikan objek data yang dapat diserialisasi (misalnya, `str`, `int`, `float`, `DataFrame`, `dict`, `list`). Ini membuat salinan baru data pada setiap panggilan fungsi, sehingga aman dari mutasi dan kondisi persaingan (race condition). Perilaku `st.cache_data` adalah yang Anda inginkan dalam sebagian besar kasus – jadi jika Anda ragu, mulailah dengan `st.cache_data` dan lihat apakah itu berhasil!

 - `st.cache_resource` adalah cara yang direkomendasikan untuk menyimpan sumber daya global seperti model ML atau koneksi basis data dalam cache. Gunakan `st.cache_resource` ketika fungsi Anda mengembalikan objek yang tidak dapat diserialisasi yang tidak ingin Anda muat berulang kali. Fungsi ini mengembalikan objek yang disimpan dalam cache itu sendiri, yang dibagikan di semua eksekusi ulang dan sesi tanpa penyalinan atau duplikasi. Jika Anda memodifikasi objek yang disimpan dalam cache menggunakan `st.cache_resource`, modifikasi tersebut akan ada di semua eksekusi ulang dan sesi.


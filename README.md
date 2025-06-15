# 🛠️ UnionHelper

**UnionHelper** adalah tools Python sederhana yang dirancang untuk mempermudah saat melakukan SQL Injection manual, khususnya pada bagian `UNION SELECT`. Biasanya kita harus menulis urutan angka secara manual seperti `1,2,3,4,...`, dan tools ini akan mengotomatisasi proses tersebut.

## 🎯 Tujuan
Mempermudah pembuatan payload `UNION SELECT` dengan angka berurutan, tanpa perlu mengetiknya satu per satu secara manual.

## 🔍 Contoh Kasus
Biasanya, saat melakukan SQLi:
https://target.com/page.php?id=-1 UNION SELECT 1,2,3,4,5,6,7,8,9,10--

Dengan UnionHelper, kamu tinggal input angka awal dan akhir, dan langsung dapatkan hasil seperti `1,2,3,...`.

## ⚙️ Cara Install & Jalankan
```bash
pip install termcolor
pip install pyfiglet
git clone https://github.com/SURY0X/UnionHelper.git
cd UnionHelper
python main.py

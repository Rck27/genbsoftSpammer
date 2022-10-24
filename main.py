
import random
import requests
from string import ascii_uppercase as alc


url = "http://cbt.smekta.my.id/cbtsmekta/cbt/proses.php"

headerr = {
"POST": "/cbtsmekta/cbt/proses.php HTTP/1.1",
"Accept": "text/html, */*",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9",
"Connection": "keep-alive",
"Content-Length": "50",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Cookie": "KODE_KELAS=XII; KODE_JURUSAN=TKJ; RUANG=R1; SESI=1; NEW=baru; USERNAME=K024; PASSWORD=K024; AUTO=yes; W=1366; H=768; token=1263019; NISN=024; TABEL_UJIAN=TLJ_XII_TKJ_PH_2022103_R1_1; KODE_MATERI=TLJ_XII_TKJ_PH_2022103; AKSI=soal",
"Host": "cbt.smekta.my.id",
"Origin": "http://cbt.smekta.my.id",
"Referer": "http://cbt.smekta.my.id/cbtsmekta/cbt/",
"User-Agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}
cookie = {
        "KODE_KELAS": "XII", "KODE_JURUSAN": "TKJ", "RUANG": "R1", "SESI": "1", "NEW": "baru", "USERNAME":"K024", "PASSWORD":"K024", "AUTO":"yes", "W":"1366", "H":"768", "token":"5613836", "NISN":"024", "TABEL_UJIAN":"TLJ_XII_TKJ_PH_2022103_R1_1", "KODE_MATERI":"TLJ_XII_TKJ_PH_2022103", "AKSI":"soal"
}
jawab = ["A", "B", "C", "D", "E"]
req1 = "tabel=tlj_xii_tkj_ph_2022103_r1_1&jum_soal=100&aksi=selesai&sisa_waktu=00%3A00%3A00"
stat = True
for i in range (0, 100):
    a = str(i)
    print(i)
    rand = jawab[random.randint(0, 4)]
    print(rand)
    c = "js=1&jawaban="+rand+"&aksi=simpan_jawab&nosoal="+a+"&tabel=tlj_xii_tkj_ph_2022103_r1_1&is_essai=&timer=00%3A02%3A52"
    x = requests.post(url, data = c, headers= headerr, cookies= cookie)
    print(x.content)
# while True:
#     c = "tabel=tlj_xii_tkj_ph_2022103_r1_1&jum_soal=100&aksi=selesai&sisa_waktu=00%3A00%3A00"
#     x = requests.post(url, data = c, headers= headerr, cookies= cookie)
#     print(x.content)




# for b in range(99, 200):
#     a = str(b)
#     i = "K"
#     # for i in alc:
#     c = "username="+i+"0"+a+"&password="+i+"0"+a+"&aksi=login_val&auto=no"
#     print(i)
#     x = requests.post(url, data = c, headers = headerr)
#     print(a)
#     print(c)
#     if(x.content != "b'no_user'"):
#         print(x.content)
        



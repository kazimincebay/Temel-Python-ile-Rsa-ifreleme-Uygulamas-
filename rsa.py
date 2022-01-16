print("rsa şifreleme algoritması")


def rsa():
    nsayisi=psayisi*qsayisi
    fisayisi=(psayisi-1)*(qsayisi-1)
    print("fi sayisi = ",fisayisi)
    if fisayisi<1:
        print("Fi sayısı 1den büyük olmalıdır")
    if fisayisi>1:
        def esayi():
            esayisi=int(input("e sayısını giriniz "))
            if 1>esayisi or esayisi>fisayisi:
                print("Lütfen 1 ile fi sayısı aralığında bir değer seçiniz")
                return esayi()
            else:
                mesaj=input("mesajınızı giriniz ")
                print("Şifreli Metin ")
            for i in mesaj:
                sifre=(ord(i)**esayisi)%nsayisi
                print(sifre)
            
        esayi()

psayisi=int(input("p sayısını giriniz "))
qsayisi=int(input("q sayısını giriniz "))

if(psayisi%2==0 or qsayisi%2==0) and (psayisi%3==0 or qsayisi%3==0) and (psayisi%4==0 or qsayisi%4==0) and (psayisi%5==0 or qsayisi%5==0) and (psayisi%6==0 or qsayisi%6==0) and (psayisi%7==0 or qsayisi%7==0):
    print("Sayılar Asal değil")
elif (psayisi-1==qsayisi) or (qsayisi-1==psayisi):
    rsa()
elif (psayisi==1) or (qsayisi==1):
    rsa()
else:
    rsa()









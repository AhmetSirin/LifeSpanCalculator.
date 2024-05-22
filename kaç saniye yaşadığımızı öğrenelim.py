from datetime import *
dogum_tarihi = datetime.strptime(input("Lütfen doğum tarihinizi gün.ay.yıl saat.dakika şeklinde giriniz: "),"%d.%m.%Y %H.%M")
yas = datetime.now() - dogum_tarihi
if yas.total_seconds() > 0:
    print("Siz {} yılından günümüze kadar {} saniye yaşadınız.".format(dogum_tarihi,yas.total_seconds()))
else:
    print("Malesef henüz doğmadınız...")

baska_hasta="E"
A_sayisi, B_sayisi, toplam_hasta, agir_sayisi, orta_sayisi, hafif_sayisi= 0, 0, 0, 0, 0, 0
A_inhibitor, B_inhibitor, profilaksi_A, profilaksi_B, orta_profilaksi= 0, 0, 0, 0, 0
A_plazma, A_rekombinant, B_plazma, B_rekombinant= 0, 0, 0, 0
dört_hafta_plazma_8, dört_hafta_plazma_9, dört_hafta_rekombinant_8, dört_hafta_rekombinant_9= 0, 0, 0, 0
plazma_8_binlik, plazma_8_besyuzluk, plazma_8_ikiyuzellilik= 0, 0, 0
rekombinant_8_binlik, rekombinant_8_besyuzluk, rekombinant_8_ikiyuzellilik= 0, 0, 0
plazma_9_binlik, plazma_9_besyuzluk, plazma_9_ikiyuzellilik= 0, 0, 0
rekombinant_9_binlik, rekombinant_9_besyuzluk, rekombinant_9_ikiyuzellilik= 0 ,0, 0
toplam_profilaksi, toplam_dort_haftalik_ilac_tutar, toplam_yillik_ilac_tutar= 0, 0, 0
toplam_dort_haftalik_ilac_miktari, toplam_yillik_ilac_miktari= 0, 0
A_max_dort_haftalik_ilac_miktar, B_max_dort_haftalik_ilac_miktar= 0, 0
C_max_dort_hafta_ilac_tutar=0
while baska_hasta=="E" or baska_hasta=="e":
    profilaksi, binlik, besyuzluk, ikiyuzellilik= 0, 0, 0, 0
    toplam_hasta+=1
    tc=int(input("TC no giriniz:"))
    ad_soyad=input("ad soyad giriniz:")
    tip=input("hemofili hastaliği tipini giriniz(A/a/B/b):")
    while tip!="A" and tip!="a" and tip!="B" and tip!="b": tip=input("hemofili hastaliği tipini doğru giriniz(A/a/B/b):")
    if tip=="A" or tip=="a":
        tip="A"
        A_sayisi+=1
        faktor_turu="faktor-8"
    else:
        tip="B"
        B_sayisi+=1
        faktor_turu="faktor-9"
    faktor_miktari=float(input("kandaki faktör miktarini giriniz(0-50):"))
    while not 0<=faktor_miktari<50: faktor_miktari=float(input("kandaki faktör miktarini doğru giriniz(0-50):"))
    if faktor_miktari<1:
        siddet="ağir"
        agir_sayisi+=1
    elif 1<=faktor_miktari<5:
        siddet="orta"
        orta_sayisi+=1
    else:
        siddet="hafif"
        hafif_sayisi+=1
    antikor_miktari=float(input("kandaki antikor miktarini giriniz(0+):"))
    while antikor_miktari<0: antikor_miktari=float(input("kandaki antikor miktarini doğru giriniz(0+):"))
    if siddet=="orta":
        kanama_sayisi=int(input("son 1 yilda meydana gelen kanama sayisi giriniz(0+):"))
        while kanama_sayisi<0:kanama_sayisi=int(input("son 1 yilda meydana gelen kanama sayisini dogru giriniz(0+):"))
    if antikor_miktari<=5:
        if siddet=="ağir": profilaksi=1 #PROFİLAKSİ TEDAVİSİ UYGULANIP UYGULANMAYACAĞININ BELİRLENMESİ
        elif siddet=="orta" and kanama_sayisi>0:
            if kanama_sayisi/12>3:profilaksi=1 #PROFİLAKSİ TEDAVİSİ UYGULANIP UYGULANMAYACAĞININ BELİRLENMESİ
    else:
        if tip=="A":A_inhibitor+=1
        else:B_inhibitor+=1
    if profilaksi==1:
        toplam_profilaksi+=1
        kg=float(input("kilonuzu giriniz(0+):"))
        while kg<0:kg=float(input("kilonuzu doğru giriniz(0+):"))
        faktör_ilac_türü=input("kullanacağiniz faktör ilaci türünü giriniz(P/p/R/r):")
        while faktör_ilac_türü!="P" and faktör_ilac_türü!="p" and faktör_ilac_türü!="R" and faktör_ilac_türü!="r":
            faktör_ilac_türü = input("kullanacağiniz faktör ilaci türünü doğru giriniz(P/p/R/r):")
        if faktör_ilac_türü=="P" or faktör_ilac_türü=="p":tür="plazma kaynakli"
        else: tür="Rekombinant"
    print("TC kimlik numarasi:",tc,"ad soyad:",ad_soyad)
    print("hastaliğin tipi:",tip,"şiddeti:", siddet)
    if profilaksi==1:print("profilaksi uygulanacaktir")
    else:print("profilaksi uygulanmayacaktir")
    if profilaksi==1:
        print("Kullanilacak faktor ilaci:",tür,faktor_turu)
        gerekli_fak=40-faktor_miktari #BİR SEFERDE KULLANILACAK MİNİMUM İLAC MİKTARININ HESAPLANMASI İÇİN
        if tip=="A":
            profilaksi_A+=1
            print("haftada 3 kez ilac kullanılacak")
            bir_sefer_min_ilac = gerekli_fak / 2 * kg
        else:
            profilaksi_B+=1
            print("haftada 2 kez ilac kullanılacak")
            bir_sefer_min_ilac=gerekli_fak*kg
        print("bir seferde kullanilmasi gereken minimum ilac miktari:",round(bir_sefer_min_ilac,2),"unite")
        binlik=int(bir_sefer_min_ilac//1000)
        kalan=int(bir_sefer_min_ilac%1000)
        if kalan>750:binlik+=1
        elif 500<kalan<=750: #FLAKON HESAPLANMASI
            besyuzluk=1
            ikiyuzellilik=1
        elif 250<kalan<=500:besyuzluk=1
        elif 0<kalan<=250:ikiyuzellilik=1
        bir_sefer_ilac=binlik*1000+besyuzluk*500+ikiyuzellilik*250
        print("bir seferde kullanilmasi gereken ilac miktari:",bir_sefer_ilac,"unite")
        print("flakon miktarlari:1000 unitelik:",binlik,"/500 unitelik:",besyuzluk,"/250 unitelik:",ikiyuzellilik)
        if tip=="A":
            dört_haftalik_ilac=12*bir_sefer_ilac #DÖRT HAFTALIK İLAÇ MİKTARININ HESAPLANMASI
            print("4 haftalik toplam ilac miktari:",dört_haftalik_ilac)
            print("flakon miktarlari:1000 unitelik:", binlik*12, "/500 unitelik:", besyuzluk*12, "/250 unitelik:", 12*ikiyuzellilik)
        else:
            dört_haftalik_ilac=8*bir_sefer_ilac #DÖRT HAFTALIK İLAÇ MİKTARININ HESAPLANMASI
            print("4 haftalik toplam ilac miktari", dört_haftalik_ilac)
            print("flakon miktarlari:1000 unitelik:", binlik * 8, "/500 unitelik", besyuzluk * 8, "/250 unitelik",8 * ikiyuzellilik)
        if faktör_ilac_türü=="P" or faktör_ilac_türü=="p":
            dört_haftalik_ilac_tutar=1.25*dört_haftalik_ilac #DÖRT HAFTALIK İLAÇ TUTARININ HESAPLANMASI
            if tip=="A": #DÖRT HAFTALIK TOPLAM PLAZMA KAYNAKLI FAKTOR-8 İLAC MİKTARİ HESAPLANMASI
                A_plazma+=1
                dört_hafta_plazma_8+=dört_haftalik_ilac
                plazma_8_binlik+=12*binlik
                plazma_8_besyuzluk+=12*besyuzluk
                plazma_8_ikiyuzellilik+=12*ikiyuzellilik
            else:#DÖRT HAFTALIK TOPLAM PLAZMA KAYNAKLI FAKTOR-9 İLAC MİKTARİ HESAPLANMASI
                B_plazma+=1
                dört_hafta_plazma_9+=dört_haftalik_ilac
                plazma_9_binlik+=8*binlik
                plazma_9_besyuzluk+=8*besyuzluk
                plazma_9_ikiyuzellilik+=8*ikiyuzellilik
        else:
            dört_haftalik_ilac_tutar=1.5*dört_haftalik_ilac
            if tip=="A":#DÖRT HAFTALIK TOPLAM REKOMBİNANT KAYNAKLI FAKTOR-8 İLAC MİKTARİ HESAPLANMASI
                A_rekombinant+=1
                dört_hafta_rekombinant_8+=dört_haftalik_ilac
                rekombinant_8_binlik+=12*binlik
                rekombinant_8_besyuzluk+=12*besyuzluk
                rekombinant_8_ikiyuzellilik+=12*ikiyuzellilik
            else:#DÖRT HAFTALIK TOPLAM REKOMBİNANT KAYNAKLI FAKTOR-9 İLAC MİKTARİ HESAPLANMASI
                B_rekombinant+=1
                dört_hafta_rekombinant_9+=dört_haftalik_ilac
                rekombinant_9_binlik+=8*binlik
                rekombinant_9_besyuzluk+=8*besyuzluk
                rekombinant_9_ikiyuzellilik+=8*ikiyuzellilik
        print("dort haftalik ilac tutari:",round(dört_haftalik_ilac_tutar,2),"TL")
        toplam_dort_haftalik_ilac_tutar+=dört_haftalik_ilac_tutar
        toplam_dort_haftalik_ilac_miktari+=dört_haftalik_ilac
        if siddet=="orta":orta_profilaksi+=1
        if tip=="A":
            if dört_haftalik_ilac>A_max_dort_haftalik_ilac_miktar:
                A_max_dort_haftalik_ilac_miktar=dört_haftalik_ilac
                A_max_tc=tc
                A_max_ad_soyad=ad_soyad
                A_max_siddet=siddet
                A_max_kg=kg
                A_max_tür=tür
                A_max_dort_hafta_ilac_tutar=dört_haftalik_ilac_tutar
        elif dört_haftalik_ilac>B_max_dort_haftalik_ilac_miktar:
            B_max_dort_haftalik_ilac_miktar = dört_haftalik_ilac
            B_max_tc = tc
            B_max_ad_soyad = ad_soyad
            B_max_siddet = siddet
            B_max_kg = kg
            B_max_tür = tür
            B_max_dort_hafta_ilac_tutar = dört_haftalik_ilac_tutar
        if dört_haftalik_ilac_tutar>C_max_dort_hafta_ilac_tutar:
            C_max_dort_hafta_ilac_tutar = dört_haftalik_ilac_tutar
            C_max_tc = tc
            C_max_ad_soyad = ad_soyad
            C_max_siddet = siddet
            C_max_kg = kg
            C_max_tür = tür
            C_max_dort_hafta_ilac_miktar = dört_haftalik_ilac
    print("------------------------------------------------------------------------------------------------------------")
    baska_hasta=input("baska hasta girisi yapilacak mi?(E/e/H/h)")
    while baska_hasta!="E" and baska_hasta!="e" and baska_hasta!="H" and baska_hasta!="h":
        baska_hasta = input("baska hasta girisi yapilacak mi?(E/e/H/h)")
    if baska_hasta=="H" or baska_hasta=="h":
        toplam_yillik_ilac_tutar=toplam_dort_haftalik_ilac_tutar*13 #SGK NİN KARŞILADIGI TOPLAM 1 YILLIK İLAC TUTARI HESAPLANMASI
        toplam_yillik_ilac_miktari=toplam_dort_haftalik_ilac_miktari*13 #YLLIK TOPLAM İLAC MİKTARI HESAPLANMASI
        ortalama_yillik_ilac_miktari=toplam_yillik_ilac_miktari/toplam_profilaksi #ORTALAMA YLLIK İLAC MİKARI HESAPLANMASI
        ortalama_yillik_ilac_tutari=toplam_yillik_ilac_tutar/toplam_profilaksi #ORTALAMA YLLIK İLAC TUTARI HESAPLANMASI
        print("Hemofili-A hastalari sayisi:",A_sayisi)
        print("Hemofili-B hastalari sayisi:",B_sayisi)
        print("toplam hasta sayisi:",toplam_hasta)
        print("hastaliginin siddeti agir olan hastalarin sayisi:",agir_sayisi,"yuzdesi:",round(agir_sayisi/toplam_hasta*100,2))
        print("hastaliginin siddeti orta olan hastalarin sayisi:",orta_sayisi,"yuzdesi:",round(orta_sayisi/toplam_hasta*100,2))
        print("hastaliginin siddeti hafif olan hastalarin sayisi:",hafif_sayisi,"yuzdesi:",round(hafif_sayisi/toplam_hasta*100,2))
        print("Hemofili-A hastalarinin inhibitor varligi yuzdesi:",round(A_inhibitor/toplam_hasta*100,2))
        print("Hemofili-B hastalarinin inhibitor varligi yuzdesi:",round(B_inhibitor/toplam_hasta*100,2))
        print("Profilaksi uygulanan Hemofili-A hastalarinin sayisi:",profilaksi_A,"yuzdesi:",round(profilaksi_A/toplam_hasta*100,2))
        print("Profilaksi uygulanan Hemofili-B hastalarinin sayisi:",profilaksi_B,"yuzdesi:",round(profilaksi_B/ toplam_hasta*100,2))
        if orta_sayisi>0:print("Hastaligininn siddeti orta olan hemofili hastalari icinde, profilaksi uygulanan hastalarin yuzdesi:",round(orta_profilaksi/orta_sayisi*100,2))
        print("Hemofili-A plazma kaynakli ilac kullananlarin yuzdesi:",round(A_plazma/toplam_profilaksi*100,2),"Rekombinant ilac kullananlarin yuzdesi",round(A_rekombinant/toplam_profilaksi*100,2))
        print("Hemofili-B plazma kaynakli ilac kullananlarin yuzdesi:",round(B_plazma / toplam_profilaksi * 100,2), "Rekombinant ilac kullanlarin yuzdesi",round(B_rekombinant/toplam_profilaksi*100,2))
        print("dört haftalik toplam plazma kaynakli faktor-8 ilac miktari:",dört_hafta_plazma_8,"unite")
        print("flakon miktarlari:1000 unitelik:",plazma_8_binlik,"/500 unitelik:",plazma_8_besyuzluk,"/250 unitelik:",plazma_8_ikiyuzellilik)
        print("dört haftalik toplam rekombinant faktor-8 ilac miktari:", dört_hafta_rekombinant_8, "unite")
        print("flakon miktarlari:1000 unitelik:", rekombinant_8_binlik, "/500 unitelik:", rekombinant_8_besyuzluk, "/250 unitelik:",rekombinant_8_ikiyuzellilik)
        print("dört haftalik toplam plazma kaynakli faktor-8 ilac miktari:", dört_hafta_plazma_9, "unite")
        print("flakon miktarlari:1000 unitelik:", plazma_9_binlik, "/500 unitelik:", plazma_9_besyuzluk, "/250 unitelik:",plazma_9_ikiyuzellilik)
        print("dört haftalik toplam rekombinant faktor-9 ilac miktari:", dört_hafta_rekombinant_9, "unite")
        print("flakon miktarlari:1000 unitelik:", rekombinant_9_binlik, "/500 unitelik:", rekombinant_9_besyuzluk,"/250 unitelik:", rekombinant_9_ikiyuzellilik)
        print("SGK'nin karsiladigi 4 haftalik ilac tutari:",round(toplam_dort_haftalik_ilac_tutar,2),"TL")
        print("SGK'nin karsiladigi 1 yillik ilac tutari:",round(toplam_yillik_ilac_tutar,2),"TL")
        print("Ortalama 1 hasta icin yillik ilac miktari:",ortalama_yillik_ilac_miktari,"ünite.Tutari:",round(ortalama_yillik_ilac_tutari,2),"TL")
        if profilaksi_A>0:
            print("\n4 haftalik ilac kullanim miktari en cok olan Hemofili-A hastasinin bilgileri:\n"
                 "TC kimlik no:", A_max_tc,
                 "\nAd soyad:", A_max_ad_soyad,
                 "\nhastalik siddeti:", A_max_siddet,
                 "\nkilosu:", A_max_kg,
                 "\nkullandigi ilac turu:", A_max_tür,
                 "\n4 haftalik toplam ilac kullanim miktari:", A_max_dort_haftalik_ilac_miktar, "unite"
                 "\n4 haftalik ilac kullanim tutari:",round(A_max_dort_hafta_ilac_tutar, 2), "TL")
        if profilaksi_B>0:
            print("\n4 haftalik ilac kullanim miktari en cok olan Hemofili-B hastasinin bilgileri:"
                  "\nTC kimlik no:", B_max_tc,
                  "\nAd soyad:", B_max_ad_soyad,
                  "\nhastalik siddeti:", B_max_siddet,
                  "\nkilosu:", B_max_kg,
                  "\nkullandigi ilac turu:", B_max_tür,
                  "\n4 haftalik toplam ilac kullanim miktari:", B_max_dort_haftalik_ilac_miktar, "unite"
                  "\n4 haftalik ilac kullanim tutari:",round(B_max_dort_hafta_ilac_tutar, 2), "TL")
        print("\n4 haftalik ilac tutari en cok olan hastanin bilgileri:"
              "\nTC kimlik no:", C_max_tc,
              "\nAd soyad:", C_max_ad_soyad,
              "\nhastalik siddeti:", C_max_siddet,
              "\nkilosu:", C_max_kg,
              "\nkullandigi ilac turu:", C_max_tür,
              "\n4 haftalik toplam ilac kullanim miktari:", C_max_dort_hafta_ilac_miktar,"unite"
              "\n4 haftalik ilac kullanim tutari:", round(C_max_dort_hafta_ilac_tutar,2),"TL")
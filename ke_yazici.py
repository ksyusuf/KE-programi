
def ke_yazici(dosya_adi):
    dosyanin_yeni_hali = ""
    dosyanin_yeni_adi = ""
    dosya_adi_txt = dosya_adi + ".txt"
    with open(dosya_adi_txt, "r", encoding="utf-8") as dosya:
        for paragraf in dosya:
            kelime_listesi = paragraf.split()
            for kelime in kelime_listesi:
                dosyanin_yeni_hali += kelime + " ke "
            dosyanin_yeni_hali += "\n"

    print(dosyanin_yeni_hali)
    dosyanin_yeni_adi += dosya_adi + " (ke).txt"
    with open(dosyanin_yeni_adi, "w", encoding="utf-8") as yeni_dosya:
        yeni_dosya.write(dosyanin_yeni_hali)


if __name__ == '__main__':
    ke_yazici("lorem nedir")

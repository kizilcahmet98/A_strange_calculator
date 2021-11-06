import math as mat

def dort_islem_sec(islem, hafiza, sayi):
    if islem == "+":
        hafiza += sayi
    elif islem == "-":
        hafiza -= sayi
    elif islem == "*":
        hafiza *= sayi
    elif islem == "/":
        hafiza /= sayi
    return hafiza

def esittir(hafiza):
    if islem == "=":
        print("Sonuç: ", hafiza)
        breakpoint()

def helper(islem, hafiza, sayi):
    sayi = int(input("Sayı girin: "))
    esittir(hafiza)
    return sayi

def islem_iste_sonuc(hafiza):
    islem = input("İşlem girin: ")
    if islem == "=":
        print("Sonuç: ", hafiza)
        breakpoint()
    else:
        return islem

def esit_degilse(islem, hafiza, sayi):
    sayi = helper(islem, hafiza, sayi)
    hafiza = dort_islem_sec(islem, hafiza, sayi)
    return sayi, hafiza

print("""
************************
İşlemler:
1 - Toplama    = +
2 - Çıkarma    = -
3 - Çarpma     = *
4 - Bölme      = /
5 - Faktöriyel = !
6 - e üzeri    = exp
7 - Ln         = ln
8 - Karekök    = kk
************************
""")

i = -1
hafiza = 0
sayi = float(input("Sayı girin: "))
hafiza += sayi
islem_liste = []
while True:
    islem = input("İşlem girin: ")
    islem_liste.append(islem)
    i += 1
    if islem == "+" or islem == "-" or islem == "*" or islem == "/":
        sayi = int(input("Sayı girin: "))
    hafiza = dort_islem_sec(islem, hafiza, sayi)
    if islem == "!":
        if islem_liste[i - 1] == "+":
            hafiza -= sayi
            hafiza += mat.factorial(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "-":
            hafiza += sayi
            hafiza -= mat.factorial(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "*":
            hafiza /= sayi
            hafiza *= mat.factorial(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "/":
            hafiza *= sayi
            hafiza /= mat.factorial(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        else:
            hafiza = mat.factorial(sayi)
            continue
    elif islem == "exp":
        if islem_liste[i - 1] == "+":
            hafiza -= sayi
            hafiza += mat.exp(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi = helper(islem, hafiza, sayi)
                hafiza = dort_islem_sec(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "-":
            hafiza += sayi
            hafiza -= mat.exp(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "*":
            hafiza /= sayi
            hafiza *= mat.exp(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "/":
            hafiza *= sayi
            hafiza /= mat.exp(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        else:
            hafiza = mat.exp(sayi)
            continue
    elif islem == "ln":
        if islem_liste[i - 1] == "+":
            hafiza -= sayi
            hafiza += mat.log1p(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "-":
            hafiza += sayi
            hafiza -= mat.log1p(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "*":
            hafiza /= sayi
            hafiza *= mat.log1p(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "/":
            hafiza *= sayi
            hafiza /= mat.log1p(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        else:
            hafiza = mat.log1p(sayi)
            continue
    elif islem == "kk":
        if islem_liste[i - 1] == "+":
            hafiza -= sayi
            hafiza += mat.sqrt(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "-":
            hafiza += sayi
            hafiza -= mat.sqrt(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "*":
            hafiza /= sayi
            hafiza *= mat.sqrt(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        elif islem_liste[i - 1] == "/":
            hafiza *= sayi
            hafiza /= mat.sqrt(sayi)
            islem = islem_iste_sonuc(hafiza)
            if islem != "=":
                sayi, hafiza = esit_degilse(islem, hafiza, sayi)
                continue
        else:
            hafiza = mat.sqrt(sayi)
            continue
    if islem == "=":
        print("Sonuç: ", hafiza)
        break

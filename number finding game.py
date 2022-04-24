import random as r
print("Assalomu alykum. Son topish o'yniga hush kelibsiz"
      "\nKeling o'yinni boshlaymiz")
print("\nAvval o'yin uchun yuqori raqam chegarasini kiriting:")
quyi = 1
yuqori = int(input("Yuqori chegara: "))
input("\nAgar o'yinga tayyor bo'lsangiz Enter tugmasini bosing.")
while True:
    print(f"\n1 dan {yuqori} gacha son o'yladim. Topa olasizmi?:")
    x = r.randint(quyi,yuqori)
    n = 0
    while True:
        n+=1
        input_son = int(input(">> "))
        if input_son>x:
            print("Topa olmadingiz men o'ylagan son bundan kichikroq. Yana harakat qilib ko'ring:")
        elif input_son<x:
            print("Topa olmadingiz men o'ylagan son bundan kattaroq. Yana harakat qilib ko'ring:")
        else:
            break
    print(f"Tabriklayman siz topdingiz, men {x} sonini o'yalgan edim va siz {n} urunishda topdingiz")

    print(f"\nEndi siz 1 dan {yuqori} gacha son o'ylaysiz men topishga harakat qilaman")
    input("\nTayyor bo'lsangiz Enter tugmasini bosing:")
    m = 0
    while True:
        m+=1
        y = r.randint(quyi,yuqori)
        answer = input(f"Siz {y} sonini o'yladingiz: To'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq(-)?: ")
        if answer == "+":
            quyi = y+1
        elif answer == "-":
            yuqori = y-1
        elif answer.lower() == 't':
            break
        else:
            print("Iltimos faqat so'ralgan belgilarni kiriting!")

    print(f"Siz o'ylagan raqamni topdim, siz {y} sonini o'ylagan edingiz:")
    if m>n:
        print(f"\nMen {m} urunishda topdim, siz esa {n} urunishda topdingiz va g'olib bo'ldingiz")
        print("Sizni tabriklayman.")
    elif m==n:
        print(f"\nDurrang. Ikkimizham {n} urunishda topdik.")
    else:
        print(f"\nSiz {n} urunishda topdingiz, men esa {m} urunishda topdim va bu o'yinda men g'olib bo'ldim")
        print("Hafa bo'lmang sizham yomon o'ynamadingiz.")

    while True:
        final_answer = input("\nAgar hohlasangiz o'yinni yana davom etirshimiz mumkin. yes/no: ")
        if final_answer == "yes":
            print("\nUnda o'yinni yana boshladik.")
            break
        elif final_answer == "no":
            print("\nAfusus o'yin qiziq davom etayotgan edi.")
            break
        else:
            print("\nIltimos faqat yes yoki no ni kiriting!")

    if final_answer == 'no':
        break
print("O'yin juda maroqli bo'ldi buning uchun sizga rahmat.")


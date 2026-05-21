copy() - listni nusxasini yaratadi va qaytaradi.

mevalar = ["olma", "banan"]

nusxa = mevalar.copy()

print(nusxa)  # Natija: ['olma', 'banan']

append() - listga yangi element qo'shadi.

sonlar = [1, 2, 3]

sonlar.append(4)

print(sonlar)  # Natija: [1, 2, 3, 4]

extend() - listni berilgan list bilan kengaytiradi.

a = [1, 2]

b = [3, 4]

a.extend(b)

print(a)  # Natija: [1, 2, 3, 4]

pop() - so'ng index dagi elementni o'chiradi va qaytaradi.

ranglar = ["qizil", "yashil", "ko'k"]

element = ranglar.pop(1)

print(element)  # Natija: yashil

print(ranglar)  # Natija: ['qizil', 'ko'k']

index() - berilgan qiymatni indexni qaytaradi.

harflar = ['a', 'b', 'c', 'b']

idx = harflar.index('b')

print(idx)  # Natija: 1

count() - berilgan qiymat listda necha marotaba takrorlangan ligini qaytaradi.

sonlar = [1, 2, 2, 3, 2]

print(sonlar.count(2))  # Natija: 3

insert() - qiymatni berilgan indexga qo'shadi.

xatlar = ['a', 'c']

xatlar.insert(1, 'b')

print(xatlar)  # Natija: ['a', 'b', 'c']

remove() - berilgan qiymatni o'chiradi.

mevalar = ["olma", "nok", "olma"]

mevalar.remove("olma")

print(mevalar)  # Natija: ['nok', 'olma']

sort() - listni tartiblaydi.

raqamlar = [3, 1, 4, 2]

raqamlar.sort()

print(raqamlar)  # Natija: [1, 2, 3, 4]

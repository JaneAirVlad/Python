a = input('Добро пожаловать в шифратор Цезаря! Введите фразу, которую необходимо зашифровать: \n').split()
print('Шифрую...')
b = []                                      # Cписок фразы с раздельными знаками препинания
c = []                                      # Зашифрованный список с раздельными знаками препинания
def splitting():                            # Функция отделения знаков препинания от слов
    for i in a:
        if i[0] == '"':
            k = i[0]
            i = i[1:-1]
            b.append(k)
            b.append(i)
            b.append(k)
        elif i.isalpha() == True:
            b.append(i)
        elif i.isalpha() == False:
            k = i[-1]
            i = i[:-1]
            b.append(i)
            b.append(k)
def caesars():                              # Функция шифрования
    for j in b:
        if j.isalpha() == True:
            r = ''
            for k in j:
                g = ord(k)
                if g > 64 and g < 91:
                    g = ord(k) + len(j)
                    if g > 90:
                        g -=26
                elif g > 96 and g <= 121:
                    g = ord(k) + len(j)
                    if g > 122:
                        g -=26
                r += chr(g)
            c.append(r)
        else:
            c.append(j)
splitting()
caesars()
s = ''                                      # Cоздания списка для шифрования
for l in c:                                 # Добавление знаков
    s += ' '   
    if l == ',' or l == '.' or l == '!':
        s = s[:-1]
        s += l
        continue
    s += l
s = s.strip()
m = s.find('"')
n = s.rfind('"')
if m > 0 and n > 0:
    s1 = s[:m + 1]
    s2 = s[n:]
    s3 = s[m + 2 : n - 1]
    s = s1 + s3 + s2
    print('Зашифрованная фраза:\n', s, sep = '')
else:
    print('Зашифрованная фраза:\n', s, sep = '')
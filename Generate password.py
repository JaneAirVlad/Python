import random

digits = '0123456789'                               # ����������� ��������� ��������
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
                                          
def data_collection():                              # ������� ����� ������� ��������� ������
    global quantity, lenght, symbol, chars
    chars = ''                        
    quantity = int(input('���������� ������� ��� ���������? (����� �����)\n'))
    lenght = int(input('����� ������ ������? (����� �����)\n'))
    if quantity == 0 or lenght== 0:
        print('�������� ���������� ������� ��� �� �����!')
        restart()
    c = input('�������� �� �����? (�� = ��������, ��� = �� ��������)\n')
    if c.lower() == '��':
        chars += digits
    d = input('�������� �� ��������� �����? (�� = ��������, ��� = �� ��������)\n')
    if d.lower() == '��':
        chars += lowercase_letters   
    e = input('�������� �� �������� �����? (�� = ��������, ��� = �� ��������)\n')
    if e.lower() == '��':
        chars += uppercase_letters    
    f = input('�������� �� ������� !#$%&*+-=?@^_? (�� = ��������, ��� = �� ��������)\n')
    if f.lower() == '��':
        chars += punctuation 
    symbol = input('��������� �� ������������� ������� il1Lo0O? (�� = ���������, ��� = �� ���������)\n')
    if chars == '':
        print('�� ����������� ������������ ������ ��� ������. ���������� ��� ���!')
        restart()

def generate_password(lenght, quantity, chars):         # ������� ��������� ������
    password = ''
    for i in range(quantity):
        num = lenght
        while num > 0:
            password += random.choice(chars)
            num -= 1
        if symbol.lower() == '��':                      # �������� �� ������������� �������
            for c in 'il1Lo0O':
                chars = chars.replace(c, '')
        print(password)
        num = lenght
        password = ''

def restart():                                          # ������� ������� ���� � �������
    again = '��'
    while again.lower() == '��':
        data_collection()
        generate_password(lenght, quantity, chars)    
        again = input('��� ��� ����� ������ ? (�� = ��������� ��� ���, ����� ������� = ����� �� ���������) \n' )
        
print('����� ���������� � ��������� �������. �������� �� ��������� �������� ��� �������� ������.')
restart()
print('������ ���� ��� ������! ����������.')
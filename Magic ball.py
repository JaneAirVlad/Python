import random
think = ['������ � ������� �������...', '��������� � ������ ����...', '�����...', '�������� �����...', '������� ����� ����...', '���������� ����� � ��������...']
answer = ['���������', '����������', '������� ��������', '���������� ��', '������ ���� ������ � ����', '���� �� �����', '��� ����� - ���', '�� ���� ������ - ���', '����������� �� ����� �������', '������ �����������', '���� ������', '������ �����', '����� �� ������������', '������ ������ �����������', '��������������� � ������ �����', '��� ������� - ��', '��������� �����', '������� �����������', '����� ������� - ��', '��']
print('������ ���, � ���������� ���, � � ���� ����� �� ����� ���� ������.')
a = input('����� �����������. ��� ���� �����? \n')
again = '��'
while again.lower() == '��':
    print(f'������ {a}, ����� ��� ������, �� ������� �� ������ �������� �����?')
    b = input()
    print(random.choice(think))
    print('����� �� ���� ������:', random.choice(answer))
    again = input('� ���� ��� �������� �� ��� �������? (�� = ������ ��� ������, ����� ������� = ��������� ������) \n' )
print('����������� ���� ��������� �������!')
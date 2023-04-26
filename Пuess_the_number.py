import random

print('Добро пожаловать в числовую угадайку') 
right_border = int(input('Выберите правую границу выбора чисел: \n',))
num = random.randint(0, right_border)

def is_valid(num_user):             # функция защиты от дурачка
    if num_user.isdigit() == False:
        return False
    elif int(num_user) < 0 or int(num_user) >= right_border:
        return False
    else:
        return True
a = 0               # запуск счетчика количества попыток
again = 'да'        # запуск цикла на повторение игры

while again.lower() == 'да':
    while True:
        num_user = input('Введите число:')
        if is_valid(num_user) == False: 
            print(f'А может быть все-таки введем целое число от 1 до {right_border}?')
        else: 
            num_user = int(num_user)
            if num_user > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                a += 1
            elif num_user < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                a += 1
            else:
                print('Вы угадали, поздравляем!')
                print('Число попыток:', a)
                again = input('Хотите сыграть еще раз? (Да = еще раз, Нет = выход из игры) \n')
                if again.lower() == 'нет':
                    break
                elif again.lower() == 'да':
                    a = 0
                    right_border = int(input('Выберите правую границу выбора чисел: \n',))
                    num = random.randint(0, right_border)
                else:
                    break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

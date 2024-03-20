# Доработать декоратор logger в коде ниже. Должен получиться декоратор,
# который записывает в файл 'main.log' дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. 
# Функция test_1 в коде ниже также должна отработать без ошибок.
# date_now, time_now, name_function, args,kwargs, return 
import datetime
import os

def logger(old_function):
            
    def new_function(*args, **kwargs):
        
        # print(f'''
        # Сейчас будет вызвана {old_function.__name__}
        # с аргументами {args} и {kwargs}''')
        result = old_function(*args, **kwargs)
        # print(f'Результат: {result}')
        dt_now = datetime.datetime.now()
        with open('main.log','a') as f:
            str_result = f"{dt_now} {old_function.__name__} {args} {kwargs} {result}\n"
            f.write(str_result)
        return result

    return new_function

# @logger
# def hello_world():
#     return 'Hello World'

# @logger
# def summator(a, b=0):
#     return a + b


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()
    # hello_world()
    # summator(2,b=3)

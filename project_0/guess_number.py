import numpy as np

def guess_random_number(number:int=1) -> int:
    
    """Рандомно угадываем число
    
    Args:
        number(int, optional) загаданное число Defaults to 1
        
    Return:
        количество попыток (int)
    """
    
    round_number = lambda i : 1 if i == 0.5 else round(i) #округляет 0.5 до единицы
    
    count = 0 #Счетчик попыток
    predict_number = 50 #предполагаемое число
    prev_predict_number = 0 #предполагаемое число в предыдущей итерации

    while True:
    
        count += 1
                      
        if predict_number > number:
            
            predict_number = prev_predict_number + round_number((predict_number - prev_predict_number)/2)
            
        elif predict_number < number:
            
            prev_predict_number = predict_number
            predict_number = predict_number + round_number((100 - predict_number)/2)
            
        else:
            break
        
    return count
    
def average_attempts(guess_random_number) -> int:
    
    """Вычисляет среднее количество попыток угадать число  на 1000 испытаний
    
    Arg:
        guess_random_predict - функция угадывания
    
    Return:
        среднее число попыток (int)"""
        
    r_num = np.random.randint(1, 100, size=1000) #Создаем список 1000 случайных чисел

    count = [] #список для сохранения кол-ва попыток
    
    for num in r_num:
        count.append(guess_random_number(num))
    
    return int(np.mean(count))

"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def game_core(number) -> int:
    # компьютер загадывает число
    pr_min = 1
    pr_max = 101
    # количество попыток
    count = 1
    predict_number = np.random.randint(1, 101)  # компьютер предсказывает число

    while number != predict_number:
        if (pr_max - pr_min) < 2:
            break 
        count += 1

        if predict_number > number:  # если предсказанное число больше, чем загаданное
            pr_max = predict_number
            predict_number = round((pr_min + pr_max) / 2)
        
        else:
            # если предсказанное число меньше загаданного
            pr_min = predict_number
            predict_number = round((pr_min + pr_max) / 2)
    return count

def score_game(game_core) -> int:

    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел
    for number in random_array:
        count_ls.append(game_core(number))
        score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за: {score} попыток")
score_game(game_core)
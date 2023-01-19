def print_statistics(answers):
    total_tasks = 5
    answered_correctly = 0
    answered_incorrectly = 0
    for answer in answers:
        if answer == True:
            answered_correctly += 1
        else:
            answered_incorrectly += 1

    print(f'Всего задачек: {total_tasks}\nОтвечено верно: {answered_correctly} \nОтвечено неверно: {answered_incorrectly}')
1

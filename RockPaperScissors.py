import random

count_rounds = 0
count_wins = 0
count_draws = 0
count_losses = 0
line = "----------------------------------------"

while True:
    rules_dict = {1: "Камень", 2: "Ножницы", 3: "Бумага"}
    count_rounds += 1
    print(line)
    print("Раунд {}:".format(count_rounds))
    print(line)
    print("Введи:\n1 - \"Камень\"\n2 - \"Ножницы\"\n3 - \"Бумага\"\nq - выход из программы")
    x = input("Ты вводишь: ")
    while x not in ('1', '2', '3', 'q', 'Q'):
       x = input("Неверный ввод! Введи 1, 2, 3 или q: ")
    if x in ('q', 'Q'):
        quit()
    x = int(x)
    r = random.randint(1, 3)
    print("У тебя: \"{}\"\nУ компьютера: \"{}\"".format(rules_dict[x], rules_dict[r]))
    if x == 1 and r == 1 or x == 2 and r == 2 or x== 3 and r == 3:
        print("Ничья!")
        count_draws += 1
    elif x == 1 and r == 2 or x == 2 and r == 3 or x == 3 and r == 1:
        print("Победа!")
        count_wins += 1
    else:
        print("Проигрыш!")
        count_losses += 1
    print("Выигрышей: {}, вничью: {}, проигрышей: {}".format(count_wins, count_draws, count_losses))

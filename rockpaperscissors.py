import random

def get_user_choice():
    choice = input("Выберите (камень, ножницы, бумага): ").lower()
    while choice not in ["камень", "ножницы", "бумага"]:
        choice = input("Неверный выбор. Попробуйте снова: ").lower()
    return choice

def get_bot_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def determine_winner(user, bot):
    if user == bot:
        return "Ничья"
    elif (user == "камень" and bot == "ножницы") or \
         (user == "ножницы" and bot == "бумага") or \
         (user == "бумага" and bot == "камень"):
        return "Игрок"
    else:
        return "Бот"

def play_game():
    user_score = 0
    bot_score = 0

    while True:
        user_choice = get_user_choice()
        bot_choice = get_bot_choice()
        print(f"Бот выбрал: {bot_choice}")
        winner = determine_winner(user_choice, bot_choice)

        if winner == "Игрок":
            user_score += 1
            print("Вы выиграли этот раунд!")
        elif winner == "Бот":
            bot_score += 1
            print("Бот выиграл этот раунд!")
        else:
            print("Ничья!")

        print(f"Счёт: Игрок {user_score} - {bot_score} Бот")

        again = input("Сыграть ещё раз? (да/нет): ").lower()
        if again != "да":
            break

play_game()
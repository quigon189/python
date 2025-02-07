from random import choice

K = "Камень"
N = "Ножницы"
B = "Бумага"

knb_list = [K, N, B]

def return_knb():
    return knb_list

def kanobu(player):

    computer = choice(return_knb())

    computer_choice = f"Компьютер выбрал {computer}"

    if computer == player:
        return computer_choice, "Ничья"
    elif player == N:
        if computer == B:
            return computer_choice, "Игрок победил"
        elif computer == K:
            return computer_choice, "Компьютер победил"
    elif player == K:
        if computer == N:
            return computer_choice, "Игрок победил"
        elif computer == B:
            return computer_choice, "Компьютер победил"
    elif player == N:
        if computer == B:
            return computer_choice, "Игрок победил"
        elif computer == K:
            return computer_choice, "Компьютер победил"
        
    return computer_choice, "Не верные значения"
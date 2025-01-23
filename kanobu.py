K = "Камень"
N = "Ножницы"
B = "Бумага"

knb_list = [K, N, B]

def kanobu(player, computer):

    if computer == player:
        return "Ничья"
    elif player == N:
        if computer == B:
            return "Игрок победил"
        elif computer == K:
            return "Компьютер победил"
    elif player == K:
        if computer == N:
            return "Игрок победил"
        elif computer == B:
            return "Компьютер победил"
    elif player == N:
        if computer == B:
            return "Игрок победил"
        elif computer == "Камемь":
            return "Компьютер победил"
        
    return "Не верные значения"
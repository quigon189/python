def kanobu(player, computer):
    k = "Камень"
    n = "Ножницы"
    b = "Бумага"

    if computer == player:
        return "Ничья"
    elif player == n:
        if computer == b:
            return "Игрок победил"
        elif computer == k:
            return "Компьютер победил"
    elif player == k:
        if computer == n:
            return "Игрок победил"
        elif computer == b:
            return "Компьютер победил"
    elif player == n:
        if computer == b:
            return "Игрок победил"
        elif computer == "Камемь":
            return "Компьютер победил"
        
    return "Не верные значения"
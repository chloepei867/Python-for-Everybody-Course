def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    dice1_wins=0
    dice2_wins=0

    for value1 in dice1:
        for value2 in dice2:
            if value1>value2:
                dice1_wins=dice1_wins+1
            elif value1<value2:
                dice2_wins=dice2_wins+1
            else:
                continue
    return(dice1_wins,dice2_wins)

dice1 =  [1, 1, 6, 6, 8, 8]
dice2 =  [2, 2, 4, 4, 9, 9]
x= count_wins(dice1,dice2)

print(x)

dice1 =  [1, 2, 3, 4, 5, 6]
dice2 =  [1, 2, 3, 4, 5, 6]
y = count_wins(dice1,dice2)

print(y)

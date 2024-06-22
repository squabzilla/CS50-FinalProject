# sum = []
# a = 3
# b = 4
# c = 1
# d = 2
# sum.append(a)
# sum.append(b)
# sum.append(c)
# sum.append(d)

# sum.sort(reverse=True)

# print(sum)

# 4d6 best 3
sum = 0
manual_sum = 0
count = 0
result_list = [0,1,2,3]
for dice_one in range(6):
    first_die_roll = dice_one + 1
    for dice_two in range(6):
        second_die_roll = dice_two + 1
        for dice_three in range(6):
            third_dice_roll = dice_three + 1
            for dice_four in range(6):
                fourth_dice_roll = dice_four + 1
                result_list[0] = first_die_roll
                result_list[1] = second_die_roll
                result_list[2] = third_dice_roll
                result_list[3] = fourth_dice_roll
                result_list.sort()
                sum_of_dice = result_list[1] + result_list[2] + result_list[3]
                sum += sum_of_dice
                count += 1
average = sum / count
print(f"Average value is: {average}")
print(f"Average value multiplied by six attributes: {average * 6}")
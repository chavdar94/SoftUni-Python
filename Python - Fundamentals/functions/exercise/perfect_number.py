def perfect_number(num):
    sum_num = 0
    for i in range(1,num):
        if num % i == 0:
            sum_num += i
    if sum_num == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)
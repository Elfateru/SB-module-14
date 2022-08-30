def user_ip(nums):
    if len(nums) == 4:
        for num in nums:
            if not num.isdigit():
                print(f'{num} - это не целое число')
                return False
            if int(num) > 255:
                print(f'{num} превышает 255.')
                return False
            elif int(num) < 0:
                print(f'{num} меньше 0.')
                return False
    else:
        print('Адрес — это четыре числа, разделённые точками.')
        return False
    return True


input_ip = input('Введите IP:').split('.')
ip_status = user_ip(input_ip)
if ip_status:
    print('IP-адрес корректен')

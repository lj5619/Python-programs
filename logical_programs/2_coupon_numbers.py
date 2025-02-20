import random

class Coupon:

    def random_number(num):
        random_generation=random.randint(0,num)
        return random_generation
    
    def coupons_collected(num):
        distinct_coupons = set()
        count = 0
        while len(distinct_coupons) != num:
            new_num = Coupon.random_number(num)
            distinct_coupons.add(new_num)
            count += 1
        return count

num=int(input('Enter the number of distinct coupon numbers: '))
total = Coupon.coupons_collected(num)
print(f'The total random numbers needed to have all distinct numbers are {total}')
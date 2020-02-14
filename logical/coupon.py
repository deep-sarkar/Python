from logical import *
class CouponGenerator:
    number_of_coupon = int(input('How many coupons you want : '))
    count = 0
    cp = LogicalMethods()

#Passing argument 
    all_couopn = cp.check_duplicate(number_of_coupon)
    print(all_couopn)
    
# 原始的錯誤寫法
# def sum(items):
#     for i in account_product_money.items():
#         i.split()
#         for j in account_how_many_products.items():
#             j.split()
#             products_account = 0
#             products_account += i[1] * j[1]
#             all_the_pay[i] = products_account

#我能在shoppiny_tips裡創建一個all裡面直接是all=(account_product_moneys, account_how_many_productss)然後把def sum(alls)這樣是可以的嗎？
#calculate_total_cost如用sum作為代替會有問題嗎？
def calculate_total_cost(account_product_moneys, account_how_many_products):
    all_the_pay = 0 #如果想歸零就放回圈外 想累加就放回圈內
    for name , price in account_product_moneys.items():
        if name in account_how_many_products:
            real_price = price[:-1]   #等於int(price.split('元')[0])
            quantity = account_how_many_products[name]
            total_price = int(real_price) * int(quantity)
            #經查證return type(real_price) , type(quantity) real_price是str所以要改成int
            all_the_pay += total_price
    #忘記return
    return all_the_pay

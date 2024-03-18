import all_pay

products = {"牛奶":"25元" , "餅乾":"20元" , "蘋果":"30元" , "汽水":"30元" , "糖果":"20元"}
account_product_money = {}
account_how_many_products = {}

while True:
    buying = (f"商品有:{products}\n") #ok 沒有\n
    i_want = str(input(buying))
    if i_want == "end":
        # 錯誤打法all_pay.sum(package_product_money_account)
        total_pay = all_pay.calculate_total_cost(account_product_money, account_how_many_products)
        print (account_product_money,account_how_many_products,total_pay)
        break

    elif i_want in products:
        account_product_money[i_want] = products.get(i_want)
        if i_want in account_how_many_products:
            account_how_many_products[i_want] += 1        
        else:
            account_how_many_products[i_want] = 1
    else:
        #ok 為什麼這裡不能用return要用print 
        print("商品不存在，请重新输入。")

# #如果我要一次牛奶兩瓶 餅乾10個怎麼辦
# import all_pay

# products = {"牛奶": "25元", "餅乾": "20元", "蘋果": "30元", "汽水": "30元", "糖果": "20元"}
# account_product_money = {}
# account_how_many_products = {}

# while True:
#     buying = f"商品有:{products}\n"
#     input_string = str(input(buying))

#     if input_string.lower() == "end":
#         total_pay = all_pay.calculate_total_cost(account_product_money, account_how_many_products)
#         print(account_product_money, account_how_many_products, total_pay)
#         break

#     # 分割輸入字符串，例如 "牛奶 2 餅乾 10"
#     input_list = input_string.split()

#     # 迭代分割後的列表，每隔兩個元素為一對商品和數量
#     for i in range(0, len(input_list), 2):
#         item = input_list[i]
#         quantity = int(input_list[i + 1])

#         if item in products:
#             account_product_money[item] = products[item]

#             if item in account_how_many_products:
#                 account_how_many_products[item] += quantity
#             else:
#                 account_how_many_products[item] = quantity
#         else:
#             print(f"商品 {item} 不存在，请重新输入。")


#商品加只定數量用數字
# 4.除法 剪髮
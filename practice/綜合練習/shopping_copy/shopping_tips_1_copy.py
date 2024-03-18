import all_pay

products = {"牛奶":"25元" , "餅乾":"20元" , "蘋果":"30元" , "汽水":"30元" , "糖果":"20元"}

account_product_moneys = {}
account_how_many_products = {}

while True:
    buying = (f"商品有:{products}\n") #ok 沒有\n
    i_want = str(input(buying))

    if i_want == "end":
        break
    elif i_want in products:
        account_product_moneys[i_want] = products.get(i_want)
        if i_want in account_how_many_products:
            account_how_many_products[i_want] += 1
        else:
            account_product_moneys[i_want] = products[i_want]
            account_how_many_products[i_want] = 1
            
        total_cost = all_pay.calculate_total_cost(account_product_moneys, account_how_many_products)
        print(f"總花費: {total_cost}元")
    else:
        print("商品不存在，请重新输入。")
#如果我要一次牛奶兩瓶 餅乾10個怎麼辦
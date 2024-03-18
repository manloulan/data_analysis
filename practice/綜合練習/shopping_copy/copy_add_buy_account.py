def function_select_1(products):
    i_want_add = input("想新增什麼選項")
    if i_want_add in products:
        print("已有此項產品")
    else:
        i_want_add_price = input("多少元")
        products[i_want_add] = i_want_add_price     

def function_select_2(products,all_pay,i_want):
    if i_want in products:
        price = products[i_want]
        price = price[:-1]
        all_pay += int(price)
        print("還需要什麼？")
        return all_pay
    else:
        print("商品不存在，请重新输入。")
        return all_pay

def buy_two_get_one_for_free_items(buy_two_get_one_for_free_account,buy_two_get_one_for_free_name,count,one_for_free,price):
    count_num = buy_two_get_one_for_free_account // 3 
    buy_two_get_one_for_free_account -= count_num
    count[buy_two_get_one_for_free_name] = buy_two_get_one_for_free_account
    add_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
    if add_one_for_free == None:
        add_one_for_free = 0
        one_for_free[buy_two_get_one_for_free_name] = int(add_one_for_free)+1
        price_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
        price_one_for_free = int(price_one_for_free)
        price_one_for_free *= price
        return price_one_for_free
    else:
        one_for_free[buy_two_get_one_for_free_name] = int(add_one_for_free)+1
        price_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
        price_one_for_free = int(price_one_for_free)
        price_one_for_free *= price
        return price_one_for_free


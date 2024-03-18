products = {"牛奶":"25元" , "餅乾":"20元" , "蘋果":"30元" , "汽水":"30元" , "糖果":"20元"}
with open("item.txt","r",encoding = "utf-8") as all_items:
    for items in all_items.readlines():
        items = items.split("：")
        items_name = items[0].strip()
        items_price = items[1].strip()   
        products[items_name] = items_price
    function_select = {1:"新增商品",2:"購買商品",3:"結帳"}
while True:
    chose_function_select = (f"功能選項:{function_select}\n")
    i_chose = int(input(chose_function_select))
    if i_chose == 1 :
        i_want_add = str(input("想新增什麼選項"))
        if i_want_add in products:
            print("已有此項產品")
        else:
            i_want_add_price = str(input("多少元"))
            products[i_want_add] = i_want_add_price
    elif i_chose == 2:
        all_pay = 0 
        count = {}
        count_num = 0
        one_for_free = {}
        price_one_for_free = 0
        price_one_for_free_price = 0
        while True:
            buying = (f"商品有:{products}\n") 
            i_want = (str(input(buying))) #*****要如何寫terminal才會回 購買：牛奶  而不是只回牛奶
            add_count = count.get(i_want)
            if add_count == None:
                add_count = 0
                count[i_want] = int(add_count)+1
            else:
                count[i_want] = int(add_count)+1
            if i_want == "end":
                print("購買結束")
                print("還需要什麼？")
                # *****原這裡有下面的句子但會一直出現KeyError: 'end'說是因為products[i_want]為什麼
                # price_one_for_free_price = products[i_want]
                # price_one_for_free_price = price_one_for_free_price[:-1]
                # price_one_for_free_price = int(price_one_for_free_price)
                for buy_two_get_one_for_free_name , buy_two_get_one_for_free_account in count.items():
                    if buy_two_get_one_for_free_account % 3 == 0:
                        count_num =  buy_two_get_one_for_free_account // 3 
                        buy_two_get_one_for_free_account -= count_num
                        count[buy_two_get_one_for_free_name] = buy_two_get_one_for_free_account
                        add_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
                        if add_one_for_free == None:
                            add_one_for_free = 0
                            one_for_free[buy_two_get_one_for_free_name] = int(add_one_for_free)+1
                            price_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
                            price_one_for_free = int(price_one_for_free)
                            price_one_for_free *= price
                        else:
                            one_for_free[buy_two_get_one_for_free_name] = int(add_one_for_free)+1
                            price_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
                            price_one_for_free = int(price_one_for_free)
                            price_one_for_free *= price
                    elif buy_two_get_one_for_free_account % 3 == 1:
                        count_num =  buy_two_get_one_for_free_account // 3 
                        buy_two_get_one_for_free_account -= count_num
                        count[buy_two_get_one_for_free_name] = buy_two_get_one_for_free_account
                        add_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
                        if add_one_for_free == None:
                            add_one_for_free = 0
                            one_for_free[buy_two_get_one_for_free_name] = int(add_one_for_free)+1
                            price_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
                            price_one_for_free = int(price_one_for_free)
                            price_one_for_free *= price
                        else:
                            one_for_free[buy_two_get_one_for_free_name] = int(add_one_for_free)+1
                            price_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
                            price_one_for_free = int(price_one_for_free)
                            price_one_for_free *= price
                    elif buy_two_get_one_for_free_account % 3 == 2:
                        count_num =  buy_two_get_one_for_free_account // 3 
                        buy_two_get_one_for_free_account -= count_num
                        count[buy_two_get_one_for_free_name] = buy_two_get_one_for_free_account
                        add_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
                        if add_one_for_free == None:
                            add_one_for_free = 0
                            one_for_free[buy_two_get_one_for_free_name] = int(add_one_for_free)+1
                            price_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
                            price_one_for_free = int(price_one_for_free)
                            price_one_for_free *= price
                        else:
                            one_for_free[buy_two_get_one_for_free_name] = int(add_one_for_free)+1
                            price_one_for_free = one_for_free.get(buy_two_get_one_for_free_name)
                            price_one_for_free = int(price_one_for_free)
                            price_one_for_free *= price
                    else:
                        continue
                break
            elif i_want in products:
                price = products[i_want]
                price = price[:-1]
                price = int(price)
                all_pay += price
            else:
                print("商品不存在，请重新输入。")
    else:
        print("購買總金額為:" , all_pay - price_one_for_free)
        print("已折扣:" , price_one_for_free)
        
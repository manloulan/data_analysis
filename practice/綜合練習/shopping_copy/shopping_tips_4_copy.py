products = {"牛奶":"25元" , "餅乾":"20元" , "蘋果":"30元" , "汽水":"30元" , "糖果":"20元"}
import copy_add_buy_account
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
        copy_add_buy_account.function_select_1(products)
    elif i_chose == 2 :
        all_pay = 0 
        count = {}
        count_num = 0
        one_for_free = {}
        price_one_for_free = 0
        price_one_for_free_price = 0
        while True: 
            buying = (f"商品有:{products}\n")
            i_want = input(buying)
            add_count = count.get(i_want)
            if add_count == None:
                add_count = 0
                count[i_want] = int(add_count)+1
            else:
                count[i_want] = int(add_count)+1
            if i_want == "end":
                print("購買結束")
                for buy_two_get_one_for_free_name , buy_two_get_one_for_free_account in count.items():
                    price_one_for_free = copy_add_buy_account.buy_two_get_one_for_free_items(buy_two_get_one_for_free_account,buy_two_get_one_for_free_name,count,one_for_free,price)
                break
            elif i_want in products:
                price = products[i_want]
                price = price[:-1]
                price = int(price)
                all_pay += price
            else:
                all_pay = copy_add_buy_account.function_select_2(products,all_pay,i_want)      
    elif i_chose == 3 :
        print("購買總金額為:" + str(all_pay - price_one_for_free))
        print("已折扣:" , price_one_for_free)
        break
    else:
        print("沒有這個選項，請重新選擇")
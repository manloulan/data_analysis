products = {"牛奶":"25元" , "餅乾":"20元" , "蘋果":"30元" , "汽水":"30元" , "糖果":"20元"}
function_select = {1:"新增商品",2:"購買商品",3:"結帳"}
import copy_add_buy_account #問*****會搞不清楚什麼時候要+.py什麼時候不用 #答：import module時不用.py
while True:
    chose_function_select = (f"功能選項:{function_select}\n")
    i_chose = int(input(chose_function_select))
    if i_chose == 1 :
        copy_add_buy_account.function_select_1(products)
    elif i_chose == 2 :
        all_pay = 0
        while True: 
            buying = (f"商品有:{products}\n")
            i_want = input(buying)
            if i_want == "end":
                print("購買結束")
                break
            else:
                all_pay = copy_add_buy_account.function_select_2(products,all_pay,i_want)
    elif i_chose == 3 :
        print("購買總金額為:" + str(all_pay))
        break
    else:
        print("沒有這個選項，請重新選擇")
        


products = {"牛奶":"25元" , "餅乾":"20元" , "蘋果":"30元" , "汽水":"30元" , "糖果":"20元"}
# 因為17行  all_pay = 0  位置放錯導致價格一直歸零
function_select = {1:"新增商品",2:"購買商品",3:"結帳"}
while True:
    chose_function_select = (f"功能選項:{function_select}\n")
    i_chose = int(input(chose_function_select))#忘了加int就一直輪迴因為input是輸出str不是int
    if i_chose == 1 :
        i_want_add = str(input("想新增什麼選項"))
        if i_want_add in products:
            print("已有此項產品")
        else:
            i_want_add_price = str(input("多少元"))
            products[i_want_add] = i_want_add_price     
            #以為要加continue這裡才會回到 i_chose  

    elif i_chose == 2:
        all_pay = 0 #*****位置放錯導致價格一直歸零
        while True:
            buying = (f"商品有:{products}\n") #*****沒有\n
            i_want = (str(input(buying)))
            if i_want == "end":
                print("購買結束")
                break
            elif i_want in products:
                price = products[i_want]#*****dic[]跟dic.get()容易搞混
                price = price[:-1]
                all_pay += int(price)
                print("還需要什麼？")
            else:
                print("商品不存在，请重新输入。")
    else:
        print("購買總金額為:" , all_pay)
    

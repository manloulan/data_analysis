products = {"牛奶":"25元" , "餅乾":"20元" , "蘋果":"30元" , "汽水":"30元" , "糖果":"20元"}
with open("item.txt","r",encoding = "utf-8") as all_items:
    for items in all_items.readlines():
        items = items.split("：")#item.txt的：跟我原本的:不一樣所以無法連結
        items_name = items[0].strip()#原本沒加.strip，其實看不出空格不懂為什麼要strip
        items_price = items[1].strip()   
        products[items_name] = items_price
    function_select = {1:"新增商品",2:"購買商品",3:"結帳"}
    #原錯誤寫法
    # for items in all_items.readlines():
    #     items = items.split("：")#item.txt的：跟我原本的:不一樣所以無法連結
    #     items_name = items[0].strip()#原本沒加.strip
    #     items_price = items[1].strip()
    #     products = {"牛奶":"25元" , "餅乾":"20元" , "蘋果":"30元" , "汽水":"30元" , "糖果":"20元"}
    #     products[items_name] = items_price
    #     function_select = {1:"新增商品",2:"購買商品",3:"結帳"}
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
        while True:
            buying = (f"商品有:{products}\n") 
            i_want = (str(input(buying)))#*****寫法錯誤i_want = ("選購商品":str(input(buying)))
            if i_want == "end":
                print("購買結束")
                break
            elif i_want in products:
                price = products[i_want]
                price = price[:-1]
                all_pay += int(price)
                print("還需要什麼？")
            else:
                print("商品不存在，请重新输入。")
    else:
        print("購買總金額為:" , all_pay)
#下面有兩大問題           

# all_pay是我的疑問
# with open("item.txt", "r", encoding="utf-8") as all_items:
#     for item in all_items.readlines():
#         item = item.split(":")
#         item_name = item[0].strip()
#         item_price = item[1].strip()
#         products = {"牛奶": "25元", "餅乾": "20元", "蘋果": "30元", "汽水": "30元", "糖果": "20元"}
#         products[item_name] = item_price

# function_select = {1: "新增商品", 2: "購買商品", 3: "結帳"}
# all_pay = 0

# while True:
#     chose_function_select = f"功能選項:{function_select}\n"
#     i_chose = int(input(chose_function_select))

#     if i_chose == 1:
#         i_want_add = input("想新增什麼選項: ")
#         if i_want_add in products:
#             print("已有此項產品")
#         else:
#             i_want_add_price = input("多少元: ")
#             products[i_want_add] = i_want_add_price

#     elif i_chose == 2:
#         local_all_pay = 0
#         while True:
#             buying = f"商品有:{products}\n"
#             i_want = input(buying)
#             if i_want == "end":
#                 break
#             elif i_want in products:
#                 price = products[i_want]
#                 price = price[:-1]
#                 local_all_pay += int(price)
#             else:
#                 print("商品不存在，请重新输入。")
#         all_pay += local_all_pay

#     elif i_chose == 3:
#         print(f"總價格: {all_pay}元")

#     else:
#         break  # 在選擇非法選項時結束循環

# # 顯示結束的提示
# print("程式結束。")



#在while的部分是不是有問題因為上面with open已經被關閉了為什麼可以這樣寫
#解:因為如果把while的部分放進with將只會讀第一個 無法全部都讀取
# with open("item.txt", "r", encoding="utf-8") as all_items:
#     products = {}
#     for item in all_items.readlines():
#         item = item.split(":")
#         item_name = item[0].strip()
#         item_price = item[1].strip()
#         products[item_name] = item_price

# # 主程式
# function_select = {1: "新增商品", 2: "購買商品", 3: "結帳"}
# all_pay = 0

# while True:
#     chose_function_select = f"功能選項:{function_select}\n"
#     i_chose = int(input(chose_function_select))

#     if i_chose == 1:
#         i_want_add = input("想新增什麼選項: ")
#         if i_want_add in products:
#             print("已有此項產品")
#         else:
#             i_want_add_price = input("多少元: ")
#             products[i_want_add] = i_want_add_price

#     elif i_chose == 2:
#         local_all_pay = 0
#         while True:
#             buying = f"商品有:{products}\n"
#             i_want = input(buying)
#             if i_want == "end":
#                 break
#             elif i_want in products:
#                 price = products[i_want]
#                 price = price[:-1]
#                 local_all_pay += int(price)
#             else:
#                 print("商品不存在，请重新输入。")
#         all_pay += local_all_pay

#     elif i_chose == 3:
#         print(f"總價格: {all_pay}元")

#     else:
#         break  # 在選擇非法選項時結束循環

# # 顯示結束的提示
# print("程式結束。")
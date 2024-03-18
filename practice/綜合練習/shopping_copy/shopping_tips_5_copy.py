#chatgpt寫的
import os

products = {"牛奶": "25元", "餅乾": "20元", "蘋果": "30元", "汽水": "30元", "糖果": "20元"}

with open("item.txt", "r", encoding="utf-8") as all_items:
    for items in all_items.readlines():
        items = items.split("：")
        items_name = items[0].strip()
        items_price = items[1].strip()
        products[items_name] = items_price

function_select = {1: "新增商品", 2: "購買商品", 3: "結帳"}

customers_directory = "customers"
file_list = os.listdir(customers_directory)#ok 要再更了解到底什麼是listdir  

for all_customers in file_list:
    all_customers_path = os.path.join(customers_directory, all_customers)#ok 要再更了解到底什麼是os.path.join
    with open(all_customers_path, "r") as r_mode_all_customers:
        all_pay = 0
        count = {}
        one_for_free = {}
        price_one_for_free = 0
        price_one_for_free_price = 0

        print(f"\n處理 {all_customers} 的購物清單:") #ok 不懂此步驟的原因 此步驟是輸出customers裡的五個檔案名雃以嗎？
        for line in r_mode_all_customers.readlines():
            item, quantity = line.strip().split(":") #ok 此處是先用：把商品名跟價格分開後再消除空格意思會是["牛奶","購買的數量"]後再分別丟到item,quantity做儲存
            if item in products:
                price = products[item]
                price = price[:-1]#ok 表示最後一個不計所以只剩數字
                price = int(price)
                price = int(price) * int(quantity)
                all_pay += price
                print(f"{item}: {quantity}，小計: {price}元")

        print(f"\n總金額: {all_pay}元")
from logistic_class import Shop, Store, Request


if __name__ == '__main__':
    shop = Shop()
    shop.add("печенье", 5)
    shop.add("вафли", 5)
    shop.add("помидоры", 5)
    shop.add("сок", 5)
    store = Store()
    store.add("печенье_5", 5)

    user_str = input()
    user_str_list = user_str.split(" ")
    is_error = False

    try:
        user_str_list[1] = int(user_str_list[1])
    except:
        print("введите число")

    is_error = False
    if ("забрать" and "доставить") not in user_str_list[0].lower():
        print("Введите ''забрать/доставить")
        is_error = True

    if ("магазин" and "склад") not in user_str_list[4].lower():
        print("введите место назначения")
        is_error = True

    if not is_error:
        r = Request(user_str)
        print(r)
        if "магазин" in r.from_:
            print("Доставка возможно только со склада")
        elif "склад" in r.from_:
            if r.product in store.get_item():
                if r.amount <= store.get_item()[r.product]:
                    print("Нужное количество есть на складе")
                    print("Курьер везет со склада в магазин")
                    if sum(shop.get_item().values()) + int(r.amount) <= shop.capacity:
                        print(f"Курьер доставил {r.amount} {r.product} в магазин")
                        store.remove(r.product, r.amount)
                        shop.add(r.product, r.amount)

                    else:
                        print("В магазине недостаточно места, попробуйте что-то другое")
                else:
                    print("Не хватает на складе попробуйте заказать меньше")
            else:
                print("Такого товара нет на складе")

        print("В магазине храниться:")
        if shop.get_unique_items_count():
            for key, value in shop.items.items():
                print(key, value)
        else:
            print("ничего")

        print("На складе храниться:")
        if store.get_unique_items_count():
            for key, value in store.items.items():
                print(key, value)
        else:
            print("ничего")









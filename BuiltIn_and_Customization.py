phonelist_price = [200, 300, 400, 500, 600]


def maxCustom(phonelist_price):
    max_cost = 0
    for cost in phonelist_price:
        if cost > max_cost:
            max_cost = cost
    return max_cost


print("The max is:", max(phonelist_price))
print("The min is:", min(phonelist_price))


print("Custom function max cost:", maxCustom(phonelist_price))
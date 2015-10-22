def format_shopping_list(products):
    output = ""
    if len(products) == 0:
        output = "no items in list"
    elif len(products) > 1:
        n = len(products)
        output = "{0} items:\n".format(n)
    else:
        output = "1 item:\n"
    i = 1
    for item in products:
        output += "{0}: {1}\n".format(i, item.title())
        i += 1
    return output

print(format_shopping_list(products=["banan", "senap", "gorilla"]))
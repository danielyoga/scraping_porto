import re

txt = "The rain in Spain 012"
x = re.findall("\d", txt)
all = "".join(x)

print(all)

# print( ((Stock.text).replace("\n","")).strip() )
        # price_currency = re.sub("\d+", " ", Price.text)
        # price_currency = price_currency.replace(".","")
        # print(price_currency)
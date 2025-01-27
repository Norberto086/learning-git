shopping = {"piekarnia" : ["bulki", "paczek", "chleb"],
           "warzywniak" : ["marchew", "seler", "rukola"]}
product_count = 0 

for sklep, product in shopping.items():
    shop_capitalize = sklep.capitalize()
    product_capitalize = [product.capitalize() for product in product]

#     print(f"Ide do {shop_capitalize} i kupuje tam {product_capitalize}.")
#     product_count = product_count + len(product_capitalize)

# print (f"W sumie kupuje {product_count} produktow")
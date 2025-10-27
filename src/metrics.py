# Intäkter per kategori

# Kräver att man först öppnar en csv och därefter kör "variabel" = csvreader, och matar sedan in variabeln i denna funktion
import csv


def revenue_per_category(reader): 
    dictionary_of_category_and_revenue = {}
    list_of_category_and_revenue = []
    next(reader)

    for row in reader:
        if row[3] not in dictionary_of_category_and_revenue:
            dictionary_of_category_and_revenue[row[3]] = float(row[6])
        elif row[3] in dictionary_of_category_and_revenue:
            dictionary_of_category_and_revenue[row[3]] += float(row[6])
        else:
            print("Error - cannot read your input variabel correctly. Please check if it is a dictionary! Only dictionaries here plz <3")

    for category, revenue in dictionary_of_category_and_revenue.items():
        list_of_category_and_revenue.append((category, revenue))
    
    return sorted(list_of_category_and_revenue, key=lambda item: item[1], reverse=True)
    

# Nedan testar om funktionen fungerar
#with open("data/ecommerce_sales.csv", "r", encoding="utf-8") as files:
#    reader = csv.reader(files)
#    dictionary_of_test = revenue_per_category(reader)
#    print(dictionary_of_test)

def top_3_categories(reader):
    top_list_of_categories = revenue_per_category(reader)
    return top_list_of_categories[0:3]

with open("data/ecommerce_sales.csv", "r", encoding="utf-8") as files:
    reader = csv.reader(files)
    dictionary_of_test = top_3_categories(reader)
    print(dictionary_of_test)



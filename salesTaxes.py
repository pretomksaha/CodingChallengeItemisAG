import inputList
def itemize(nameOfItem):
    'categories item in food, book, medicine and others product section.'
    if 'chocolate' in nameOfItem:
        category = "food"
    elif 'book' in nameOfItem:
        category = 'book'
    elif 'pill' in nameOfItem:
        category = 'medicine'
    else:
        category = 'others'
    return category


def taxes(salesList,actualTax,importTax):
    'Funtion to split every item and price then calculate the sales taxes and total price'
    'Input:'
    'salesList: List of sales including quantity, product name and price.'
    'actualTax: % of tax on all goods except books, food, and medical.'
    'importTax: % of tax on all imported goods.'
    'Output:'
    'priceList: return a list including quantity, product name, price, sales taxes and total price.'
    priceList = []
    totalCost = 0
    totalTaxItem = 0
    for i in salesList:
        items = i.split()
        numberOfItem = int(items[0])
        priceOfItem = float(items[len(items) - 1])
        nameOfItem = (' '.join(items[1: len(items) - 2]))
        nameOfItem =(''.join([nameOfItem, ':']))
        category = itemize(nameOfItem)
        if 'import' in nameOfItem:
            taxOnitem= (priceOfItem*numberOfItem)*(importTax/100)
            if category == 'others':
                tax= (priceOfItem*numberOfItem)*(actualTax/100)
            else:
                tax=0
            totalTax= taxOnitem + tax
        else:
            if category == 'others':
                totalTax = (priceOfItem * numberOfItem) * (actualTax / 100)
            else:
                totalTax = 0
        totalTaxItem = totalTaxItem + totalTax
        totalTaxItem = round(totalTaxItem, 2)
        totalCostOfitem = (priceOfItem*numberOfItem)+totalTax
        totalCostOfitem = round(totalCostOfitem, 2)
        finalItem = (' '.join([str(numberOfItem), nameOfItem, str(format(totalCostOfitem, '.2f'))]))
        priceList.append(finalItem)
        totalCost = totalCost + totalCostOfitem

    taxSum = (' '.join(['Sales Taxes:', str(format(totalTaxItem, '.2f'))]))
    priceList.append(taxSum)
    totalSum = (' '.join(['Total:', str(format(totalCost, '.2f'))]))
    priceList.append(totalSum)
    return priceList

def initialize():
    'Function to Initialize the solution for sales taxes problem.'
    print('\t\tProblem 1: SALES TAXES\n')
    salesList = inputList.initialize()
    indexNumbe= [i for i, word in enumerate(salesList) if 'Input' in word]
    indexNumbe.append(len(salesList))
    actualTax = 10 # % of tax on all goods except books, food, and medical
    importTax = 5 # % of tax on all imported goods
    for i in range(len(indexNumbe)-1):
        print('Output ', i+1, ':')
        subSalesList = salesList[indexNumbe[i]+1:indexNumbe[i+1]]
        price = taxes(subSalesList, actualTax, importTax)
        print('\n'.join(price))
        print('\n')

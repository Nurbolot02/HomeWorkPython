import pickle

from useFulFutires.IsNumber import isNumber


def AddProduct():
    dataBase = {}
    flag = True

    while flag:
        path = 'LastID.txt'
        with open(path, 'r') as data:
            idProduct = int(data.read())
        print()
        dataBase[idProduct] = {
            'name': input('Имя продукта: '),
            'date_of_manufacture': input('Дата изготовления продукта: '),
            'product_expiration_date': input('Срок годности: '),
            'store_at_temperature': input('Хранить при температуре: '),
        }
        path1 = 'dataBase.txt'
        with open(path1, 'ab') as f:
            pickle.dump(dataBase, f)
        with open(path, 'w') as data:
            data.write(f'{idProduct + 1}')
        print(f'\nВы добавили новый продукт идентификатор продукта: {idProduct} \n\n1 - Добавить еще продукт \n0 - Выйти в главное меню')
        while True:
            txt = 'Выберите операцию: '
            userInput = isNumber(txt)
            if userInput == 0:
                flag = False
                break
            elif userInput == 1:
                break
def ShowProductList():
    count = 1
    path = 'LastID.txt'
    with open(path, 'r') as data:
        length = int(data.read())

    path2 = 'dataBase.txt'
    with open(path2, 'rb') as file:
        dataBase = pickle.load(file)
        print(dataBase)

    # def ShowProductListToId():
#     print()
#     searchingProductId = int(input('Выведите id продукта: '))
#     print(f'имя продукта: {dataBase[searchingProductId]["name"]}')
#     print(f'дата изготовления продукта: {dataBase[searchingProductId]["date_of_manufacture"]}')
#     print()
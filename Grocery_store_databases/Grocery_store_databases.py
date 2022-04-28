import Product

dataBase = {
    1: {
        'name': 'milk',
        'date_of_manufacture': '05/04/2022',
        'product expiration date': '',
        'store at temperature': '',
    }
}
idProduct = 2
operator = {1: 'Добавить продукт',
            2: 'Cписок продуктов',
            3: 'Найти продукт по id',
            4: 'Заменить продукт по id',
            5: 'Удалить продукт по id',
            0: 'Выход из программы'
            }

while True:
    print()
    d = {'name': 'hfdg', 'date_of_manufacture': 'h', 'product_expiration_date': 'h', 'store_at_temperature': 'hh'}
    for key, value in operator.items():
        print(f'{key} - {value}')
    userOperation = int(input('Выберите операцию: '))
    if userOperation == 1:
        Product.AddProduct()
    elif userOperation == 2:
        Product.ShowProductList()
    elif userOperation == 3:
        print()
        searchingProductId = int(input('Выведите id продукта: '))
        print(f'имя продукта: {dataBase[searchingProductId]["name"]}')
        print(f'дата изготовления продукта: {dataBase[searchingProductId]["date_of_manufacture"]}')
        print()
    elif userOperation == 0:
        print('Пока')
        break



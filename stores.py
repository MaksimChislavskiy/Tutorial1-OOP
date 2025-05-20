class Store():
    def __init__(self, name, address, items=None):
        self.name = name
        self.address = address
        self.items = {} if items is None else items

    def add_product(self, product, price):
        self.items[product] = price
        print(f'Товар {product} успешно добавлен.')

    def product_delete(self, product):
        if product in self.items:
            del self.items[product]
            print(f'Продукт {product} удален.')
        else:
            print('Продукт не найден')

    def price_info(self, product):
        if product in self.items:
            return f'Цена {product}: {self.items[product]}'
        return None

    def price_update(self, product, new_price):
        self.items[product] = new_price
        print('Цена успешно изменена')


store1 = Store('Фрукты', 'ул. Ленина, 10', items={'Яблоки': 0.5, 'Бананы': 0.75})
store2 = Store('Фрукты-Овощи', 'ул. Пушкина, 5', items={'Яблоки': 0.4, 'Вишня': 0.7, 'Бананы': 0.65})
store3 = Store('Природа', 'ул. Речная, 23', items={'Яблоки': 0.6, 'Бананы': 0.85})
store3.add_product('Груша', 0.5)
store3.price_update('Яблоки', 0.4)
store3.product_delete('Бананы')
print(store3.price_info('Груша'))
print(store3.price_info('aaa'))


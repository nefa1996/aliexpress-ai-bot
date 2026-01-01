import csv

def get_best_products_csv(file_path, count=5):
    products = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Преобразуем рейтинг и количество заказов в числа для сортировки
            row['rating'] = float(row.get('rating', 0))
            row['orders'] = int(row.get('orders', 0))
            products.append(row)

    # Сортировка по рейтингу и количеству заказов
    products.sort(key=lambda x: x['rating']*0.5 + x['orders']*0.5, reverse=True)
    return products[:count]

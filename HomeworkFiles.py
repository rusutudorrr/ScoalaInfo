import csv

dict_keys = ['id', 'brand', 'model', 'hp', 'price']

cars = []
brands = []

with open('input.csv') as in_file:
    csv_reader = csv.reader(in_file)
    for row in csv_reader:
        row = [csv_reader.line_num] + row
        row_dict = {}
        for i in range(0, 5):
            row_dict[dict_keys[i]] = row[i]
        cars.append(row_dict)
        brands.append(row_dict['brand'])

    brands = list(set(brands))

    for brand in brands:
        unique_brands = list(filter(lambda car: car['brand'] == brand, cars))

        with open('output_data/slow_cars.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for slow in unique_brands:
                slow_cars = []
                if int(slow['hp']) < 120:
                    slow_cars.append(slow)
                    slow_dict = {}
                    slow_dict.update(slow)
                    writer.writerow(slow_dict.values())

        with open('output_data/fast_cars.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for fast in unique_brands:
                fast_cars = []
                if 120 < int(fast['hp']) < 180:
                    fast_cars.append(fast)
                    fast_dict = {}
                    fast_dict.update(fast)
                    writer.writerow(fast_dict.values())

        with open('output_data/sport_cars.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for sport in unique_brands:
                sport_cars = []
                if int(sport['hp']) >= 180:
                    sport_cars.append(sport)
                    sport_dict = {}
                    sport_dict.update(sport)
                    writer.writerow(sport_dict.values())

        with open('output_data/cheap_cars.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for cheap in unique_brands:
                cheap_cars = []
                if int(cheap['price']) < 1000:
                    cheap_cars.append(cheap)
                    cheap_dict = {}
                    cheap_dict.update(cheap)
                    writer.writerow(cheap_dict.values())

        with open('output_data/medium_cars.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for medium in unique_brands:
                medium_cars = []
                if 1000 <= int(medium['price']) < 5000:
                    medium_cars.append(medium)
                    medium_dict = {}
                    medium_dict.update(medium)
                    writer.writerow(medium_dict.values())

        with open('output_data/expensive_cars.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for exp in unique_brands:
                expensive_cars = []
                if int(exp['price']) >= 5000:
                    expensive_cars.append(exp)
                    expensive_dict = {}
                    expensive_dict.update(exp)
                    writer.writerow(expensive_dict.values())
    pass

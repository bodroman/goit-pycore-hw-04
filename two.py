def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділення рядка за комою та вилучення інформації що стосується кота
                cat_id, cat_name, cat_age = line.strip().split(',')
                cat_info = {"id": cat_id, "name": cat_name, "age": cat_age}
                cats_info.append(cat_info)

        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

# Приклад для використання
cats_info = get_cats_info("path/to/cats_file.txt")
if cats_info is not None:
    print(cats_info)


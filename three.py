import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізуєм модуль colorama
init()

def list_directory_contents(directory_path, indent=0):
    # Получаємо шляху до директорії
    directory = Path(directory_path)

    # Перевіряємо наявності директорії
    if not directory.exists() or not directory.is_dir():
        print(f"{Fore.RED}Error: The specified path does not exist or is not a directory.{Style.RESET_ALL}")
        return

    # Виводимо вміст директорії
    for item in directory.iterdir():
        if item.is_dir():
            print(Fore.BLUE + " " * indent + "📁 " + item.name)
            list_directory_contents(item, indent + 2)
        else:
            print(Fore.GREEN + " " * indent + "📄 " + item.name)

if __name__ == "__main__":
    # Перевіряємо наявності аргументів командного рядка
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python script_name.py /path/to/directory{Style.RESET_ALL}")
    else:
        # Отримуємо шлях до директорії з аргументів командного рядка
        directory_path = sys.argv[1]
        # Викликаємо функцію для виведення структури директорії
        list_directory_contents(directory_path)

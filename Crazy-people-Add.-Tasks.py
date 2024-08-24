def quiz():
    # Список варіантів відповідей
    options = [
        "PewDiePie",
        "Рет і Лінк",
        "SlivkiShow",
        "TheBrianMaps",
        "Mister Max",
        "EeOneGuy"
    ]
    
    # Виводимо питання та варіанти відповідей
    print("-> Як звали першого ютуб-блогера, який набрав 100000000 підписників?")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # Отримуємо відповідь користувача
    answer = int(input("Виберіть номер правильної відповіді (1-6): ").strip())
    
    # Перевірка відповіді
    if options[answer - 1] == "PewDiePie":
        print("Ви виграли зустріч з творцями каналу!")
    else:
        print("Пощастить іншим разом!")

# Викликаємо функцію для запуску конкурсу
quiz()
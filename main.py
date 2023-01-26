from random import randint

from graphic_arts.start_game_banner import run_screensaver


# Атакующая способность персонажа.
def attack(char_name: str, char_class: str) -> str:
    """Определяет выбранного персонажа и выводит нанесенный противнику урон."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(3, 10)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(-3, -1)}')
    return (f'Атака {char_name} была парирован...')


# Защитная способность персонажа.
def defence(char_name: str, char_class: str) -> str:
    """Определяет выбранного персонажа и выводит заблокированный урон."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} ед. урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} ед. урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} ед. урона')
    return (f'{char_name} не смог заблокировать удар...')


# Специальная способность персонажа.
def special(char_name: str, char_class: str) -> str:
    """Определяет выбранного персонажа и выводит новые характеристики."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение '
                f'«Берсерк» выносливость: {15 + 80}')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение '
                f'«Магический всплеск» атака: {10 + 5}')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение '
                f'«Защита {10 + 10}»')
    return (f'{char_name} не применил специальное умение...')


# Начало тренировки после выбора персонажа.
def start_training(char_name: str, char_class: str) -> str:
    """Информация о выбранном классе и способностях персонажа."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        """Выбор команды для тренировки."""
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


# Функция отвечает за выбор персонажа.
def choice_char_class() -> str:
    """Информация о персонажах. Выбор персонажа и его подтверждение."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
            return 'warrior'
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
            return 'mage'
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
            return 'healer'
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа.').lower()
    return 'Подтвердите свой выбор, нажав (Y).'


# Начальный блок кода.
if __name__ == '__main__':
    """
    Приветственный текст. Модуль аннимированой заставки.
    Выбор имени будущего персонажа.
    """
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))

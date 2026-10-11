import telebot

from logic import DB_Manager
from config import DATABASE, TOKEN

bot = telebot.TeleBot(TOKEN)

manager = DB_Manager(DATABASE)


def extract_arguments(text):
    return text.split(' ', 1)[1]


@bot.message_handler(commands=['random'])
def random_recipe(message):
    recipe = manager.get_random_recipe()

    if recipe:
        name, time, ingredients = recipe

        text = (
            f'Рецепт: {name}\n\n'
            f'Время приготовления: {time}\n'
            f'Ингредиенты: {ingredients}'
        )

        bot.send_message(message.chat.id, text)

    else:
        bot.send_message(message.chat.id, 'В базе пока нет рецептов.')


@bot.message_handler(commands=['recipe'])
def recipe(message):
    name = message.text.split(' ', 1)[1]

    result = manager.get_recipe(name)

    if result:
        name, time, ingredients = result

        text = (
            f'Рецепт: {name}\n\n'
            f'Время приготовления: {time}\n'
            f'Ингредиенты: {ingredients}'
        )

        bot.send_message(message.chat.id, text)

    else:
        bot.send_message(message.chat.id, 'Такого рецепта нет в базе.')


if __name__ == '__main__':
    manager.create_tables()

    manager.add_recipe(
        'Лазанья',
        '1 час 20 минут',
        'Листы лазаньи, фарш, лук, морковь, томатный соус, сыр, молоко, мука, сливочное масло'
    )

    manager.add_recipe(
        'Сырники',
        '30 минут',
        'Творог, яйца, мука, сахар, масло'
    )

    manager.add_recipe(
        'Паста Карбонара',
        '25 минут',
        'Спагетти, бекон, яйца, Пармезан, чеснок, перец'
    )

    manager.add_recipe(
        'Тирамису',
        '40 минут',
        'Печенье Савоярди, маскарпоне, яйца, сахар, кофе, какао'
    )

    manager.add_recipe(
        'Пельмени',
        '1 час',
        'Мука, вода, яйца, фарш, лук, соль, перец'
    )

    manager.add_recipe(
        'Плов',
        '1 час 10 минут',
        'Рис, мясо, морковь, лук, чеснок, масло, специи'
    )

    manager.add_recipe(
        'Голубцы',
        '1 час 30 минут',
        'Капуста, фарш, рис, лук, морковь, томатный соус'
    )

    manager.add_recipe(
        'Панкейки',
        '25 минут',
        'Мука, молоко, яйца, сахар, разрыхлитель, масло'
    )

    bot.infinity_polling()
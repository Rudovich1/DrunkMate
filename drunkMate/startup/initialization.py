from drunkMate.core import repository
from drunkMate.core.cruds import user_crud, ingredient_crud, cocktail_crud, comment_crud

async def create_admin():
    if repository.get_user('admin1') is None:
        user1 = {'login': 'admin1', 'password': 'password1', 'name': 'name1', 'role': repository.Role.DRUNKMASTER.value}
        await user_crud.create_user(user1)

    if repository.get_user('admin2') is None:
        user2 = {'login': 'admin2', 'password': 'password2', 'name': 'name2', 'role': repository.Role.DRUNKMASTER.value}
        await user_crud.create_user(user2)
        

async def create_ingredients():
    if repository.get_ingredient('Белый ром') is None:
        await ingredient_crud.post_ingredient({"name": "Белый ром",
                                            "description": "Карибский крепкий алкоголь получают методом вертикальной перегонки спирта, полученного путем брожения патоки или сока из сахарного тростника. Перед купажированием выдерживают не менее 12 месяцев в обожженных дубовых бочках из-под бурбона и фильтруют, чтобы обесцветить напиток.",
                                            "tags": ["тростник", "крепкий"]})
    if repository.get_ingredient('Сахарный сироп') is None:
        await ingredient_crud.post_ingredient({"name": "Сахарный сироп",
                                            "description": "Самый распространенный коктейльный сироп производят из натурального экстракта сахарного тростника, смешанного с водой.",
                                            "tags": ['сладкие', 'добавки']})
    if repository.get_ingredient('Содовая') is None:
        await ingredient_crud.post_ingredient({"name": "Содовая",
                                            "description": "Газированную воду, ставшую незаменимым компонентом физзов и других газированных напитков, ранее производили методом газирования углекислым газом, а сегодня все чаще готовят, добавляя пищевую соду к нейтральной чистой воде.",
                                            "tags": ['безалкогольные', 'газированные']})
    if repository.get_ingredient('Лайм') is None:
        await ingredient_crud.post_ingredient({"name": "Лайм",
                                            "description": "Тропический цитрусовый фрукт, растущий на низкорослых деревьях преимущественно в Китае, Индии и Мексике. Содержит клетчатку, витамин С и кальций, хорошо раскрывает аромат и вкус других продуктов. Один плод весит в среднем 80 г и дает 30 мл сока, разрезается на 4 дольки по 7,5 мл каждая или 8 кружков.",
                                            "tags": ['цитрусовые', 'фрукт']})
    if repository.get_ingredient('Мята') is None:
        await ingredient_crud.post_ingredient({"name": "Мята",
                                            "description": "Самая разрекламированная трава в коктейльном мире насчитывает более 30 видов. В миксологии используют преимущественно перечную и сладкую мяту. Хранится в холодильнике в бумажном полотенце не более двух суток.",
                                            "tags": ['зелень']})
    if repository.get_ingredient('Дробленый лед') is None:
        await ingredient_crud.post_ingredient({"name": "Дробленый лед",
                                            "description": "Первый «бритый» лед бармены срезали специальными ножами с больших ледяных плит. Позже появились дробильные машинки и ледогенераторы.",
                                            "tags": ['лед']})
    if repository.get_ingredient('Лаймовый сок') is None:
        await ingredient_crud.post_ingredient({"name": "Лаймовый сок",
                                            "description": "Для производства сока лаймы пускают под пресс, затем фильтруют и разливают сок по бутылкам.",
                                            "tags": ['безалкогольные', 'цитрусовые']})
    if repository.get_ingredient('Лед в кубиках') is None:
        await ingredient_crud.post_ingredient({"name": "Лед в кубиках",
                                            "description": "При производстве этого незаменимого ингредиента основное внимание уделяют чистоте воды и скорости заморозки. Чем медленнее замораживается вода, тем прозрачнее получается продукт. Идеальные образцы не имеют полостей и медленнее тают в бокале.",
                                            "tags": ['лед']})
    if repository.get_ingredient('Клубничный сироп') is None:
        await ingredient_crud.post_ingredient({"name": "Клубничный сироп",
                                            "description": "Ягодный сироп производят методом пастеризации сока спелой клубники, смешанного с сахаром и водой.",
                                            "tags": ['ягодные', 'добавки']})
    if repository.get_ingredient('Апельсиновый сок') is None:
        await ingredient_crud.post_ingredient({"name": "Апельсиновый сок",
                                            "description": "Для производства сока апельсины пускают под пресс, затем фильтруют и разливают сок по бутылкам.",
                                            "tags": ['безалкогольные', 'цитрусовые']})
    if repository.get_ingredient('Клубничное пюре') is None:
        await ingredient_crud.post_ingredient({"name": "Клубничное пюре",
                                                "description": "Мякоть крупных красных ягод, растущих небольших кустарниках преимущественно в США, Турции, Испании, Египте и Мексике смешивают с сахаром в равных пропорциях и пастеризуют для сохранения неизменного вкуса круглый год.",
                                                "tags": ['ягодные', 'добавки', 'пюре']})
    if repository.get_ingredient('Клубника') is None:
        await ingredient_crud.post_ingredient({"name": "Клубника",
                                            "description": "Крупная красная ягода, растущая на небольших кустарниках преимущественно в США, Турции, Испании, Египте и Мексике. Содержит сахара, пектиновые и дубильные вещества, аскорбиновую и другие кислоты, обладает противовоспалительным действием. Одна ягода весит в среднем 20 г.",
                                            "tags": ['ягода']})
    if repository.get_ingredient('Лондонский сухой джин') is None:
        await ingredient_crud.post_ingredient({"name": "Лондонский сухой джин",
                                                "description": "Крепкий алкоголь изготавливается в вертикальных перегонных кубах, зерновой спирт настаивают в течение суток на можжевельнике и десятке других трав и специй, а затем дистиллируют и разливают в бутылки.",
                                                "tags": ['крепкие', 'можжевельник']})
    if repository.get_ingredient('Тоник') is None:
        await ingredient_crud.post_ingredient({"name": "Тоник",
                                            "description": "Газированный напиток с хинином был изобретен в Индии для борьбы с малярией. Производят из газированной воды, смешанной с хинином и небольшим количеством сахара.",
                                            "tags": ['безалкогольные', 'горькие', 'газированные']})


async def create_cocktails():
    admin1_id = str(repository.get_user('admin1')['_id'])
    cocktail_names = set()
    
    for cocktail in list(repository.get_cocktails()):
        cocktail_names.add(cocktail['name'])
    
    if 'Мохито' in cocktail_names:
        await cocktail_crud.post_cocktail({ "name": "Мохито",
                                        "description": "Это освежающий сладкий лонг на основе рома с большим количеством мяты и лайма. Кстати, когда-то их добавляли для того, чтобы перебить вкус плохого рома и обезопасить себя от болезней, но сегодня этого можно не бояться. Традиционно в коктейль добавляют газированную воду, но можно заменить её на спрайт, если вы предпочитаете более сладкий вкус.",
                                        "tags": ["слабоалкогольные", "мятные", "кислые", "цитрусовые", "на роме"],
                                        "recipe": """Положи в хайбол лайм 3 дольки и подави мадлером
Возьми мяту 10 листиков в одну руку и хлопни по ним другой рукой
Положи мяту в хайбол
Наполни бокал дробленым льдом доверху
Добавь сахарный сироп 15 мл и белый ром 50 мл
Долей содовую доверху и аккуратно размешай коктейльной ложкой
Досыпь немного дробленого льда
Укрась веточкой мяты и долькой лайма""",
                                        "strength": repository.Strength.LOW.name,
                                        "ingredients": [{"name": "Белый ром",
                                                        "amount": 50,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Сахарный сироп",
                                                        "amount": 15,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Содовая",
                                                        "amount": 100,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Лайм",
                                                        "amount": 80,
                                                        "unit": repository.UnitType.GRAMS.name
                                                        },
                                                        {"name": "Мята",
                                                        "amount": 3,
                                                        "unit": repository.UnitType.UNITS.name
                                                        },
                                                        {"name": "Дробленый лед",
                                                        "amount": 200,
                                                        "unit": repository.UnitType.GRAMS.name
                                                        },],
                                        "parent_cocktails": []
                                        }, admin1_id)
    
    if 'Дайкири' in cocktail_names:
        await cocktail_crud.post_cocktail({ "name": "Дайкири",
                                        "description": "Хотите попробовать \"Дайкири\"? Это кислый коктейль на основе рома с добавлением лаймового сока и сахарного сиропа. \"Дайкири\" придумал американец, посетивший Кубу, поэтому этот классический коктейль встречается на страницах многих произведений американской литературы ХХ века.",
                                        "tags": ['крепкие', 'кислые', 'цитрусовые', 'на роме', 'классика'],
                                        "recipe": """Налей в шейкер лаймовый сок 30 мл, сахарный сироп 15 мл и белый ром 60 мл
Наполни шейкер кубиками льда и взбей
Перелей через стрейнер в охлажденное шампанское блюдце""",
                                        "strength": repository.Strength.STRONG.name,
                                        "ingredients": [{"name": "Белый ром",
                                                        "amount": 60,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Сахарный сироп",
                                                        "amount": 15,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Лаймовый сок",
                                                        "amount": 30,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Лед в кубиках",
                                                        "amount": 200,
                                                        "unit": repository.UnitType.GRAMS.name
                                                        }],
                                        "parent_cocktails": []
                                        }, admin1_id)
    
    if 'Клубничный дайкири' in cocktail_names:
        await cocktail_crud.post_cocktail({ "name": "Клубничный дайкири",
                                        "description": "Вам нравится дайкири? Тогда попробуйте Клубничный дайкири. Это крепкий, ягодный, кислый и сладкий коктейль на основе рома.",
                                        "tags": ['крепкие', 'ягодные', 'сладкие', 'кислые', 'на роме'],
                                        "recipe": """Налей в шейкер лаймовый сок 25 мл и клубничный сироп 25 мл
Добавь белый ром 75 мл
Наполни шейкер кубиками льда и тщательно взбей
Перелей через стрейнер в шампанское блюдце""",
                                        "strength": repository.Strength.STRONG.name,
                                        "ingredients": [{"name": "Белый ром",
                                                        "amount": 75,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Клубничный сироп",
                                                        "amount": 25,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Лаймовый сок",
                                                        "amount": 25,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Лед в кубиках",
                                                        "amount": 200,
                                                        "unit": repository.UnitType.GRAMS.name
                                                        }],
                                        "parent_cocktails": ['Дайкири']
                                        }, admin1_id)
    
    if 'Горячий апельсин' in cocktail_names:
        await cocktail_crud.post_cocktail({ "name": "Горячий апельсин",
                                        "description": "Вам нравятся десертные горячие коктейли? Тогда попробуйте этот слабоалкогольный ягодный, цитрусовый и сладкий коктейль на основе рома.",
                                        "tags": ['слабоалкогольные', 'ягодные', 'цитрусовые', 'сладкие', 'на роме'],
                                        "recipe": """Положи в питчер клубничное пюре 10 к. ложек
Добавь клубничный сироп 30 мл, апельсиновый сок 100 мл и белый ром 50 мл
Помешивая, нагрей, не доводя до кипения
Перелей в бокал для ирландского кофе
Укрась нарезанной клубникой""",
                                        "strength": repository.Strength.LOW.name,
                                        "ingredients": [{"name": "Белый ром",
                                                        "amount": 50,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Клубничный сироп",
                                                        "amount": 30,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Апельсиновый сок",
                                                        "amount": 100,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Клубничное пюре",
                                                        "amount": 50,
                                                        "unit": repository.UnitType.GRAMS.name
                                                        },
                                                        {"name": "Клубника",
                                                        "amount": 20,
                                                        "unit": repository.UnitType.GRAMS.name
                                                        }],
                                        "parent_cocktails": []
                                        }, admin1_id)
    
    if 'Джин тоник' in cocktail_names:
        await cocktail_crud.post_cocktail({ "name": "Джин тоник",
                                        "description": "Хотите попробовать \"Джин тоник\"? Это бессмертный микс джина и тоника, который подается, наверное, в каждом баре Земли. Травяной и немного горький коктейль прекрасно освежает и тонизирует. Украсить его можно лаймом или огурцом в зависимости от того, преобладание чего вам больше нравится - свежести или кислинки.",
                                        "tags": ['слабоалкогольные', 'горькие', 'на джине', 'миксы' ,'лонги'],
                                        "recipe": """Наполни хайбол кубиками льда доверху
Налей джин 50 мл
Долей тоник доверху и аккуратно размешай коктейльной ложкой
Укрась кружками лайма""",
                                        "strength": repository.Strength.LOW.name,
                                        "ingredients": [{"name": "Лондонский сухой джин",
                                                        "amount": 50,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Тоник",
                                                        "amount": 150,
                                                        "unit": repository.UnitType.MILLILITERS.name
                                                        },
                                                        {"name": "Лайм",
                                                        "amount": 20,
                                                        "unit": repository.UnitType.GRAMS.name
                                                        },
                                                        {"name": "Лед в кубиках",
                                                        "amount": 180,
                                                        "unit": repository.UnitType.GRAMS.name
                                                        }],
                                        "parent_cocktails": []
                                        }, admin1_id)
    

async def create_test_users():
    if repository.get_user('test_user_1') is None:
        await user_crud.create_user({'login': 'test_user_1', 'password': 'test_user_1', 'name': 'test_user_1', 'role': repository.Role.USER.value})
        
    if repository.get_user('test_user_2') is None:
        await user_crud.create_user({'login': 'test_user_2', 'password': 'test_user_2', 'name': 'test_user_2', 'role': repository.Role.USER.value})
        
    if repository.get_user('test_user_3') is None:
        await user_crud.create_user({'login': 'test_user_3', 'password': 'test_user_3', 'name': 'test_user_3', 'role': repository.Role.USER.value})
        

async def create_comments():
    user1 = repository.get_user('test_user_1')
    user2 = repository.get_user('test_user_2')
    user3 = repository.get_user('test_user_3')
    
    for cocktail in list(repository.get_cocktails()):
        await comment_crud.post_comment(str(cocktail['_id']),
                                        str(user1['_id']),
                                        'test1',
                                        1)
        await comment_crud.post_comment(str(cocktail['_id']),
                                        str(user2['_id']),
                                        'test2',
                                        2)
        await comment_crud.post_comment(str(cocktail['_id']),
                                        str(user3['_id']),
                                        'test3',
                                        3)
        
        
async def initialization():
    await create_admin()
    await create_ingredients()
    await create_cocktails()
    await create_test_users()
    await create_comments()
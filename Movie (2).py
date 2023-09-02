# Создать сервис по просмотру сериала
# Для данного задания понадобится класс Сериал(название, год выхода, список актеров,
# режиссер, жанр, сезоны) (для сезона рекомендуется создать свой класс с атрибутами название кол-серий, список серий)
# можете выбрать любые 2 функциональности из списка ниже

# реализовать общий список сериалов +
# реализовать возможность добавлять список любимых сериалов +

#(Остальное уже вне домашки)

# реализовать возможность добавлять список любимых сезонов 
# реализовать возможность добавлять список любимых серий 
# Необходимо реализовать поиск по номеру серии, названию сезонов, названию сериалов 


import tabulate

class Netflix:
    def __init__(self, name, year, actor, director, genre, seasons):
        self.name = name
        self.year = year
        self.actor = actor
        self.director = director
        self.genre = genre
        self.seasons = seasons

    def show_info(self):
        print(f'Название сериала: {self.name}\n'
              f'Год сериала: {self.year}\n'
              f'Актеры: {", ".join(self.actor)}\n'
              f'Режиссер: {self.director}\n'
              f'Жанр: {self.genre}\n'
              f'Кол-во сезонов: {self.seasons}\n')
        
        

def main():
    movie1 = Netflix('Игра престолов', 2011, ['Лена Хиди', 'Кит Харингтон', 'Эмилия Кларк'], 'Дэвид Бениофф', 'фэнтези', 8)
    movie2 = Netflix('Во все тяжкие', 2008, ['Брайан Крэнстон', 'Аарон Пол', 'Анна Ганн'], 'Винс Гиллиган', 'драма', 5)
    movie3 = Netflix('Кремниевая долина', 2014, ['Томас Миддлдитч', 'Мартин Старр', 'Кумэйл Наньяни'], 'Майк Джадж', 'комедия', 6)
    movie4 = Netflix('Черное зеркало', 2011, ['Дэниэл Калуя', 'Джессика Браун-Финдли', 'Тоби Кеббелл'], 'Чарли Брукер', 'фантастика', 5)
    movie5 = Netflix('Мистер Робот', 2015, ['Рами Малек', 'Кристиан Слэйтер', 'Карли Чейкин'], 'Сэм Эсмейл', 'драма', 4)
    movie6 = Netflix('Стрела', 2012, ['Стивен Амелл', 'Дэвид Рэмси', 'Уилла Холлэнд'], 'Грег Берланти', 'приключения', 8)
    movie7 = Netflix('Ведьмак', 2019, ['Генри Кавилл', 'Фрейя Аллан', 'Эмилия Беч'], 'Лорен Шмидт', 'фэнтези', 2)
    movie8 = Netflix('Люди в черном', 1997, ['Уилл Смит', 'Томми Ли Джонс', 'Линда Фиорентино'], 'Барри Зонненфельд', 'фантастика', 3)
    movie9 = Netflix('Сверхъестественное', 2005, ['Джаред Падалеки', 'Дженсен Эклс', 'Миша Коллинз'], 'Эрик Крипке', 'ужасы', 15)
    movie10 = Netflix('Шерлок', 2010, ['Бенедикт Камбербэтч', 'Мартин Фриман', 'Руперт Грейвз'], 'Марк Гэтисс', 'детектив', 4)
    
    

    movies = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10]
    favorites = []

    first = input('Привет, хочешь увидеть список сериалов? Да/нет: ').lower()
    if first == 'да':
        headers = ["Номер", "Название", "Год", "Актеры", "Режиссер", "Жанр", "Кол-во сезонов"]
        table_data = []

        for index, movie in enumerate(movies, start=1):
            table_data.append([
                index,
                movie.name,
                movie.year,
                ", ".join(movie.actor),
                movie.director,
                movie.genre,
                movie.seasons
            ])

        print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
        add_to_favorites(movies, favorites)
    else:
        print('Ну ладно, пока')
        
        

def add_to_favorites(movies, favorites):
    Chose = input('Добавим в избранное сериал? Да/Нет: ').lower()

    if Chose == 'да':
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. {movie.name}")
        favorite_index = int(input('Введите номер сериала для добавления в избранное: '))
        if 1 <= favorite_index <= len(movies):
            favorites.append(movies[favorite_index - 1])
            print('Сериал добавлен в избранное')
        else:
            print('Неверный номер сериала')
        add_to_favorites(movies, favorites)
    elif Chose == 'нет':
        if len(favorites) == 0:
            print('Хорошо, тогда потом')
        else:
            show_favorites_list(favorites)
    else:
        print('Нажми что надо, лол')
        add_to_favorites(movies, favorites)
        
        

def show_favorites_list(favorites):
    show_favorites = input('Все сериалы добавлены. Показать список избранного? Да/нет: ').lower()
    if show_favorites == 'да':
        print('Список избранных сериалов:')
        for index, favorite in enumerate(favorites, start=1):
            print(f"{index}.")
            favorite.show_info()
    else:
        print('Ок, до свидания!')

if __name__ == "__main__":
    main()




































# movies = [movie1, movie2, movie3]
# favorites = []

# first = input('Привет, хочешь увидеть список сериалов? Да/нет: ').lower()
# if first == 'да':
#     for index, movie in enumerate(movies, start=1):
#         print(f"Номер {index}")
#         movie.show_info()
# else:
#     print('Ну ладно, пока')
    
    
    
    

# Chose = input('Добавим в избранное сериал? Да/Нет: ').lower()

# if Chose == 'да':
#     favorite_index = int(input('Введите номер сериала для добавления в избранное: '))
#     if 1 <= favorite_index <= len(movies):
#         favorites.append(movies[favorite_index - 1])
#         print('Сериал добавлен в избранное')
#     else:
#         print('Неверный номер сериала')
# elif Chose == 'нет':
#     print('Хорошо, тогда потом')
# else:
#     print('Нажми что надо, лол')
    
    
    

# chose2 = input('Продолжим добавлять? Да/Нет: ').lower()

# if chose2 == 'да':
#     for index, movie in enumerate(movies, start=1):
#         print(f"{index}. {movie.name}")
#     favorite_index2 = int(input('Введите номер сериала для добавления в избранное: '))
    
#     if 1 <= favorite_index2 <= len(movies):
#         favorites.append(movies[favorite_index2 - 1])
#         print('Сериал добавлен в избранное')
#     else:
#         print('Неверный номер сериала')
        
         
        
# chose3 = input('Продолжим добавлять? Да/Нет: ').lower()

# if chose3 == 'да':
#     for index, movie in enumerate(movies, start=1):
#         print(f"{index}. {movie.name}")
#     favorite_index3 = int(input('Введите номер сериала для добавления в избранное: '))
       
#     if 1 <= favorite_index3 <= len(movies):
#         favorites.append(movies[favorite_index3 - 1])
#         print('Сериал добавлен в избранное')
#     else:
#         print('Неверный номер сериала')
        
            
# show_favorites = input('Все сериалы добавлены. Показать список избранного? Да/нет: ').lower()
# if show_favorites == 'да':
#     print('Список избранных сериалов:')
#     for index, favorite in enumerate(favorites, start=1):
#         print(f"{index}.")
#         favorite.show_info()
# else:
#     print('Ок, до свидания!')
        

 


























# favorites = []              
# movie = [Netflix(n,y,a,d,g,s) for n,y,a,d,g,s in series_info]
# def show_name():
#     for i in movie:
#         print((movie.index(i) + 1),i.name,i.year,i.actor,i.director,i.genre,i.seasons)
#     print('Выберите номер сериала')
#     choice = int(input('Пользователь: '))
    
#     if choice == 1:
#         favorites.append(i)
        
 
    
# chose = input('Хотите добавить свой любимый сериал в избранное? да/нет: ').lower()
# if chose == 'да':  
#      show_name()
# else:
#     print('Мудак, сделай выбор')    
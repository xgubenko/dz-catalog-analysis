import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, 
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    """
    Функция возвращает среднюю оценку по каталогу, округленную до одного знака (round).
    """

    sum = 0
    for i in movies:
        sum += i["rating"]
    return round(sum / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    """
    Функция возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах,
    средний возраст фильмов в массиве), 
    где среднее округлено вверх до целого с помощью math.ceil.
    """

    min_year = movies[0]["year"]
    max_year = movies[0]["year"]
    sum = 0

    for i in movies:
        tmp = i["year"]
        if tmp < min_year:
            min_year = tmp
        elif tmp > max_year:
            max_year = tmp
        sum += current_year - tmp

    avg_age = math.ceil(sum / len(movies))

    return (current_year - min_year, current_year - max_year, avg_age)

def duration_in_hours(minutes):
    """
    Функция переводит минуты в формат "2ч 35м",
    используя целочисленное деление и остаток от деления.
    """

    hours_res = minutes // 60
    mins_res = minutes % 60
    return f"{hours_res}ч {mins_res}м"

def rating_tier(rating):
    """
    По оценке возвращает категорию:
    "шедевр" (≥9),
    "хорошо" (7-8.9),
    "средне" (5-6.9),
    "слабо" (<5). 
    """

    return "шедевр" if rating >= 9 else "хорошо" if rating >= 7 else "средне" \
          if rating >= 5 else "слабо"

def decade_label(year):
    """
    Возвращает метку:
    "новые" (после 2020),
    "недавние" (2015-2020),
    "старые" (раньше 2015).
    """

    match year:
        case y if y > 2020:
            return "новые"
        case y if y >= 2015:
            return "недавние"
        case _: 
            return "старые"

def for_and_while_demonstration(movies):
    """
    Выводит на экран названия всех фильмов,
    которые НЕ относятся к жанру "comedy"

    Находит первый по порядку в списке фильм с рейтингом выше 9.0;
    если такого фильма нет, цикл должен завершиться веткой
    else с сообщением "Шедевров не найдено"
    """

    for m in movies:
        if "comedy" in m["genres"]:
            continue
        print(m["title"])
        print(m)

    i = 0
    title = None

    while i < len(movies):
        if movies[i]["rating"] > 9:
            title = movies[i]["title"]
            print(f"Первый найденный фильм с оценкой выше 9.0: {title}")
            break
        i += 1
    else: 
        print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    """
    через for с накопительной переменной считает количество фильмов
    длиннее threshold минут
    """

    sum = 0
    for m in movies:
        if m["duration_min"] > 120:
            sum += 1
    return sum

def normalize_title(title):
    """
    Приводит строку к формату Title Case
    """

    words = title.split()
    for i, w in enumerate(words):
        words[i] = w[0].upper() + w[1:]
    return " ".join(words)

def make_slug(title):
    """
    Превращает нормализованное название в «слаг» вида the-quiet-algorithm.
    """
    words = title.split()
    words = [word.replace(word, word.lower()) for word in words]
    return "-".join(words)

def format_report_line(movie):
    """
    Возвращает единую строку с описанием фильма
    '"The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi'
    """

    return f'"{movie["title"]}" ({movie["year"]}) - ' \
    f'{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, ' \
    f'жанры: {", ".join(sorted(movie["genres"]))}'

def titles_sorted_by_rating(movies):
    """
    Возвращает список названий фильмов, отсортированных по убыванию рейтинга
    """
    sorted_movies = sorted(movies, key = lambda m: m["rating"], reverse=True)
    return [m["title"] for m in sorted_movies]

def top_n_by_rating(movies, n=3):
    """
    Возвращает список из n кортежей (title, rating) — топ по рейтингу
    """

    sorted_movies = sorted(movies, key = lambda m: m["rating"], reverse=True)[:n]
    return [(m["title"], m["rating"]) for m in sorted_movies]

def count_by_genre(movies):
    """
    Возвращает словарь {жанр: количество фильмов}, 
    построенный вручную через цикл и метод dict.get() (без Counter).
    """

    res = {}
    for m in movies:
        for g in m["genres"]:
            res[g] = res.get(g, 0) + 1
    return res

def actor_filmography(movies):
    """
    Возвращает словарь {актер: [список названий фильмов]}
    """

    res = {}
    for m in movies:
        for a in m["actors"]:
            res[a] = res.get(a, 0) + 1
    return res

"""
С помощью генератора словаря (dict comprehension) постройте словарь 
{title: rating} только для фильмов с рейтингом выше среднего 
(используйте average_rating из этапа 1).
"""
high_rated = {m["title"]: m["rating"] for m in movies \
               if m["rating"] > average_rating(movies)}

def all_genres(movies):
    """
    Возвращает множество всех уникальных жанров каталога
    """
    res = set()
    for m in movies:
        res.update(m["genres"])
    return res

def common_actors(movie1, movie2):
    """
    Возвращает множество актеров, снимавшихся в обоих фильмах.
    """
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    """
    Возвращает жанры, встречающиеся в movies_a, 
    но не встречающиеся в movies_b
    """
    return movies_a["genres"] - movies_b["genres"]

def iter_high_rated(movies, min_rating=8.0):
    """
    Лениво отдает фильмы с рейтингом не ниже min_rating
    """

    for m in movies:
        if m["rating"] > min_rating:
            yield m

"""
Продемонстрируйте работу циклом for с вызовом format_report_line.
"""
# for movie in iter_high_rated(movies):
#         print(format_report_line(movie))

"""
Напишите генераторное выражение, которое считает 
суммарную длительность всех фильмов с рейтингом 
выше 7 в минутах, и передайте его в sum().
"""
# print(sum(m["duration_min"] for m in movies if m["rating"] > 7))

def build_report(movies):
    """
    объединяет результаты всех предыдущих этапов 
    в единый консольный отчет: общую статистику, 
    топ-3 фильма, количество фильмов по каждому 
    жанру и полный список уникальных жанров каталога.
    """

    titles = [x[0] for x in top_n_by_rating(movies)]
    top_movies = [m for m in movies if m["title"] in titles]

    genre_counts = count_by_genre(movies).items()
    sorted_genres = sorted(genre_counts, key=lambda x: x[1], reverse=True)

    print(f"""ОТЧЕТ ПО КАТАЛОГУ
Средний рейтинг: {average_rating(movies)}
Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет

Топ-3 фильма:
    {'\n    '.join(format_report_line(m) for m in top_movies)}

Фильмов по жанрам:
    {"\n    ".join(f"{k} — {v}" for k, v in sorted_genres)}
    

Все жанры каталога: {", ".join(sorted(all_genres(movies)))}""")

def main() -> None:
    build_report(movies)

if __name__ == "__main__":
    main()
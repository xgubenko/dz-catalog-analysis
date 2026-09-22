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
    else: print("Шедевров не найдено")

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
    Пприводит строку к формату Title Case
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

    return f'"{movie["title"]}" ({movie['year']}) - ' \
    f'{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, ' \
    f'жанры: {", ".join(sorted(movie["genres"]))}'



def main() -> None:
    # stats = catalog_age_stats(movies)
    # print(f"Средний рейтинг: {average_rating(movies)}")
    # print(f"Статистика каталога. Самому старому фильму лет: {stats[0]}; \
    #       самому новому: {stats[1]}; Фильмам в среднем лет: {stats[2]}.")
    # print(f"Продолжительность первого фильма в каталоге: \
    #       {duration_in_hours(movies[0]['duration_min'])}")
    # print(rating_tier(8))
    # print(decade_label(2014))
    # for_and_while_demonstration(movies)
    # print(count_long_movies(movies))
    print(normalize_title("silent hours"))      # "Silent Hours"
    print(make_slug("Silent Hours"))            # "silent-hours"
    print(format_report_line(movies[7]))
    # '"The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi' 
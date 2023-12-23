import os
import csv
import json
from homework11_info import films_data
from homework11_info import ganres

json_ganres = json.loads(ganres)

colums = ["title", "year", "rating", "type", "ganres"]
result_title = []
result_year = []
result_rating = []
result_type = []
result_gen = []
result_genre = []
inside_list = []
result_list = []
path_genre = []

for film in films_data:
    inside_list = []
    result_title = film.get('title')
    result_year = film.get('year')
    result_rating = film.get('rating')
    result_type = film.get('type')
    result_gen = film.get('gen')
    inside_list.extend(list((result_title, result_year, result_rating, result_type)))
    for genre in result_gen:
        inside_list.append(genre.get('genre'))
    result_list.append(inside_list)

for data in json_ganres['results']:
    genre_data = data.get('genre')
    genre_path_dir = os.path.join("genre", genre_data)
    os.makedirs(genre_path_dir, exist_ok=True)

    file_path = 'file_csv.csv'
    file_csv_path = os.path.join(genre_path_dir, file_path)
    if not os.path.exists(file_csv_path):
        with open(file_csv_path, 'a', encoding='utf-8') as file_obj_ganres:
            file_reader = csv.reader(file_obj_ganres)
            file_writer = csv.writer(file_obj_ganres)
            file_writer.writerow(colums)
    else:
        with open(file_csv_path, 'r', encoding='utf-8') as file_obj_ganres:
            file_reader = csv.reader(file_obj_ganres)

    for row in result_list:
        for k in row:
            if k == genre_data:
                file_path = 'file_csv.csv'
                file_csv_path = os.path.join(f'genre/{k}', file_path)
                with open(file_csv_path, 'a', encoding='utf-8') as file_obj_ganres:
                    file_reader = csv.reader(file_obj_ganres)
                    file_writer = csv.writer(file_obj_ganres)
                    file_writer.writerow(row)

            else:
                pass
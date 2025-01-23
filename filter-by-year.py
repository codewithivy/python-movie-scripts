import os
import shutil
from datetime import datetime

def filter_and_sort_movies_by_year(directory, year_filter):
    movies_by_year = {}

    # Step 1: Filter movies by year
    for filename in os.listdir(directory):
        match = re.match(r"(.*?)(\d{4})(.*)", filename)
        if match:
            movie_name = match.group(1).strip()
            year = match.group(2)

            if int(year) == year_filter:
                if year not in movies_by_year:
                    movies_by_year[year] = []
                movies_by_year[year].append(filename)

    # Step 2: Sort and move movies by year
    for year, movies in movies_by_year.items():
        year_folder = os.path.join(directory, year)
        if not os.path.exists(year_folder):
            os.makedirs(year_folder)

        for movie in movies:
            old_file = os.path.join(directory, movie)
            new_file = os.path.join(year_folder, movie)
            shutil.move(old_file, new_file)
            print(f"Moved: {movie} -> {year_folder}")

# Set your directory path and year filter here
directory_path = "/path/to/your/movies"
year_to_filter = 2020
filter_and_sort_movies_by_year(directory_path, year_to_filter)

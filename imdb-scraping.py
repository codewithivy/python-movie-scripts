from imdb import IMDb
import csv

def scrape_movie_metadata(directory):
    ia = IMDb()
    movie_data = []

    for filename in os.listdir(directory):
        # Match the movie name and year
        match = re.match(r"(.*?)(\d{4})(.*)", filename)
        if match:
            movie_name = match.group(1).strip()
            year = match.group(2)

            # Search for the movie on IMDb
            search_results = ia.search_movie(f"{movie_name} {year}")
            if search_results:
                movie = search_results[0]
                ia.update(movie)

                # Get metadata
                title = movie.get('title')
                rating = movie.get('rating')
                genre = ", ".join(movie.get('genres', []))
                plot = movie.get('plot', [''])[0]

                movie_data.append([title, year, rating, genre, plot])

    # Write metadata to CSV
    with open('movie_metadata.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Year', 'Rating', 'Genre', 'Plot'])
        writer.writerows(movie_data)

    print(f"Scraped {len(movie_data)} movies' metadata.")

# Set your directory path here
directory_path = "/path/to/your/movies"
scrape_movie_metadata(directory_path)

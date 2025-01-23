# python-movie-scripts
My python scripts to manage Plex movie server content. 
Automating tedious tasks like renaming, organizing, and syncing.

### rename-to-conventions.py
Batch Renaming Files (to match Plex naming conventions)
This script batch renames movie files to match the correct Plex naming conventions, which generally follow a format like: MovieName (Year).ext.

### moves-movie-files-on-keyword.py
This script moves movie files into different folders based on certain keywords in the filename (e.g., genre or type).

### filter-by-year.py
This script filters movies from a directory based on their release year and sorts them accordingly.

## imdb-scraping.py

First install the IMDb library
```bash
pip install IMDbPY
```

This script scrapes movie metadata from IMDb (e.g., rating, genre, plot) and stores it in a CSV file for organizing and updating Plex content.

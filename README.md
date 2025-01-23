# python-movie-scripts
My python scripts to manage Plex movie server content. 
Automating tedious tasks like renaming, organizing, and syncing.

Ensure that the script is run in a directory where you have permission to rename files.

### rename-to-conventions.py
Batch Renaming Files (to match Plex naming conventions)
This script batch renames movie files to match the correct Plex naming conventions, which generally follow a format like: MovieName (Year).ext.

Example input

``` lua
TheMatrix1999.mkv
Inception2010.mp4
Avatar2009.avi
```

Example output

```lua
Renamed: TheMatrix1999.mkv -> TheMatrix (1999).mkv
Renamed: Inception2010.mp4 -> Inception (2010).mp4
Renamed: Avatar2009.avi -> Avatar (2009).avi
```
After running the script, your directory /path/to/your/movies will have the following renamed files

```lua 
TheMatrix (1999).mkv
Inception (2010).mp4
Avatar (2009).avi
```

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

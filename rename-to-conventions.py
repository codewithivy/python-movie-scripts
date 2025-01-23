import os
import re

def rename_movie_files(directory):
    for filename in os.listdir(directory):
        # Match the movie name and year from the filename
        match = re.match(r"(.*?)(\d{4})(.*)", filename)
        if match:
            movie_name = match.group(1).strip()
            year = match.group(2)
            extension = match.group(3)
            
            # Create a new filename with Plex naming convention
            new_filename = f"{movie_name} ({year}){extension}"
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_filename}")

# Set your directory path here
directory_path = "/path/to/your/movies"
rename_movie_files(directory_path)

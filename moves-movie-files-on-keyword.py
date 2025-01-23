import os
import shutil

def organize_movies_by_genre(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp4") or filename.endswith(".mkv"):  # Only process movie files
            genre = "Uncategorized"  # Default genre

            if "action" in filename.lower():
                genre = "Action"
            elif "comedy" in filename.lower():
                genre = "Comedy"
            elif "drama" in filename.lower():
                genre = "Drama"
            
            # Create a genre folder if it doesn't exist
            genre_folder = os.path.join(directory, genre)
            if not os.path.exists(genre_folder):
                os.makedirs(genre_folder)

            # Move the file into the genre folder
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(genre_folder, filename)
            shutil.move(old_file, new_file)
            print(f"Moved: {filename} -> {genre_folder}")

# Set your directory path here
directory_path = "/path/to/your/movies"
organize_movies_by_genre(directory_path)

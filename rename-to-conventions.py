'''os is a module that provides functions to interact with the operating system, like listing files in a directory or renaming files.

re is a module for working with regular expressions, allowing pattern matching in strings.'''
import os
import re

'''This defines the function rename_movie_files which takes a directory as an argument. This directory is where the movie files are located.'''

def rename_movie_files(directory):
    '''# Iterating Through Files,This loop goes through each file in the specified directory using os.listdir(directory)'''
    for filename in os.listdir(directory): 
        # Match the movie name and year from the filename
        # The pattern (.*?)(\d{4})(.*) breaks the filename into three parts
        match = re.match(r"(.*?)(\d{4})(.*)", filename)
        #any character except newline, 0 or more preceding characters, ? makes the * non greedy for regex from consuming too many charcters

        '''if match extract the first part of the filename(movie name) and strip() removes any leading trailing spaces, year extracts 4 digit year, extension: Extracts the remaining part of the filename (e.g., .mp4)'''
        if match:
            movie_name = match.group(1).strip()
            year = match.group(2)
            extension = match.group(3)

            '''This creates the new filename in the Plex naming convention format: MovieName (2022).mp4.'''
            # Create a new filename with Plex naming convention
            new_filename = f"{movie_name} ({year}){extension}" #This line creates a new filename by using an f-string to format a string. 
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_filename}")

# Set your directory path here
directory_path = "/path/to/your/movies"
rename_movie_files(directory_path)

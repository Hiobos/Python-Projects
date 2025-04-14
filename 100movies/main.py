import requests
from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/').text

soup = BeautifulSoup(response, 'html.parser')

movie_title = soup.select('h3', class_='title')

movie_list = [movie.string.split(')') for movie in movie_title]
movie_list = [movie.string.split(':') for movie in movie_title]

movie_list = list(reversed(movie_list))

with open('movies.txt', 'w') as movies_file:
    for b in range(0, len(movie_list) - 1):
        movies_file.writelines(f"{movie_list[b][0]}\n")
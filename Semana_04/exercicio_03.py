def list_movies():
    movies = {
    'Carros' : {'villain_name' :'Ferrugem', 'release_year' : '2006'},
    'Toy Story' : {'villain_name' : 'Zurg', 'release_year' : '1995'},
    'Harry Potter' : {'villain_name' : 'Voldemort', 'release_year' : '2001'},
    'O Poderoso Chefão' : {'villain_name' : 'Michael Corleone', 'release_year' : '1972'},
    'Procurando Nemo' : {'villain_name' : 'Tubarão', 'release_year' :'2003'}
    }
    return movies

def main():
    movies = list_movies()
    for movie_name, info_movies in movies.items():
        villain_name = info_movies['villain_name']
        release_year = info_movies['release_year']
        print(f"Nome do filme: {movie_name} - Vilão: {villain_name} - Ano/Lançamento: {release_year}")
main()
import datetime

def add_movie(movies):
    movie_name = input("Enter movie name: ")
    movie_actors = []
    actor = ''
    while actor != '0':
        actor = input("Enter actor name, when done enter 0: ")
        if actor != '0':
            movie_actors.append(actor)
    movies[movie_name] = {'actors':movie_actors,'Rating':5.0}
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    movie_added_time = f"{current_time} - added movie"
    with open("timed_log.txt", 'a+') as file:
        if file.read(1) != None :
            file.write('\n')
        file.write(movie_added_time)
    with open("timed_log.txt", 'r') as file:
        content = file.read()
        print("all movies added time: ")
        print(content)
    return movies

movies = {'Extraction':{'actors':['Chris Hemsworth','Rudhraksh Jaiswal'],'Rating':8.7}}
print(movies)
print(add_movie(movies))
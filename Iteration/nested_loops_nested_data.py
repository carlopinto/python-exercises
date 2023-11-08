def filter_list(filter, data):
    list = []
    for (element, subjects) in data:
        if filter in subjects:
            list.append(element)
    return list

students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

input_subject = input("Enter a subject and I will tell you who is enrolled for it: ")

enrolled = filter_list(input_subject, students)

print("The number of students taking", input_subject, "is", len(enrolled))
print("The students are", enrolled)

movies = [
    ("title1", ["actor1", "actor2", "actor3"]),
    ("title2", ["actor1", "actor4", "actor5"]),
    ("title3", ["actor5", "actor6", "actor7"]),
    ("title4", ["actor1", "actor2", "actor7"]),
    ("title5", ["actor1", "actor3", "actor5"]),
    ("title6", ["actor1", "actor6", "actor7", "actor8"])]

input_actor = input("Enter the name of an actor and I will tell you which movies he/she has acted for: ")

actor_movies = filter_list(input_actor, movies)

print("The number of movies starring", input_actor, "is", len(actor_movies))
print("The movies are", actor_movies)
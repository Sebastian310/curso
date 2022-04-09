DATA = [                                               #esto es una constante:lista de diccionarios
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
#list and dicts comprehensions
#     all_python_devs=[worker["name"]for worker in DATA if worker["language"] == "python"]   #worker, nombre que le voy a poner a cada uno de los diccionarios internos de la lista #de worker quiero el contenido de la llave "name" de DATA 
#     all_platzi= [platzi["name"] for platzi in DATA if platzi["organization"] == "Platzi"]  #para filtrar solo los empleados
    
# #high order funtions "filter" y "Map"
#     adults = list(filter(lambda worker: worker["age"] > 18,DATA)) 
#     adults= list(map(lambda worker: worker["name"],adults))

#     old_people= list(map(lambda worker: worker | {"old":worker["age"] > 70},DATA)) 


#RETO high order funtions "función que recibe como parámetro otra función"

    # python_devs=list(filter(lambda worker:worker["language"]=="python",DATA))
    # python_devs=list(map(lambda worker:worker["name"],python_devs))
    # for worker in python_devs:
    #     print(worker)


    # only_platzi=list(filter(lambda platzi:platzi["organization"]=="Platzi",DATA))
    # only_platzi=list(map(lambda platzi:platzi["name"],only_platzi))  
    # for platzi in only_platzi:
    #     print(platzi)

#RETO list and dicts comprehensions
    adult=[employee["name"] for employee in DATA if employee["age"]>18 ]
    for employee in adult:
        print(employee)



    # for worker in all_python_devs:
    #     print(worker)

    # for platzi in all_platzi:
    #     print(platzi)    

    # for worker in adults:
    #     print(worker)    

    # for worker in old_people:
    #       print(worker)

if __name__=="__main__":
    run()
def run():
    my_list= [1,"Hello",True,4.5]    #los elementos de una lista se separan con comas (,)
    my_dict= {"firstname":"Sebas","lastname":"orrego"}
   
    super_list= [
        {"firstname":"Sebas","lastname":"orrego"},
        {"firstname":"Pepe","lastname":"Yepez"},
        {"firstname":"José","lastname":"Martinez"},
        {"firstname":"Carlos","lastname":"Ososrio"},
    ]

    super_dict= {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.4,4.5,6.43]
    }
    for key,valor in super_dict.items():
        print(key,"=",valor)

    
    for value in super_list:
        print(value["firstname"],"-",value["lastname"])      
  





if __name__=="__main__":
    run()
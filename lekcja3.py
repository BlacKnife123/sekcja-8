names = {"Arkadiusz", "Wioletta","Karol"}
numbers = [1,2,3]
celcius = {"t1":-20,'t2':-15,'t3':0}

namesLength = {
    name : len(name)
    for name in names
    if name.startswith("A")
}

multiply = {
    number : number**3
    for number in numbers
}

temperatureF = {
    key: temp*1.8+32
    for key,temp in celcius.items()
        
}


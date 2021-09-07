loop = 1

while (loop < 10):

    # Todas las preguntas que se le realiza al usuario para que las conteste
    noun = input("Selecciona un sustantivo: ")
    p_noun = input("Selecciona un sustantivo en plural: ")
    noun2 = input("Selecciona un sustantivo: ")
    place = input("Nombra un lugar: ")
    adjective = input("Selecciona un adjetivo (Describe una palabra): ")
    noun3 = input("Selecciona un sustantivo: ")

    # Displays the story based on the users input
    print ("------------------------------------------")
    print ("Sé amable con tu",noun,"- pies", p_noun)
    print ("Porque un pato puede ser de alguien", noun2,",")
    print ("Sea amable con su",p_noun,"en",place)
    print ("Donde siempre hace el tiempo",adjective,".")
    print ()
    print ("Puedes pensar que este es el",noun3,",")
    print ("Bueno, lo es")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1
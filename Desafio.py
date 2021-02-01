def calcula():
    print("Desafio de programação inicial")
    gal = float(input("Insira o volume do galão: "))
    garrafas = int(input("Insira a quantidade de garrafas de 2 a 4 garrafas: "))
    print("A quantidade de garrafas é {} ".format(garrafas))
    lt = "L"
    if garrafas < 2 or garrafas > 4:
        print("Digite entre 2 e 4")
        return calcula()
    elif garrafas == 2:
        v1 = float(input("Digite o volume da garrafa 1: "))
        v2 = float(input("Digite o volume da garrafa 2: "))
        final = (v1+v2)
        teste = gal - final
        print ("A Garrafa 1 tem : {}{}, A Garrafa 2 tem :{}{}, sobra {:.2f}{}".format(v1,lt,v2,lt, teste,lt))
    elif garrafas == 3:
        v1 = float(input("Digite o volume da garrafa 1: "))
        v2 = float(input("Digite o volume da garrafa 2: "))
        v3 = float(input("Digite o volume da garrafa 3: "))
        final = (v1+v2+v3)
        teste = gal - final
        print ("A Garrafa 1 tem :{}{},A Garrafa 2 tem : {}{}, A Garrafa 3 tem: {}{}, sobra {:.2f}{}".format(v1,lt,v2,lt,v3,lt, teste,lt))
    elif garrafas == 4:
        v1 = float(input("Digite o volume da garrafa 1: "))
        v2 = float(input("Digite o volume da garrafa 2: "))
        v3 = float(input("Digite o volume da garrafa 3: "))
        v4 = float(input("Digite o volume da garrafa 4: "))
        final = (v1+v2+v3+v4)
        teste = gal - final
        print ("A Garrafa 1 tem :{}{}, a Garrafa 2 tem :{}{}, a Garrafa 3 tem :{}{}, a Garrafa 4 tem :{}{}, {:.2f}{}".format(v1,lt,v2,lt,v3,lt,v4,lt, teste,lt))

calcula()

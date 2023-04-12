from pilhaEncadeada import Pile

rua = Pile()
print("Bem vindo ao programa da rua sem saida")
while True:
    print("1 - Adicionar Carro")
    print("2 - Ver Rua")
    print("3 - Verificar Carro")
    print("4 - Sair")
    inpt = input()
    if inpt == "1":
        car_plate = input("Digite a placa do carro")
        rua.insert(int(car_plate))
        print("Carro inserido")
    elif inpt == "2":
        if rua.size() == 0:
            print("Rua vazia")
        else:
            for i in range(rua.size()):
                if i == rua.size()-1:
                    print(rua.get_value_index(i))
                else:
                    print(str(rua.get_value_index(i))+"->",end="")
    elif inpt == "3":
        try:
            car_plate = int(input("Digite a placa do carro"))
            if rua.is_element_in_pile(car_plate):
                index_car = rua.get_index_value(car_plate)
                for i in range(index_car+1):
                    if i == index_car:
                        print(rua.get_index_value(i))
                    else:
                        print(str(rua.get_value_index(i))+"->",end="")
        except AssertionError:
            print("Carro nao esta na rua")
    elif inpt=="4":
        break
    else:
        print("Opçao invalida")


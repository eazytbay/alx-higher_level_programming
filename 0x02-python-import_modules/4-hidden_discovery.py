#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    nom = dir(hidden_4)
    for nom in nom:
        if nom[:2] != "__":
            print(nom)

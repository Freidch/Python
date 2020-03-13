import datetime

class animal :
    """
        Cette classe est la classe mère, toutes les classes filles
        héritent des attributs de cette classe
        
    """
    
    def __init__(self, name, age, sexe):
        self.name = name
        self.age = age
        self.sexe = sexe
        
    def __str__(self):
        return "Un " + self.name + " âgé(e) de " + self.age + "an(s) et c est un(e) " + self.sexe
class Farm :

    def __init__(self, name):
        self.name = name
        self.Farm_animals = []
 
    def __str__(self):
        
        out = "Nous avons dans cette ferme\n"    
        for my_key in self.Farm_animals:
            out += str(my_key)+"\n"
            out += "_____________________\n"
            
        return out


if __name__ == "__main__":
    
    Farm_list = []
    Farm_list.append(Farm("Première ferme"))
    Farm_list.append(Farm("Deuxième ferme"))
    Farm_list.append(Farm("Troisième ferme"))
    Farm_list[0].Farm_animals.append(animal("Brebis", "2", "femelle"))
    Farm_list[0].Farm_animals.append(animal("Coq", "1", "mâle"))
    Farm_list[0].Farm_animals.append(animal("Poule", "7", "femelle"))
    Farm_list[1].Farm_animals.append(animal("Lion", "4", "mâle"))
    Farm_list[1].Farm_animals.append(animal("Lynx", "2", "mâle"))
    Farm_list[1].Farm_animals.append(animal("Tigre", "4", "femelle"))
    Farm_list[2].Farm_animals.append(animal("Chien", "3", "mâle"))
    Farm_list[2].Farm_animals.append(animal("Chat", "8", "mâle"))
    Farm_list[2].Farm_animals.append(animal("Hamster", "1", "mâle"))
    
    requette = int(input("Vous sélectionnez quelle ferme ?\n"))
    print(Farm_list[requette])
    

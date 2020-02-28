import sys

def write(file_name):
    fichier = open(file_name, "w+")
    fichier.write("Bonjour")
    fichier.close();

def read(file_name):
    fichier = open(file_name, "r")
    l = fichier.read()
    print (l)
    fichier.close();

if __name__ == "__main__":
    file_name = input(sys.argv[0])
    write(file_name)
    read(file-name)
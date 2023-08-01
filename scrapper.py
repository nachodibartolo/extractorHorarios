from bs4 import BeautifulSoup
import os


def limpiarArch():
    lines_seen = set() # holds lines already seen
    outfile = open("tempord.txt", "w")
    for line in open("tempdes.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    os.remove("tempdes.txt")
    outfile.close()


def guardar(f, n):
    for i in range(int(n)):
        nombreMat = input("Ingrese el codigo de la materia: ")
        with open("siu.html", "r", encoding="UTF-8") as html_file:
            content = html_file.read()
        soup = BeautifulSoup(content, "lxml")

        materia = soup.find('div', attrs={"actividad" : nombreMat})
        clases = materia.find_all("table", attrs={"sede" : "1"})
        print("\n\n", nombreMat, "\n")
        c=0
        for comision in clases:
            codigo = comision.find("h5")
            infocom = comision.find_all("tr", class_="js-dia")
            print(codigo.text)

            for casilla in infocom:

                tipo = casilla.select("td")[0].text.replace("\n", "").replace("\t", "").replace(" ", "")
                dia = casilla.select("td")[1].text.replace("\n", "").replace("\t", "").replace(" ", "")
                hora = casilla.select("td")[2].text.replace("\n", "").replace("\t", "").replace(" ", "").replace("a", ",").replace(":", ".")

                print("\n\t", tipo, dia, hora, "\n\n")
                f.write(" " + nombreMat + ";" + codigo.text + ";" + tipo + "," + dia + "," + hora + "\n")
            c+=1
    


        
            
def main():

    n = input("Ingrese la cantidad de materias: ")
    matriz = [["" for i in range(int(n))] for i in range(int(n))]
    f = open("tempdes.txt", "w")
    guardar(f, n)
    f.close()
    limpiarArch()



main()


from bs4 import BeautifulSoup

x = input("Ingrese el codigo de la materia: ")

with open("siu.html", "r", encoding="UTF-8") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")
    
    materia = soup.find('div', attrs={"actividad" : x})

    clases = materia.find_all("table", attrs={"sede" : "1"})
    for comision in clases:
        codigo = comision.find("h5")
        infocom = comision.find_all("tr", class_="js-dia")
        #print(infocom)
        print(codigo)
        for casilla in infocom:
            tipo = casilla.select("td")[0].text.replace("\n", "").replace("\t", "").replace(" ", "")
            dia = casilla.select("td")[1].text.replace("\n", "").replace("\t", "").replace(" ", "")
            hora = casilla.select("td")[2].text.replace("\n", "").replace("\t", "").replace(" ", "")
            print("\n\t", tipo, dia, hora, "\n\n")
        
        
        
        #print(codigo,infocom)
        #print("--------------------------------------------------")

    
    
    
    
    
    #for materia in materias:
        #sede = materia.find("table", attrs={"sede" : "1"})
            #for row in comision:
                #row = comision.find("td").text
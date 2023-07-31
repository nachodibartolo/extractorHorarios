
from bs4 import BeautifulSoup

with open("hrhs.html", "r", encoding="UTF-8") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")
    
    materia = soup.find('div', attrs={"actividad" : "Álgebra y Geometría (GMA0126)"})

    clases = materia.find_all("table", attrs={"sede" : "1"})
    for comision in clases:
        codigo = comision.find("h5")
        infocom = comision.find("tr", class_="js-dia")
        tipo = infocom.select("td")[0].text.replace("\n", "").replace("\t", "").replace(" ", "")
        dia = infocom.select("td")[1].text.replace("\n", "").replace("\t", "").replace(" ", "")
        hora = infocom.select("td")[2].text.replace("\n", "").replace("\t", "").replace(" ", "")
        print(codigo.text,"\n\t", tipo, dia, hora, "\n\n")
        
        
        
        #print(codigo,infocom)
        #print("--------------------------------------------------")

    
    
    
    
    
    #for materia in materias:
        #sede = materia.find("table", attrs={"sede" : "1"})
            #for row in comision:
                #row = comision.find("td").text
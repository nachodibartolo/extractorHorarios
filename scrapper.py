
from bs4 import BeautifulSoup

with open("hrhs.html", "r", encoding="UTF-8") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")
    materia = soup.find('div', attrs={"actividad" : "Álgebra y Geometría (GMA0126)"})
    for mat in materia:
        dia = mat.find('th', attrs={"class" : "dia"})
    print(dia)

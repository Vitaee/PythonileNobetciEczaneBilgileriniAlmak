from bs4 import BeautifulSoup
import requests

class Eczane:
    def __init__(self):
        self.eczaneIsim = []
        self.eczaneSokak = []
        self.EczaneTel = []
        self.EczaneSaat = []
        self.url = "http://www.kteb.org/kibris-turk-eczacilar-birligi-nobetci-eczane/5_Lefko%C5%9Fa"

        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def VeriCek(self):
        for veri in self.soup.find_all('div', class_='rc-info'):
            for isim in veri.find_all('h4'):
                self.eczaneIsim.append(isim.text)

        print(self.eczaneIsim)

        for veri in self.soup.find_all('div', class_= 'rc-info'):
            for sokak in veri.find('p'):
                if len(sokak) < 32:
                    pass
                else:
                    self.eczaneSokak.append(sokak)

        print(self.eczaneSokak)

        for veri in self.soup.find_all('div', class_= 'rc-info'):
            for saat in veri.find_all('p')[-1]:
                if len(saat) < 29:
                    pass
                else:
                    self.EczaneSaat.append(saat)
        print(self.EczaneSaat)

        for veri in self.soup.find_all('div', class_= 'rc-info'):
            for telno in veri.find_all('p')[-2]:
                if len(telno) < 10:
                    pass
                else:
                    self.EczaneTel.append(telno)
        print(self.EczaneTel)
eczane = Eczane()
eczane.VeriCek()

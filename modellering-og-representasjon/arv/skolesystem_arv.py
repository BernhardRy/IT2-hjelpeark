class Bruker():
    """Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
    
    """
    def __init__(self, epost, fornavn, etternavn) -> None:
        self.epost = epost
        self.fornavn = fornavn
        self.etternavn = etternavn

    def logg_inn(self):
        print(f"{self.epost} logget inn")

    def logg_ut(self):
        print(f"{self.epost} logget ut")
    
class Lærer(Bruker):
    def __init__(self, epost, fornavn, etternavn, lønnskonto) -> None:
        super().__init__(epost, fornavn, etternavn)
        self.lønsskonto = lønnskonto

class Kontaktlærer(Lærer):
    """Superklasse for Kontaktlærer i skolesystemet.

    Attributes:
        epost: En string med kontaktlærerens epost
        fornavn: En string med kontaktlærerens fornavn
        etternavn: En string med kontaktlærerens etternavn
        lønnskonto: En string med kontaktlærerens lønnskonto nummer
        klasse: En string med kontaktlærerens klasse
        trinn: En string med kontaktlærerens trinn
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto, klasse, trinn) -> None:
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.klasse = klasse
        self.klasser = trinn

class Faglærer(Lærer):
    def __init__(self, epost, fornavn, etternavn, lønnskonto) -> None:
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.kompetanse = []
        self.klasser = []

class Elev(Bruker):
    def __init__(self, epost, fornavn, etternavn, trinn, klasse, fag):
       super().__init__(epost, fornavn, etternavn)
       self.trinn = trinn
       self.klasse = klasse
       self.fag = fag

# Denne brukes for testing, betyr at koden inne i if-setningen 
# kun kjører hvis vi "trykker play" på denne filen eller kjører denne fila i terminalen
if __name__ == "__main__":
    ravi = Lærer("ravim@viken.no", "David Ravi", "Manikarnika", 970034056554)
    ravi.logg_inn()
    
    Bernhard = Elev("bernhardry@viken.no", "Bernhard", "Rynning", "3", "stf", "IT2")
    Bernhard.logg_inn()
    Bernhard.logg_ut()


       
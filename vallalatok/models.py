from django.db import models
from django.core.validators import RegexValidator

UTCA = 'uc'
UT = 'út'
SUGARUT = 'sg'
FASOR = 'fs'
TER = 'tr'
KOZ = 'kz'
kozterulet_tipusok = (
    (UTCA, 'utca'),
    (UT, 'út'),
    (SUGARUT, 'sugárút'),
    (FASOR, 'fasor'),
    (TER, 'tér'),
    (TER, 'köz'),
)


def length_validator_creator(length):
    return RegexValidator(
        regex='^\d{{{length}}}$'.format(length=length),
        message='It must have {length} digits. (Only digits).'.format(
            length=length),
        code='nomatch')


validator_4_length = length_validator_creator(4)
validator_9_length = length_validator_creator(9)


class Telepules(models.Model):
    nev = models.CharField(max_length=100)
    megyek = (
        "Budapest", "Pest", "Fejér", "Komárom-Esztergom",
        "Veszprém", "Győr-Moson-Sopron", "Vas", "Zala",
        "Baranya", "Somogy", "Tolna", "Borsod-Abaúj-Zemplén",
        "Heves", "Nógrád", "Hajdú-Bihar",
        "Jász-Nagykun-Szolnok", "Szabolcs-Szatmár-Bereg",
        "Bács-Kiskun", "Békés", "Csongrád",
    )
    FEJER = megyek.index("Fejér")
    megye = models.IntegerField(
        "megye",
        choices=list(enumerate(megyek)),
        null=True,
    )
    min_iranyitoszam = models.IntegerField()
    max_iranyitoszam = models.IntegerField()

    def __str__(self):
        return self.nev


class TermeloVallalat(models.Model):
    KUJ = models.CharField(
        "Környezetvédelmi Ügyfél Jel",
        max_length=9,
        validators=[validator_9_length]
    )
    KSH = models.CharField(
        "KSH statisztikai számjel",
        max_length=17,
        validators=[length_validator_creator(17)],
        help_text="Csak a számjegyeket írja be,"
                  "a kötőjeleket ne.",
    )
    nev = models.CharField("vállalat neve", max_length=100)
    iranyitoszam = models.CharField(
        "irányítószám",
        max_length=4,
        validators=[validator_4_length]
    )
    telepules = models.ForeignKey(Telepules)
    kozterulet_nev = models.CharField("közterület neve", max_length=200)
    kozterulet_tipus = models.CharField(
        "közterület típusa",
        max_length=2,
        choices=kozterulet_tipusok,
        default=UTCA)
    hazszam = models.CharField("házszám", max_length=30)

    def __str__(self):
        return self.nev


class Telephely(models.Model):
    KTJ = models.CharField(
        "Környezetvédelmi Területi Jel",
        max_length=9,
        validators=[validator_9_length]
    )
    nev = models.CharField("neve", max_length=100)
    tipus = models.CharField(
        "típusa", choices=(("T", "termelő"),),
        max_length = 1,
    )
    iranyitoszam = models.CharField(
        "irányítószám",
        max_length=4,
        validators=[validator_4_length]
    )
    telepules = models.ForeignKey(Telepules)
    kozterulet_nev = models.CharField("közterület neve", max_length=200)
    kozterulet_tipus = models.CharField(
        "közterület típusa",
        max_length=2,
        choices=kozterulet_tipusok,
        default=UTCA)
    hazszam = models.CharField("házszám", max_length=30)
    foglalkoztatottak_szama = models.IntegerField("foglalkoztatottak száma")
    felelos_nev = models.CharField("felelős személy neve", max_length=200)
    felelos_beosztas = models.CharField(
        "felelős személy beosztása",
        max_length=30)

    def __str__(self):
        return "{} {}".format(self.KTJ, self.ne)


class Tevekenyseg:
    telephely = models.ForeignKey(Telephely)
    TEAOR = models.CharField(
        "TEÁOR szám",
        max_length=4,
        validators=[validator_4_length]
    )

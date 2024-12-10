from django.db import models
from django.urls import reverse

# Create your models here.

# ------------------------------- LIEFERANT ---------------------------------
class Lieferant(models.Model):
    name = models.CharField(("Name"), max_length=50)
    email = models.CharField(("E-Mail"), max_length=50)
    telefon = models.CharField(("Telefonnummer"), max_length=50)    

    class Meta:
        verbose_name = ("Lieferant")
        verbose_name_plural = ("Lieferanten")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Lieferant_detail", kwargs={"pk": self.pk})


# ------------------------------- LIEFERUNG ------------------------------
class Lieferung(models.Model):
    datum = models.DateField(("Lieferdatum"), auto_now=False, auto_now_add=False)
    lieferant = models.ForeignKey("Lieferant", verbose_name=("Lieferant"), on_delete=models.RESTRICT)
  
    class Meta:
        verbose_name = ("Lieferung")
        verbose_name_plural = ("Lieferungen")

    def __str__(self):
        return f"{self.datum}/{self.lieferant}"

    def get_absolute_url(self):
        return reverse("Lieferung_detail", kwargs={"pk": self.pk})



# ------------------------------- ARTIKEL ---------------------------------
class Artikel(models.Model):
    mindestbestand = models.IntegerField(("Mindestbestand"))
    bezeichnung = models.CharField(("Bezeichnung"), max_length=250)
    liefereinheit = models.CharField(("Liefereinheit"), max_length=50)
    bemerkung = models.TextField(("Bemerkung"), null=True, blank=True)
    ekpreis = models.IntegerField(("Einkaufspreis in Cent"))

    class Meta:
        verbose_name = ("Artikel")
        verbose_name_plural = ("Artikel")

    def __str__(self):
        return self.bezeichnung

    def get_absolute_url(self):
        return reverse("Artikel_detail", kwargs={"pk": self.pk})


# ----------------------------- LIEFERPOSITION -------------------------------
class Lieferposition(models.Model):
    artikel = models.ForeignKey(Artikel, verbose_name=("Artikel"), on_delete=models.CASCADE)
    lieferung = models.ForeignKey(Lieferung, verbose_name=("Lieferung"), on_delete=models.CASCADE)
    verkaufspreis = models.IntegerField(("Verkaufspreis in €-Cent"))
    menge = models.IntegerField(("Anzahl"))


    class Meta:
        verbose_name = ("Lieferposition")
        verbose_name_plural = ("Lieferposition")

    def __str__(self):
        return f"{self.artikel} - {self.lieferung}"

    def get_absolute_url(self):
        return reverse("Lieferposition_detail", kwargs={"pk": self.pk})


# ----------------------------- Lagerplatz  -------------------------------
class Lagerplatz(models.Model):
    bestand = models.IntegerField(("Bestand"))
    artikel = models.ForeignKey(Artikel, verbose_name=("Artikel"), on_delete=models.CASCADE)
    bezeichnung = models.CharField(("Bezeichnung"), max_length=50)
    
    class Meta:
        verbose_name = ("Lagerplatz")
        verbose_name_plural = ("Lagerplätze")

    def __str__(self):
        return f"{self.bezeichnung} - {self.artikel} ({self.bestand} {self.artikel.liefereinheit})"

    def get_absolute_url(self):
        return reverse("Lagerplatz_detail", kwargs={"pk": self.pk})

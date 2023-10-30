from django.db import models

# Create your models here.

class Bangle(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Bangle')

    def __str__(self):
        return self.name

class Chain(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Chain')

    def __str__(self):
        return self.name

class Bracelets(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Bracelets')

    def __str__(self):
        return self.name

class Couple(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Couple')

    def __str__(self):
        return self.name

class Earrings(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Earrings')

    def __str__(self):
        return self.name

class Coin(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Coin')

    def __str__(self):
        return self.name

class Mangalsutra(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Mangalsutra')

    def __str__(self):
        return self.name

class Neckwear(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Neckwear')

    def __str__(self):
        return self.name

class Nosepin(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Nosepin')

    def __str__(self):
        return self.name

class Set(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Set')

    def __str__(self):
        return self.name

class Ring(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Ring')

    def __str__(self):
        return self.name

class Pendant(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Pendant')

    def __str__(self):
        return self.name

class Anklet(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Anklet')

    def __str__(self):
        return self.name

class Ban(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Ban')

    def __str__(self):
        return self.name

class Brace(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Brace')

    def __str__(self):
        return self.name

class Co(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Co')

    def __str__(self):
        return self.name

class Ear(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Ear')

    def __str__(self):
        return self.name

class Neck(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Neck')

    def __str__(self):
        return self.name

class Pen(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Pen')

    def __str__(self):
        return self.name

class Ri(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Ri')

    def __str__(self):
        return self.name

class Diamond(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Diamond')

    def __str__(self):
        return self.name

class Men(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Men')

    def __str__(self):
        return self.name

class Women(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Women')

    def __str__(self):
        return self.name

class Kid(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Kid')

    def __str__(self):
        return self.name


class Product(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Product')


    def __str__(self):
        return self.name
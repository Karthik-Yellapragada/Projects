from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class Local_news(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class National_news(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class International_news(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class Movies(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class Shows(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class Kdrama(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class car_mov(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class desi_car(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class anime(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'


class Games(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    link = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
        app_label = 'myapp'

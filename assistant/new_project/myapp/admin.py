from django.contrib import admin
from .models import Destination
from .models import Local_news
from .models import National_news
from .models import International_news
from .models import Movies
from .models import Shows
from .models import Games
from .models import Kdrama
from .models import desi_car
from .models import car_mov
from .models import anime

# Register your models here.
admin.site.register(Destination)
admin.site.register(Local_news)
admin.site.register(National_news)
admin.site.register(International_news)
admin.site.register(Movies)
admin.site.register(Shows)
admin.site.register(Kdrama)
admin.site.register(anime)
admin.site.register(car_mov)
admin.site.register(desi_car)
admin.site.register(Games)

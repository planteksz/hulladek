from django.contrib import admin
from .models import Vezeto
from .models import Telepules
from .models import TermeloVallalat
from .models import Telephely
#from .models import Tevekenyseg

# Register your models here.
admin.site.register(Vezeto)
admin.site.register(Telepules)
admin.site.register(TermeloVallalat)
admin.site.register(Telephely)
#admin.site.register(Tevekenyseg)


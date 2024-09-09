

# Register your models here.
from django.contrib import admin



from .models import sched #model name

admin.site.register(sched)


from .models import teacher #model name

admin.site.register(teacher)

from .models import classs #model name

admin.site.register(classs)


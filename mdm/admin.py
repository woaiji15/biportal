from django.contrib import admin

# Register your models here.

from .models import Company 
from .models import Department 
from .models import Position 
from .models import Employee 
from .models import Org_Relation 
from .models import Job_Data 
from .models import Probation_Data 
from .models import Dept_Supervisor 
from .models import Conf 


admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Org_Relation)
admin.site.register(Job_Data)
admin.site.register(Probation_Data)
admin.site.register(Dept_Supervisor)
admin.site.register(Conf)

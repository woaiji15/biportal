from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route


from mdm.serializers import CompanySerializer
from mdm.serializers import DepartmentSerializer
from mdm.serializers import PositionSerializer
from mdm.serializers import EmployeeSerializer
from mdm.serializers import Org_RelationSerializer
from mdm.serializers import Job_DataSerializer
from mdm.serializers import Probation_DataSerializer
from mdm.serializers import Dept_SupervisorSerializer
from mdm.serializers import ConfSerializer

from mdm.models import Company 
from mdm.models import Department 
from mdm.models import Position 
from mdm.models import Employee 
from mdm.models import Org_Relation 
from mdm.models import Job_Data 
from mdm.models import Probation_Data  
from mdm.models import Dept_Supervisor
from mdm.models import Conf

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    #/mdm/companies/22/?format=json
    #/mdm/companies/?format=json
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #mdm/companies/21/changeName/?newName=xxxx
    '''
    @detail_route()
    def changeName(self, request, *args, **kwargs):
        get = request.GET
        company = self.get_object()
        company.name = get.get('newName')
        company.save()

        return Response(company.name)

    @list_route()
    def filterCompanies(self, request):
        companies = Company.objects.filter(short_name='浙圣')
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)

    '''	
class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
	
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
	
class Org_RelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Org_Relation.objects.all()
    serializer_class = Org_RelationSerializer
	
class Job_DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Job_Data.objects.all()
    serializer_class = Job_DataSerializer

class Probation_DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Probation_Data.objects.all()
    serializer_class = Probation_DataSerializer
	
class Dept_SupervisorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Dept_Supervisor.objects.all()
    serializer_class = Dept_SupervisorSerializer
	
class ConfViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Conf.objects.all()
    serializer_class = ConfSerializer


from .models import Company 
from .models import Department 
from .models import Position 
from .models import Employee 
from .models import Org_Relation 
from .models import Job_Data 
from .models import Probation_Data  
from .models import Dept_Supervisor
from .models import Conf
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    '''
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField(required=True, allow_blank=False, max_length=40)
    name = serializers.CharField(required=True, allow_blank=False, max_length=200)
    short_name = serializers.CharField(required=False, allow_blank=True, max_length=200)
    parent_company_key = serializers.IntegerField(required=False)
    head_of_company_key = serializers.IntegerField(required=False)
    status = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.short_name = validated_data.get('short_name', instance.short_name)
        instance.parent_company_key = validated_data.get('parent_company_key', instance.parent_company_key)
        instance.head_of_company_key = validated_data.get('head_of_company_key', instance.head_of_company_key)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    '''
    class Meta:
        model = Company 
        fields = ('url', 'id', 'key', 'code', 'name', 'short_name', 'parent_company_key', 'head_of_company_key', 'status','created_job','created_tr','created_date')
		
class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department 
        fields = ('url', 'id', 'key', 'code', 'name', 'short_name', 'parent_dept_key', 'parent_dept_key', 'head_of_dept_key','base_key','cost_center','status','created_job','created_tr','created_date')

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position 
        fields = ('url', 'id', 'key', 'code', 'name', 'dept_key', 'job_key', 'pos_series_key', 'job_grade_key','job_rank_key','parent_pos_key','key_pos_flag','status','created_job','created_tr','created_date')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position 
        fields = ('url', 'id', 'key', 'code', 'name', 'sex', 'nationality_key', 'birthday', 'work_start_date','id_number','id_card_expiry_date','political_status_key','marital_staus_key','native_place_key','household_type_key','permanent_residence','address','private_emial','company_email','telephone','mobile','emergency_contact','emergency_contact_phone','recruitment_type_key','labour_union_flag','mutual_fund_flag','biz_card_dept_cn','biz_card_dept_en','biz_card_pos_cn','biz_card_pos_en','status','created_job','created_tr','created_date')
	
class Org_RelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position 
        fields = ('url', 'id', 'key', 'empl_id', 'previous_serving_age', 'serving_age', 'start_date', 'end_date','join_company_date','last_work_day','last_flag','created_job','created_tr','created_date')
		
class Job_DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position 
        fields = ('url', 'id', 'key', 'dept_key', 'company_key', 'empl_key', 'org_relation_key', 'dept_l2', 'dept_l3','dept_l4','dept_l5','dept_l6','pos_series_key','parent_pos_key','job_key','job_grade_key','job_rank_key','job_rank_key','empl_type_key','empl_status_key','start_date','end_date','supervisor_key','team_leader_key','work_city_key','action','transfer_type_key','resign_apply_date','action_reason_key','seq','last_flag','created_job','created_tr','created_date')
		
class Probation_DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position 
        fields = ('url', 'id', 'key', 'empl_key', 'job_data_key', 'start_date', 'expected_end_probation_date', 'actual_end_probation_date', 'probation_reason','probation_result','created_job','created_tr','created_date')
		
class Dept_SupervisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position 
        fields = ('url', 'id', 'key', 'dept_key', 'supervisor_key','created_job','created_tr','created_date')
				
class ConfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position 
        fields = ('url', 'id', 'key', 'code', 'name', 'short_name', 'scope','created_job','created_tr','created_date')



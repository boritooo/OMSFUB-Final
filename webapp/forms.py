from django import forms # type: ignore
from .models import Employee, OrgChartList, Post, UserData, Equipment, Availability, Comlab
from .models import Ins_Schedule
import datetime  # Add this import

class Dtrc(forms.Form):
    image  = forms.ImageField(label='Profile Picture', required=False)
    name = forms.CharField()

class EditEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'middle_name', 'last_name', 'birthday', 'age', 'status', 'position', 'organization']

    STATUS_CHOICES = [
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Permanent', 'Permanent'),
    ]

    POSITION_CHOICES = [
        ('Instructor 1', 'Instructor 1'),
        ('Instructor 2', 'Instructor 2'),
        ('Instructor 3', 'Instructor 3'),
    ]

    ORGANIZATION_CHOICES = [
        ('Chairperson,DCS', 'Chairperson,DCS'),
        ('Program Chair,CS', 'Program Chair,CS'),
        ('Program Chair, IT', 'Program Chair, IT'),
        ('Instructor', 'Instructor'),
        ('Head, LMS', 'Head, LMS'),
        ('Head, DCS RDE', 'Head, DCS RDE'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    position = forms.ChoiceField(choices=POSITION_CHOICES, required=True)
    organization = forms.ChoiceField(choices=ORGANIZATION_CHOICES, required=True)

class ListofstaffForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['idNum', 'first_name', 'last_name', 'middle_name', 'birthday', 'status', 'position', 'profile','age', 'gender','organization', 'fingerprint_id', 'backup_fingerprint_id','password']

class OrgChartListForm(forms.ModelForm):
    class Meta:
        model = OrgChartList
        fields = '__all__' 

class ListofstaffForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['idNum', 'first_name', 'last_name', 'middle_name', 'birthday', 'age', 'status', 'position', 'profile', 'gender', 'organization', 'fingerprint_id', 'backup_fingerprint_id', 'password']

class TimeRecordForm(forms.Form):
    idNum = forms.CharField(max_length=20)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'image']

class SuperUserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'equipment', 'date', 'status']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['name', 'status']
        widgets = {
            'status': forms.Select(choices=Availability.STATUS_CHOICES)
        }

class AvailabilityEditForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['name', 'status']
        widgets = {
            'status': forms.Select(choices=Availability.STATUS_CHOICES)
        }

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'  # List the fields you want to include in the form

class ScheduleForm(forms.ModelForm):
    DAYS_CHOICES = [
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('TH', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday'),
        ('SU', 'Sunday'),
    ]

    days = forms.MultipleChoiceField(choices=DAYS_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Ins_Schedule
        fields = ['subject_code', 'subject', 'section', 'days', 'time', 'end_time', 'room']  
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_days(self):
        days = self.cleaned_data.get('days')
        return ''.join(days)  # Convert list of days to a concatenated string

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if isinstance(time, datetime.time):
            return time.isoformat()
        return time

    def clean_end_time(self):
        end_time = self.cleaned_data.get('end_time')
        if isinstance(end_time, datetime.time):
            return end_time.isoformat()
        return end_time
    
class ComlabForm(forms.ModelForm):
    class Meta:
        model = Comlab
        fields = ['comlab', 'cards']
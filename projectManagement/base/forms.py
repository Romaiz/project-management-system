from django import forms
from .models import Project

class CreateProjectForm(forms.ModelForm):
  projName = forms.CharField(label="Name", max_length=50)
  projDesc = forms.CharField(label="Description", required=False, widget=forms.Textarea)
  Status_choices = [('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Overdue', 'Overdue'), ('Inactive', 'Inactive')]
  projStatus = forms.ChoiceField(label="Status", choices=Status_choices)
  dueDate = forms.DateTimeField(label="Due Date", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
  endDate = forms.DateTimeField(label="End Date", required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
  
  
  class Meta:
    model = Project
    fields = ('projName', 'projDesc','dueDate','endDate','projStatus',)

class ManageProjectForm(forms.Form):
  Status_choices = [('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Overdue', 'Overdue'), ('Inactive', 'Inactive')]
  
  projStatus = forms.CharField(widget=forms.Select(choices=Status_choices))
  task_name = forms.CharField()
  task_desc = forms.CharField()
  taskStatus = forms.CharField(widget=forms.Select(choices=Status_choices))
  assigned_to = forms.CharField()
  project_availableHours = forms.IntegerField(min_value=0)
  effort_so_far = forms.IntegerField(min_value=0)
  budget_spent_so_far = forms.IntegerField(min_value=0)
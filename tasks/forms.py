from django import forms
from tasks.models import Task,TaskDetail
# Django Forms
# class TaskForm(forms.Form):
#     title = forms.CharField( max_length=150, required=True, label="Task Title")
#     description = forms.CharField(widget=forms.Textarea, label="Description")
#     due_date = forms.DateField(widget=forms.SelectDateWidget, label="Dadline Date")
#     assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[])

#     def __init__(self,*args, **kwargs):
#         employee = kwargs.pop('employee',[])
#         super().__init__(*args, **kwargs)
#         # self.fields['assigned_to'].choices = [(emp.id,emp.name) for emp in employee] // working mekanizon using lisat comprihenson
#         # face employee from db and show without list compriihanson 
#         emp_list = []
#         for emp in employee:
#             emp_list.append((emp.id,emp.name))
#         self.fields['assigned_to'].choices = emp_list

# Django mixin class for design forms fild

class StyleFormMixin:
    defultStyleClass = "w-full px-4 py-3 rounded-xl border border-slate-200 bg-white text-slate-800 placeholder-slate-400 focus:border-rose-500 focus:ring-4 focus:ring-rose-100 transition-all duration-200 outline-none"
    
    def applyFormStyle(self):
        for field_name,field in self.fields.items():
            if isinstance(field.widget, forms.DateInput):
                field.widget.attrs.update(
                    {
                        'class': self.defultStyleClass,
                        'type': 'date'
                    }
                )
            elif isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update(
                    {
                        'class':self.defultStyleClass,
                        'placeholder':f'Enter {field_name.lower().replace("_", " ")}'
                    }
                )
                print("Titel")
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update(
                    {
                        'class':self.defultStyleClass,
                        'placeholder':f'Enter {field_name.lower().replace("_", " ")} in details...',
                        'rows':4
                    }
                )
            elif isinstance(field.widget , forms.SelectDateWidget):
                field.widget.attrs.update(
                    {
                        'class':'px-3 py-2 rounded-lg border border-slate-200 focus:border-rose-500 focus:ring-4 focus:ring-rose-100 outline-none transition-all duration-200'
                    }
                )
            elif isinstance(field.widget , forms.Select):
                field.widget.attrs.update(
                    {
                         'class': "w-full px-4 py-3 rounded-xl border border-slate-200 bg-white text-slate-800 focus:border-rose-500 focus:ring-4 focus:ring-rose-100 transition-all duration-200"
                    }
                )
            
  

#Django model form
class TaskForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date','status']
        widgets = {
            'description':forms.Textarea(),
            'title':forms.TextInput(),
            'due_date':forms.DateInput(attrs={'type': 'date'}),
            'status':forms.Select()
        }
        
        # widgets = {
        #     'title':forms.TextInput(attrs={
        #         'class':"border-2 rounded-md border-gray-200 p-3 focus:border-rose-400 focus:ring-rose-500 w-full",
        #         'placeholder': 'Enter Task'
        #     }),
        #     'description':forms.Textarea(attrs={
        #         'class':"border-2 rounded-md border-gray-200 p-3 focus:border-rose-400 focus:ring-rose-500 w-full",
        #         'placeholder': 'Enter Task Details',
        #         'rows':5
        #     }),
        #     'due_date':forms.SelectDateWidget(attrs={
        #         'class':"border-2 rounded-md border-gray-200 p-3 focus:border-rose-400 focus:ring-rose-500 "
        #     })
        # }
    def __init__(self ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyFormStyle()

        
class TaskDetailsForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['assigned_to','priority','notes']
        widgets = {
            'assigned_to':forms.CheckboxSelectMultiple(),
            'priority':forms.Select(),
            'notes':forms.Textarea()
        }
        # mathod ragulason order Or MRO systemm e calld
    def __init__(self ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyFormStyle()
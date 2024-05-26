from django import forms

JOBS = (
    ('python', 'Developpeur Python'),
    ('javascript', 'Dev JS'),
    ('java', 'Dev Java'),
    ('c++', 'Dev C++'),
    ('c#', 'Dev C#'),
)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    pseudo = forms.CharField(max_length=30, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    cgu_accept = forms.BooleanField(initial=True)
    jobs = forms.ChoiceField(choices=JOBS)
    
    def clean_pseudo(self):
        pseudo = self.cleaned_data['pseudo']
        if "$" in pseudo:
            raise forms.ValidationError('desole ce pseudo contient $')
        return pseudo
    
from django import forms

'''pwd
cd
    ls
    cd/desktop/djangoproject/mysite
    python3 manage.py runserver'''

#PAGE 2
class page2_form(forms.Form):
    
    grades1= [
('I', 'I'),
('II', 'II'),
('III', 'III'),
('IV','IV'),
('V','V'),
('VI','VI'),
('VII','VII'),
('VIII','VIII'),
('IX','IX'),
('X','X'),
('XI','XI'),
('XII', 'XII')
]
    grades = forms.ChoiceField(choices=grades1,label="class")

    section1 =[
('A','A'),
('B','B'),
('C' ,'C'),
('D', 'D'),
('E','E')]

    section =forms.ChoiceField(choices=section1, label="section")


#PAGE 4
class page4_form(forms.Form):
    subject=forms.CharField()
    teacher=forms.CharField()  


#PAGE 3
class page3_form(forms.Form):
    stime=forms.TimeField()
    etime=forms.TimeField()
    nperiod=forms.IntegerField()
    

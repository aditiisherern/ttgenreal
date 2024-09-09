import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.utils.timezone import timedelta
#from .models import subject
from .forms import page2_form
from .forms import page4_form
from .forms import page3_form
from polls.models import classs
from polls.models import teacher 
from polls.models import sched


#  line 20,21,22
#  line 39... we take the input right?
#what does index1,2,3,4 do?
#line 36 what does data store in 1 st key
#subthing1 should contain all sujects
## double hash means Akshaya has commetedd may not be necessary
#line 151
#line 179... subthing1 right... no model like subthing exists
#line 189 print(subthing_values... right not subthing1)
#model name and list name are the same.... so changed list of fixed subj as subthing
#why are there two variables for storing objects of subthing1
 ## line 193 Subjects for the day would have the timetable for the whole day right?
## line 201 subthing1...that is subthing now is already a list so why?
from polls.models import nofixed


obj= nofixed()
No_fixed_real = obj.nofix 
No_fixed_real=7












days={'Monday':[],'Tuesday':[],'Wednesday':[],'Thursday':[],'Friday':[]}
no_p_d=10

def index(request: HttpRequest):
    return render(request, "index.html", {"test": "this is my template"})

def index1(request):
    # this is like doing a select * from subject
    #.all makes all rows of the database into list
    '''subjectlist = subject.objects.all() 
    print(subjectlist)

    # printing out all the subjects
    for x in subjectlist:
        print(f"Subject: {x.subject} Freq: {x.frequency_s}")'''
    return render(request, "page 1.html", {"test": "this is my p1"})

def index2(request):
    return render(request, "page 2.html", {"test": "this is my p2"})

def index3(request):
    return render(request, "page 3.html", {"test": "this is my p3"})

def index4(request):
    return render(request, "page 4.html", {"test": "this is my p4"})



 
def page2(request): #for the entry blocks
    data={"form2":page2_form()}
    #print("lol")

    if request.method=="POST":
        print('ugh anirudh')
        class1=request.POST.get('grades')
        section1=request.POST.get('section')
        data={'form2':page2_form(),"grades":class1,"section":section1}
    print("lol")
    return render(request,'page 2.html',data)

def save_classinfo(request):  #to get the stuff and put it in admin
    if request.method=="POST":
        value_g=request.POST.get('grades') #from forms
        value_s=request.POST.get('section')

        datas=classs(grade=value_g,section=value_s)
        datas.save()
        # go to the next page
        return redirect(page3)
    else:
        return render(request,'page 2.html')


def page4(request): #this is the view
    data1={'form4':page4_form()}
    if request.method=="POST":
        
        subject1=request.POST.get('subject')
        teacher1=request.POST.get('teacher')
        data1={'form4':page4_form(),"subject":subject1,'teacher':teacher1}
        


    return render(request,'page 4.html',data1)

   
def save_teacherinfo(request): #thing to save in admin page
    
   
    if request.method=="POST":
        
        value_sub=request.POST.get('subject')
        value_t=request.POST.get('teacher')
        

        datas=teacher(subject=value_sub,t_name=value_t)
        datas.save()

        #GENERATION ALGO AHAHHAH
        


        #print(dictionary_of_teach_subj)
        
        
    return redirect(page4)
    
    
        


       


def page3(request): #this is the view       
        if request.method=="POST":
            data2={'form3':page3_form()}
            start_time=request.POST.get('stime')
            end_time=request.POST.get('etime')
            noperiod=request.POST.get('nperiod')
            

            data2={'form3':page3_form(),'start':start_time,'end':end_time,'periodss':noperiod}

            return render(request,'page 3.html',data2)
        else:
            return render(request,'page 3.html',{'form3':page3_form()})


def save_timings(request):
    global value_etime
    global value_stime
    global value_nperiod
    ##Have we stored this globally
    if request.method=="POST":
        value_stime=request.POST.get('stime')
        value_etime=request.POST.get('etime')
        value_nperiod=request.POST.get('nperiod')

        datas=sched(s_time=value_stime,e_time=value_etime,n_periods=value_nperiod)
        datas.save()
        return redirect(page4)

    else:
     return render(request,'page 3.html')
    

# Function to generate a schedule for a day
def generate_day_schedule(request):
        
        #GETTING ALL OUR DATA 
    
        teach_subj=teacher.objects.all()   #gets everything in the model teacher
        dictionary_of_teach_subj = list(teach_subj.values())  #makes it a dictionary

        

        
        #to get our class
        # appears like <QuerySet [{'grade': 'XII'}]> <QuerySet [{'section': 'B'}]>

        gradee_query=classs.objects.all().values('grade')
        sec_query=classs.objects.all().values('section')
        class_sec=''
        for m in gradee_query:
            class_sec+=m['grade']
        class_sec+=" "
        for n in sec_query:
            class_sec+=n['section']

        print('my class is',class_sec)


        
        #to get a list of all our subjects

        list_subjects_query=teacher.objects.all().values('subject')  #gets only the values of the subjects
        actual_listof_subject=[] 

        for i in list_subjects_query:#[{'subject':math},{'subject':english}]
            actual_listof_subject+=[i['subject']]
        print('my subjects are',actual_listof_subject)
        no_of_default_periods=len(actual_listof_subject)
        
        print('so, i have this many default subjects',no_of_default_periods)



        #no of periods user wants in a day

        no_periods_query=sched.objects.all().values('n_periods')
        no_periods=2
        for individual_dictionary in no_periods_query:
            no_periods=individual_dictionary['n_periods']

        print('in a day i have this many subjects',no_periods)
        
        no_of_periods_to_shuffle=no_periods-no_of_default_periods
        print('no of periods to shuffle',no_of_periods_to_shuffle)


        #for our timings

        snacks=15
        lunch=30
        breaks=snacks+lunch
        sched_objects = sched.objects.all()
        

        for obj in sched_objects:
            s_time_hour = obj.s_time.hour 
            e_time_hour = obj.e_time.hour

        working_hours=e_time_hour-s_time_hour
    
        working_hours_in_mins=working_hours*60

        only_studying_hours = working_hours_in_mins-breaks

        duration_of_each_period=only_studying_hours//no_periods
        print('each period lasts:',duration_of_each_period)

        #oK MAKING THE ACTUAL TIMETABLE 
        days=[]

        # function to generate a candidate schedul
        def generate_schedule(num_additional_classes, existing_classes):
            day_class_list = []

            # ADDING THE DEFAULT SUBJECTS TO EACH DAY 
            day_class_list += existing_classes
            #print(f"Adding {num_additional_classes} additional classes")

            for i in range(num_additional_classes):
                # picking a random period to add to our day
                random_period = random.choice(existing_classes)
                # adding it to the list of that day
                day_class_list.append(random_period)

            random.shuffle(day_class_list)
            return day_class_list
    
        # function to check if the timetable is valid
        def check_day_timetable(day_timetable):
            valid = True
            # check if there are more than two of the same class in a day
            subj_freq = {}
            # generate the count of classes for each subject
            for subject in day_timetable:
                if subject not in subj_freq.keys():
                    subj_freq[subject] = 1
                else: 
                    subj_freq[subject] += 1

            for subject, freq in subj_freq.items():
                if freq > 2:
                    valid = False
                    break
            return valid

        # generate daily schedules until we have all valid schedules
        for i in range(5):
            timetable_is_valid = False
            # repeat until we have a valid schedule
            while not timetable_is_valid:
                # generate a candidate schedule
                day_timetable = generate_schedule(no_of_periods_to_shuffle, actual_listof_subject)
                # check if the schedule is valid
                timetable_is_valid = check_day_timetable(day_timetable)

            # set the timetable to the valid timetable for the day
            days.append(day_timetable)
            print(f"Timetable for the day -> {day_timetable}")

        print(f"All timetables => {days}")
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        combined_data = list(zip(weekdays, days))

        return render(request,'generation.html',{'days': days,'combined_data':combined_data,'class_sec':class_sec,'no_periods':[f"Subject {x+1}" for x in range(no_periods)]})



 
        
        


from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("main", views.index1, name="main"),
    #path("class", views.index2, name="index2"),
    path("timings", views.index3, name="index3"),
   # path("teachers", views.index4, name="index4"),
    path("classreal", views.page2, name="class1"),
    path("save_class",views.save_classinfo,name='saveclass'),
    path("teachersreal", views.page4, name="teachers1"),
    path("save_teacher",views.save_teacherinfo,name='saveteachersub'),
    path("timingsreal",views.page3, name="timingss"),
    path("save_timings",views.save_timings,name="savetimings"),
    path("generator",views.generate_day_schedule,name='ttgen')
]  
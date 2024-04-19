from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
   
     path('', views.index,name='home'),
     path('about/',views.about,name='about'),
      path('booking/',views.booking,name='booking'),
        path('doctors/',views.doctors,name='doctors'),
         path('department/',views.department,name='department'),




     #     ---------crud---------------

          path('crud/',views.CRUD_index,name='crud'),
          path('add/',views.CRUD_add,name='add'),
           path('addrec/',views.addrec,name='addrec'),
          path('delete/<id>/',views.delete,name="delete"),
          path('update/<int:id>/',views.update,name='update'),
           path('update/uprec/<int:id>/',views.uprec,name='uprec')


]         
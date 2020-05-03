from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
# Create your views here.
from .models import *
from .forms import *

def home(request):
        Article = Home_Page_Pics_Article.objects.all()
        return render(request, 'blog/home.html',{'Article' : Article})


def public_notice(request):
    pub_notice = social_notice_data.objects.all().order_by('-pk')
    return render(request, 'blog/public_notice.html',{'pub_notice' : pub_notice})


def gallery(request):
    all_images = Home_Dynamic_Pics.objects.count()
    if (all_images > 9):
        Images_pics = Home_Dynamic_Pics.objects.only('home_dynamic_images').first()
        Images_pics.delete()
        return redirect('gallery')
    else:
        data = Home_Dynamic_Pics.objects.all().order_by('-pk')
        return render(request, 'blog/gallery.html', {'data' : data})



def school(request):
    all_images = School_Data.objects.count()
    if (all_images > 6):
        Images_pics = School_Data.objects.all().first()
        Images_pics.delete()
        return redirect('school')
    else:
        data = School_Data.objects.all().order_by('-pk')
        data4 = School_admission.objects.all().order_by('-pk')
        return render(request, 'blog/school.html', {'data' : data, 'data4' : data4})


@login_required(login_url='/login/')
def school_view(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('show_data')
    else:
        form = SchoolForm()
        return render(request, 'blog/school_update.html', {'form': form})


@login_required(login_url='/login/')
def run_activity(request):
    if request.method == 'POST':
        form = Run_Activity_Form(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('show_data')
    else:
        form = Run_Activity_Form()
        return render(request, 'blog/activity.html', {'form': form})



@login_required(login_url='/login/')
def home_update(request):
    if request.method == 'POST':
        form = BaseHomeForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('show_data')
    else:
        form = BaseHomeForm()
        return render(request, 'blog/HomeUpdate.html', {'form': form})

    



# def admin_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('http://127.0.0.1:8000/admin/')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'blog/admin.html', {'form': form})


def activity(request):
    data6 = running_activities.objects.all().order_by('-pk')
    return render(request, 'blog/notice.html', {'data6' : data6})

@login_required(login_url='/login/')
def running_delete(request, id):
    query = running_activities.objects.get(pk=id)
    query.delete()
    return redirect('show_data')


#========================Feedback signup viewd============================
def feedback_signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commentbox_view')
    else:
        form = UserForm()
        #user = User.objects.all().last()
    return render (request, 'blog/feedback_signup.html', {'form':form})

#=====================================Login view========================



def login_view(request):   #
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('show_data')
    else:
        form = AuthenticationForm()
        data = Sarpanch_Name_Pic.objects.all()
        data1 = Home_Page_Pics_Article.objects.all()
        data2 = Home_Dynamic_Pics.objects.all()
        data3 = Admin_Name_Pic.objects.all()
        data4 = School_admission.objects.all()
        data5 = School_Data.objects.all().order_by('-pk')
        data6 = running_activities.objects.all()
        data7 = social_notice_data.objects.all()
        data8 = user_form.objects.all()
    return render(request, 'blog/showdata.html', {'form':form,'data1': data1, 'data2': data2, 'data': data, 'data3' : data3, 'data4' : data4, 'data5' : data5, 'data6' : data6, 'data7' : data7, 'data8' : data8})
    


#============================logout==============================
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def upload_image(request):
    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES)
        if form.is_valid():
            #blog_item = form.save#(commit=False)
            form.save()
        return redirect('show_data')
    else:
        form = AdminForm()
        return render(request, 'blog/upload.html', {'form': form})

    

def present_members(request):
            Images_pic = Sarpanch_Name_Pic.objects.all()
            return render(request, 'blog/present_members.html',{'show_pics' : Images_pic})



@login_required(login_url='/login/')
def show_data(request):
    data = Sarpanch_Name_Pic.objects.all()
    data1 = Home_Page_Pics_Article.objects.all()
    data2 = Home_Dynamic_Pics.objects.all()
    data3 = Admin_Name_Pic.objects.all()
    data4 = School_admission.objects.all()
    data5 = School_Data.objects.all().order_by('-pk')
    data6 = running_activities.objects.all()
    data7 = social_notice_data.objects.all()
    data8 = user_form.objects.all()
    return render(request, 'blog/showdata.html', {'data1': data1, 'data2': data2, 'data': data, 'data3' : data3, 'data4' : data4, 'data5' : data5, 'data6' : data6, 'data7' : data7, 'data8' : data8})


@login_required(login_url='/login/')
def delete_items(request, id):
    query = Sarpanch_Name_Pic.objects.get(pk=id)
    query.delete()
    return redirect('show_data')

@login_required(login_url='/login/')
def article_image_delete(request, id):
    query = Home_Page_Pics_Article.objects.get(pk=id)
    query.delete()
    return redirect('show_data')

@login_required(login_url='/login/')
def delete_social_notice(request, id):
    query = social_notice_data.objects.get(pk=id)
    query.delete()
    return redirect('show_data')


@login_required(login_url='/login/')
def delete_gallery_item(request, id):
    query = Home_Dynamic_Pics.objects.get(pk=id)
    query.delete()
    return redirect('show_data')

@login_required(login_url='/login/')
def user_form_delete(request, id):
    query = user_form.objects.get(pk=id)
    query.delete()
    return redirect('show_data')


@login_required(login_url='/login/')
def School_item_delete(request, id):
    query = School_Data.objects.get(pk=id)
    query.delete()
    return redirect('show_data')

@login_required(login_url='/login/')
def Admin_item_delete(request, id):
    query = Admin_Name_Pic.objects.get(pk=id)
    query.delete()
    return redirect('show_data')



@login_required(login_url='/login/')
def home_dynamic_images(request):
    if request.method == 'POST':
        form = HomeDynamicPicsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('show_data')
    else:
        form = HomeDynamicPicsForm()
        return render(request, 'blog/HomeDynamic.html', {'form' : form})



#Yeh Admin_name view ko base.html mein call karna hai, how ? Jo Mahatma Gandhi ji ki photo aa rahi hai
@login_required(login_url='/login/')
def admin_name(request):
    if request.method == 'POST':
        form = AdminNamePicForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('show_data')
    else:
        form = AdminNamePicForm()
        return render(request, 'blog/AdminName.html', {'form': form})


@login_required(login_url='/login/')
def school_admission(request):
    if request.method == 'POST':
        form = School_Admission_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_data')
    else:
        form = School_Admission_Form()
    return render (request, 'blog/schoolAdmission.html', {'form' : form})


@login_required(login_url='/login/')
def edit(request, id):
    query = School_admission.objects.get(id=id)
    if request.method == 'POST':
        form = School_Admission_Form(request.POST, instance=query)
        if form.is_valid():
            form.save()
        return redirect('show_data')
    else:
        form = School_Admission_Form(instance=query)
    return render(request, 'blog/edit.html', {'form': form})


@login_required(login_url='/login/')
def social_notice(request):
    if request.method == 'POST':
        form = Social_Notice_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_data')
    else:
        form = Social_Notice_Form()
    return render (request, 'blog/socialnotice.html', {'form' : form})


def user_form_msg(request):
    if request.method == 'POST':
        form = User_Data_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('public_notice')
    else:
        form = User_Data_Form()
    return render (request, 'blog/public_notice.html', {'form' : form})


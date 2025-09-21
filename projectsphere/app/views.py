from django.shortcuts import render,redirect
from django.urls import reverse
from.models import*
from django.contrib.auth.models import auth,User
from django.contrib.auth.hashers import check_password
from django.utils import timezone
from django.contrib.auth import logout



# Create your views here.
def index(request):
    if request.method == 'POST':
        a=request.POST['user']
        if a == 'Student':
            return redirect(student_sign_up)
        elif a == 'Co_ordinator':
            return redirect(coordinator_sign_up)
        elif a == 'Guide':
            return redirect(guide_sign_up)
        
    return render(request,'index.html')

def sign_up(request):
    return render(request,'sign_up.html')

def student_home(request):
    val = User.objects.get(username=request.user)
    context = {
        'name':val.first_name
    }
    return render(request,'student/student_home.html',context)

def student_mark(request):
    return render(request,'student/student_mark.html')

def student_progress(request):
    val = StudentReg.objects.get(user=request.user)
    value = RegisterProject.objects.get(student=val)
    cal = Calender.objects.all()
    lis =[]
    n = 0
    m = 0
    for i in cal:
        n = n+1
        if Resource.objects.filter(project=value,calender=i).exists():
            lis.append(100)
            m=m+100
        else:
            lis.append(0)
    avg = m//n
    val = zip(cal, lis)
    dic = {
        'key':value,
        'ppp':val,
        'avg':avg,
        'key':value
    }
    return render(request,'student/student_progress.html',dic)


def progress_of_team(request,pk):
    value = RegisterProject.objects.get(id=pk)
    cal = Calender.objects.all()
    lis =[]
    n = 0
    m = 0
    for i in cal:
        n = n+1
        if Resource.objects.filter(project=value,calender=i).exists():
            lis.append(100)
            m=m+100
        else:
            lis.append(0)
    avg = m//n
    val = zip(cal, lis)
    dic = {
        'key':value,
        'ppp':val,
        'avg':avg
    }
    return render(request,'coordinator/progress_of_team.html',dic)

def view_progress(request,pk):
    value = RegisterProject.objects.get(id=pk)
    cal = Calender.objects.all()
    lis =[]
    n = 0
    m = 0
    for i in cal:
        n = n+1
        if Resource.objects.filter(project=value,calender=i).exists():
            lis.append(100)
            m=m+100
        else:
            lis.append(0)
    avg = m//n
    val = zip(cal, lis)
    dic = {
        'key':value,
        'ppp':val,
        'avg':avg
    }
    return render(request,'guide/view_progress.html',dic)

def register_project(request):
    val = StudentReg.objects.get(user=request.user)
    u = User.objects.get(username=request.user)
    ab = None
    if RegisterProject.objects.filter(user=request.user).exists():

        hello = 'Already A Project team Exists'
        ab = RegisterProject.objects.get(user=request.user)
    else:
        hello = 'Register Project'
    context = {
        'name':val.teamHeadName,
        'id':val.teamHeadId,
        'username':val.username,
        'hello':hello,
        'ab':ab
    }
    if request.method == 'POST':
        teamName = request.POST['teamName']
        projectTitle = request.POST['projectTitle']
        teamHeadName = request.POST['teamHeadName']
        teamHeadId = request.POST['teamHeadId']
        username = request.POST['username']
        teamMember1 = request.POST['teamMember1']
        teamMember1Id = request.POST['teamMember1Id']
        teamMember2 = request.POST['teamMember2']
        teamMember2Id = request.POST['teamMember2Id']
        teamMember3 = request.POST['teamMember3']
        teamMember3Id = request.POST['teamMember3Id']
        if RegisterProject.objects.filter(user=request.user).exists():
            hello = 'Already A Project team Exists'
            return redirect(register_project)
        else:
            hello = 'Project is Registered'
            RegisterProject(
                user = u,
                student = val,
                teamName = teamName,
                projectTitle = projectTitle,
                teamHeadName = teamHeadName,
                teamHeadId = teamHeadId,
                username = username,
                teamMember1 = teamMember1,
                teamMember2 = teamMember2,
                teamMember3 = teamMember3,
                teamMember1Id = teamMember1Id,
                teamMember2Id = teamMember2Id,
                teamMember3Id = teamMember3Id
            ).save()
            return redirect(register_project)
        
    return render(request,'student/register_project.html',context)

def student_view_announcement(request):
    val = ProjectAnnouncement.objects.all()
    dic = {
        'val':val
    }
    return render(request,'student/student_view_announcement.html',dic)

def student_sign_up(request):
    return render(request,'student/student_sign_up.html')

def coordinator_home(request):
    val = User.objects.get(username=request.user)
    context = {
        'name':val.first_name
    }
    return render(request,'coordinator/coordinator_home.html',context)

def coordinator_sign_up(request):
    return render(request,'coordinator/coordinator_sign_up.html')

def coordinator_view_guide(request):
    val = GuideReg.objects.all()
    dic = {
        'key':val
    }
    return render(request,'coordinator/coordinator_view_guide.html',dic)

def view_announcement(request):
    val = ProjectAnnouncement.objects.all()
    dic = {
        'key':val
    }
    return render(request,'coordinator/view_announcement.html',dic)

def create_guide(request):
    return render(request,'coordinator/create_guide.html')

def coordinator_announcement(request):
    val = User.objects.get(username=request.user)
    co = Co_ordinatorReg.objects.get(user=request.user)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        date = request.POST['date']
        ProjectAnnouncement(
            user = val,
            co_ordinator = co,
            subject = subject,
            message = message,
            date = date,
            now_date = timezone.now().date()
        ).save()
        return redirect(view_announcement)
    return render(request,'coordinator/coordinator_announcement.html')

def coordinator_delete_announcement(request,pk):
    val = ProjectAnnouncement.objects.get(id=pk)
    val.delete()
    return redirect(view_announcement)


def guide_home(request):
    val = User.objects.get(username=request.user)
    context = {
        'name':val.first_name
    }
    return render(request,'guide/guide_home.html',context)

def guide_sign_up(request):
    return render(request,'guide/guide_sign_up.html')


def student_register(request):
    if request.method=='POST':
        Username = request.POST['Username']
        Full_name = request.POST['Full_name']
        Member_ID = request.POST['Member_ID']
        email = request.POST['email']
        Phone = request.POST['Phone']
        Password = request.POST['Password']
        Confirm_password = request.POST['Confirm_password']
        if Password==Confirm_password:
            if User.objects.filter(username=Username).exists():
                context = {
                    'msg' :'Username already exists..'
                }
                return render(request,'student/student_sign_up.html',context)
            if User.objects.filter(email=email).exists():
                context = {
                    'msg' :'Email already exists..'
                }
                return render(request,'student/student_sign_up.html',context)
            else:
                a=User.objects.create_user(username=Username,email=email,password=Password,first_name=Full_name)
                a.save()
                StudentReg(
                    	user = a,
                        phone = Phone,
                        teamHeadName = Full_name,
                        teamHeadId = Member_ID,
                        username = Username
	
                    ).save()
                return redirect(student_sign_up)
        else:
            context={
                'msg':'Password does not match',
                'app_title':'Charity',
                'title':'User Register',
            }
            return render(request,'student/student_sign_up.html',context)



def student_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if StudentReg.objects.filter(user__username=username).exists():
            u=auth.authenticate(username=username,password=password)
            if u is not None:
                auth.login(request,u)
                return redirect(student_home)
            else:
                context = {
                    'app_title':'project',
                    'title':'project',
                    'msg':'Invalid username or password'
                }
                return render(request,'student/student_sign_up.html',context)
        else:
            context = {
                'app_title':'project',
                'title':'project',
                'msg':'Invalid User'
                }
            return render(request,'student/student_sign_up.html',context)
    

def guide_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if GuideReg.objects.filter(user__username=username).exists():
            u=auth.authenticate(username=username,password=password)
            if u is not None:
                auth.login(request,u)
                return redirect(guide_home)
            else:
                context = {
                    'app_title':'project',
                    'title':'project',
                    'msg':'Invalid username or password'
                }
                return render(request,'guide/guide_sign_up.html',context)
        else:
            context = {
                'app_title':'project',
                'title':'project',
                'msg':'Invalid User'
                }
            return render(request,'guide/guide_sign_up.html',context)
    

def logout_view(request):
    logout(request)
    return redirect(index)



def coordinator_register(request):
    if request.method=='POST':
        Username = request.POST['Username']
        Full_name = request.POST['Full_name']
        email = request.POST['email']
        Phone = request.POST['Phone']
        Password = request.POST['Password']
        Confirm_password = request.POST['Confirm_password']
        if Password==Confirm_password:
            if User.objects.filter(username=Username).exists():
                context = {
                    'msg' :'Username already exists..'
                }
                return render(request,'coordinator/coordinator_sign_up.html',context)
            if User.objects.filter(email=email).exists():
                context = {
                    'msg' :'Email already exists..'
                }
                return render(request,'coordinator/coordinator_sign_up.html',context)
            else:
                a=User.objects.create_user(username=Username,email=email,password=Password,first_name=Full_name)
                a.save()
                Co_ordinatorReg(
                    	user = a,
                        phone = Phone,
                    ).save()
                return redirect(coordinator_sign_up)
        else:
            context={
                'msg':'Password does not match',
                'app_title':'project',
                'title':'project',
            }
            return render(request,'coordinator/coordinator_sign_up.html',context)



def create_guide(request):
    if request.method=='POST':
        Username = request.POST['Username']
        Full_name = request.POST['Full_name']
        email = request.POST['email']
        Phone = request.POST['Phone']
        Password = request.POST['Password']
        Confirm_password = request.POST['Confirm_password']
        if Password==Confirm_password:
            if User.objects.filter(username=Username).exists():
                context = {
                    'msg' :'Username already exists..'
                }
                return render(request,'coordinator/create_guide.html',context)
            if User.objects.filter(email=email).exists():
                context = {
                    'msg' :'Email already exists..'
                }
                return render(request,'coordinator/create_guide.html',context)
            else:
                a=User.objects.create_user(username=Username,email=email,password=Password,first_name=Full_name)
                a.save()
                GuideReg(
                    	user = a,
                        phone = Phone,
                    ).save()
                return redirect(coordinator_view_guide)
        else:
            context={
                'msg':'Password does not match',
                'app_title':'project',
                'title':'project',
            }
            return render(request,'coordinator/create_guide.html',context)
    else:
        return render(request,'coordinator/create_guide.html')



def coordinator_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if Co_ordinatorReg.objects.filter(user__username=username).exists():
            u=auth.authenticate(username=username,password=password)
            if u is not None:
                auth.login(request,u)
                return redirect(coordinator_home)
            else:
                context = {
                    'app_title':'project',
                    'title':'project',
                    'msg':'Invalid username or password'
                }
                return render(request,'coordinator/coordinator_sign_up.html',context)
        else:
            context = {
                'app_title':'project',
                'title':'project',
                'msg':'Invalid User'
                }
            return render(request,'coordinator/coordinator_sign_up.html',context)
    

def review1(request):
    return render(request,'coordinator/review1.html')

def view_team(request):
    val = RegisterProject.objects.all()
    dic = {
        'val':val
    }
    return render(request,'coordinator/view_team.html',dic)

def view_resource_one(request):
    val = RegisterProject.objects.all()
    dic = {
        'val':val
    }
    return render(request,'coordinator/view_resource_one.html',dic)

def guide_view_team(request):
    gui = GuideReg.objects.get(user__username = request.user)
    val = RegisterProject.objects.filter(guide = gui)
    dic = {
        'val':val
    }
    return render(request,'guide/guide_view_team.html',dic)

def coordinator_assign_guide(request,pk):
    val = RegisterProject.objects.get(id = pk)
    guides = GuideReg.objects.all()
    dic = {
        'val':val,
        'guides':guides
    }
    if request.method == 'POST':
        gui = request.POST['gui']
        abc = GuideReg.objects.get(user__first_name = gui)
        RegisterProject.objects.filter(id = pk).update(assign = 'A Guide Is Assigned',guide=abc)
        return redirect(view_team)
    return render(request,'coordinator/coordinator_assign_guide.html',dic)

def view_staff(request):
    return render(request,'coordinator/view_staff.html')

def coordinator_delete_guide(request,pk):
    val = GuideReg.objects.get(id=pk)
    val.delete()
    return redirect(coordinator_view_guide)

def student_chat(request):
    # Assuming 'user_type' in session to differentiate between guide and student
    a = RegisterProject.objects.get(user=request.user)
    
    # Retrieve old chats based on the user type and user ID
    old_chats = Chat.objects.filter(project=a)

    context = {
        'old_chats': old_chats,
    }
    return render(request, 'student/student_chat.html', context)
   
def student_review_mark(request,pk):
    print(pk)
    ml = []

    marks = 0
    if ReviewOne.objects.filter(Name=pk).exists():
        loop1 = ReviewOne.objects.get(Name=pk)
        ml.append(loop1.total)
        marks = marks + loop1.total
    else:
        ml.append(" ")
    if ReviewTwo.objects.filter(Name=pk).exists():
        loop2 = ReviewTwo.objects.get(Name=pk)
        ml.append(loop2.total)
        marks = marks + loop2.total
    else:
        ml.append(" ")
    if ReviewThree.objects.filter(Name=pk).exists():
        loop3 = ReviewThree.objects.get(Name=pk)
        ml.append(loop3.total)
        marks = marks + loop3.total
    else:
        ml.append(" ")
    if AttendenceTab.objects.filter(Name=pk).exists():
        loop4 = AttendenceTab.objects.get(Name=pk)
        ml.append(loop4.attendence)
        marks = marks + loop4.attendence
    else:
        ml.append(" ")
    if ReportTab.objects.filter(Name=pk).exists():
        loop5 = ReportTab.objects.get(Name=pk)
        ml.append(loop5.report)
        marks = marks + loop5.report
    else:
        ml.append(" ")
    if GuideMark.objects.filter(Name=pk).exists():
        loop6 = GuideMark.objects.get(Name=pk)
        ml.append(loop6.total)
        marks = marks + loop6.total
    else:
        ml.append(" ")
    # if EndSemEval.objects.filter(Name=pk).exists():
    #     loop7 = EndSemEval.objects.get(Name=pk)
    #     ml.append(loop7.total)
    #     marks = marks + loop7.total
    # else:
    #     ml.append(" ")

    
    dic = {
        'value':ml,
        'marks':marks
    }
    return render(request, 'student/student_review_mark.html',dic)
   
def guide_review_mark(request,pk):
    print(pk)
    ml = []

    marks = 0
    if ReviewOne.objects.filter(Name=pk).exists():
        loop1 = ReviewOne.objects.get(Name=pk)
        ml.append(loop1.total)
        marks = marks + loop1.total
    else:
        ml.append(" ")
    if ReviewTwo.objects.filter(Name=pk).exists():
        loop2 = ReviewTwo.objects.get(Name=pk)
        ml.append(loop2.total)
        marks = marks + loop2.total
    else:
        ml.append(" ")
    if ReviewThree.objects.filter(Name=pk).exists():
        loop3 = ReviewThree.objects.get(Name=pk)
        ml.append(loop3.total)
        marks = marks + loop3.total
    else:
        ml.append(" ")
    if AttendenceTab.objects.filter(Name=pk).exists():
        loop4 = AttendenceTab.objects.get(Name=pk)
        ml.append(loop4.attendence)
        marks = marks + loop4.attendence
    else:
        ml.append(" ")
    if ReportTab.objects.filter(Name=pk).exists():
        loop5 = ReportTab.objects.get(Name=pk)
        ml.append(loop5.report)
        marks = marks + loop5.report
    else:
        ml.append(" ")
    if GuideMark.objects.filter(Name=pk).exists():
        loop6 = GuideMark.objects.get(Name=pk)
        ml.append(loop6.total)
        marks = marks + loop6.total
    else:
        ml.append(" ")
    # if EndSemEval.objects.filter(Name=pk).exists():
    #     loop7 = EndSemEval.objects.get(Name=pk)
    #     ml.append(loop7.total)
    #     marks = marks + loop7.total
    # else:
    #     ml.append(" ")

    
    dic = {
        'value':ml,
        'marks':marks
    }
    return render(request, 'guide/guide_review_mark.html',dic)
   
def student_review_mark_one(request):
    a = RegisterProject.objects.get(user=request.user)
    dic = {
        'a':a
    }
    return render(request, 'student/stu_review_mark_one.html',dic)

def view_reviews(request):
    a = RegisterProject.objects.get(user=request.user)
    dic = {
        'a':a
    }
    return render(request,'student/view_reviews.html',dic)

def send_chat(request):
    a = RegisterProject.objects.get(user=request.user)
    b = User.objects.get(username=request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
    
        # Save the new chat message
        Chat.objects.create(user=b, message=message, project=a)

        # Redirect to the chat page after sending the message
        return redirect(student_chat)
    
def guide_chat(request,id):
    # Assuming 'user_type' in session to differentiate between guide and student
    a = RegisterProject.objects.get(id=id)
    print(a)
    # Retrieve old chats based on the user type and user ID
    old_chats = Chat.objects.filter(project=a.id)
    context = {
        'old_chats': old_chats,
        'id':id
    }
    return render(request, 'guide/guide_chat.html', context)



def guide_send_chat(request):
    
    b = User.objects.get(username=request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        ids = request.POST.get('ids')

        a = RegisterProject.objects.get(id = ids)

        # Save the new chat message
        Chat.objects.create(user=b, message=message, project=a)

        url = reverse('guide_chat', kwargs={'id': a.id})
        return redirect(url)

    
def guide_review(request,pk):
    a = RegisterProject.objects.get(id=pk)
    dic = {
        'a':a
    }
    return render(request,'guide/guide_review.html',dic)
    
def coordinator_review(request):
    a = RegisterProject.objects.all()

    students_name = []
    students_id = []
    students_project = []
    ml = []
    m2 = []
    m3 = []
    m4 = []
    m5 = []
    m6 = []
    m7 = []
    marks = []
    for i in a :
        ###############
        students_name.append(i.teamHeadName)
        if ReviewOne.objects.filter(Name=i.teamHeadName).exists():
            loop1 = ReviewOne.objects.get(Name=i.teamHeadName)
            ml.append(loop1.total)
            # marks = marks + int(loop1.total)
        else:
            ml.append(" ")
        if ReviewTwo.objects.filter(Name=i.teamHeadName).exists():
            loop2 = ReviewTwo.objects.get(Name=i.teamHeadName)
            m2.append(loop2.total)
            # marks = marks + loop2.total
        else:
            m2.append(" ")
        if ReviewThree.objects.filter(Name=i.teamHeadName).exists():
            loop3 = ReviewThree.objects.get(Name=i.teamHeadName)
            m3.append(loop3.total)
            # marks = marks + loop3.total
        else:
            m3.append(" ")
        if AttendenceTab.objects.filter(Name=i.teamHeadName).exists():
            loop4 = AttendenceTab.objects.get(Name=i.teamHeadName)
            m4.append(loop4.attendence)
            # marks = marks + loop4.attendence
        else:
            m4.append(" ")
        if ReportTab.objects.filter(Name=i.teamHeadName).exists():
            loop5 = ReportTab.objects.get(Name=i.teamHeadName)
            m5.append(loop5.report)
            # marks = marks + loop5.report
        else:
            m5.append(" ")
        if GuideMark.objects.filter(Name=i.teamHeadName).exists():
            loop6 = GuideMark.objects.get(Name=i.teamHeadName)
            m6.append(loop6.total)
            # marks = marks + loop6.total
        else:
            m6.append(" ")
        if EndSemEval.objects.filter(Name=i.teamHeadName).exists():
            loop7 = EndSemEval.objects.get(Name=i.teamHeadName)
            m7.append(loop7.total)
            # marks = marks + loop7.total
        else:
            m7.append(" ")

        ###############
        students_name.append(i.teamMember1)
        if ReviewOne.objects.filter(Name=i.teamMember1).exists():
            loop1 = ReviewOne.objects.get(Name=i.teamMember1)
            ml.append(loop1.total)
            # marks = marks + loop1.total
        else:
            ml.append(" ")
        if ReviewTwo.objects.filter(Name=i.teamMember1).exists():
            loop2 = ReviewTwo.objects.get(Name=i.teamMember1)
            m2.append(loop2.total)
            # marks = marks + loop2.total
        else:
            m2.append(" ")
        if ReviewThree.objects.filter(Name=i.teamMember1).exists():
            loop3 = ReviewThree.objects.get(Name=i.teamMember1)
            m3.append(loop3.total)
            # marks = marks + loop3.total
        else:
            m3.append(" ")
        if AttendenceTab.objects.filter(Name=i.teamMember1).exists():
            loop4 = AttendenceTab.objects.get(Name=i.teamMember1)
            m4.append(loop4.attendence)
            # marks = marks + loop4.attendence
        else:
            m4.append(" ")
        if ReportTab.objects.filter(Name=i.teamMember1).exists():
            loop5 = ReportTab.objects.get(Name=i.teamMember1)
            m5.append(loop5.report)
            # marks = marks + loop5.report
        else:
            m5.append(" ")
        if GuideMark.objects.filter(Name=i.teamMember1).exists():
            loop6 = GuideMark.objects.get(Name=i.teamMember1)
            m6.append(loop6.total)
            # marks = marks + loop6.total
        else:
            m6.append(" ")
        if EndSemEval.objects.filter(Name=i.teamMember1).exists():
            loop7 = EndSemEval.objects.get(Name=i.teamMember1)
            m7.append(loop7.total)
            # marks = marks + loop7.total
        else:
            m7.append(" ")

        ###############
        students_name.append(i.teamMember2)
        if ReviewOne.objects.filter(Name=i.teamMember2).exists():
            loop1 = ReviewOne.objects.get(Name=i.teamMember2)
            ml.append(loop1.total)
            # marks = marks + loop1.total
        else:
            ml.append(" ")
        if ReviewTwo.objects.filter(Name=i.teamMember2).exists():
            loop2 = ReviewTwo.objects.get(Name=i.teamMember2)
            m2.append(loop2.total)
            # marks = marks + loop2.total
        else:
            m2.append(" ")
        if ReviewThree.objects.filter(Name=i.teamMember2).exists():
            loop3 = ReviewThree.objects.get(Name=i.teamMember2)
            m3.append(loop3.total)
            # marks = marks + loop3.total
        else:
            m3.append(" ")
        if AttendenceTab.objects.filter(Name=i.teamMember2).exists():
            loop4 = AttendenceTab.objects.get(Name=i.teamMember2)
            m4.append(loop4.attendence)
            # marks = marks + loop4.attendence
        else:
            m4.append(" ")
        if ReportTab.objects.filter(Name=i.teamMember2).exists():
            loop5 = ReportTab.objects.get(Name=i.teamMember2)
            m5.append(loop5.report)
            marks = marks + loop5.report
        else:
            m5.append(" ")
        if GuideMark.objects.filter(Name=i.teamMember2).exists():
            loop6 = GuideMark.objects.get(Name=i.teamMember2)
            m6.append(loop6.total)
            # marks = marks + loop6.total
        else:
            m6.append(" ")
        if EndSemEval.objects.filter(Name=i.teamMember2).exists():
            loop7 = EndSemEval.objects.get(Name=i.teamMember2)
            m7.append(loop7.total)
            # marks = marks + loop7.total
        else:
            m7.append(" ")
        ###############
        students_name.append(i.teamMember3)
        if ReviewOne.objects.filter(Name=i.teamMember3).exists():
            loop1 = ReviewOne.objects.get(Name=i.teamMember3)
            ml.append(loop1.total)
            # marks = marks + loop1.total
        else:
            ml.append(" ")
        if ReviewTwo.objects.filter(Name=i.teamMember3).exists():
            loop2 = ReviewTwo.objects.get(Name=i.teamMember3)
            m2.append(loop2.total)
            # marks = marks + loop2.total
        else:
            m2.append(" ")
        if ReviewThree.objects.filter(Name=i.teamMember3).exists():
            loop3 = ReviewThree.objects.get(Name=i.teamMember3)
            m3.append(loop3.total)
            # marks = marks + loop3.total
        else:
            m3.append(" ")
        if AttendenceTab.objects.filter(Name=i.teamMember3).exists():
            loop4 = AttendenceTab.objects.get(Name=i.teamMember3)
            m4.append(loop4.attendence)
            # marks = marks + loop4.attendence
        else:
            m4.append(" ")
        if ReportTab.objects.filter(Name=i.teamMember3).exists():
            loop5 = ReportTab.objects.get(Name=i.teamMember3)
            m5.append(loop5.report)
            marks = marks + loop5.report
        else:
            m5.append(" ")
        if GuideMark.objects.filter(Name=i.teamMember3).exists():
            loop6 = GuideMark.objects.get(Name=i.teamMember3)
            m6.append(loop6.total)
            # marks = marks + loop6.total
        else:
            m6.append(" ")
        if EndSemEval.objects.filter(Name=i.teamMember3).exists():
            loop7 = EndSemEval.objects.get(Name=i.teamMember3)
            m7.append(loop7.total)
            # marks = marks + loop7.total
        else:
            m7.append(" ")

        students_id.append(i.teamHeadId)
        students_id.append(i.teamMember1Id)
        students_id.append(i.teamMember2Id)
        students_id.append(i.teamMember3Id)

        students_project.append(i.projectTitle)
        students_project.append(i.projectTitle)
        students_project.append(i.projectTitle)
        students_project.append(i.projectTitle)

    a = zip(students_id,students_name,students_project,ml,m2,m3,m4,m5,m6,m7)    

    dic = {
        'a':a
    }
    return render(request,'coordinator/coordinator_review.html',dic)
    
def coordinator_calender(request):
    val = Calender.objects.all()
    if request.method == 'POST':
        a = request.POST['week']
        b = request.POST['data']
        Calender(
            week = a,
	    submit = b
        ).save()
        return redirect(coordinator_calender)
    dic = {
        'key':val
    }
    return render(request,'coordinator/coordinator_calender.html',dic)
    
def view_calender(request):
    val = User.objects.get(username=request.user)
    val1 = Calender.objects.all()
    dic = {
        'key':val1,
        'name':val.first_name
    }
    return render(request,'student/view_calender.html',dic)
    
def submit_resource(request):
    val = Calender.objects.all()
    li = []
    for i in val:
        if Resource.objects.filter(calender = i.id).exists():
            abc = 'submited'
            li.append(abc)
        else:
            abcd = 'not submited'
            li.append(abcd)
    print(li)

    vi = []
    for i in val:
        if Resource.objects.filter(calender = i.id).exists():
            abc = Resource.objects.get(calender = i.id)
            vi.append(abc.drive_link)
        else:
            abcd = 'not submitted'
            vi.append(abcd)
    print(vi)

    zipped = zip(val, li ,vi)
    dic = {
        'key':zipped
    }
    return render(request,'student/submit_resource.html',dic)
    
def resource_form(request,pk):
    val = Calender.objects.get(id = pk)
    val1 = User.objects.get(username = request.user)
    val2 = RegisterProject.objects.get(user = val1)
    dic = {
        'key':val
    }
    if request.method == 'POST':
        if Resource.objects.filter(calender = val).exists():
            print('already exists')
            return redirect(submit_resource)
        else:
            a = request.POST['drive_link_val']
            Resource(
            calender = val,
            project = val2,
            user = val1,
            drive_link = a
            ).save()
            return redirect(submit_resource)
    return render(request,'student/resource_form.html',dic)
 

def view_resource_two(request,pk):
    pq = Resource.objects.filter(project=pk)
    dic = {
        'key':pq
    }
    return render(request,'coordinator/view_resource_two.html',dic)

def view_resources(request,pk):
    pq = Resource.objects.filter(project=pk)
    dic = {
        'key':pq
    }
    return render(request,'guide/view_resources.html',dic)


def coordinator_review_one(request,pk):
    hi = RegisterProject.objects.get(id = pk)
    context = {
        'key':hi
    }
    return render(request,'coordinator/coordinator_review_one.html',context)

def review_1(request,pk,pk1,pk2):
    hi = RegisterProject.objects.get(id = pk)
    tab_val = ReviewOne.objects.filter(memberId = pk2)

    context = {
        'key':hi,
        'member_name':pk1,
        'member_id':pk2,
        'tab_val':tab_val
    }
    if request.method == 'POST':
        a1 = request.POST['ident_pro']
        a2 = request.POST['liter_review']
        a3 = request.POST['obj_des_meth']
        a4 = request.POST['total']
        if ReviewOne.objects.filter(memberId = pk2).exists():
            print("exists")
        else:
            ReviewOne(
                ident_pro=a1,
                liter_review=a2,
                obj_des_meth=a3,
                total=a4,
                project = hi,
                projectTitle = hi.projectTitle,
                Name = pk1,
                memberId = pk2
                ).save()
    return render(request,'coordinator/review_1.html',context)

def review_2(request,pk,pk1,pk2):
    hi = RegisterProject.objects.get(id = pk)
    tab_val = ReviewTwo.objects.filter(memberId = pk2)
    context = {
        'key':hi,
        'member_name':pk1,
        'member_id':pk2,
        'tab_val':tab_val
    }
    if request.method == 'POST':
        a1 = request.POST['det_meth_algo']
        a2 = request.POST['pro_implement']
        a3 = request.POST['viva']
        a4 = request.POST['total']
        if ReviewTwo.objects.filter(memberId = pk2).exists():
            print("exists")
        else:
            ReviewTwo(
                det_meth_algo=a1,
                pro_implement=a2,
                viva=a3,
                total=a4,
                project = hi,
                projectTitle = hi.projectTitle,
                Name = pk1,
                memberId = pk2
            ).save()

    return render(request,'coordinator/review_2.html',context)

def review_3(request,pk,pk1,pk2):
    hi = RegisterProject.objects.get(id = pk)
    tab_val = ReviewThree.objects.filter(memberId = pk2)
    context = {
        'key':hi,
        'member_name':pk1,
        'member_id':pk2,
        'tab_val':tab_val,
    }
    if request.method == 'POST':
        a1 = request.POST['level_com_demo']
        
        a4 = request.POST['total']
        if ReviewThree.objects.filter(memberId = pk2).exists():
            print("exists")
        else:
            ReviewThree(
                level_com_demo=a1,
                total=a4,
                project = hi,
                projectTitle = hi.projectTitle,
                Name = pk1,
                memberId = pk2
            ).save()
    return render(request,'coordinator/review_3.html',context)

def review_ese(request,pk,pk1,pk2):
    hi = RegisterProject.objects.get(id = pk)
    tab_val = EndSemEval.objects.filter(memberId = pk2)
    context = {
        'key':hi,
        'member_name':pk1,
        'member_id':pk2,
        'tab_val':tab_val
    }
    if request.method == 'POST':
        a1 = request.POST['ppt']
        a2 = request.POST['presentation']
        a3 = request.POST['demo']
        a4 = request.POST['total']
        a5 = request.POST['viva']
        if EndSemEval.objects.filter(memberId = pk2).exists():
            print("exists")
        else:
            EndSemEval(
                ppt=a1,
                presentation=a2,
                demo=a3,
                viva=a5,
                total=a4,
                project = hi,
                projectTitle = hi.projectTitle,
                Name = pk1,
                memberId = pk2
            ).save()
    return render(request,'coordinator/review_ese.html',context)

def review_guide(request,pk,pk1,pk2):
    hi = RegisterProject.objects.get(id = pk)
    tab_val = GuideMark.objects.filter(memberId = pk2)
    context = {
        'key':hi,
        'member_name':pk1,
        'member_id':pk2,
        'tab_val':tab_val
    }
    if request.method == 'POST':
        a1 = request.POST['reg_std_mini_pro']
        a2 = request.POST['know_invol_work']
        a4 = request.POST['total']
        if GuideMark.objects.filter(memberId = pk2).exists():
            print("exists")
        else:
            GuideMark(
                reg_std_mini_pro=a1,
	            know_invol_work=a2,
                total=a4,
                project = hi,
                projectTitle = hi.projectTitle,
                Name = pk1,
                memberId = pk2
            ).save()
    return render(request,'coordinator/review_guide.html',context)

def review_attendence(request,pk,pk1,pk2):
    hi = RegisterProject.objects.get(id = pk)
    tab_val = AttendenceTab.objects.filter(memberId = pk2)
    context = {
        'key':hi,
        'member_name':pk1,
        'member_id':pk2,
        'tab_val':tab_val
    }
    if request.method == 'POST':
        a1 = request.POST['attendence']
        if AttendenceTab.objects.filter(memberId = pk2).exists():
            print("exists")
        else:
            AttendenceTab(
                attendence=a1,
                project = hi,
                projectTitle = hi.projectTitle,
                Name = pk1,
                memberId = pk2
            ).save()
    return render(request,'coordinator/review_attendence.html',context)

def review_report(request,pk,pk1,pk2):
    hi = RegisterProject.objects.get(id = pk)
    tab_val = ReportTab.objects.filter(memberId = pk2)
    context = {
        'key':hi,
        'member_name':pk1,
        'member_id':pk2,
        'tab_val':tab_val
    }
    if request.method == 'POST':
        a1 = request.POST['report']
        if ReportTab.objects.filter(memberId = pk2).exists():
            print("exists")
        else:
            ReportTab(
                report=a1,
                project = hi,
                projectTitle = hi.projectTitle,
                Name = pk1,
                memberId = pk2
            ).save()
    return render(request,'coordinator/review_report.html',context)
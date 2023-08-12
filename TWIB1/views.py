from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q


a=''

def check(request):
    n1=request.POST['user']
    n2=request.POST['password']
    user=User.objects.all().values()
    for i in user:
        if i['name']==n1 and i['password']==n2:
            return render(request,'index1.html')
    return render(request,'index1.html')


def register(request):
    user1=request.POST.get('email')
    password1=request.POST.get('password')
    if password1 is not None:
            user=User(name=user1,password=password1)
            user.save()
            return render(request,'index1.html')
    return render(request,'index1.html')

def func(para,b):
        option=Content.objects.all()
        a=type
        option1=Webpage.objects.filter(type=para).values()
        option2=Content.objects.filter(type=para).values()
        return render(b,'men3.html',{'values':option1,'value':option2,'val':option})
def func2(para,b):
        a=type
        option=Content.objects.all()
        option1=Webpage.objects.filter(type='search').values()
        option2=Content.objects.filter(Q(typ2__contains=para) | Q(name__contains=para)).values()
        return render(b,'men3.html',{'values':option1,'value':option2,'v':para,'val':option})

def func1(para,b):
        a=type
        option=Content.objects.all()
        option1=Webpage.objects.filter(type=para).values()
        option2=Content.objects.filter(type=para).values()
        return render(b,'men4.html',{'values':option1,'value':option2,'val':option})


def index(request):
        option=Content.objects.all()
        option2=Content.objects.filter(type='home').values()
        return render(request,'index1.html',{'value':option2,'values':option})



def men(request):
        option1=Webpage.objects.filter(type='men').values()
        option2=Content.objects.filter(Q(type='men') | Q(type='dad')|Q(type='teenboys')|Q(type='boyfriend')|Q(type='husband')).values()
        return render(request,'men3.html',{'values':option1,'value':option2})

def women(request):
        option1=Webpage.objects.filter(type='women').values()
        option2=Content.objects.filter(Q(type='women')| Q(type='mom')|Q(type='teengirls')).values()
        return render(request,'men3.html',{'values':option1,'value':option2})

def dad(request):
        return func1('dad',request)


def mom(request):
        return func('mom',request)


def kids(request):
        return func('kids',request)


def teenboys(request):
        return func1('teenboys',request)


def teengirls(request):
        return func1('teengirls',request)


def boyfriend(request):
        return func('boyfriend',request)


def husband(request):
        return func('husband',request)


def couples(request):
        return func('couples',request)


def wife(request):
        return func('wife',request)


def persons(request):
        return func('persons',request)


def coworkers(request):
        return func('coworkers',request)


def boss(request):
        return func('boss',request)


def grandma(request):
        return func('grandma',request)


def fathersday(request):
        return func1('fathersday',request)

def girlfriend(request):
        return func1('girlfriend',request)

def mothersday(request):
        return func1('mothersday',request)



def valentine(request):
        option1=Webpage.objects.filter(type='valentine').values()
        option2=Content.objects.filter(type='valentine').values()
        return render(request,'men3.html',{'values':option1,'value':option2})

def aniversary(request):
        option1=Webpage.objects.filter(type='anniversary').values()
        option2=Content.objects.filter(type='anniversary').values()
        return render(request,'men3.html',{'values':option1,'value':option2})





def whiteelephanth(request):
        return func1('whiteelephanth',request)


def secretsanta(request):
        return func1('secretsanta',request)


def uglychristmas(request):
        return func1('uglychristmas',request)


def graduation(request):
        return func('graduation',request)


def engagement(request):
        return func1('engagement',request)

def search(request,genre=a):
        name=request.POST.get('query')
        print(name)
        return func2(name,request)
def groomsmen(request):
        return func1('groomsmen',request)


def bridesmaids(request):
        return func('bridesmaids',request)


def wedding(request):
        return func1('wedding',request)


def housewarming(request):
        return func1('housewarming',request)


def stockingboys(request):
        return func('stockingboys',request)


def birthdaygift(request):
        option1=Webpage.objects.filter(type='birthdaygift').values()
        option2=Content.objects.filter(type='birthdaygift').values()
        return render(request,'men4.html',{'values':option1,'value':option2})


def personalizedgifts(request):
        return func('personalizedgifts',request)


def workfromhome(request):
        return func1('workfromhome',request)


def funny(request):
        return func('funny',request)


def pranks(request):
        return func1('pranks',request)


def gaggifts(request):
        return func1('gaggifts',request)


def geek(request):
        return func1('geek',request)


def gamers(request):
        return func1('gamers',request)


def movie(request):
        return func1('movie',request)


def starwars(request):
        return func1('starwars',request)


def harrypotter(request):
        return func1('harrypotter',request)


def travel(request):
        return func1('travel',request)


def campingandoutdoor(request):
        return func1('campingandoutdoor',request)


def apoclypsesurvival(request):
        return func('apoclypsesurvival',request)


def food(request):
        return func1('food',request)


def coffee(request):
        return func1('coffee',request)


def chocolate(request):
        return func1('chocolate',request)


def wine(request):
        return func('wine',request)


def allgiftsguide(request):
        return render(request,'guides.html')



def random(request):
        return func('random',request)


def submitaproduct(request):
        return render(request,'submitprd.html')


def contactus(request):
        name1=request.POST.get('name')
        type1=request.POST.get('topic')
        email1=request.POST.get('email')
        message1=request.POST.get('message')
        if name1 is not None:
                user=Contact(name=name1,type=type1,email=email1,message=message1)
                user.save()
                return render(request,'contact.html')
        return render(request,'contact.html')


def login(request):
        return func('login',request)



def girlfriend(request):
        return func('girlfriend',request)


def men4(request):
        option1=Webpage.objects.filter(type='men4').values()
        return render(request,'men4.html',{'values':option1})# Create your views here.

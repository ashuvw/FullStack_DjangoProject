from django.shortcuts import render
from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from.models import Post,Like

def index(request):
    user=request.user
    print(user)
    return HttpResponse("Hello world!")



def home(request):  

    return render(request,'home.html')  





def postview(request):
    qs=Post.objects.all(); 
    user=request.user;
    print(qs); 
    print(user); 


    context={

                'qs':qs,
                'user':user
    }

    



    return render(request,'home.html',context)     




def likepost(request): 
    user=request.user
    print(user) 
    if request.method == 'POST':
        postid=request.POST.get('obj.id')
        print(postid) 
        postobj=Post.objects.get(id=postid)
        if user in postobj.liked.all():
            print(user) 
            Post.obj.liked.remove(user)
        else:
                postobj.liked.add(user)



        like, created=Like.objects.get_or_create(user=user,postid=postid)
        
        
        
        
        if not created:
            if like.value =='Like':
                like.value='Unlike'
            else:  
                like.value =='Like'  


        like.save()              
        
        








    return redirect(postview)  

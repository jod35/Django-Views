from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import MyForm
from .models import User
from django.views.generic import UpdateView
from django.core.paginator import Paginator

class MyView(View):
    template_name='blog/index.html'
    form_class=MyForm
    initial={'key':'value'}

    def get(self,request,*args,**kwargs):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            confirm=form.cleaned_data['confirm']

            new_user=User(username=username,email=email,password=password)

            new_user.save()

            print("User Created")
            return redirect('blog:users')

        return render(request,self.template_name,{'form':form})


def listing(request):
    users=User.objects.all()
    paginator=Paginator(users,2)

    page_number=request.GET.get('page')

    page_obj=paginator.get_page(page_number)

    return render(request,'blog/users.html',{'page_obj':page_obj})

def delete(request,id):
    user=get_object_or_404(User,id=id)

    user.delete()

    return redirect('blog:users')


class UserUpdateView(UpdateView):
    model = User
    template_name = "blog/update.html"
    success_url='/users'
    fields=['username','email','password']





        


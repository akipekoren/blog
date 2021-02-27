from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Category
from .forms import PostForms,EditForms
from django.urls import reverse_lazy


# Create your views here.


"""
def home(req):
    return render(req, 'home.html', {})
"""


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']
    #ordering = ['-id']

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DetailsView(DetailView):
    model = Post
    template_name='details.html'


    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DetailsView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context  


class AddPostView(CreateView):
    model = Post
    form_class = PostForms
    template_name = 'addPost.html'
    #fields = '__all__'
    #fields=('title', 'body')



class EditPostView(UpdateView):
    model = Post
    form_class = EditForms
    template_name = 'editPost.html'
    #fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')




class AddCategoryView(CreateView):
    model = Category
    template_name = 'addCategory.html'
    fields = '__all__'
    #fields=('title', 'body')



def CategoryView(request,cats):
    print(cats.replace('-', ' ').title())
    category_posts = Post.objects.filter(category=(cats.replace('-', ' ')).title())

    return render(request, 'categories.html', {'cats' : cats.replace('-', ' ').title(), 'category_posts' : category_posts})


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categoryList.html',{'cat_menu_list' : cat_menu_list})




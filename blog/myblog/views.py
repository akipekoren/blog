from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Category,Comment
from .forms import PostForms,EditForms,AddCommentForms
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage


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

        post_items = Post.objects.all().order_by('-date')


        p = Paginator(post_items,5)
        page_num = self.request.GET.get('page',1)

        try:
            page =p.page(page_num)      
        except EmptyPage:
            page = p.page(1)

        context["post_items"] = page
        return context




class DetailsView(DetailView):
    model = Post
    template_name='details.html'


    def get_context_data(self,*args, **kwargs):
        
        cat_menu = Category.objects.all()
        context = super(DetailsView, self).get_context_data(*args, **kwargs)

        count_total_likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = count_total_likes.get_total_likes()

        liked = False
        if count_total_likes.likes.filter(id = self.request.user.id).exists():
            liked= True
        context["cat_menu"] = cat_menu
        context["total_likes"] =total_likes
        context["liked"] = liked
        context["commentform"] = AddCommentForms()
        return context  

    def post(self,request,pk):
        post = get_object_or_404(Post, pk=pk)
        form =AddCommentForms(request.POST)
        if form.is_valid():
           obj  = form.save(commit=False)
           obj.post = post
           obj.author = self.request.user
           obj.save()
           return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))



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
    category_posts = Post.objects.filter(category=(cats.replace('-', ' ')).title())

    return render(request, 'categories.html', {'cats' : cats.replace('-', ' ').title(), 'category_posts' : category_posts})


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categoryList.html',{'cat_menu_list' : cat_menu_list})


def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


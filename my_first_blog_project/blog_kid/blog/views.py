from blog.models import Post,comment
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,
CreateView,ListView,DetailView,UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm,commentForm
from django.urls import reverse_lazy




# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(publish_Date__lte=timezone.now()).order_by('-publish_date'))
        # اولا در اینجا 
        # lte به معنی 
        # less than or equal to 
        # هست دوما در order_by 
        # وقتی منها مینویسیم یعنی برای ما نزولی سورت کنه

class PostDetailView(DetailView):
    model = Post

class CreatePostView(CreateView,LoginRequiredMixin):
    model = Post
    # اگر بخواهیم که هیچ کسی به این ویو به جز اعضا دست رسی نداشته باشد
    # مثل @login_required بجای آن از میکس اینز استفاده میکنیم
    # mixins
    # حالا باید یک لینک برای لاگین کردن بهش بدیم
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm


class UpdatePostView(UpdateView,LoginRequiredMixin):
    model = Post

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm

    
class PostDeleteView(DeleteView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(ListView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_Date__isnull=True).order_by('created_date')


#####################################
#####################################
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk = pk) # یک آبجکت از پست بساز
    if request.method == 'POST':
        from = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk = post.pk)
        else:
            form = commentForm()
        return render ( request , ' blog/comment_form.html',{'form': form})
@login_required
def comment_approve (requst, pk):
    comment = get_object_or_404(comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk = comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(comment,pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk = post_pk)


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.publish()
    return redirect('post_detail',pk = pk)

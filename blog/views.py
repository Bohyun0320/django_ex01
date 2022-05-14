from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/post_list.html'

class PostDetail(DetailView):
    model = Post

    
# FBV 형식으로 구현할 때 사용한 코드
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
# 
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )
# 
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
# 
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post,
#         }
#     )

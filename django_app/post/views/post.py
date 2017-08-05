from django.contrib.auth import get_user_model

from ..models.post import Post

User = get_user_model()



# def post_list_original(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#     }
#     return render(request, )
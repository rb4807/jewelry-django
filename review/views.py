from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from django.contrib.auth.decorators import login_required

#personal comments list 


@login_required
def comments_list(request):
    user_comments = Comment.objects.filter(user=request.user)
    return render(request, 'review/comments.html', {'user_comments': user_comments})

# create comments

@login_required
def create_comment(request):
    if request.method == 'POST':
        text = request.POST.get('comment_text') 
        files = request.FILES.get('files') 
        Comment.objects.create(user=request.user, text=text,files=files)
        return redirect('create_comment')
    else:
        comments = Comment.objects.all()
        return render(request, 'review/create_comment.html', {'comments': comments})

# update comments

@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.text = request.POST.get('comment_text')
        comment.files = request.FILES.get('files')
        comment.save()
        return redirect('create_comment')
    return render(request, 'review/update_comment.html', {'comment': comment})

# delete comments

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('comments_list')
    return render(request, 'review/comments.html', {'comment': comment})

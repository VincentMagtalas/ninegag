
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse

from .forms import UserRegistrationForm, PostForm,CommentForm,SubCommentForm,VoteForm
from .services import get_posts, get_post_detail
from comment.models import Comment,Vote,SubComment


#User Regiustration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                errors = 'Looks like a username with that email or password already exists'
                return render(request, 'registration/register.html', {'form' : form,'errors' : errors})

    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})

#post
def post_list(request):
    posts = get_posts()
    return render(request, 'posts/post_list.html', posts)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_new.html', {'form': form})

def post_detail(request, pk):
    post = get_post_detail(pk)
    return render(request, 'posts/post_detail.html', post)

def post_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.owner = request.user
        comment.upvote = 0
        comment.downvote = 0
        comment.save()
        return redirect('post_detail',pk=pk)

def comment_subcomment(request, pk):
    form = SubCommentForm(request.POST)
    if form.is_valid():
        subcomment = form.save(commit=False)
        subcomment.owner = request.user
        subcomment.upvote = 0
        subcomment.downvote = 0
        subcomment.save()
        return redirect('post_detail',pk=pk)

def vote_comment(request, pk):
    if 'btnUpVote' in request.POST:
        #validate
        if Vote.objects.filter(commentid=request.POST['commentid'],owner=request.user).exists():
            pass
            return redirect('post_detail', pk=pk)
        else:
            form = VoteForm(request.POST)
            if form.is_valid():
                vote = form.save(commit=False)
                vote.owner = request.user
                vote.reaction = True
                vote.save()
                comment = Comment.objects.get(pk=request.POST['commentid'])
                comment.upvote += 1
                comment.save()
                return redirect('post_detail', pk=pk)

    if 'btnDownVote' in request.POST:
        if Vote.objects.filter(commentid=request.POST['commentid'],owner=request.user).exists():
            pass
            return redirect('post_detail', pk=pk)
        else:
            form = VoteForm(request.POST)
            if form.is_valid():
                vote = form.save(commit=False)
                vote.owner = request.user
                vote.reaction = False
                vote.save()
                comment = Comment.objects.get(pk=request.POST['commentid'])
                comment.downvote += 1
                comment.save()
                return redirect('post_detail', pk=pk)

def vote_subcomment(request, pk):
    if 'btnUpVote' in request.POST:
        # validate
        if Vote.objects.filter(subcommentid=request.POST['subcommentid'], owner=request.user).exists():
            pass
            return redirect('post_detail', pk=pk)
        else:
            form = VoteForm(request.POST)
            if form.is_valid():
                vote = form.save(commit=False)
                vote.owner = request.user
                vote.reaction = True
                vote.save()

                subcomment = SubComment.objects.get(pk=request.POST['subcommentid'])
                subcomment.upvote += 1
                subcomment.save()

                return redirect('post_detail', pk=pk)

    if 'btnDownVote' in request.POST:
        if Vote.objects.filter(subcommentid=request.POST['subcommentid'], owner=request.user).exists():
            pass
            return redirect('post_detail', pk=pk)
        else:
            form = VoteForm(request.POST)
            if form.is_valid():
                vote = form.save(commit=False)
                vote.owner = request.user
                vote.reaction = False
                vote.save()
                subcomment = SubComment.objects.get(pk=request.POST['subcommentid'])
                subcomment.downvote += 1
                subcomment.save()
                return redirect('post_detail', pk=pk)


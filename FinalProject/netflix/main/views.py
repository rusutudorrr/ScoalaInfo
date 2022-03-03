from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from main.models import Profile, Movie


def homepage(request):
    if request.user.is_authenticated:
        return redirect('main:profile_list')
    return render(request, 'index.html')


@login_required
def profilelist(request):
    profiles = request.user.profiles.all()
    return render(request, 'profileList.html', {
        'profiles': profiles
    })


@method_decorator(login_required, name='dispatch')
class NewProfile(View):
    def get(self, request, *args, **kwargs):
        # Form for profile creation
        form = ProfileForm()
        return render(request, 'profileCreate.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)

        if form.is_valid():
            # Will redirect user to where they choose their profile
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                # it checks the profiles here
                request.user.profiles.add(profile)
                return redirect('main:profile_list')
        return render(request, 'profileCreate.html', {
            'form': form
        })


@login_required
def browse(request, profile_id):
    try:
        profile = Profile.objects.get(uuid=profile_id)
        movies = Movie.objects.filter(age_limit=profile.age_limit)

        if profile not in request.user.profiles.all():
            return redirect(to='main:profile_list')

        return render(request, 'movieList.html', {
            'movies': movies,
            })

    except Profile.DoesNotExist:
        return redirect(to='main:profile_list')


@login_required
def moviedetail(request, movie_id):
    try:
        movie = Movie.objects.get(uuid=movie_id)

        return render(request, 'movieDetail.html', {
               'movie': movie
        })
    except Movie.DoesNotExist:
        return redirect('main:profile_list')


@login_required
def playbutton(request, movie_id):
    try:
        movie = Movie.objects.get(uuid=movie_id)
        movie = movie.videos.values()

        return render(request, 'moviePlay.html', {
            'movie': list(movie)
        })
    except Movie.DoesNotExist:
        return redirect('main:profile_list')

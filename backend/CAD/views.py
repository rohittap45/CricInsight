# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .cric_api import get_live_matches,get_live_match_data

# home page view
def home(request):
    return render(request,'CAD/index.html')

# user register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect( 'CAD:login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# user login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('CAD:profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

# user logout view
@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

# user profile view
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('CAD:live_matches')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'main/profile.html', context)

# live matches 
def live_matches(request):
    data = get_live_matches()
    matches = data.get('data', [])

    return render(request, 'CAD/live_matches.html',{'matches': matches})

# match details and scorecaerd view 
def match_details(request,match_id):
    data = get_live_match_data(match_id)
    match = data.get('data', [])
    return render(request, 'CAD/scorecard.html',{'match': match} )


# Prediction model

import joblib
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

# Load the trained model
model = joblib.load('ipl_victory_predictor.pkl')

# Define lists for dropdown options
teams = [
    "Gujarat Titans", "Rajasthan Royals", "Lucknow Super Giants", "Punjab Kings",
    "Mumbai Indians", "Royal Challengers Bangalore", "Kolkata Knight Riders",
    "Sunrisers Hyderabad", "Delhi Capitals", "Chennai Super Kings"
]

cities = [
    "Ahmedabad", "Kolkata", "Mumbai", "Navi Mumbai", "Pune", "Dubai", "Sharjah",
    "Abu Dhabi", "Delhi", "Chennai", "Hyderabad", "Visakhapatnam", "Chandigarh",
    "Bengaluru", "Jaipur", "Indore", "Bangalore", "Kanpur", "Rajkot", "Raipur",
    "Ranchi", "Cuttack", "Dharamsala", "Kochi", "Nagpur", "Johannesburg",
    "Centurion", "Durban", "Bloemfontein", "Port Elizabeth", "Kimberley",
    "East London", "Cape Town", "Lucknow", "Guwahati"
]

wickets =["1","2","3","4","5","6","7","8","9","10"]

# Ipl victory predictiion view
 
def predict_victory(request):
    if request.method == 'POST':
        batting_team = request.POST.get('batting_team')
        bowling_team = request.POST.get('bowling_team')
        city = request.POST.get('city')
        runs_left = int(request.POST.get('runs_left'))
        balls_left = int(request.POST.get('balls_left'))
        wickets_remaining = int(request.POST.get('wickets_remaining'))
        total_run_x = int(request.POST.get('total_run_x'))
     

        data = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets_remaining': [wickets_remaining],
            'total_run_x': [total_run_x],
            
        })

        prediction = model.predict_proba(data)
        team1_win_probability = prediction[0][1] * 100
        team2_win_probability = prediction[0][0] * 100

        context = {
            'batting_team': batting_team,
            'bowling_team': bowling_team,
            'team1_win_probability': team1_win_probability,
            'team2_win_probability': team2_win_probability,
        }

        return render(request, 'CAD/predict_result.html', context)

    context = {
        'teams': teams,
        'cities': cities,
        'wickets':wickets,
    }
    return render(request, 'CAD/predict.html', context)

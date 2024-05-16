import datetime
import pyjokes
import pywhatkit
from django.shortcuts import render, redirect
import speech_recognition as sr
import pyttsx3
import webbrowser
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Destination, Movies, Shows, Kdrama
from .models import Local_news
from .models import International_news
from .models import National_news
from .models import desi_car
from .models import anime
from .models import car_mov
from .models import Games


def index(request):
    # Query all Destination objects from the database
    dests = Destination.objects.all()
    return render(request, 'index1.html', {'dests': dests})


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        name1 = request.POST["firstName"]
        name2 = request.POST["lastName"]
        username = request.POST["username"]
        password1 = request.POST["password"]
        password2 = request.POST["confirmPassword"]
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists! Please try another one.")
                return render(request, "register.html")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "email already exists! Please try another one.")
                return render(request, "register.html")
            else:
                user = User.objects.create_user(first_name=name1, last_name=name2, username=username,
                                                password=password1, email=email)
                user.save()
                messages.success(request, "Registration Successful! You can now login.")
                return render(request, "login.html")

        else:
            messages.error(request, "Password didn't match with Confirmpassword")
    return render(request, 'register.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        name1 = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=name1, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfull")
            return redirect('/')
        else:
            messages.error(request, "Enter Correct Credentials!")
            return redirect('login')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return render(request, 'login.html')


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def contact(request):
    return render(request, 'contact.html')


def voice_assistant(request):
    if request.method == 'POST':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak('listening...!')
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio).lower()
            print(f"User said: {query}")
            response_text = process_query(query)
            response_data = {'text': response_text}
        except Exception as e:
            speak("Could not understand audio.")

    return render(request, 'index1.html')


def process_query(query):
    if 'open youtube' in query:
        webbrowser.open('https://www.crazygames.com/game/evowarsio/')
        speak("Opening YouTube.")
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M%p')
        speak("The current time is " + time)
    elif 'wish' in query:
        speak("Hello! How can I assist you today?")
    elif 'joke' in query:
        a = pyjokes.get_joke()
        print(a)
        speak(a)
    elif 'news' in query:
        url = 'http://localhost:8000/news/'
        webbrowser.open(url)
        speak('opening news')
    elif 'music' in query:
        url = 'http://localhost:8000/news/'
        webbrowser.open(url)
        speak('opening news')
    elif 'sports' in query:
        url = 'http://localhost:8000/sports/'
        webbrowser.open(url)
        speak('opening sports')
    elif 'entertainment' in query:
        url = 'http://localhost:8000/entertainment/'
        webbrowser.open(url)
        speak('opening entertainment')
    elif ' cartoons' in query:
        url = 'http://localhost:8000/cartoon/'
        webbrowser.open(url)
        speak('opening cartoons')
    elif 'etv' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/news/play/ETV'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'ntv' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/news/play/NTV'
        webbrowser.open(url)
        speak(song)
    elif 'abn' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/news/play/ABN'
        webbrowser.open(url)
        speak(song)
    elif 'tv9 telugu' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/news/play/TV9_telugu'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'tv9 hindi' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/news/play/TV9_hindi'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'tv9 kannada' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/news/play/TV9_kannada'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'tv5' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/news/play/TV5news'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'sun news' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/news/play/sunnews'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'tv18 ' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/news/play/CNBC'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'bahubali' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/baahubali'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'bbc' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/news/play/BBC'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'aravinda' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/aravinda'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'legend' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/legend'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'okkadu' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/okkadu'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'zindagi' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/zindagi'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'iifaa' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/iifa'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'zee cine' in query:
        query.lower()
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/zee'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'ritesh' in query:
        query.lower()
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/riteish'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'hrithik' in query:
        query.lower()
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/hrithik'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'siima' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/siima'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'lost' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/lost'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'venom' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/venom'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'american' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/american'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'nun' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/nun'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'mysterious' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/entertainment/play/mysterious'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'chhota bheem' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/cartoon/play/bheem'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'oggy' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/cartoon/play/oggy'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'bean' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/cartoon/play/bean'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'courage' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/cartoon/play/cou'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'doraemon' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/cartoon/play/dora'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'doraemon Movie' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/cartoon/play/doramov'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'nemo' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/cartoon/play/nemo'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'good' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/cartoon/play/good'
        webbrowser.open(url)
        speak("Playing" + song)
    elif '2048' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/games/twenty'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'subway' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/games/play_evowars'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'hill' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/games/hill'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'moto' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/games/bike'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'temple' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/games/temple'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'rope' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/games/cut'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'bubble' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/games/bubble'
        webbrowser.open(url)
        speak("Playing" + song)

    else:
        speak("I'm sorry, I don't understand that command.")


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


@login_required
def news(request):
    objects = Local_news.objects.all()
    objects1 = National_news.objects.all()
    objects2 = International_news.objects.all()
    return render(request, 'news.html', {'objects': objects, 'objects1': objects1, 'objects2': objects2})


@login_required
def music(request):
    return render(request, 'music_page.html')


@login_required
def entertainment(request):
    objects = Movies.objects.all()
    objects1 = Shows.objects.all()
    objects2 = Kdrama.objects.all()
    return render(request, 'entertainment.html', {'objects': objects, 'objects1': objects1, 'objects2': objects2})


@login_required
def cartoon(request):
    objects = desi_car.objects.all()
    objects1 = anime.objects.all()
    objects2 = car_mov.objects.all()
    return render(request, 'cartoon.html', {'objects': objects, 'objects1': objects1, 'objects2': objects2})


@login_required
def after_ETVTelugu(request):
    abcd = 'uEAmtfwKuX0'
    return render(request, 'news_respg.html', {'source': abcd})


@login_required
def after_NTV(request):
    abcd = 'L0RktSIM980'
    return render(request, 'news_respg.html', {'source': abcd})


@login_required
def after_ABN(request):
    abcd = 'Q-nSNssz3p0'
    return render(request, 'news_respg.html', {'source': abcd})


@login_required
def after_TV9telugu(request):
    abcd = 'II_m28Bm-iM'
    return render(request, 'news_respg.html', {'source': abcd})


@login_required
def after_TV9hindi(request):
    abcd = 'bxZSoCw6JW0'
    return render(request, 'news_respg.html', {'source': abcd})


@login_required
def after_TV9kannada(request):
    abcd = 'jdJoOhqCipA'
    return render(request, 'news_respg.html', {'source': abcd})


@login_required
def after_TV5news(request):
    abcd = 'MQr6p9TrPyQ'
    return render(request, 'news_respg.html', {'source': abcd})


@login_required
def after_sunnews(request):
    abcd = '9M02G5c6x6w'
    return render(request, 'news_respg.html', {'source': abcd})


@login_required
def after_CNBC(request):
    abcd = '1_Ih0JYmkjI'
    return render(request, 'news_respg.html', {'source': abcd})


@login_required
def after_BBC(request):
    abcd = 'w9uJg68CV4g'
    return render(request, 'news_respg.html', {'source': abcd})


@login_required
def after_bahubali(request):
    abcd = 'u3Zcaeei_H8'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_aravinda(request):
    abcd = 'JPs8EoPHtV8'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_legend(request):
    abcd = 'Px5nHPQZ-1o'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_jawani(request):
    abcd = 'qXgUlhSzlXI'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_zindagi(request):
    abcd = 'lHubgWDweAE'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_iifa(request):
    abcd = 'czjq5PlyFpw'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_cine(request):
    abcd = 'n9oyDtfACo8'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_riteish(request):
    abcd = '-Qb-0uWsGkI'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_hrithik(request):
    abcd = 'Qmpb2XPPtCg'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_siima(request):
    abcd = 'byvqAINMJYI'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_lost(request):
    abcd = 'jqd-OHU7OMw'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_venom(request):
    abcd = 'nZ6txXT1uSw'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_american(request):
    abcd = '4XXDw_PbLJE'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_nun(request):
    abcd = 'Y0IkU7yV-KU'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_myst(request):
    abcd = 'qG5VkoPXPuA'
    return render(request, 'entertainment_respg.html', {'source': abcd})


@login_required
def after_bheem(request):
    abcd = 'eTVYvG44cNM'
    return render(request, 'cartoon_respg.html', {'source': abcd})


@login_required
def after_oggy(request):
    abcd = '9cmae_aFhTs'
    return render(request, 'cartoon_respg.html', {'source': abcd})


@login_required
def after_bean(request):
    abcd = 'GIhq_I6LClo'
    return render(request, 'cartoon_respg.html', {'source': abcd})


@login_required
def after_cou(request):
    abcd = 'H40v3ISrHhQ'
    return render(request, 'cartoon_respg.html', {'source': abcd})


@login_required
def after_dora(request):
    abcd = 'I-Lv9YWXd48'
    return render(request, 'cartoon_respg.html', {'source': abcd})


@login_required
def after_doramov(request):
    abcd = '34Ud1CSDY7M'
    return render(request, 'cartoon_respg.html', {'source': abcd})


@login_required
def after_nemo(request):
    abcd = 'GjiZRzDVBBY'
    return render(request, 'cartoon_respg.html', {'source': abcd})


@login_required
def after_good(request):
    abcd = '3KPIgP7PBmg'
    return render(request, 'cartoon_respg.html', {'source': abcd})


def play_evowars(request):
    return render(request, 'play_evowars.html')


def hill(request):
    return render(request, 'hill.html')


def bike(request):
    return render(request, 'bike.html')


def temple(request):
    return render(request, 'temple.html')


def cut(request):
    return render(request, 'cut.html')


def bubble(request):
    return render(request, 'bubble.html')


def twenty(request):
    return render(request, '2048.html')


def games(request):
    # Query all Destination objects from the database
    dests1 = Games.objects.all()
    return render(request, 'games.html', {'dests1': dests1})


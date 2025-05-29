from .models import Utilisateur, Pub
import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request, 'football/index.html')

def pubs(request):
    pubs = Pub.objects.all()
    return render(request, 'football/pubs.html', {'pubs': pubs})

def abonnement_step1(request):
    code_envoye = False
    error = ""
    gmail = ""
    username = ""
    if request.method == "POST":
        if "send_code" in request.POST:
            username = request.POST.get("username")
            gmail = request.POST.get("gmail")
            code = str(random.randint(100000, 999999))
            request.session['abonnement'] = {
                'username': username,
                'gmail': gmail,
                'code': code
            }
            send_mail(
                "Votre code de validation FoudeFoot",
                f"Votre code de validation est : {code}",
                "noreply@foudefoot.com",
                [gmail],
                fail_silently=False,
            )
            code_envoye = True
        elif "validate_code" in request.POST:
            code = request.POST.get("code")
            data = request.session.get('abonnement')
            if data and code == data['code']:
                return redirect('abonnement_step3')
            else:
                code_envoye = True
                gmail = data['gmail'] if data else ""
                username = data['username'] if data else ""
                error = "Code invalide."
    return render(request, "football/abonnement_step1.html", {
        "code_envoye": code_envoye,
        "gmail": gmail,
        "username": username,
        "error": error
    })
def abonnement_step2(request):
    data = request.session.get('abonnement')
    if not data:
        return redirect('abonnement_step1')
    error = ""
    if request.method == "POST":
        code = request.POST.get("code")
        if code == data['code']:
            return redirect('abonnement_step3')
        else:
            error = "Code invalide."
    return render(request, "football/abonnement_step2.html", {"gmail": data['gmail'], "error": error})

def abonnement_step3(request):
    data = request.session.get('abonnement')
    if not data:
        return redirect('abonnement_step1')
    error = ""
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        genre = request.POST.get("genre")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password != password2:
            error = "Les mots de passe ne correspondent pas."
        else:
            data['nom'] = nom
            data['prenom'] = prenom
            data['genre'] = genre
            data['password'] = make_password(password)
            request.session['abonnement'] = data
            return redirect('abonnement_step4')
    return render(request, "football/abonnement_step3.html", {"error": error})

def abonnement_step4(request):
    data = request.session.get('abonnement')
    if not data:
        return redirect('abonnement_step1')
    if request.method == "POST":
        paiement = request.POST.get("paiement")
        data['paiement'] = paiement
        User.objects.create(
            username=data['username'],
            first_name=data['prenom'],
            last_name=data['nom'],
            email=data['gmail'],
            password=data['password'],
        )
        del request.session['abonnement']
        return render(request, "football/abonnement_success.html")
    return render(request, "football/abonnement_step4.html")

def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'football/utilisateurs.html', {'utilisateurs': utilisateurs})

def envoyer_pub(request):
    abonnes = Utilisateur.objects.filter(est_abonne=True)
    pub = Pub.objects.latest('date_pub')
    for abonne in abonnes:
        send_mail(
            'Nouvelle publicité footballistique !',
            pub.contenu,
            'noreply@foudefoot.com',
            [abonne.email],
            fail_silently=False,
        )
    return render(request, 'football/envoyer_pub.html', {'message': "Emails envoyés avec succès !"})
from django.shortcuts import render
from django.http import HttpResponse
from CARTAS.models import Serie , Juego , Pelicula


# Create your views here

def ver_serie(request):

    mis_series = Serie.objets.all()
    info = {"series":mis_series}

    return render(request, "CARTAS/series.html", info)


def ver_juego(request):

    mis_juego = Juego.objets.all()
    info = {"series":mis_juego}

    return render(request, "CARTAS/juego.html", info)


def ver_pelicula(request):

    mis_pelicula = Pelicula.objets.all()
    info = {"series":mis_pelicula}

    return render(request, "CARTAS/peliculas.html", info)



def inicio(request): 

    return render(request,"CARTAS/inicio.html")


def agregar_serie(request):
    
    serie1 = Serie(nombre = "YUGIOH DUEL MONSTERS", año = 2004, invocacion = "sacrificio", personaje = "Yugi Muto") #Crear un objeto usando el modulo
    serie1.save()

    return HttpResponse("Se agrego una serie..")



def agregar_juego(request):
    
    juego1 = Juego(nombre = "YUGIOH Duel Link", año = 2006, invocacion = "sacrificio,especial,xyz,sincro,pendulo", personaje = "Yugi Muto, Seto Kaiba") #Crear un objeto usando el modulo
    juego1.save()

    return HttpResponse("Se agrego un juego..")


def agregar_pelicula(request):
    
    pelicula1 = Pelicula(nombre = "YUGIOH ", año = 2007, invocacion = "sacrificio,especial,xyz,sincro,pendulo", personaje = "Yugi Muto, Seto Kaiba, Joy willer") #Crear un objeto usando el modulo
    pelicula1.save()

    return HttpResponse("Se agrego un juego..")



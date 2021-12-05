import geocoder  ##--importer pour determiner la localisation d'ip
import folium  ##--importer pour marquer l'ip sur map
import webbrowser  ##-- importer pour ouvrir le fichier ".html" sur web


def getIP():  # fontion pour saisir l'IP adresse
    while True:  # boucle while pour verifier que IP n'est pas vide
        ip = input('\nDonner adress ip: ')  # entrer l'IP adresse
        if ip != []:  # verification: si ip n'est pas vide faire
            break  # sortir
        else:  # ip est vide
            print('\nverifier votre IP adresse')  # message d erreur
    return ip  # retourner ip


def localisation(ip):  # fonction localisation
    geo = geocoder.ip(ip)  # collecter des donnees sur IP adresse
    address = geo.latlng  # retourner 'lattitude' et 'longitude' de ip adresse sous la forme [lat,lng]
    map = folium.Map(address, zoom_start=12)  # creation map
    folium.Marker(address, popup=ip, tooltip='localisation ip', icon=folium.Icon(color='red', icon='off')).add_to(
        map)  # marque la localisation d'Ip
    map.save('localisation.html')  # enregistrer map sous forme html


print("localisation d'adresse ip")
ip = getIP()
localisation(ip)
o = input("pour ouvrir la localisation de l'adresse ip sur web taper:[ouvrir]: ").lower()
if (o == "ouvrir"):
    webbrowser.open('localisation.html')  # ouvrir fichier sur web

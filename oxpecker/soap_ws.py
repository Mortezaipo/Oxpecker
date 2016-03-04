from pyws.server import SoapServer
from pyws.functions.register import register
from django.contrib.auth import authenticate
from games.models import Game, Version


server = SoapServer(
    service_name='Oxpecker-WS',
    tns='http://localhost/',
    location='http://localhost:8000/api/',
)


@register()
def authentication(username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            return 'user is valid'
        else:
            return 'user is locked'
    else:
        return 'username or password is incorrect'
    
    
@register()
def search_game(name):
    records = Game.objects.filter(name=name)
    return records


@register()
def fetch_package(game_name, version):
    pass
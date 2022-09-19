from django.urls import path
from mywatchlist.views import home
from mywatchlist.views import show_xml
from mywatchlist.views import show_json 
from mywatchlist.views import show_json_by_id
from mywatchlist.views import show_xml_by_id
from mywatchlist.views import show_watch_list

app_name = 'watchlist'

urlpatterns = [
    path('', home, name='home'),
    path('html', show_watch_list, name="show_watch_list"),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('explore',views.explore,name='explore'),
    path('search/', views.search, name='search'),   
    path('bangle',views.bangle,name='bangle'),
    path('chain',views.chain,name='chain'),
    path('bracelets',views.bracelets,name='bracelets'),
    path('couple',views.couple,name='couple'),
    path('earrings',views.earrings,name='earrings'),
    path('coin',views.coin,name='coin'),
    path('mangalsutra',views.mangalsutra,name='mangalsutra'),
    path('neckwear',views.neckwear,name='neckwear'),
    path('nosepin',views.nosepin,name='nosepin'),
    path('set',views.set,name='set'),
    path('pendant',views.pendant,name='pendant'),
    path('ring',views.ring,name='ring'),
    path('silver_anklet',views.anklet,name='silver_anklet'),
    path('silver_bangle',views.ban,name='silver_bangle'),
    path('silver_bracelet',views.brace,name='silver_bracelet'),
    path('silver_coin',views.co,name='silver_coin'),
    path('silver_earrrings',views.ear,name='silver_earrings'),
    path('silver_necklace',views.neck,name='silver_necklace'),
    path('silver_pendant',views.pen,name='silver_pendant'),
    path('silver_ring',views.ri,name='silver_ring'),
    path('diamond',views.diamond,name='diamond'),
    path('men',views.men,name='men'),
    path('women',views.women,name='women'),
    path('kid',views.kid,name='kid'),
    
]
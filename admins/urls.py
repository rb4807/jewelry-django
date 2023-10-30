from django.urls import path
from . import views

urlpatterns = [

    path('admin_home/',views.admin_home,name='adminhome'),

    ###########################################GOLD#################################################################
    
    path('add_bangle/',views.add_bangle,name='add_bangle'),
    path('admin_bangle',views.admin_bangle,name='admin_bangle'),
    path('update_bangle/<int:bangle_id>/', views.update_bangle, name='update_bangle'),
    path('delete_bangle/<int:bangle_id>/', views.delete_bangle, name='delete_bangle'),

    path('add_chain/',views.add_chain,name='add_chain'),
    path('admin_chain',views.admin_chain,name='admin_chain'),
    path('update_chain/<int:chain_id>/', views.update_chain, name='update_chain'),
    path('delete_chain/<int:chain_id>/', views.delete_chain, name='delete_chain'),

    path('add_bracelets/',views.add_bracelets,name='add_bracelets'),
    path('admin_bracelets',views.admin_bracelets,name='admin_bracelets'),
    path('update_bracelets/<int:bracelets_id>/', views.update_bracelets, name='update_bracelets'),
    path('delete_bracelets/<int:bracelets_id>/', views.delete_bracelets, name='delete_bracelets'),

    path('add_couple/',views.add_couple,name='add_couple'),
    path('admin_couple',views.admin_couple,name='admin_couple'),
    path('update_couple/<int:couple_id>/', views.update_couple, name='update_couple'),
    path('delete_couple/<int:couple_id>/', views.delete_couple, name='delete_couple'),

    path('add_earrings/',views.add_earrings,name='add_earrings'),
    path('admin_earrings',views.admin_earrings,name='admin_earrings'),
    path('update_earrings/<int:earrings_id>/', views.update_earrings, name='update_earrings'),
    path('delete_earrings/<int:earrings_id>/', views.delete_earrings, name='delete_earrings'),

    path('add_coin/',views.add_coin,name='add_coin'),
    path('admin_coin',views.admin_coin,name='admin_coin'),
    path('update_coin/<int:coin_id>/', views.update_coin, name='update_coin'),
    path('delete_coin/<int:coin_id>/', views.delete_coin, name='delete_coin'),

    path('add_mangalsutra/',views.add_mangalsutra,name='add_mangalsutra'),
    path('admin_mangalsutra',views.admin_mangalsutra,name='admin_mangalsutra'),
    path('update_mangalsutra/<int:mangalsutra_id>/', views.update_mangalsutra, name='update_mangalsutra'),
    path('delete_mangalsutra/<int:mangalsutra_id>/', views.delete_mangalsutra, name='delete_mangalsutra'),

    path('add_neckwear/',views.add_neckwear,name='add_neckwear'),
    path('admin_neckwear',views.admin_neckwear,name='admin_neckwear'),
    path('update_neckwear/<int:neckwear_id>/', views.update_neckwear, name='update_neckwear'),
    path('delete_neckwear/<int:neckwear_id>/', views.delete_neckwear, name='delete_neckwear'),

    path('add_nosepin/',views.add_nosepin,name='add_nosepin'),
    path('admin_nosepin',views.admin_nosepin,name='admin_nosepin'),
    path('update_nosepin/<int:nosepin_id>/', views.update_nosepin, name='update_nosepin'),
    path('delete_nosepin/<int:nosepin_id>/', views.delete_nosepin, name='delete_nosepin'),

    path('add_set/',views.add_set,name='add_set'),
    path('admin_set',views.admin_set,name='admin_set'),
    path('update_set/<int:set_id>/', views.update_set, name='update_set'),
    path('delete_set/<int:set_id>/', views.delete_set, name='delete_set'),

    path('add_ring/',views.add_ring,name='add_ring'),
    path('admin_ring',views.admin_ring,name='admin_ring'),
    path('update_ring/<int:ring_id>/', views.update_ring, name='update_ring'),
    path('delete_ring/<int:ring_id>/', views.delete_ring, name='delete_ring'),

    path('add_pendant/',views.add_pendant,name='add_pendant'),
    path('admin_pendant',views.admin_pendant,name='admin_pendant'),
    path('update_pendant/<int:pendant_id>/', views.update_pendant, name='update_pendant'),
    path('delete_pendant/<int:pendant_id>/', views.delete_pendant, name='delete_pendant'),

    ##############################################Silver############################################################

    path('add_anklet/',views.add_anklet,name='add_anklet'),
    path('admin_anklet',views.admin_anklet,name='admin_anklet'),
    path('update_anklet/<int:anklet_id>/', views.update_anklet, name='update_anklet'),
    path('delete_anklet/<int:anklet_id>/', views.delete_anklet, name='delete_anklet'),

    path('add_silver_bangle/',views.add_silver_bangle,name='add_silver_bangle'),
    path('admin_silver_bangle',views.admin_silver_bangle,name='admin_silver_bangle'),
    path('update_silver_bangle/<int:ban_id>/', views.update_silver_bangle, name='update_silver_bangle'),
    path('delete_silver_bangle/<int:ban_id>/', views.delete_silver_bangle, name='delete_silver_bangle'),

    path('add_silver_bracelet/',views.add_silver_bracelet,name='add_silver_bracelet'),
    path('admin_silver_bracelet',views.admin_silver_bracelet,name='admin_silver_bracelet'),
    path('update_silver_bracelet/<int:brace_id>/', views.update_silver_bracelet, name='update_silver_bracelet'),
    path('delete_silver_bracelet/<int:brace_id>/', views.delete_silver_bracelet, name='delete_silver_bracelet'),

    path('add_silver_coin/',views.add_silver_coin,name='add_silver_coin'),
    path('admin_silver_coin',views.admin_silver_coin,name='admin_silver_coin'),
    path('update_silver_coin/<int:co_id>/', views.update_silver_coin, name='update_silver_coin'),
    path('delete_silver_coin/<int:co_id>/', views.delete_silver_coin, name='delete_silver_coin'),

    path('add_silver_earring/',views.add_silver_earring,name='add_silver_earring'),
    path('admin_silver_earring',views.admin_silver_earring,name='admin_silver_earring'),
    path('update_silver_earring/<int:ear_id>/', views.update_silver_earring, name='update_silver_earring'),
    path('delete_silver_earring/<int:ear_id>/', views.delete_silver_earring, name='delete_silver_earring'),

    path('add_silver_neckwear/',views.add_silver_neckwear,name='add_silver_neckwear'),
    path('admin_silver_neckwear',views.admin_silver_neckwear,name='admin_silver_neckwear'),
    path('update_silver_neckwear/<int:neck_id>/', views.update_silver_neckwear, name='update_silver_neckwear'),
    path('delete_silver_neckwear/<int:neck_id>/', views.delete_silver_neckwear, name='delete_silver_neckwear'),

    path('add_silver_ring/',views.add_silver_ring,name='add_silver_ring'),
    path('admin_silver_ring',views.admin_silver_ring,name='admin_silver_ring'),
    path('update_silver_ring/<int:ri_id>/', views.update_silver_ring, name='update_silver_ring'),
    path('delete_silver_ring/<int:ri_id>/', views.delete_silver_ring, name='delete_silver_ring'),

    path('add_silver_pendant/',views.add_silver_pendant,name='add_silver_pendant'),
    path('admin_silver_pendant',views.admin_silver_pendant,name='admin_silver_pendant'),
    path('update_silver_pendant/<int:pen_id>/', views.update_silver_pendant, name='update_silver_pendant'),
    path('delete_silver_pendant/<int:pen_id>/', views.delete_silver_pendant, name='delete_silver_pendant'),

    ##############################################Diamond############################################################

    path('add_diamond/',views.add_diamond,name='add_diamond'),
    path('admin_diamond',views.admin_diamond,name='admin_diamond'),
    path('update_diamond/<int:diamond_id>/', views.update_diamond, name='update_diamond'),
    path('delete_diamond/<int:diamond_id>/', views.delete_diamond, name='delete_diamond'),
    
    ##############################################Staff############################################################

    path('add_staff/',views.add_staff,name='add_staff'),
    path('admin_staff',views.admin_staff,name='admin_staff'),
    path('update_staff/<int:staff_id>/', views.update_staff, name='update_staff'),
    path('delete_staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),

    ############################################## Working ############################################################

    path('add_working/',views.add_working,name='add_working'),
    path('admin_working',views.admin_working,name='admin_working'),
    path('update_working/<int:working_id>/', views.update_working, name='update_working'),
    path('delete_working/<int:working_id>/', views.delete_working, name='delete_working'),


]

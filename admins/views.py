from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from explore.models import Bangle,Chain,Bracelets,Couple,Earrings,Coin,Mangalsutra,Neckwear,Nosepin,Set,Ring,Pendant,Anklet,Ban,Brace,Co,Ear,Neck,Pen,Ri,Diamond,Men,Women,Kid,Product,Diamond
from appointments.models import Staff,Working

def admin_home(request):
    return render(request,'admin/adminhome.html')

############################################GOLD####################################################################

# Bangle

def admin_bangle(request):
    bang = Bangle.objects.all()
    return render(request, 'admin/gold/bangle/admin_bangle.html',{'bang' :bang})

def add_bangle(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Bangle.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_bangle') 
        else:           
            return redirect('admin_bangle') 
    return render(request, 'admin/gold/bangle/add_bangle.html')
    
@login_required
def update_bangle(request, bangle_id):
    bang = get_object_or_404(Bangle, id=bangle_id)
    if request.method == 'POST':
        bang.name = request.POST.get('name')
        bang.image = request.FILES.get('image')
        bang.price = request.POST.get('price')
        bang.save()
        return redirect('admin_bangle')
    return render(request, 'admin/gold/bangle/update_bangle.html', {'bang': bang})

@login_required
def delete_bangle(request, bangle_id):
    bang = get_object_or_404(Bangle, id=bangle_id)
    if request.method == 'POST':
        bang.delete()
        return redirect('admin_bangle')
    return render(request, 'admin/gold/bangle/admin_bangle.html', {'bang': bang})

# Chain

def admin_chain(request):
    chain = Chain.objects.all()
    return render(request, 'admin/gold/chain/admin_chain.html',{'chain' :chain})

def add_chain(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Chain.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_chain') 
        else:           
            return redirect('admin_chain') 
    return render(request, 'admin/gold/chain/add_chain.html')
    
@login_required
def update_chain(request, chain_id):
    chain = get_object_or_404(Chain, id=chain_id)
    if request.method == 'POST':
        chain.name = request.POST.get('name')
        chain.image = request.FILES.get('image')
        chain.price = request.POST.get('price')
        chain.save()
        return redirect('admin_chain')
    return render(request, 'admin/gold/chain/update_chain.html', {'chain': chain})

@login_required
def delete_chain(request, chain_id):
    chain = get_object_or_404(Chain, id=chain_id)
    if request.method == 'POST':
        chain.delete()
        return redirect('admin_chain')
    return render(request, 'admin/gold/chain/admin_chain.html', {'chain': chain})

# Bracelets

def admin_bracelets(request):
    bracelets = Bracelets.objects.all()
    return render(request, 'admin/gold/bracelets/admin_bracelets.html',{'bracelets' :bracelets})

def add_bracelets(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Bracelets.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_bracelets') 
        else:           
            return redirect('admin_bracelets') 
    return render(request, 'admin/gold/bracelets/add_bracelets.html')
    
@login_required
def update_bracelets(request, bracelets_id):
    bracelets = get_object_or_404(Bracelets, id=bracelets_id)
    if request.method == 'POST':
        bracelets.name = request.POST.get('name')
        bracelets.image = request.FILES.get('image')
        bracelets.price = request.POST.get('price')
        bracelets.save()
        return redirect('admin_bracelets')
    return render(request, 'admin/gold/bracelets/update_bracelets.html', {'bracelets': bracelets})

@login_required
def delete_bracelets(request, bracelets_id):
    bracelets = get_object_or_404(Bracelets, id=bracelets_id)
    if request.method == 'POST':
        bracelets.delete()
        return redirect('admin_bracelets')
    return render(request, 'admin/gold/bracelets/admin_bracelets.html', {'bracelets': bracelets})

# Couple Ring

def admin_couple(request):
    couple = Couple.objects.all()
    return render(request, 'admin/gold/couple/admin_couple.html',{'couple' :couple})

def add_couple(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Couple.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_couple') 
        else:           
            return redirect('admin_couple') 
    return render(request, 'admin/gold/couple/add_couple.html')
    
@login_required
def update_couple(request, couple_id):
    couple = get_object_or_404(Couple, id=couple_id)
    if request.method == 'POST':
        couple.name = request.POST.get('name')
        couple.image = request.FILES.get('image')
        couple.price = request.POST.get('price')
        couple.save()
        return redirect('admin_couple')
    return render(request, 'admin/gold/couple/update_couple.html', {'couple': couple})

@login_required
def delete_couple(request, couple_id):
    couple = get_object_or_404(Couple, id=couple_id)
    if request.method == 'POST':
        couple.delete()
        return redirect('admin_couple')
    return render(request, 'admin/gold/couple/admin_couple.html', {'couple': couple})

# Earrings

def admin_earrings(request):
    earrings = Earrings.objects.all()
    return render(request, 'admin/gold/earrings/admin_earrings.html',{'earrings' :earrings})

def add_earrings(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Earrings.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_earrings') 
        else:           
            return redirect('admin_earrings') 
    return render(request, 'admin/gold/earrings/add_earrings.html')
    
@login_required
def update_earrings(request, earrings_id):
    earrings = get_object_or_404(Earrings, id=earrings_id)
    if request.method == 'POST':
        earrings.name = request.POST.get('name')
        earrings.image = request.FILES.get('image')
        earrings.price = request.POST.get('price')
        earrings.save()
        return redirect('admin_earrings')
    return render(request, 'admin/gold/earrings/update_earrings.html', {'earrings': earrings})

@login_required
def delete_earrings(request, earrings_id):
    earrings = get_object_or_404(Earrings, id=earrings_id)
    if request.method == 'POST':
        earrings.delete()
        return redirect('admin_earrings')
    return render(request, 'admin/gold/earrings/admin_earrings.html', {'earrings': earrings})

# Coin

def admin_coin(request):
    coin = Coin.objects.all()
    return render(request, 'admin/gold/coin/admin_coin.html',{'coin' :coin})

def add_coin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Coin.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_coin') 
        else:           
            return redirect('admin_coin') 
    return render(request, 'admin/gold/coin/add_coin.html')
    
@login_required
def update_coin(request, coin_id):
    coin = get_object_or_404(Coin, id=coin_id)
    if request.method == 'POST':
        coin.name = request.POST.get('name')
        coin.image = request.FILES.get('image')
        coin.price = request.POST.get('price')
        coin.save()
        return redirect('admin_coin')
    return render(request, 'admin/gold/coin/update_coin.html', {'coin': coin})

@login_required
def delete_coin(request, coin_id):
    coin = get_object_or_404(Coin, id=coin_id)
    if request.method == 'POST':
        coin.delete()
        return redirect('admin_coin')
    return render(request, 'admin/gold/coin/admin_chain.html', {'coin': coin})

# Mangalsutra

def admin_mangalsutra(request):
    mangalsutra = Mangalsutra.objects.all()
    return render(request, 'admin/gold/mangalsutra/admin_mangalsutra.html',{'mangalsutra' :mangalsutra})

def add_mangalsutra(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Mangalsutra.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_mangalsutra') 
        else:           
            return redirect('admin_mangalsutra') 
    return render(request, 'admin/gold/mangalsutra/add_mangalsutra.html')
    
@login_required
def update_mangalsutra(request, mangalsutra_id):
    mangalsutra = get_object_or_404(Mangalsutra, id=mangalsutra_id)
    if request.method == 'POST':
        mangalsutra.name = request.POST.get('name')
        mangalsutra.image = request.FILES.get('image')
        mangalsutra.price = request.POST.get('price')
        mangalsutra.save()
        return redirect('admin_mangalsutra')
    return render(request, 'admin/gold/mangalsutra/update_mangalsutra.html', {'mangalsutra': mangalsutra})

@login_required
def delete_mangalsutra(request, mangalsutra_id):
    mangalsutra = get_object_or_404(Mangalsutra, id=mangalsutra_id)
    if request.method == 'POST':
        mangalsutra.delete()
        return redirect('admin_mangalsutra')
    return render(request, 'admin/gold/mangalsutra/admin_mangalsutra.html', {'mangalsutra': mangalsutra})

# Neckwear

def admin_neckwear(request):
    neckwear = Neckwear.objects.all()
    return render(request, 'admin/gold/neckwear/admin_neckwear.html',{'neckwear' :neckwear})

def add_neckwear(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Neckwear.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_neckwear') 
        else:           
            return redirect('admin_neckwear') 
    return render(request, 'admin/gold/neckwear/add_neckwear.html')
    
@login_required
def update_neckwear(request, neckwear_id):
    neckwear = get_object_or_404(Neckwear, id=neckwear_id)
    if request.method == 'POST':
        neckwear.name = request.POST.get('name')
        neckwear.image = request.FILES.get('image')
        neckwear.price = request.POST.get('price')
        neckwear.save()
        return redirect('admin_neckwear')
    return render(request, 'admin/gold/neckwear/update_neckwear.html', {'neckwear': neckwear})

@login_required
def delete_neckwear(request, neckwear_id):
    neckwear = get_object_or_404(Neckwear, id=neckwear_id)
    if request.method == 'POST':
        neckwear.delete()
        return redirect('admin_neckwear')
    return render(request, 'admin/gold/neckwear/admin_neckwear.html', {'neckwear': neckwear})

# Nosepin

def admin_nosepin(request):
    nosepin = Nosepin.objects.all()
    return render(request, 'admin/gold/nosepin/admin_nosepin.html',{'nosepin' :nosepin})

def add_nosepin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Nosepin.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_nosepin') 
        else:           
            return redirect('admin_nosepin') 
    return render(request, 'admin/gold/nosepin/add_nosepin.html')
    
@login_required
def update_nosepin(request, nosepin_id):
    nosepin = get_object_or_404(Nosepin, id=nosepin_id)
    if request.method == 'POST':
        nosepin.name = request.POST.get('name')
        nosepin.image = request.FILES.get('image')
        nosepin.price = request.POST.get('price')
        nosepin.save()
        return redirect('admin_nosepin')
    return render(request, 'admin/gold/nosepin/update_nosepin.html', {'nosepin': nosepin})

@login_required
def delete_nosepin(request, nosepin_id):
    nosepin = get_object_or_404(Nosepin, id=nosepin_id)
    if request.method == 'POST':
        nosepin.delete()
        return redirect('admin_nosepin')
    return render(request, 'admin/gold/nosepin/admin_chain.html', {'nosepin': nosepin})

# Set

def admin_set(request):
    set = Set.objects.all()
    return render(request, 'admin/gold/set/admin_set.html',{'set' :set})

def add_set(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Set.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_set') 
        else:           
            return redirect('admin_set') 
    return render(request, 'admin/gold/set/add_set.html')
    
@login_required
def update_set(request, set_id):
    set = get_object_or_404(Set, id=set_id)
    if request.method == 'POST':
        set.name = request.POST.get('name')
        set.image = request.FILES.get('image')
        set.price = request.POST.get('price')
        set.save()
        return redirect('admin_set')
    return render(request, 'admin/gold/set/update_set.html', {'set': set})

@login_required
def delete_set(request, set_id):
    set = get_object_or_404(Set, id=set_id)
    if request.method == 'POST':
        set.delete()
        return redirect('admin_set')
    return render(request, 'admin/gold/set/admin_set.html', {'set': set})

# Ring

def admin_ring(request):
    ring = Ring.objects.all()
    return render(request, 'admin/gold/ring/admin_ring.html',{'ring' :ring})

def add_ring(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Ring.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_ring') 
        else:           
            return redirect('admin_ring') 
    return render(request, 'admin/gold/ring/add_ring.html')
    
@login_required
def update_ring(request, ring_id):
    ring = get_object_or_404(Ring, id=ring_id)
    if request.method == 'POST':
        ring.name = request.POST.get('name')
        ring.image = request.FILES.get('image')
        ring.price = request.POST.get('price')
        ring.save()
        return redirect('admin_ring')
    return render(request, 'admin/gold/ring/update_ring.html', {'ring': ring})

@login_required
def delete_ring(request, ring_id):
    ring = get_object_or_404(Ring, id=ring_id)
    if request.method == 'POST':
        ring.delete()
        return redirect('admin_ring')
    return render(request, 'admin/gold/ring/admin_ring.html', {'ring': ring})

# Pendant

def admin_pendant(request):
    pendant = Pendant.objects.all()
    return render(request, 'admin/gold/pendant/admin_pendant.html',{'pendant' :pendant})

def add_pendant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Pendant.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_pendant') 
        else:           
            return redirect('admin_pendant') 
    return render(request, 'admin/gold/pendant/add_pendant.html')
    
@login_required
def update_pendant(request, pendant_id):
    pendant = get_object_or_404(Pendant, id=pendant_id)
    if request.method == 'POST':
        pendant.name = request.POST.get('name')
        pendant.image = request.FILES.get('image')
        pendant.price = request.POST.get('price')
        pendant.save()
        return redirect('admin_pendant')
    return render(request, 'admin/gold/pendant/update_pendant.html', {'pendant': pendant})

@login_required
def delete_pendant(request, pendant_id):
    pendant = get_object_or_404(Pendant, id=pendant_id)
    if request.method == 'POST':
        pendant.delete()
        return redirect('admin_pendant')
    return render(request, 'admin/gold/pendant/admin_pendant.html', {'pendant': pendant})

##############################################Silver###############################################################

#Anklet

def admin_anklet(request):
    anklet = Anklet.objects.all()
    return render(request, 'admin/silver/anklet/admin_silver_anklet.html',{'anklet' :anklet})

def add_anklet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Anklet.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_anklet') 
        else:           
            return redirect('admin_anklet') 
    return render(request, 'admin/silver/anklet/add_anklet.html')
    
@login_required
def update_anklet(request, anklet_id):
    anklet = get_object_or_404(Anklet, id=anklet_id)
    if request.method == 'POST':
        anklet.name = request.POST.get('name')
        anklet.image = request.FILES.get('image')
        anklet.price = request.POST.get('price')
        anklet.save()
        return redirect('admin_anklet')
    return render(request, 'admin/silver/anklet/update_anklet.html', {'anklet': anklet})

@login_required
def delete_anklet(request, anklet_id):
    anklet = get_object_or_404(Anklet, id=anklet_id)
    if request.method == 'POST':
        anklet.delete()
        return redirect('admin_anklet')
    return render(request, 'admin/silver/anklet/admin_anklet.html', {'anklet': anklet})

# Bangle

def admin_silver_bangle(request):
    ban = Ban.objects.all()
    return render(request, 'admin/silver/bangle/admin_silver_bangle.html',{'ban' :ban})

def add_silver_bangle(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Ban.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_silver_bangle') 
        else:           
            return redirect('admin_silver_bangle') 
    return render(request, 'admin/silver/bangle/add_silver_bangle.html')
    
@login_required
def update_silver_bangle(request, ban_id):
    ban = get_object_or_404(Ban, id= ban_id)
    if request.method == 'POST':
        ban.name = request.POST.get('name')
        ban.image = request.FILES.get('image')
        ban.price = request.POST.get('price')
        ban.save()
        return redirect('admin_silver_bangle')
    return render(request, 'admin/silver/bangle/update_silver_bangle.html', {'ban': ban})

@login_required
def delete_silver_bangle(request, ban_id):
    ban = get_object_or_404(Ban, id= ban_id)
    if request.method == 'POST':
        ban.delete()
        return redirect('admin_silver_bangle')
    return render(request, 'admin/silver/bangle/admin_silver_bangle.html', {'ban': ban})

# Bracelets

def admin_silver_bracelet(request):
    brace = Brace.objects.all()
    return render(request, 'admin/silver/bracelet/admin_silver_bracelet.html',{'brace' :brace})

def add_silver_bracelet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Brace.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_silver_bracelet') 
        else:           
            return redirect('admin_silver_bracelet') 
    return render(request, 'admin/silver/bracelet/add_silver_bracelet.html')
    
@login_required
def update_silver_bracelet(request, brace_id):
    brace = get_object_or_404(Brace, id= brace_id)
    if request.method == 'POST':
        brace.name = request.POST.get('name')
        brace.image = request.FILES.get('image')
        brace.price = request.POST.get('price')
        brace.save()
        return redirect('admin_silver_bracelet')
    return render(request, 'admin/silver/bracelet/update_silver_bracelet.html', {'brace': brace})

@login_required
def delete_silver_bracelet(request, brace_id):
    brace = get_object_or_404(Brace, id=brace_id)
    if request.method == 'POST':
        brace.delete()
        return redirect('admin_silver_bracelet')
    return render(request, 'admin/silver/bracelet/admin_silver_bracelet.html', {'brace': brace})

# Coin

def admin_silver_coin(request):
    co = Co.objects.all()
    return render(request, 'admin/silver/coin/admin_silver_coin.html',{'co' :co})

def add_silver_coin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Co.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_silver_coin') 
        else:           
            return redirect('admin_silver_coin') 
    return render(request, 'admin/silver/coin/add_silver_coin.html')
    
@login_required
def update_silver_coin(request, co_id):
    co = get_object_or_404(Co, id=co_id)
    if request.method == 'POST':
        co.name = request.POST.get('name')
        co.image = request.FILES.get('image')
        co.price = request.POST.get('price')
        co.save()
        return redirect('admin_silver_coin')
    return render(request, 'admin/silver/coin/update_silver_coin.html', {'co': co})

@login_required
def delete_silver_coin(request, co_id):
    co = get_object_or_404(Co, id=co_id)
    if request.method == 'POST':
        co.delete()
        return redirect('admin_silver_coin')
    return render(request, 'admin/silver/coin/admin_silver_coin.html', {'co': co})

# Earrings
def admin_silver_earring(request):
    ear = Ear.objects.all()
    return render(request, 'admin/silver/earring/admin_silver_earring.html',{'ear' :ear})

def add_silver_earring(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Ear.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_silver_earring') 
        else:           
            return redirect('admin_silver_earring') 
    return render(request, 'admin/silver/earring/admin_silver_earring.html')
    
@login_required
def update_silver_earring(request, ear_id):
    ear = get_object_or_404(Ear, id = ear_id)
    if request.method == 'POST':
        ear.name = request.POST.get('name')
        ear.image = request.FILES.get('image')
        ear.price = request.POST.get('price')
        ear.save()
        return redirect('admin_silver_earring')
    return render(request, 'admin/silver/earring/update_silver_earring.html', {'ear': ear})

@login_required
def delete_silver_earring(request, ear_id):
    ear = get_object_or_404(Ear, id = ear_id)
    if request.method == 'POST':
        ear.delete()
        return redirect('admin_silver_earring')
    return render(request, 'admin/silver/earring/admin_silver_earring.html', {'ear': ear})

# Neckwear

def admin_silver_neckwear(request):
    neck = Neck.objects.all()
    return render(request, 'admin/silver/neckwear/admin_silver_neckwear.html',{'neck' :neck})

def add_silver_neckwear(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Neck.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_silver_neckwear') 
        else:           
            return redirect('admin_silver_neckwear') 
    return render(request, 'admin/silver/neckwear/add_silver_neckwear.html')
    
@login_required
def update_silver_neckwear(request, neck_id):
    neck = get_object_or_404(Neck, id=neck_id)
    if request.method == 'POST':
        neck.name = request.POST.get('name')
        neck.image = request.FILES.get('image')
        neck.price = request.POST.get('price')
        neck.save()
        return redirect('admin_silver_neckwear')
    return render(request, 'admin/silver/neckwear/update_silver_neckwear.html', {'neck': neck})

@login_required
def delete_silver_neckwear(request, neck_id):
    neck = get_object_or_404(Neck, id=neck_id)
    if request.method == 'POST':
        neck.delete()
        return redirect('admin_silver_neckwear')
    return render(request, 'admin/silver/neckwear/admin_silver_neckwear.html', {'neck': neck})

# Pendant

def admin_silver_pendant(request):
    pen = Pen.objects.all()
    return render(request, 'admin/silver/pendant/admin_silver_pendant.html',{'pen' :pen})

def add_silver_pendant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Pendant.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_silver_pendant') 
        else:           
            return redirect('admin_silver_pendant') 
    return render(request, 'admin/silver/pendant/add_silver_pendant.html')
    
@login_required
def update_silver_pendant(request, pendant_id):
    pendant = get_object_or_404(Pendant, id=pendant_id)
    if request.method == 'POST':
        pendant.name = request.POST.get('name')
        pendant.image = request.FILES.get('image')
        pendant.price = request.POST.get('price')
        pendant.save()
        return redirect('admin_silver_pendant')
    return render(request, 'admin/silver/pendant/update_silver_pendant.html', {'pen' : pen })

@login_required
def delete_silver_pendant(request, pendant_id):
    pendant = get_object_or_404(Pendant, id=pendant_id)
    if request.method == 'POST':
        pendant.delete()
        return redirect('admin_silver_pendant')
    return render(request, 'admin/silver/pendant/admin_silver_pendant.html', {'pen': pen })

# Ring

def admin_silver_ring(request):
    ri = Ri.objects.all()
    return render(request, 'admin/silver/ring/admin_silver_ring.html',{'ri' :ri})

def add_silver_ring(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Pendant.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            return redirect('add_silver_ring') 
        else:           
            return redirect('admin_silver_ring') 
    return render(request, 'admin/silver/ring/add_silver_ring.html')
    
@login_required
def update_silver_ring(request, ri_id):
    ri = get_object_or_404(Ri, id= ri_id)
    if request.method == 'POST':
        ri.name = request.POST.get('name')
        ri.image = request.FILES.get('image')
        ri.price = request.POST.get('price')
        ri.save()
        return redirect('admin_silver_ring')
    return render(request, 'admin/silver/ring/update_silver_ring.html', {'ri': ri})

@login_required
def delete_silver_ring(request, ri_id):
    ri = get_object_or_404(Ri, id= ri_id)
    if request.method == 'POST':
        ri.delete()
        return redirect('admin_silver_ring')
    return render(request, 'admin/silver/ring/admin_silver_ring.html', {'ri': ri})

###########################################Diamond###############################################################

def admin_diamond(request):
    diamond = Diamond.objects.all()
    return render(request, 'admin/diamond/admin_diamond.html',{'diamond' :diamond})

def add_diamond(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        Diamond.objects.create(name=name,image=image,price=price)
        if 'add_another' in request.POST:
            
            return redirect('add_diamond') 
        else:
            return redirect('admin_diamond') 
    return render(request, 'admin/diamond/add_diamond.html')
    
@login_required
def update_diamond(request, diamond_id):
    diamond = get_object_or_404(Diamond, id=diamond_id)
    if request.method == 'POST':
        diamond.name = request.POST.get('name')
        diamond.image = request.FILES.get('image')
        diamond.price = request.POST.get('price')
        diamond.save()
        return redirect('admin_diamond')
    return render(request, 'admin/diamond/update_diamond.html', {'diamond': diamond})

@login_required
def delete_diamond(request, diamond_id):
    diamond = get_object_or_404(Diamond, id= diamond_id)
    if request.method == 'POST':
        diamond.delete()
        return redirect('admin_diamond')
    return render(request, 'admin/diamond/admin_diamond.html', {'diamond': diamond})

########################################### Staff ###############################################################

def admin_staff(request):
    staff = Staff.objects.all()
    return render(request, 'admin/staff/admin_staff.html',{'staff' :staff})

def add_staff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        department = request.POST.get('department')
        Staff.objects.create(name=name,image=image,department=department)
        if 'add_another' in request.POST:
            
            return redirect('add_staff') 
        else:
            return redirect('admin_staff') 
    return render(request, 'admin/staff/add_staff.html')
    
@login_required
def update_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    if request.method == 'POST':
        staff.name = request.POST.get('name')
        staff.image = request.FILES.get('image')
        staff.department = request.POST.get('department')
        staff.save()
        return redirect('admin_staff')
    return render(request, 'admin/staff/update_staff.html', {'staff': staff})

@login_required
def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id= staff_id)
    if request.method == 'POST':
        staff.delete()
        return redirect('admin_staff')
    return render(request, 'admin/staff/admin_staff.html', {'staff': staff})

########################################### Working ###############################################################

def admin_working(request):
    working = Working.objects.all()
    return render(request, 'admin/staff/admin_working.html',{'working' :working})

def add_working(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        department = request.POST.get('department')
        Working.objects.create(name=name,image=image,department=department)
        if 'add_another' in request.POST:
            
            return redirect('add_working') 
        else:
            return redirect('admin_working') 
    return render(request, 'admin/staff/add_working.html')
    
@login_required
def update_working(request, working_id):
    working = get_object_or_404(Working, id=working_id)
    if request.method == 'POST':
        working.name = request.POST.get('name')
        working.image = request.FILES.get('image')
        working.department = request.POST.get('department')
        working.save()
        return redirect('admin_working')
    return render(request, 'admin/staff/update_working.html', {'working': working})

@login_required
def delete_working(request, working_id):
    working = get_object_or_404(Working, id= working_id)
    if request.method == 'POST':
        working.delete()
        return redirect('admin_working')
    return render(request, 'admin/staff/admin_working.html', {'working': working})
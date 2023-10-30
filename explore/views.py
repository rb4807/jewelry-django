from django.shortcuts import render
from .models import Bangle,Chain,Bracelets,Couple,Earrings,Coin,Mangalsutra,Neckwear,Nosepin,Set,Ring,Pendant,Anklet,Ban,Brace,Co,Ear,Neck,Pen,Ri,Diamond,Men,Women,Kid,Product

def explore(request):
    return render(request, 'explore/explore.html')

def bangle(request):
    bang = Bangle.objects.all()
    return render(request, 'explore/bangle.html',{'bang' :bang})

def chain(request):
    chain = Chain.objects.all()
    return render(request, 'explore/chain.html',{'chain' :chain})

def bracelets(request):
    bracelets = Bracelets.objects.all()
    return render(request, 'explore/bracelets.html',{'bracelets' :bracelets})

def couple(request):
    couple = Couple.objects.all()
    return render(request, 'explore/couple.html',{'couple' :couple})

def earrings(request):
    earrings = Earrings.objects.all()
    return render(request, 'explore/earrings.html',{'earrings' :earrings})

def coin(request):
    coin = Coin.objects.all()
    return render(request, 'explore/coin.html',{'coin' :coin})

def mangalsutra(request):
    mangalsutra = Mangalsutra.objects.all()
    return render(request, 'explore/mangalsutra.html',{'mangalsutra' :mangalsutra})

def neckwear(request):
    neckwear = Neckwear.objects.all()
    return render(request, 'explore/neckwear.html',{'neckwear' :neckwear})

def nosepin(request):
    nosepin = Nosepin.objects.all()
    return render(request, 'explore/nosepin.html',{'nosepin' :nosepin})

def set(request):
    set = Set.objects.all()
    return render(request, 'explore/set.html',{'set' :set})

def ring(request):
    ring = Ring.objects.all()
    return render(request, 'explore/ring.html',{'ring' :ring})

def pendant(request):
    pendant = Pendant.objects.all()
    return render(request, 'explore/pendant.html',{'pendant' :pendant})

def anklet(request):
    anklet = Anklet.objects.all()
    return render(request, 'explore/silver_anklet.html',{'anklet' :anklet})

def ban(request):
    ban = Ban.objects.all()
    return render(request, 'explore/silver_bangle.html',{'ban' :ban})

def brace(request):
    brace = Brace.objects.all()
    return render(request, 'explore/silver_bracelet.html',{'brace' :brace})

def co(request):
    co = Co.objects.all()
    return render(request, 'explore/silver_coin.html',{'co' :co})

def ear(request):
    ear = Ear.objects.all()
    return render(request, 'explore/silver_earrings.html',{'ear' :ear})

def neck(request):
    neck = Neck.objects.all()
    return render(request, 'explore/silver_necklace.html',{'neck' :neck})
    
def pen(request):
    pen = Pen.objects.all()
    return render(request, 'explore/silver_pendant.html',{'pen' :pen})

def ri(request):
    ri = Ri.objects.all()
    return render(request, 'explore/silver_ring.html',{'ri' :ri})

def diamond(request):
    diamond = Diamond.objects.all()
    return render(request, 'explore/diamond.html',{'diamond' :diamond})

def men(request):
    men = Men.objects.all()
    return render(request, 'explore/men.html',{'men' :men})

def women(request):
    women = Women.objects.all()
    return render(request, 'explore/women.html',{'women' :women})

def kid(request):
    kid = Kid.objects.all()
    return render(request, 'explore/kid.html',{'kid' :kid})

# searchbar

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            pro = Product.objects.filter(name__icontains=query) 
            return render(request, 'explore/search.html', {'pro': pro})
        else:
            print("No products")
            return render(request, 'explore/search.html', {})



from django.shortcuts import render

def home(request):
    products = [
        {
            "name": "10 SWG Welding Electrode",
            "size": "10 SWG",
            "description": "High quality welding electrode for industrial welding applications.",
            "image": "images/about.jpg"
        },
        {
            "name": "12 SWG Welding Electrode",
            "size": "12 SWG",
            "description": "Durable and reliable welding electrode with excellent strength.",
            "image": "images/about.jpg"
        }
    ]

    return render(request, 'home.html', {'products': products})




def about(request):
    return render(request, 'about.html')




def products_page(request):
    return render(request, 'products.html')



def e7018(request):
    return render(request, 'e7018.html')


def e6013(request):
    return render(request,'e6013.html')
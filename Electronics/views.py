from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    if request.method == "POST":
        fm = ProductForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("home")  # Ensure you have a URL pattern named 'success'
    else:
        fm = ProductForm()

    prod = Product.objects.all()  # Get all product details
    return render(request, 'Electronics/home.html', {'prod': prod, 'fm': fm})

    prod = Product.objects.all() #Render all the product details on tythe Browser
    fm = ProductForm() #fetch all the product from the database
    return render(request, 'Electronics/home.html', {'prod': prod, 'fm':fm}) #Render the home.html template

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id) #fetch the product by id
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product) # bind the from with the product instance
        if form.is_valid():
            form.save() # save the updated product details
            return redirect('home')
    else:
        form = ProductForm(instance=product) # create a form instance with the product data
    return render(request, 'Electronics/edit_product.html', {'form' : form}) 

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'Electronics/delete_product.html',{'product':product})
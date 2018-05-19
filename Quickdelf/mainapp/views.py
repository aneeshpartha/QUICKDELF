from django.contrib import messages
from django.views import generic
from .models import hotels,items,cardvalidation
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm,loginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


itemslist = {}
inc = 0
sum = 0


# Creating class based views

# LoginView - View for managing login information.User is validated and authenticated

class loginview(View):
    form_class = loginForm
    template_name = 'mainapp/login.html'

    # Get method
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form}) # Rendering login.html at begining

    # Post method
    def post(self,request):
        print("post")
        form = self.form_class(request.POST) # Giving POST parameter details to loginForm class.
        status = 0
        if form.is_valid(): # Checking if form is valid

            username = form.cleaned_data['username'] # cleaning Username
            password = form.cleaned_data['password'] # cleaning Password

            user = authenticate(username=username, password=password) # Authenticating user

            if user is not None:

                if user.is_active:
                   login(request, user)
                   return redirect('mainapp:index') # Once authenticated sending to mainpage which is index.html
                   status = 0
                else:
                    status = 1
            return redirect('mainapp:index')
        context = hotels.objects.all()
        if(status == 0):
            return render(request, 'mainapp/index.html', {'form': context})
        else:
            return render(request, 'mainapp/login.html', {'form': form})


# Class Hotelview for retrieving hotel information

class Hotelview(generic.ListView):
    template_name = "mainapp/index.html"  # Sending hotel object to index.html for display
    context_object_name = "form"

    def get_queryset(self):
        return hotels.objects.all()


# Class itemsview .Class to display items available in an restaurant to user.

def itemsview(request,hotel_id):

    obs = items.objects.filter(hotel_id = hotel_id) # Fetching items information from database
    return render(request,'mainapp/items.html',{'object':obs }) # Rendering content


#Cart class . class to display items marked by user

class cartview(View):

    def get(self,request):
        cartlist = [] # Using list to record the items

        for key in itemslist:
            listid = itemslist[key]

            itemname = items.objects.filter(id = listid[1],hotel_id = listid[0]) # Filtering information from the database
            for obj in itemname:
                cartlist.append(obj) # Appending objects to send to view

        global sum
        for ob in cartlist:
            sum += ob.itemamount # Finding the total cart amount

        return render(request, 'mainapp/cart.html' , {'itemname':cartlist})

    def post(self,request):

        return render(request,'mainapp/payment.html',{'sum':sum})

# Finding initial cart amount

def itemscartcalc(request,items_hotel_id,items_id):
    global itemslist,inc


    itemslist[str(inc)] = [items_hotel_id,items_id] # Creating list to track items
    inc+=1

    obs = items.objects.filter(hotel_id=items_hotel_id) # Fetching and filtering information from database

    return render(request, 'mainapp/items.html', {'object': obs})


# Class used during user registration

class UserProfileview(View):
    form_class = UserForm
    template_name = 'mainapp/registration.html' # Registration html file

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name)

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False) # Saving initial contents to database but not validating
            username = form.cleaned_data['username'] # cleaning username
            password = form.cleaned_data['password'] # cleaning password
            first_name = form.cleaned_data['first_name'] # Clearning firstname
            last_name = form.cleaned_data['last_name'] # Cleaning lastname
            email = form.cleaned_data['email'] # Cleaning email
            user.set_password(password)
            user.save() # Saving content to database

            user = authenticate(username=username,password = password) # once created user will be authenticated

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('mainapp:index')

        return render(request,'mainapp/index.html',{'form':form})


# Class for payment.

class paymentview(View):

        form_class = cardvalidation

        def get(self,request):
            return render(request, 'mainapp/index.html')

        def post(self,request):


            print(request.POST.get('cvv')) # Getting cvv information
            print(request.POST.get('cardnumber')) # Getting cardnumber

            cardobj = cardvalidation.objects.all() # retrieving card information from database

            found = 0

            for obj in cardobj:
                if( (str(obj.cardnumber) == str(request.POST.get('cardnumber'))) and ( str(obj.cvv) == str(request.POST.get('cvv')))): # Cross verifying the card details
                    found = 1

            if(found == 1): # Based on variable set html file will be rendered.
                print("1")
                return render(request, 'mainapp/paymentsucess.html')
            else:
                print("0")
                return render(request, 'mainapp/paymentfailed.html')



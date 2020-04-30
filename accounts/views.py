from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, CustomerForm
from accounts.models import Customer
from checkout.models import Order


def register(request):
    """
    Render registration page
    """
    if request.user.is_authenticated:
        messages.info(request, "You're already logged in",
                         button='Ok', timer=3000)
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request,
                                 "You have successfully registered your account")
                return redirect(reverse('index'))
            else:
                messages.info(request,
                              "Sorry but we're unable to register your account at this time!",
                              button='Ok', timer=3000)
    else:
        # Create an instance of reg form
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {
        "registration_form": registration_form})
    """
    registration_form passed through as a context dictionary.
    """


def login(request):
    """
    Render login page
    """
    if request.user.is_authenticated:
        messages.info(request, "You're already logged in!",
                         button='OK', timer=3000)
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request,
                                 "You have successfully logged in!")

                if request.GET.get('next', False):
                    return HttpResponseRedirect(request.GET.get('next'))
                else:
                    return redirect(reverse('index'))
            else:
                login_form.add_error(None,
                                     "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


@login_required
def logout(request):
    """
    Logout user
    """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")

    return redirect(reverse('index'))


@login_required()
def profile(request):
    """
    User profile page. Filter () used to return multiple records and help
    avoid an error message if using get () instead. The latter method is
    limited to getting one result only.
    """
    user = User.objects.filter(email=request.user.email)

    context = {
        'profile': user,
    }

    return render(request, 'profile.html', context)


def user_profile(request):

    """
    Renders profile page for user with a form to update
    their information. When posted creates a new customer.
    """

    customer = Customer.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request, "You have updated your profile")
    else:
        form = CustomerForm(instance=customer)
    has_order = False
    if customer:
        has_order = Order.objects.filter(customer=customer).exists()

    return render(
        request,
        "profile.html",
        {"user": request.user, "form": form, "has_order": has_order}
    )

from django.shortcuts import render
from users.forms import UserForm
from users.models import User

#the function executes with the signup url to take the inputs 
def signup(request):
    if request.method == 'POST':  # if the form has been filled

        form = UserForm(request.POST)

        if form.is_valid():  # All the data is valid
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        # creating an user object containing all the data
        user_obj = User(username=username, email=email, password=password)
        # saving all the data in the current object into the database
        user_obj.save()

        return render(request, 'users/signup.html', {'user_obj': user_obj,'is_registered':True }) # Redirect after POST

    else:
        form = UserForm()  # an unboundform

        return render(request, 'users/signup.html', {'form': form})

#the function executes with the showdata url to display the list of registered users
def showdata(request):
    all_users = User.objects.all()
    return render(request, 'users/showdata.html', {'all_users': all_users, })
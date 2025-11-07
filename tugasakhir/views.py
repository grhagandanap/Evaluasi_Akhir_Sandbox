from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from eas.forms import CustomAuthenticationForm


def login_view(request):
    """
    Handle user authentication and login.

    This view processes both GET and POST requests:
    - For GET requests, it displays the login form.
    - For POST requests, it validates the provided credentials using
      Django's built-in `AuthenticationForm`. If valid, it logs the user in
      and redirects them to the `'index'` page.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.

    Returns
    -------
    HttpResponse
        Renders the login page on GET requests or redirects to `'index'`
        after successful authentication.
    """
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('index')  # Redirect after successful login
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """
    Handle user logout.

    This view logs out the currently authenticated user
    and redirects them to the `'home'` page.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.

    Returns
    -------
    HttpResponseRedirect
        Redirects the user to the `'home'` page after logout.
    """
    logout(request)
    return redirect('home')

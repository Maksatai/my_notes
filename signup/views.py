from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .forms import UserRegistrationForm

class SignupView(TemplateView):
    template_name = "sign_up.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
            # Create a new user object but avoid saving it yet
                new_user = user_form.save(commit=False)
            # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
                new_user.save()
                return redirect("/")
        else:
            user_form = UserRegistrationForm()
        return render(request, self.template_name, {'user_form': user_form})
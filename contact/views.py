from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            context = {"name": name, "from_email": from_email, "message": message}

            send_mail(
                "Boilerplate",
                render_to_string("new_contact_email.html", context),
                from_email,
                ["paulr909@proton.me"],
                fail_silently=False,
            )
            messages.success(request, "Form sent, Thank you!")
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

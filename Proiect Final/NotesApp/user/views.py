import random
import string

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import UpdateView, CreateView

from user.forms import NewAccountForm
from user.models import UserExtend


class UpdateProfileView(UpdateView):
    model = User
    fields = [
        'first_name',
        'last_name',
        'email',
    ]

    template_name = 'registration/new_account.html'

    def get_success_url(self):
        return reverse('app:home')


punctuation = '!&%?#@'


class CreateNewAccount(CreateView):
    model = UserExtend
    form_class = NewAccountForm
    template_name = 'registration/update_account.html'

    def get_success_url(self):
        pwd = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase
                                                   + string.digits + punctuation) for _ in range(8))

        try:
            user_instance = User.objects.get(id=self.object.id)
            user_instance.set_password(pwd)
            user_instance.save()

            content_email_user = f"Your account has been created. Username: {user_instance.username}. Password: {pwd}"
            msg_html = render_to_string('emails/invite_user.html', {'content_email': str(content_email_user)})
            msg = EmailMultiAlternatives(
                subject='New Account',
                body='content_email_user',
                from_email='contact@notesapp.com',
                to=[user_instance.email]
            )
            msg.attach_alternative(msg_html, 'text/html')
            msg.send()
        except Exception:
            pass
        return reverse('login')

from django import template

from main_app.models.models import Applicant

register = template.Library()


# template tag for registering
@register.simple_tag(name='is_already_applied')
def is_already_applied(job, user):
    applied = Applicant.objects.filter(job=job, user=user)
    if applied:
        return True
    else:
        return False

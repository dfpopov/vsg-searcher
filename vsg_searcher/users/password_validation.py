from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

class RequiredNumberPasswordValidator(object):
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if not re.search("[0-9]", password):
            raise ValidationError(
                _("This password must contain at least %(min_length)d number."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_length)d number."
            % {'min_length': self.min_length}
        )
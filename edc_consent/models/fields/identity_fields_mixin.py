from django.core.exceptions import ValidationError
from django.db import models

from edc_base.encrypted_fields import IdentityField, IdentityTypeField


class IdentityFieldsMixin(models.Model):

    identity = IdentityField(
        verbose_name="Identity number")

    identity_type = IdentityTypeField()

    confirm_identity = IdentityField(
        help_text="Retype the identity number",
        null=True,
        blank=False
    )

    def save(self, *args, **kwargs):
        if self.identity != self.confirm_identity:
            raise ValidationError(
                '\'Identity\' must match \'confirm_identity\'. '
                'Catch this error on the form'
            )
        super(IdentityFieldsMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True

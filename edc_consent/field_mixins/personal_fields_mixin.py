from django.core.validators import RegexValidator
from django.db import models
from django_crypto_fields.fields import (
    FirstnameField, LastnameField, EncryptedCharField)
from django_crypto_fields.mixins import CryptoMixin

from edc_base.model_fields import IsDateEstimatedField
from edc_constants.choices import GENDER_UNDETERMINED

from ..validators import FullNameValidator
from django.utils.safestring import mark_safe


class PersonalFieldsMixin(CryptoMixin, models.Model):

    first_name = FirstnameField(
        null=True, blank=False)

    last_name = LastnameField(
        verbose_name="Last name",
        null=True, blank=False)

    initials = EncryptedCharField(
        validators=[RegexValidator(
            regex=r'^[A-Z]{2,3}$',
            message=('Ensure initials consist of letters '
                     'only in upper case, no spaces.'))],
        null=True, blank=False)

    dob = models.DateField(
        verbose_name="Date of birth",
        null=True,
        blank=False)

    is_dob_estimated = IsDateEstimatedField(
        verbose_name="Is date of birth estimated?",
        null=True,
        blank=False)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER_UNDETERMINED,
        max_length=1,
        null=True,
        blank=False)

    guardian_name = LastnameField(
        verbose_name=('Guardian\'s last and first name'),
        validators=[FullNameValidator()],
        blank=True,
        null=True,
        help_text=mark_safe(
            'Required only if participant is a minor.<BR>'
            'Format is \'LASTNAME, FIRSTNAME\'. '
            'All uppercase separated by a comma.'))

    subject_type = models.CharField(
        max_length=25)

    class Meta:
        abstract = True

from django.db import models

from ..exceptions import NotConsentedError
from ..models import ConsentType


class RequiresConsentMixin(models.Model):

    CONSENT_MODEL = None

    consent_version = models.CharField(max_length=10, default='?', editable=False)

    def save(self, *args, **kwargs):
        self.consented_for_period_or_raise()
        super(RequiresConsentMixin, self).save(*args, **kwargs)

    def consented_for_period_or_raise(self, report_datetime=None, subject_identifier=None, exception_cls=None):
        exception_cls = exception_cls or NotConsentedError
        report_datetime = report_datetime or self.report_datetime
        try:
            consent_type = self.consent_type(report_datetime, exception_cls=exception_cls)
            self.consent_version = consent_type.version
            if not subject_identifier:
                try:
                    subject_identifier = self.subject_identifier
                except AttributeError:
                    subject_identifier = self.get_subject_identifier()
            self.CONSENT_MODEL.objects.get(
                subject_identifier=subject_identifier,
                version=self.consent_version)
        except self.CONSENT_MODEL.DoesNotExist:
            raise exception_cls(
                'Cannot find a consent \'{}\' for model \'{}\' using '
                'consent version \'{}\' and report date \'{}\'. '.format(
                    self.CONSENT_MODEL._meta.verbose_name,
                    self._meta.verbose_name,
                    self.consent_version,
                    report_datetime.isoformat()))

    def consent_type(self, report_datetime, exception_cls=None):
        """Returns the consent type that matches the report datetime and consent model."""
        return ConsentType.objects.get_by_report_datetime(
            self.CONSENT_MODEL, report_datetime, exception_cls=exception_cls)

    class Meta:
        abstract = True

#     def get_versioned_field_names(self, consent_version_number):
#         """Returns a list of field names under version control by version number.
#
#         Users should override at the model class to return a list of field names for a given version_number."""
#         return []
#
#     def validate_versioned_fields(self, cleaned_data=None, exception_cls=None, **kwargs):
#         """Raises and exception if fields do not validate.
#
#         Validate fields under consent version control. If a field is not to be included for this
#         consent version, an exception will be raised."""
#         ConsentHelper(self).validate_versioned_fields()

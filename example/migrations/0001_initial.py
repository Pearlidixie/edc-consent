# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 20:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.encrypted_text_field
import django_crypto_fields.fields.firstname_field
import django_crypto_fields.fields.identity_field
import django_crypto_fields.fields.lastname_field
import django_crypto_fields.mixins
import django_extensions.db.fields
import django_revision.revision_field
import edc_base.model_fields.custom_fields
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_validators.date
import edc_consent.models_validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestConsentModel',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(
                    auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(
                    auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(
                    editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(
                    editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False,
                                                      help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(
                    editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False,
                                                                          help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False,
                                        help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('identity', django_crypto_fields.fields.identity_field.IdentityField(
                    help_text=' (Encryption: RSA local)', max_length=71, verbose_name='Identity number')),
                ('identity_type', edc_base.model.fields.custom_fields.IdentityTypeField(choices=[('OMANG', 'Omang'), ('DRIVERS', "Driver's License"), (
                    'PASSPORT', 'Passport'), ('OMANG_RCPT', 'Omang Receipt'), ('OTHER', 'Other')], max_length=15, verbose_name='What type of identity number is this?')),
                ('confirm_identity', django_crypto_fields.fields.identity_field.IdentityField(
                    help_text='Retype the identity number (Encryption: RSA local)', max_length=71, null=True)),
                ('first_name', django_crypto_fields.fields.firstname_field.FirstnameField(
                    help_text=' (Encryption: RSA local)', max_length=71, null=True)),
                ('last_name', django_crypto_fields.fields.lastname_field.LastnameField(
                    help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Last name')),
                ('initials', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[
                 django.core.validators.RegexValidator(message='Ensure initials consist of letters only in upper case, no spaces.', regex='^[A-Z]{2,3}$')])),
                ('dob', models.DateField(
                    help_text='Format is YYYY-MM-DD', null=True, verbose_name='Date of birth')),
                ('is_dob_estimated', edc_base.model.fields.custom_fields.IsDateEstimatedField(choices=[('-', 'No'), ('D', 'Yes, estimated the Day'), ('MD', 'Yes, estimated Month and Day'), (
                    'YMD', 'Yes, estimated Year, Month and Day')], help_text='If the exact date is not known, please indicate which part of the date is estimated.', max_length=25, null=True, verbose_name='Is date of birth estimated?')),
                ('gender', models.CharField(choices=[
                 ('M', 'Male'), ('F', 'Female'), ('U', 'Undetermined')], max_length=1, null=True, verbose_name='Gender')),
                ('guardian_name', django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text="Required only if subject is a minor. Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma then followe by a space. (Encryption: RSA local)",
                                                                                           max_length=71, null=True, validators=[edc_consent.models_validators.FullNameValidator()], verbose_name="Guardian's Last and first name (minors only)")),
                ('subject_type', models.CharField(max_length=25)),
                ('may_store_samples', models.CharField(choices=[
                 ('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Does the subject agree to have samples stored after the study has ended')),
                ('site_code', models.CharField(
                    help_text="This refers to the site or 'clinic area' where the subject is being consented.", max_length=25, verbose_name='Site')),
                ('is_incarcerated', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='-', help_text="( if 'Yes' STOP patient cannot be consented )", max_length=3, null=True, validators=[
                 edc_consent.models_validators.eligible_if_no], verbose_name='Is the participant under involuntary incarceration?')),
                ('is_literate', models.CharField(choices=[
                 ('Yes', 'Yes'), ('No', 'No')], default=None, help_text="( if 'No' provide witness's name on this form and signature on the paper document.)", max_length=3, verbose_name='Is the participant LITERATE?')),
                ('witness_name', django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text="Required only if subject is illiterate. Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)",
                                                                                          max_length=71, null=True, validators=[edc_consent.models_validators.FullNameValidator()], verbose_name="Witness's Last and first name (illiterates only)")),
                ('language', models.CharField(choices=[('tn', 'Setswana'), ('en', 'English')], default='not specified',
                                              help_text='The language used for the edc_consent process will also be used during data collection.', max_length=25, verbose_name='Language of consent')),
                ('is_verified', models.BooleanField(
                    default=False, editable=False)),
                ('is_verified_datetime', models.DateTimeField(
                    editable=False, null=True)),
                ('verified_by', models.CharField(
                    editable=False, max_length=25, null=True)),
                ('subject_identifier', models.CharField(
                    blank=True, max_length=50, verbose_name='Subject Identifier')),
                ('subject_identifier_as_pk', models.CharField(
                    default=None, editable=False, max_length=50, verbose_name='Subject Identifier as pk')),
                ('subject_identifier_aka', models.CharField(editable=False, help_text='track a previously allocated identifier.',
                                                            max_length=50, null=True, verbose_name='Subject Identifier a.k.a')),
                ('consent_datetime', models.DateTimeField(validators=[
                 edc_base.model.validators.date.datetime_not_before_study_start, edc_base.model.validators.date.datetime_not_future], verbose_name='Consent date and time')),
                ('version', models.CharField(default='?', editable=False,
                                             help_text="See 'Consent Type' for consent versions by period.", max_length=10, verbose_name='Consent version')),
                ('study_site', models.CharField(max_length=15, null=True)),
                ('sid', models.CharField(blank=True, help_text='Used for randomization against a prepared rando-list.',
                                         max_length=15, null=True, verbose_name='SID')),
                ('comment', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                    blank=True, help_text=' (Encryption: AES local)', max_length=250, null=True, verbose_name='Comment')),
                ('dm_comment', models.CharField(editable=False, help_text='see also edc.data manager.',
                                                max_length=150, null=True, verbose_name='Data Management comment')),
            ],
            bases=(django_crypto_fields.mixins.CryptoMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(
                    auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(
                    auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(
                    editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(
                    editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False,
                                                      help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(
                    editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False,
                                                                          help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False,
                                        help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('consent_version', models.CharField(
                    default='?', editable=False, max_length=10)),
                ('subject_identifier', models.CharField(max_length=10)),
                ('report_datetime', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('field1', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Test Model',
            },
        ),
        migrations.CreateModel(
            name='TestScheduledModel',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(
                    auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(
                    auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(
                    editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(
                    editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False,
                                                      help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(
                    editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False,
                                                                          help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False,
                                        help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('consent_version', models.CharField(
                    default='?', editable=False, max_length=10)),
                ('report_datetime', models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TestSpecimenConsent',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(
                    default=False, editable=False)),
                ('is_verified_datetime', models.DateTimeField(
                    editable=False, null=True)),
                ('verified_by', models.CharField(
                    editable=False, max_length=25, null=True)),
                ('consent_datetime', models.DateTimeField(default=django.utils.timezone.now, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                                                          validators=[edc_base.model.validators.date.datetime_not_before_study_start, edc_base.model.validators.date.datetime_not_future], verbose_name='Consent date and time')),
                ('version', models.CharField(default='?', editable=False,
                                             help_text="See 'Consent Type' for consent versions by period.", max_length=10, verbose_name='Consent version')),
                ('purpose_explained', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A',
                                                       max_length=15, null=True, verbose_name='I have explained the purpose of the specimen consent to the participant.')),
                ('purpose_understood', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=15, null=True,
                                                        verbose_name='To the best of my knowledge, the client understands the purpose, procedures, risks and benefits of the specimen consent')),
                ('offered_copy', models.CharField(choices=[('Yes', 'Yes and participant accepted the copy'), ('No', 'No'), ('Yes_declined', 'Yes but participant declined the copy')],
                                                  help_text='If participant declined the copy, return the copy to the clinic to be filed with the original specimen consent', max_length=20, null=True, verbose_name='I offered the participant a copy of the signed specimen consent and the participant accepted the copy')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(
                    auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(
                    auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(
                    editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(
                    editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False,
                                                      help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(
                    editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False,
                                                                          help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False,
                                        help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=10)),
                ('report_datetime', models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Visit',
            },
        ),
        migrations.AddField(
            model_name='testscheduledmodel',
            name='visit',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='example.Visit'),
        ),
        migrations.AlterUniqueTogether(
            name='testconsentmodel',
            unique_together=set([('first_name', 'dob', 'initials', 'version'),
                                 ('identity', 'version'), ('subject_identifier', 'version')]),
        ),
        migrations.CreateModel(
            name='TestConsentModelProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('example.testconsentmodel',),
        ),
    ]

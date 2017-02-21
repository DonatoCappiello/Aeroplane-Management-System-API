# Python objects that map DB data: author Donato Cappiello 
#
# model classes implements a __str__ for display and debug purposes

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Aeroplanes(models.Model):
    registration_no = models.CharField(primary_key=True, max_length=20)
    type = models.CharField(max_length=50)
    aircraft_hours = models.FloatField()
    hourly_rate = models.FloatField()

    def __str__(self):
        return "Aeroplanes: {}".format(self.registration_no,\
                                self.type,\
                                self.aircraft_hours,\
                                self.hourly_rate)

    class Meta:
        db_table = 'aeroplanes'
        verbose_name_plural = 'aeroplanes'

@python_2_unicode_compatible
class AeroplanesAvailabilityErrors(models.Model):
    error_id = models.AutoField(db_column='error_ID', primary_key=True)  # Field name made lowercase.
    registration_no = models.CharField(max_length=20)
    error_description = models.TextField()

    def __str__(self):
        return "AeroplanesAvailabilityErrors: {}".format(self.error_id,\
                                                self.registration_no,\
                                                self.error_description)

    class Meta:
        db_table = 'aeroplanes_availability_errors'
        verbose_name_plural = 'aeroplanes_availability_errors'

@python_2_unicode_compatible
class Amends(models.Model):
    amend_id = models.AutoField(db_column='amend_ID', primary_key=True)  # Field name made lowercase.
    amend_description = models.TextField()
    amend_priority = models.CharField(max_length=6)
    person_for_the_task = models.CharField(max_length=50)
    outcome = models.TextField()
    amend_completed_date = models.DateField()
    amend_completed_by = models.CharField(max_length=50)

    def __str__(self):
        return "Amends: {}".format(self.amend_id,\
                            self.amend_description,\
                            self.amend_priority,\
                            self.person_for_the_task,\
                            self.outcome,\
                            self.amend_completed_date,\
                            self.amend_completed_by)

    class Meta:
        db_table = 'amends'
        verbose_name_plural = 'amends'

@python_2_unicode_compatible
class Flights(models.Model):
    flight_id = models.AutoField(db_column='flight_ID', primary_key=True)  # Field name made lowercase.
    registration_no = models.CharField(max_length=20)
    date = models.DateField()
    student_passenger_name = models.CharField(max_length=50, blank=True, null=True)
    captain_name = models.IntegerField()
    duty = models.TextField()
    authorised_initials = models.IntegerField()
    captain_initials_before_flight = models.IntegerField()
    hobb_start = models.FloatField()
    hobb_stop = models.FloatField(blank=True, null=True)
    captain_initials_after_flight = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    field_serviceability = models.TextField(db_column=' serviceability', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    cheque_no = models.IntegerField(blank=True, null=True)
    treasurer_validation = models.IntegerField(blank=True, null=True)
    member_no = models.IntegerField()

    def __str__(self):
        return "Flights: {}".format(self.flight_id,\
                            self.registration_no,\
                            self.date,\
                            self.student_passenger_name,\
                            self.captain_name,\
                            self.duty,\
                            self.authorised_initials,\
                            self.captain_initials_before_flight,\
                            self.hobb_start,\
                            self.hobb_stop,\
                            self.captain_initials_after_flight,\
                            self.remarks,\
                            self.field_serviceability,\
                            self.cheque_no,\
                            self.treasurer_validation,\
                            self.member_no)

    class Meta:
        db_table = 'flights'
        verbose_name_plural = 'flights'

@python_2_unicode_compatible
class ForecastMaintananceCompleted(models.Model):
    job_completed_id = models.AutoField(db_column='job_completed_ID', primary_key=True)  # Field name made lowercase.
    job_list_id = models.IntegerField()
    aircraft_hours_after_job_completed = models.FloatField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    completed_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "ForecastMaintananceCompleted: {}".format(self.job_completed_id,\
                                                self.job_list_id,\
                                                self.aircraft_hours_after_job_completed,\
                                                self.date_completed,\
                                                self.completed_by)

    class Meta:
        db_table = 'forecast_maintanance_completed'
        verbose_name_plural = 'forecast_maintanance_completed'

@python_2_unicode_compatible
class ForecastMaintananceList(models.Model):
    job_list_id = models.AutoField(db_column='job_list_ID', primary_key=True)  # Field name made lowercase.
    registration_no = models.CharField(max_length=20)
    job_name = models.CharField(max_length=255)
    job_frequency_hours = models.IntegerField(blank=True, null=True)
    job_frequency_months = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return "ForecastMaintananceList: {}".format(self.job_list_id,\
                                            self.registration_no,\
                                            self.job_name,\
                                            self.job_frequency_hours,\
                                            self.job_frequency_months)

    class Meta:
        db_table = 'forecast_maintanance_list'
        verbose_name_plural = 'forecast_maintanance_list'

@python_2_unicode_compatible
class Members(models.Model):
    licence_no = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    member_initials = models.CharField(unique=True, max_length=10)
    member_no = models.IntegerField(primary_key=True)
    current_member = models.IntegerField()
    licence_expiring_date = models.DateField()
    licence_valid = models.IntegerField()
    medical_expiring_date = models.DateField()
    certificate_of_experience_expiring_date = models.DateField()
    flying_order_book_signature_date = models.DateField()
    role_id = models.IntegerField(db_column='role_ID')  # Field name made lowercase.

    def __str__(self):
        return "Members: {}".format(self.licence_no,\
                            self.name,\
                            self.surname,\
                            self.member_initials,\
                            self.member_no,\
                            self.current_member,\
                            self.licence_expiring_date,\
                            self.licence_valid,\
                            self.medical_expiring_date,\
                            self.certificate_of_experience_expiring_date,\
                            self.flying_order_book_signature_date,\
                            self.role_id)

    class Meta:
        db_table = 'members'
        verbose_name_plural = 'members'

@python_2_unicode_compatible
class MembersRoles(models.Model):
    role_id = models.AutoField(db_column='role_ID', primary_key=True)  # Field name made lowercase.
    role_name = models.CharField(max_length=20)

    def __str__(self):
        return "MembersRoles: {}".format(self.role_id,\
                                self.role_name)

    class Meta:
        db_table = 'members_roles'
        verbose_name_plural = 'members_roles'

@python_2_unicode_compatible
class MembersStatusErrors(models.Model):
    error_id = models.AutoField(db_column='error_ID', primary_key=True)  # Field name made lowercase.
    error_description = models.TextField()
    member_no = models.IntegerField()

    def __str__(self):
        return "MembersStatusErrors: {}".format(self.error_id,\
                                        self.error_description,\
                                        self.member_no)

    class Meta:
        db_table = 'members_status_errors'
        verbose_name_plural = 'members_status_errors'

@python_2_unicode_compatible
class Serviceability(models.Model):
    serviceability_id = models.AutoField(db_column='serviceability_ID', primary_key=True)  # Field name made lowercase.
    registration_no = models.CharField(max_length=20)
    serviceability_description = models.TextField()
    job_card = models.CharField(max_length=50, blank=True, null=True)
    work_carried_out = models.TextField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    completed_by = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Serviceability: {}".format(self.serviceability_id,\
                                    self.registration_no,\
                                    self.serviceability_description,\
                                    self.job_card,\
                                    self.work_carried_out,\
                                    self.date_completed,\
                                    self.completed_by)

    class Meta:
        db_table = 'serviceability'
        verbose_name_plural = 'serviceability'
    

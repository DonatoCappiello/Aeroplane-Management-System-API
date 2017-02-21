from django.contrib import admin
from .models import Aeroplanes, AeroplanesAvailabilityErrors, Amends, Flights, ForecastMaintananceCompleted, ForecastMaintananceList, ForecastMaintananceList, Members, MembersRoles, MembersStatusErrors, Serviceability

# Register your models here: author Donato Cappiello
# all models have been registered although only the aeeoplane one has been used by the Angular2 front end

admin.site.register(Aeroplanes)
admin.site.register(AeroplanesAvailabilityErrors)
admin.site.register(Amends)
admin.site.register(Flights)
admin.site.register(ForecastMaintananceCompleted)
admin.site.register(ForecastMaintananceList)
admin.site.register(Members)
admin.site.register(MembersRoles)
admin.site.register(MembersStatusErrors)
admin.site.register(Serviceability)
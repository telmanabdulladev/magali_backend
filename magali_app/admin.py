from django.contrib import admin
from magali_app.models import SettingsModel,ServicesImagesModel,ConsultingModel, ConsultingUnitModel, ServicesModel, ValuesImagesModel,CorporativeTrainingModel,CTCategoryModel,CTCategoryImagesModel,ContactModel


# Register your models here.
admin.site.register(SettingsModel)
admin.site.register(ValuesImagesModel)
admin.site.register(CorporativeTrainingModel)
admin.site.register(CTCategoryModel)
admin.site.register(CTCategoryImagesModel)
admin.site.register(ContactModel)
admin.site.register(ServicesModel)
admin.site.register(ServicesImagesModel)
admin.site.register(ConsultingUnitModel)
admin.site.register(ConsultingModel)




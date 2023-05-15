from django.contrib import admin
from magali_app.models import SettingsModel, ValuesImagesModel,CorporativeTrainingModel,CTCategoryModel,CTCategoryImagesModel,ContactModel


# Register your models here.
admin.site.register(SettingsModel)
admin.site.register(ValuesImagesModel)
admin.site.register(CorporativeTrainingModel)
admin.site.register(CTCategoryModel)
admin.site.register(CTCategoryImagesModel)
admin.site.register(ContactModel)



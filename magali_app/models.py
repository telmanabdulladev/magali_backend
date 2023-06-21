from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class SettingsModel(models.Model):
    about_banner = models.ImageField(upload_to="imgfiles/",null=True,blank=True)
    about_content = RichTextField()
    vision = models.CharField(max_length=256,null = True, blank= True)
    mission = models.CharField(max_length=256,null= True, blank = True)
    values_context = models.CharField(max_length=256,null= True, blank = True)

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"

    def __str__(self):
        return "Settings"
    
class ServicesModel(models.Model):
    title = models.CharField(max_length=256,null=True, blank=True)
    service_content = models.TextField(null= True, blank = True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
    

class ServicesImagesModel(models.Model):
    service = models.ForeignKey(ServicesModel,on_delete=models.CASCADE,related_name="service_images")
    image = models.ImageField(upload_to="service_imgfiles/")

    class Meta:
        verbose_name = "Service Image"
        verbose_name_plural = "Service Images"

    def __str__(self):
        return self.service.title

    
class ValuesImagesModel(models.Model):
    setting = models.ForeignKey(SettingsModel,on_delete=models.CASCADE, related_name="values_images")
    image = models.ImageField(upload_to="values_imgfiles/") 

    class Meta:
        verbose_name = "Values Image"
        verbose_name_plural = "Values Images"

    def __str__(self):
        return "Values Images " + str(self.id)

class CorporativeTrainingModel(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Corporative Training"
        verbose_name_plural = "Corporative Trainings"

    def __str__(self):
        return self.name

class CTCategoryModel(models.Model):
    corporativetraining = models.ForeignKey(CorporativeTrainingModel,on_delete=models.CASCADE,related_name="ctccategories")
    name = models.CharField(max_length=256)
    content = RichTextField()

    class Meta:
        verbose_name = "CTCategory"
        verbose_name_plural = "CTCategories"

    def __str__(self):
        return self.name

class CTCategoryImagesModel(models.Model):
    ctcategory = models.ForeignKey(CTCategoryModel,on_delete=models.CASCADE,related_name="category_images")
    image = models.ImageField(upload_to="ctc_imgfiles/") 


    class Meta:
        verbose_name = "CTCategory Image"
        verbose_name_plural = "CTCategory Images"

    def __str__(self):
        return self.ctcategory.name

class ContactModel(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    company_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone_num = models.CharField(max_length=50)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class ConsultingModel(models.Model):
    name = models.CharField(max_length=256)
    content=RichTextField()
    banner=models.ImageField(upload_to="consultingfiles/",null=True,blank=True)

    class Meta:
        verbose_name = "Consulting Model"
        verbose_name_plural = "Consulting Models"

    def __str__(self):
        return self.name

class ConsultingUnitModel(models.Model):
    consulting = models.ForeignKey(ConsultingModel,on_delete=models.CASCADE,related_name="consultingunits")
    name = models.CharField(max_length=256)
    content = RichTextField()
    banner=models.ImageField(upload_to="unitfiles/",null=True,blank=True)

    class Meta:
        verbose_name = "Consulting Unit"
        verbose_name_plural = "Consulting Units"

    def __str__(self):
        return self.name



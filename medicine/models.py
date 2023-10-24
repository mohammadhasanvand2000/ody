from django.db import models

class  Medicine (models.Model):
    title                  = models.CharField(max_length=200,null=True,blank=True)
    price                  = models.IntegerField(default='1000',null=True,blank=True)
    image                  = models.ImageField(upload_to="assets\img\poducts")
    drug_interactions      = models.CharField(max_length=10000,verbose_name=('فیلد تداخل دارویی اجباری'),help_text="نام دارویی کا بااین دارو تداخل دارد :")
    slug                   = models.SlugField(unique=True, max_length=255,null=True,blank=True)




    def __str__(self) -> str:
        return (self.title)
    

class MedicationBox(models.Model):
    selected_medicines     = models.ForeignKey(Medicine,on_delete=models.CASCADE,related_name="selected_medicines")
    cannot_be_added        = models.BooleanField(default=False)

    buy_from_avalable      = models.IntegerField(null=True,blank=True)
    avalable               = models.IntegerField(null=True,blank=True)


def __str__(self):
    return '{}'.format(self.selected_medicines.title)

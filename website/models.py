from django.db import models
from website.utils import get_uuid, image_upload_path


class Dish(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=36, default=get_uuid, editable=False)
    cover = models.ImageField(upload_to=image_upload_path,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    edible_portion = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    per_serving_size = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    gda = models.ImageField(upload_to=image_upload_path,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True,db_index=True)
    last_modified = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'website'
        db_table = 'website_dish'
        verbose_name_plural = 'dishes'
    
    def __str__(self):
        return self.name


class Nutrition(models.Model):
    dish = models.OneToOneField(Dish, related_name='dish_nutrition', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Weight')
    calories = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Calories (kcal)')
    protein = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Protein (grams)')
    carbohydrates = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Carbohydrates (grams)')
    starch  = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Starch (grams)')
    sugar_total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Sugar (grams)')
    fat_total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Total Fat (grams)')
    fat_saturated = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,verbose_name='Saturated Fat (grams)')
    fat_trans = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,verbose_name='Unsaturated Trans Fat (grams)')
    fat_monounsaturated = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,verbose_name='Monounsaturated Fat (grams)')
    fat_polyunsaturated = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,verbose_name='Polyunsaturated Fat (grams)')
    cholesterol = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Cholesterol (milligrams)')
    dietary_fibre = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Dietary Fibre (grams)')
    sodium = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Sodium (milligrams)')
    iron = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Iron (milligrams)')
    calcium = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Calcium (milligram)')
    chloride = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Chloride (grams)')
    potassium = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Potassium (milligrams)')
    phosphorus = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Phosphorus (grams)')
    magnesium = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Magnesium (grams)')
    selenium = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Selenium (microgram)')
    fluoride = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Fluoride (grams)')
    iodine = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Iodine (microgram)')
    chromium = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Chromium (microgram)')
    manganese = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Maganese (grams)')
    zinc = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Zinc (milligrams)')
    copper = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Copper (microgram)')
    water = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Water (grams)')
    beta_carotene = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Beta Carotene A (micrograms)')
    retinol = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Retinol (micrograms)')
    vitamin_a = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin A (micrograms)')
    vitamin_b = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin B (micrograms)')
    vitamin_b1 = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin B1 (milligrams)')
    vitamin_b2 = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin B2 (milligrams)')
    vitamin_b3 = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin B3 (milligrams)')
    vitamin_b5 = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin B5 (milligrams)')
    vitamin_b6 = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin B6 (milligrams)')
    vitamin_b9 = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin B9 (micrograms)')
    vitamin_b12 = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin B12 (milligrams)')
    vitamin_c = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin C (milligrams)')
    vitamin_d = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin D (micrograms)')
    vitamin_e = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin E (milligrams)')
    vitamin_k = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,verbose_name='Vitamin K (micrograms)')
    is_system_generated = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=True)
    class Meta:
        app_label = 'website'
        db_table = 'website_nutrition'
    
    def __unicode__(self):
        return u'Nutritional details for recipe %s' %(self.recipe)



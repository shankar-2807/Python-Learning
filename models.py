from django import models

class Category(models.model):
    cname = models.CharField(max_length=20)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.cname


class Cake(models.model):
    cake_name = models.CharField(max_length=20)
    price = models.CharField(default=200)
    description = models.Charfield(max_length=100)
    image_url = models.ImageField(default='abc.jpg', upload_to='static/Images')
    category = models.Foreginkey(Category,on_delete=models.CASCADE)

    class Meta:
        db_cake = "Cake"





from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

class ChaiVariety(models.Model):
   CHAI_TYPE_CHOICE = [
      ('ML', 'MASALA'),
      ('GL', 'GINGER'),
      ('KL', 'KIWI'),
      ('EL', 'ELACHI'),
   ]
   user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   name = models.CharField(max_length=100)
   image = models.ImageField(upload_to='pychais/')
   date_added = models.DateTimeField(auto_now_add=True)
   type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE, default='Select Chaitype')
   description = models.TextField(default='', max_length=500)
   method = models.TextField(default='', max_length=1000)
   price = models.DecimalField(max_digits=5, decimal_places=2 , default=0.00)

   def __str__(self):
      return self.name

class PyChaiReview(models.Model):
   chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   rating = models.IntegerField()
   comment = models.TextField()
   date_added = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.user.username + ' review for ' + self.chai.name + ' ' + str(self.rating)

class PyChaiLike(models.Model):
   chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='Likes')
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   date_added = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.chai.name + " liked by " + self.user.username  # Fixed issue

class Store(models.Model):
   name = models.CharField(max_length=100)
   location = models.CharField(max_length=100)
   Store_owner = models.ForeignKey(User, on_delete=models.CASCADE, default='')
   Store_open = models.DateTimeField(default=now)
   Store_close = models.DateTimeField(default=now)
   Store_image = models.ImageField(upload_to='store/', default='')
   chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

   def __str__(self):
      return self.name + ' ' + self.location


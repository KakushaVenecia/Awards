from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    name=models.CharField(blank=True,max_length=120)
    profile_pic=models.ImageField(upload_to='pictures/',default='default.png')
    bio=models.TextField(max_length=400,blank=True)
    location=models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='profile')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()  

    @classmethod
    def update_bio(cls,id,bio):
        update_profile = cls.object.filter(id=id).update(bio=bio) 
        return update_profile 

    @classmethod
    def search_profile(cls,search_term) :
        profiles=cls.objects.filter(user__username__icontains=search_term) 
        return profiles 
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()         


class Category (models.Model):
    name = models.CharField(max_length =60)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()   

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(name=value)


class Project(models.Model):
    photo = models.ImageField(upload_to ='pictures/')
    name = models.CharField(max_length =60)
    description = models.CharField(max_length =300)
    created_at=models.DateField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project', blank=True)
   
    def __str__(self):
        return self.name

    class Meta:
        ordering =['name']

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def update_project(cls, id, value):
        cls.objects.filter(id=id).update(Photo =value)

    @classmethod
    def search_by_category(cls, search_term):
        projects = cls.objects.filter(category__name__icontains=search_term) 
        return projects

RATE_CHOICES =[
    (1, '1- Worst'),
    (2, '2- Awful'),
    (3, '3- Bad'),
    (4, '4- Poor'),
    (5, '5- Average'),
    (6, '6- Satisfactory'),
    (7, '7- Good'),
    (8, '8- Great'),
    (9, '9- Almost Perfect'),
    (10, '10- Excellent'),
]
class Rate(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="reviews")
    date=models.DateTimeField(auto_now_add=True) 
    text=models.TextField(max_length=30000, blank=True, null=True)
    designrate=models.PositiveSmallIntegerField( choices=RATE_CHOICES)
    contentrate=models.PositiveSmallIntegerField( choices=RATE_CHOICES)
    usabilityrate=models.PositiveSmallIntegerField( choices=RATE_CHOICES)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    comment=models.TextField()
    created=models.DateField(auto_now_add=True,null=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='comments')

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(post__id=id)
        return comments

    def __str__(self):
        return self.comment

class Rating(models.Model):
	source = models.CharField(max_length=50)
	rating = models.CharField(max_length=10)

	def __str__(self):
		return self.source

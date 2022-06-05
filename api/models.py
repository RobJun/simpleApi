from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userId = models.BigIntegerField()
    title = models.TextField()
    body = models.TextField()

    def save(self,*args,**kwargs):
        if(isinstance(self.id, dict)):
            data = self.id
            self.id = data['id']
            self.userId = data['userId']
            self.title = data['title']
            self.body = data['body']
            super(Post,self).save(*args,**kwargs)
            return;
        if not Post.objects.filter(id__gt=100).count():
            self.id = 101
        else:
            self.id = Post.objects.last().id+1
        super(Post,self).save(*args,**kwargs)
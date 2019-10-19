from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suggestion(models.Model):
    suggestion = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username + " " + self.suggestion

class Comment(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username + " " + self.comment




# from django.db import models
# from django.contrib.auth.models import User				# Adding a user

# # Create your models here.
# # A model acts as a variable which will store information in the DB

# class Suggestion(models.Model):
# 	suggestion = models.CharField(max_length=240)
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)			# Added author to suggestion so need to update database
# 	created_on = models.DateTimeField(auto_now_add = True)

# 	def __str__(self):
# 		return self.author.username + " " + self.suggestion     # adds the author and the username to the suggestion


# class Comment(models.Model):
# 	comment = models.CharField(max_length=240)
# 	author = models.ForeignKey(User, on_delete=models.CASCADE)			# Added author to suggestion so need to update database
# 	suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)		
# 	created_on = models.DateTimeField(auto_now_add = True)


# 	def __str__(self):
# 		return self.author.username + " " + self.comment     # adds the author and the username to the suggestion


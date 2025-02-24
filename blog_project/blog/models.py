from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name = "Пост"
		verbose_name_plural = "Пости"

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])
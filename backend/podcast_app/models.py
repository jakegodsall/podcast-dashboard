from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".capitalize()

class Podcast(models.Model):
    name = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, blank=True, related_name='podcast')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='podcast')

    def __str__(self):
        return f"{self.name} ({self.language})"

class Episode(models.Model):
    title = models.CharField(max_length=200)
    episode_number = models.PositiveIntegerField()
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='episode')
    duration = models.CharField(max_length=10)
    listen_link = models.URLField()
    is_new = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.episode_number}: {self.title[:15]}... ({self.podcast})"
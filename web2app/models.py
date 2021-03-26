from django.db import models


class MovieModel(models.Model):
    movie_id = models.AutoField
    movieName=models.CharField(max_length=50)
    movieSize = models.FloatField(default=0)
    movieUrl = models.URLField(max_length=1000)
    movieVideo = models.FileField(upload_to='web2app/movieImage/videos',null=True,verbose_name="")

    def __str__(self):
        return self.movieName
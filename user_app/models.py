from django.db import models


class Man(models.Model):
    uid = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30, unique=True, db_index=True)
    age = models.IntegerField(default=18)
    sex = models.BooleanField(default=True)
    info = models.TextField(null=True, blank=True)
    salary = models.FloatField(default=12.00)
    money = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    birthday = models.DateField(auto_now_add=True)
    birthday2 = models.DateTimeField(auto_now=True)
    icon = models.FileField(null=True, upload_to="statics/")
    img = models.ImageField(null=True, upload_to="statics/")
    use_type = models.IntegerField(choices=((1, "a"), (2, "b")), default=1, name='utype', verbose_name="用户类型",
                                   editable=True)

    # 在admin后台显示
    def __str__(self):
        return f'{self.name}-{self.age}'

    class Meta:
        db_table = "user_app_man"


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32, unique=True)
    age = models.IntegerField(default=18)
    sex = models.CharField(max_length=10, default="0")
    is_deleted = models.BooleanField(default=False)
    uuid = models.ForeignKey(Man, on_delete=models.CASCADE)
    # uuuid = models.OneToOneField(Man, on_delete=models.PROTECT)

    # 在admin后台显示
    def __str__(self):
        return f'{self.name}-{self.age}'


class Movie(models.Model):
    name = models.CharField(max_length=10)
    duration = models.IntegerField(default=90)


class People(models.Model):
    name = models.CharField(max_length=10)
    movies = models.ManyToManyField(Movie)
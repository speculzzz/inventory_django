from django.db import models


class TimestampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Inventory(TimestampMixin):
    name = models.CharField(max_length=64, default='')


class Tag(TimestampMixin):
    text = models.CharField(max_length=32, unique=True)


class Item(TimestampMixin):
    name = models.CharField(max_length=64, unique=True)
    weight = models.PositiveSmallIntegerField(default=100)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.name} ({self.weight})'


class Sword(Item):

    class Meta:
        proxy = True

    def make_damage(self):
        print('damage!')


class UserItem(Item):
    user_name = models.CharField(max_length=32)

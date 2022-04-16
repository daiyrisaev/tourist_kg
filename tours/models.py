from django.contrib.auth.models import User
from django.db import models


class Tour(models.Model):
    title = models.CharField("название",max_length=100)
    image = models.ImageField("Фото",upload_to="tours/")
    description = models.TextField("описание")
    price = models.DecimalField("цена",max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField("Активный",default=True)

    class Meta:
        verbose_name= 'Тур'
        verbose_name_plural = 'Туры'
        ordering=['-created']

    def __str__(self):
        return self.title


class RegularTour(models.Model):
    TOUR_STATUS_WAITING='waiting'
    TOUR_STATUS_START='start'
    TOUR_STATUS_COMPLETED = 'completed'
    TOUR_STATUS_REJECTED='rejected'
    TOUR_STATUSES=(
        (TOUR_STATUS_WAITING,"идет набор"),
        (TOUR_STATUS_START,'начался'),
        (TOUR_STATUS_COMPLETED,"завершен"),
        (TOUR_STATUS_REJECTED,"отменен")
    )
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE)
    start_datetime=models.DateTimeField("Начало ")
    end = models.DateTimeField('Конец')
    places_count = models.PositiveSmallIntegerField('Количества мест')
    status = models.CharField("статус",
        choices=TOUR_STATUSES,
        default=TOUR_STATUS_WAITING,
                              max_length=10)

    class Meta:
        verbose_name = "Регуларный тур"
        verbose_name_plural = "Регуларный туры"
        ordering = ['-start_datetime']

    def __str__(self):
        return f"{self.tour.title}-{self.start_datetime.date()}"


class TourBooking(models.Model):
    STATUS_NEW = "new"
    STATUS_CONFIRMED = "confirmed"
    STATUS_FINISHED = "finished"
    STATUS_REJECTED = "rejected"
    BOOKING_STATUSES = (
        (STATUS_NEW,"Новый"),
        (STATUS_CONFIRMED,"Подтвержден"),
        (STATUS_FINISHED,"Завершен" ),
        (STATUS_REJECTED,"Отменен")
    )
    #STATUS GOOGLE

    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    regular_tour = models.ForeignKey(RegularTour,on_delete=models.DO_NOTHING)
    place_count = models.PositiveSmallIntegerField("место")
    mobile = models.CharField("Номер телефона",max_length=11,choices=BOOKING_STATUSES,default=STATUS_NEW)
    is_paid = models.BooleanField("оплачено",default=False)
    notice = models.CharField("Допю инфо",max_length=250,null=True,blank=True)
    status = models.CharField("статус",max_length=11)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "бронирование"
        verbose_name_plural="бронирования"
        ordering=["-created"]

    def __str__(self):
        return f"Бронь{self.id}"
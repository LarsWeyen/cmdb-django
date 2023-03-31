from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=150)
    Location = models.ForeignKey(Location, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=150)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Resources(models.Model):
    name = models.CharField(max_length=150)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    serial = models.CharField(max_length=150)

    class Meta:
        abstract = True


class LCD(Resources):
    resolution = models.CharField(max_length=50)
    refresh_rate = models.CharField(max_length=10)


class NetworkDevice(models.Model):
    ip_address = models.GenericIPAddressField()
    firmware = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Camera(Resources, NetworkDevice):
    frame_rate = models.CharField(max_length=25)
    compression_format = models.CharField(max_length=10)
    motion_detection = models.BooleanField()
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class DVR(Resources, NetworkDevice):
    storage_capacity = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class Router(Resources, NetworkDevice):
    hostname = models.CharField(max_length=50)
    ip_static = models.BooleanField()

    def __str__(self) -> str:
        return self.name


class QRScanner(Resources):
    port_type = models.CharField(max_length=10)
    resolution = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class RFID(Resources):
    frequency = models.CharField(max_length=10)
    voltage = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class Switch(Resources):
    num_ports = models.IntegerField()
    mac_address = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name


class LCB(Resources):
    voltage = models.CharField(max_length=25)
    connector = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name

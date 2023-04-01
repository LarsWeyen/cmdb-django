from django.db import models
from cryptography.fernet import Fernet
from django.contrib.auth.models import User

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
    parent = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True)
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
    password = models.CharField(max_length=50,null=True,blank=True)

    # def set_password(self,password,master_key):
    #     f = Fernet(master_key)
    #     password_bytes = password.encode('utf-8')
    #     encrypted_bytes = f.encrypt(password_bytes)
    #     self.encrypted_password = encrypted_bytes

    # key = Fernet.generate_key()
    #     f = Fernet(key)
    #     decrypted_password = f.decrypt(self.password).decode('utf-8')
    #     if master_password == self.master_password:
    #         return decrypted_password
    #     else:
    #         return None

    # def get_password(self,master_key):
    #     f = Fernet(master_key)
    #     decrypted_bytes = f.decrypt(self.encrypted_password)
    #     return decrypted_bytes.decode('utf-8')
    
    #   def set_password(self, master_password, new_password):
    #     if master_password == self.master_password:
    #         key = Fernet.generate_key()
    #         f = Fernet(key)
    #         self.password = f.encrypt(new_password.encode('utf-8'))
    #         self.save()
    #         return True
    #     else:
    #         return False
    
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

class IPC(Resources):
    cpu = models.CharField(max_length=50)
    android_version = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Maintenance(models.Model):
    description = models.TextField()
    date=models.DateField()
    technician = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Distrispot(models.Model):
    name=models.CharField(max_length=50)
    parent = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True)
    location = models.CharField(max_length=50)
    maintenance = models.ForeignKey(Maintenance,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self) -> str:
        return self.name


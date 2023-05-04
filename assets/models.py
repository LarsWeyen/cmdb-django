from django.db import models
from cryptography.fernet import Fernet
from django.contrib.auth.models import User

from assets.managers import AssetChildManager, AssetManager

class Type(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    
    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    # location = models.ForeignKey(Location, on_delete=models.PROTECT)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

    def sid(self):
        return "CUS-"+str(f'{self.id:04}')

class Asset(models.Model):
    name = models.CharField(max_length=150)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def sid(self):
        return "AST-"+str(f'{self.id:04}')
    
    # objects = models.Manager()
    objects = AssetManager()


class Resources(models.Model):
    manufacturer = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    serial = models.CharField(max_length=150)

    class Meta:
        abstract = True


class LCD(Resources):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='lcd')
    resolution = models.CharField(max_length=50)
    refresh_rate = models.CharField(max_length=10)

    def sid(self):
        return "LCD-"+str(f'{self.id:04}')

class NetworkDevice(models.Model):
    ip_address = models.CharField(max_length=150)
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
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='camera')
    frame_rate = models.CharField(max_length=25)
    resolution = models.CharField(max_length=25)
    compression_format = models.CharField(max_length=10)
    motion_detection = models.BooleanField()

    def __str__(self) -> str:
        return self.asset.name
    
    def sid(self):
        return "CAM-"+str(f'{self.id:04}')


class DVR(Resources, NetworkDevice):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='dvr')
    storage_capacity = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.asset.name
    
    def sid(self):
        return "DVR-"+str(f'{self.id:04}')


class Router(Resources, NetworkDevice):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='router')
    hostname = models.CharField(max_length=50)
    ip_static = models.BooleanField()

    def __str__(self) -> str:
        return self.asset.name
    
    def sid(self):
        return "RTR-"+str(f'{self.id:04}')
    
class QRScanner(Resources):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='qrscanner')
    port_type = models.CharField(max_length=10)
    resolution = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.asset.name
    
    def sid(self):
        return "QRS-"+str(f'{self.id:04}')

class RFID(Resources):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='rfid')
    frequency = models.CharField(max_length=10)
    voltage = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.asset.name
    
    def sid(self):
        return "RFID-"+str(f'{self.id:04}')

class Switch(Resources):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='switch')
    num_ports = models.IntegerField()
    mac_address = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.asset.name

    def sid(self):
        return "SWT-"+str(f'{self.id:04}')

class LCB(Resources):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='lcb')
    voltage = models.CharField(max_length=25)
    connector = models.CharField(max_length=25)

    def sid(self):
        return "LCB-"+str(f'{self.id:04}')
    

class IPC(Resources):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='ipc')
    cpu = models.CharField(max_length=50)
    android_version = models.CharField(max_length=20)
    storage = models.CharField(max_length=50)
    display_adapter = models.CharField(max_length=20)
    memory = models.CharField(max_length=50)
    input_voltage = models.CharField(max_length=20)
    power_input = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.asset.name

    def sid(self):
        return "IPC-"+str(f'{self.id:04}')
    
class Distrispot(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='distrispot')
    status_choices = (('ONLINE','Online'),('OFFLINE','Offline'))
    status=models.CharField(choices=status_choices,default="ONLINE",max_length=20)
    slots_num = models.IntegerField()
    type = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=150,default='Belgium')

    def __str__(self) -> str:
        return self.asset.name
    def sid(self):
        return 'SPT'+str(f'{self.id:06}')
    
class Maintenance(models.Model):
    distrispot = models.ForeignKey(Distrispot,on_delete=models.SET_NULL,blank=True,null=True, related_name='maintenances')
    description = models.TextField()
    date=models.DateField()
    technician = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.description
    
    def sid(self):
        return "MTN-"+str(f'{self.id:04}')

class PowerSupply(Resources):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True,null=True,related_name='psu')
    voltage = models.CharField(max_length=25)
    form_factor = models.CharField(max_length=25)
    wattage = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.asset.name
    
    def sid(self):
        return "PSU-"+str(f'{self.id:04}')
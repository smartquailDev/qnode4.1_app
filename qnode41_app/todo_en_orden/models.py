from email.policy import default
from django.db import models
#from shop.models import Product
from decimal import Decimal
from django.contrib import admin
from phone_field import PhoneField
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
#from coupons.models import Coupon
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User



class Category(models.Model):
    
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(blank=True,null=True)
    detail = models.FileField(upload_to='tours/%Y/%m/%d',null=True)
    terms = models.TextField(blank=True)

    

    class Meta:
        #ordering = ('name',)
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    def __str__(self):
        return self.name

  #  def get_absolute_url(self):
  #          return reverse('shop:product_list_by_category',
  #                         args=[self.slug])


class service(models.Model):
  
    
    name = models.CharField(max_length=200, db_index=True),
    slug = models.SlugField(max_length=200, db_index=True),
    description = models.TextField(blank=True),
    price = models.DecimalField(max_digits=10000, decimal_places=2),
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,null=True),
    
    available = models.BooleanField(default=True)

    item1 = models.CharField(max_length=200,null=True)
    item2 = models.CharField(max_length=200,null=True)
    item3 = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    image_2 = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    image_3 = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #ordering = ('name',)
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    #class Meta:
     #   ordering = ('name',)
     #   index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

  #  def get_absolute_url(self):
  #          return reverse('shop:product_detail',
  #                         args=[self.id, self.slug])

class Order(models.Model):

    QUITO = 'UIO'
    GUAYAQUIL = 'GYL'
    CUENCA = 'CA'

    CITY = [
        (QUITO, 'Quito'),
        ( GUAYAQUIL, 'Guayaquil'),
        (CUENCA, 'Cuenca'),
    ]



    HOMEDETAIL = 'HD'
    HABITAD = 'HA'
    PARTICULAR = 'PA'

    AGENCIAS = [
        (HOMEDETAIL, 'homedetail'),
        (HABITAD, 'habitad'),
        (PARTICULAR, 'particular'),
    ]

    # EDIFICIOS
    ADRIANPETRO = 'AP'
    CENTRODIDECOBOSQUE = 'CDB'
    ALCAZARSALAMANCA = 'ASM'
    ALCAZARSEVILLA = 'ASV'
    SIERRA = 'CHS'
    SANMARTIN = 'CSM'
    SIRAH = 'CS'
    VALLECARTAGO ='VC'
    VILLAMARINAUNO ='VMU'
    PIAZZATOSCANA = 'PZT'
    ARISTOPLAZA = 'APZ'
    ASIEL= 'AL'
    ASPEN= 'ASP'
    BATANPLAZA= 'BTP'
    BIZANCIO= 'BZ'
    BLUEDIAMOND = 'BD'
    BRISTOLTORRE = 'BT'
    CAMPUSCENTRAL = 'CC'
    CORYBA = 'CB'
    PEDREGAL = 'PD'
    FOURSEASONS = 'FS'
    KORONI = 'KN'
    KOUROS = 'KS'
    LAFARGUE = 'LG'
    METROPOLITAN = 'MN'
    PLUSDOS = 'PD'
    PUERTASDELSOL = 'PS'
    SCALA = 'SL'
    SOHOGALAXY = 'SG'
    SORELINA = 'SR'
    TENISBOULEVARD = 'TB'
    TERRAZASATRIUM = 'TA'
    TORRECARE = 'TC'
    TORREFINLANDIA = 'TF'
    TORRESOL = 'TS'
    TORRESUR = 'TSR'
    TRIER = 'TR'
    TRINIDAD = 'TD'
    VERONES = 'VR'
    VIENA = 'VN'
    AQUA = 'AQ'
    HOMEDETAIL = 'HD'
    KENZE = 'KZ'
    CASAENPARQUE = 'CP'
    NOVAKSTATUS = 'NS'
    PRISMANORTE = 'PN'
    CRISTIANSILVA = 'CS'
    TORREDELSOL = 'VN'
    TORRENOHA = 'TN'



    EDIFICIOS = [
        (ADRIANPETRO, 'ADRIAN PETROLEUM SERVICES S.A'),
        (CENTRODIDECOBOSQUE, 'CENTRO DE DISEÑO Y DECORACIÓN EL BOSQUE'),
        (ALCAZARSALAMANCA, 'CONJUNTO ALCAZAR DE SALAMANCA'),
        (SIERRA, 'CONJUNTO HABITACIONAL SIERRA I Y II'),
        (SANMARTIN, 'CONJUNTO SAN MARTÍN'),
        (SIRAH, 'CONJUNTO SIRAH'),
        (VALLECARTAGO, 'CONJUNTO VALLE CARTAGO'),
        (VILLAMARINAUNO, 'CONJUNTO VIA MARINA UNO'),
        (PIAZZATOSCANA, 'EDIFICIO PIAZZA TOSCANA'),
        (ARISTOPLAZA, 'EDIFICIO ARISTO PLAZA'),
        (ASIEL, 'EDIFICIO ASIEL'),
        (ASPEN, 'EDIFICIO ASPEN'),
        (BATANPLAZA, 'EDIFICIO BATAN PLAZA'),
        (BIZANCIO, 'EDIFICIO BIZANCIO'),
        (BLUEDIAMOND, 'EDIFICIO BLUE DIAMOND II'),
        (BRISTOLTORRE, 'EDIFICIO BRISTOL TORRE II'),
        (CAMPUSCENTRAL, 'EDIFICIO CAMPUS CENTRAL'),
        (CORYBA, 'EDIFICIO CORYBA'),
        (PEDREGAL, 'EDIFICIO EL PEDREGAL'),
        (FOURSEASONS, 'EDIFICIO FOUR SEASONS I'),
        (KORONI, 'EDIFICIO KORONI'),
        (KOUROS, 'EDIFICIO KOUROS'),
        (LAFARGUE, 'EDIFICIO LAFARGUE'),
        (METROPOLITAN, 'EDIFICIO METROPOLITAN'),
        (PLUSDOS, 'EDIFICIO PLUS DOS CENTRO DE NEGOCIOS'),
        (PUERTASDELSOL, 'EDIFICIO PUERTAS DEL SOL'),
        (SCALA , 'EDIFICIO SCALA '),
        (SOHOGALAXY, 'EDIFICIO SOHO GALAXY'),
        (SORELINA, 'EDIFICIO SORELINA'),
        (TENISBOULEVARD, 'EDIFICIO TENIS BOULEVARD'),
        (TERRAZASATRIUM, 'EDIFICIO TERRAZAS ATRIUM'),
        (TORRECARE, 'EDIFICIO TORRE CARE'),
        (TORREFINLANDIA, 'EDIFICIO TORRE FINLANDIA'),
        (TORRESOL, 'EDIFICIO TORRE SOL I'),
        (TRIER, 'EDIFICIO TRIER'),
        (VERONES, 'EDIFICIO VERONES'),
        (VIENA, 'EDIFICIO VIENA'),
        (AQUA, 'FIDEICOMISO INMOBILIARIO PARK QUITO'),
        (HOMEDETAIL, 'AGENCIA HOMEDETAIL'),
        (KENZE, 'EDIFICIO KENZE'),
        (CASAENPARQUE, 'LA CASA EN EL PARQUE'),
        (NOVAKSTATUS, 'EDIFICIO NOVAK STATUS'),
        (PRISMANORTE, 'EDIFICIO PRISMA NORTE'),
        (CRISTIANSILVA, 'CRISTIAN SILVA DOMINGUEZ'),
        (TORREDELSOL, 'EDIFICIO TORRE DEL SOL'),
        (TORRENOHA , 'EDIFICIO TORRE NOHA'),

    ]
    

    agencia = models.CharField(_('Codigo de reporte'),max_length=2,choices=AGENCIAS,default='HOMEDETAIL')
    numero = models.IntegerField()
    reporte =  models.CharField(_('Codigo de reporte'), max_length=50, default='PFE')
    codigo =  models.CharField(_('Codigo de reporte'), max_length=50)
    first_name = models.CharField(_('Nombre de Edificio'), max_length=4,choices=EDIFICIOS)
    #----------------------------------
    last_name = models.CharField(_('Nombre de administrador'), max_length=150)
    email = models.EmailField(_('E-mail'))
    phone = models.CharField(blank=True, help_text=_('Telefono de administración'),max_length=16)
    ruc = models.CharField(blank=True, help_text=_('R.U.C'),max_length=13)
    direccion = models.CharField(_('Dirección'), max_length=250)
    #postal_code = models.CharField(_('postal code'), max_length=20)
    city = models.CharField(_('Ciudad'),max_length=3 ,choices=CITY,default='QUITO')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    emision = models.DateTimeField(_('Fecha de emisión'),null=True)
    vencimiento = models.DateTimeField(_('Fecha de vencimiento'),null=True)
    #start_arrival_time = models.DateTimeField(_('Time for Arrival to CC-floreana'),null=True)
    #end_departure_time = models.DateTimeField(_('Time for Arrival to CC-floreana'),null=True)
    #departure = models.DateTimeField(_('Date for departure from CC-floreana'),null=True)
    agree_term = models.BooleanField(_('I accept the terms and conditions of this services.'),default=False,null=False,blank=False)
    total =  models.DecimalField(max_digits=1000, decimal_places=2,null=True,blank=True)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Perfil Financiero de Edificio'
        verbose_name_plural = 'Perfiles Financieros de Edificios'

    def __str__(self):
        return 'Reserve to {}'.format(self.first_name +' '+ self.last_name)

    @property
    @admin.display(
        ordering='last_name',
        description='Full name',
    )
    def full_name(self):
        return self.first_name + ' ' + self.last_name



    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        total_price = total_cost - total_cost * (self.discount / Decimal('100'))
        return  total_price

    def save(self):
        self.codigo = self.numero + self.reporte + self.agencia 
        super (Order, self).save()

 


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    #product = models.ForeignKey(Product,
    #                            related_name='order_items',
    #                            on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

class admininout(models.Model):

        # EDIFICIOS
    ADRIANPETRO = 'AP'
    CENTRODIDECOBOSQUE = 'CDB'
    ALCAZARSALAMANCA = 'ASM'
    ALCAZARSEVILLA = 'ASV'
    SIERRA = 'CHS'
    SANMARTIN = 'CSM'
    SIRAH = 'CS'
    VALLECARTAGO ='VC'
    VILLAMARINAUNO ='VMU'
    PIAZZATOSCANA = 'PZT'
    ARISTOPLAZA = 'APZ'
    ASIEL= 'AL'
    ASPEN= 'ASP'
    BATANPLAZA= 'BTP'
    BIZANCIO= 'BZ'
    BLUEDIAMOND = 'BD'
    BRISTOLTORRE = 'BT'
    CAMPUSCENTRAL = 'CC'
    CORYBA = 'CB'
    PEDREGAL = 'PD'
    FOURSEASONS = 'FS'
    KORONI = 'KN'
    KOUROS = 'KS'
    LAFARGUE = 'LG'
    METROPOLITAN = 'MN'
    PLUSDOS = 'PD'
    PUERTASDELSOL = 'PS'
    SCALA = 'SL'
    SOHOGALAXY = 'SG'
    SORELINA = 'SR'
    TENISBOULEVARD = 'TB'
    TERRAZASATRIUM = 'TA'
    TORRECARE = 'TC'
    TORREFINLANDIA = 'TF'
    TORRESOL = 'TS'
    TORRESUR = 'TSR'
    TRIER = 'TR'
    TRINIDAD = 'TD'
    VERONES = 'VR'
    VIENA = 'VN'
    AQUA = 'AQ'
    HOMEDETAIL = 'HD'
    KENZE = 'KZ'
    CASAENPARQUE = 'CP'
    NOVAKSTATUS = 'NS'
    PRISMANORTE = 'PN'
    CRISTIANSILVA = 'CS'
    TORREDELSOL = 'VN'
    TORRENOHA = 'TN'



    EDIFICIOS = [
        (ADRIANPETRO, 'ADRIAN PETROLEUM SERVICES S.A'),
        (CENTRODIDECOBOSQUE, 'CENTRO DE DISEÑO Y DECORACIÓN EL BOSQUE'),
        (ALCAZARSALAMANCA, 'CONJUNTO ALCAZAR DE SALAMANCA'),
        (SIERRA, 'CONJUNTO HABITACIONAL SIERRA I Y II'),
        (SANMARTIN, 'CONJUNTO SAN MARTÍN'),
        (SIRAH, 'CONJUNTO SIRAH'),
        (VALLECARTAGO, 'CONJUNTO VALLE CARTAGO'),
        (VILLAMARINAUNO, 'CONJUNTO VIA MARINA UNO'),
        (PIAZZATOSCANA, 'EDIFICIO PIAZZA TOSCANA'),
        (ARISTOPLAZA, 'EDIFICIO ARISTO PLAZA'),
        (ASIEL, 'EDIFICIO ASIEL'),
        (ASPEN, 'EDIFICIO ASPEN'),
        (BATANPLAZA, 'EDIFICIO BATAN PLAZA'),
        (BIZANCIO, 'EDIFICIO BIZANCIO'),
        (BLUEDIAMOND, 'EDIFICIO BLUE DIAMOND II'),
        (BRISTOLTORRE, 'EDIFICIO BRISTOL TORRE II'),
        (CAMPUSCENTRAL, 'EDIFICIO CAMPUS CENTRAL'),
        (CORYBA, 'EDIFICIO CORYBA'),
        (PEDREGAL, 'EDIFICIO EL PEDREGAL'),
        (FOURSEASONS, 'EDIFICIO FOUR SEASONS I'),
        (KORONI, 'EDIFICIO KORONI'),
        (KOUROS, 'EDIFICIO KOUROS'),
        (LAFARGUE, 'EDIFICIO LAFARGUE'),
        (METROPOLITAN, 'EDIFICIO METROPOLITAN'),
        (PLUSDOS, 'EDIFICIO PLUS DOS CENTRO DE NEGOCIOS'),
        (PUERTASDELSOL, 'EDIFICIO PUERTAS DEL SOL'),
        (SCALA , 'EDIFICIO SCALA '),
        (SOHOGALAXY, 'EDIFICIO SOHO GALAXY'),
        (SORELINA, 'EDIFICIO SORELINA'),
        (TENISBOULEVARD, 'EDIFICIO TENIS BOULEVARD'),
        (TERRAZASATRIUM, 'EDIFICIO TERRAZAS ATRIUM'),
        (TORRECARE, 'EDIFICIO TORRE CARE'),
        (TORREFINLANDIA, 'EDIFICIO TORRE FINLANDIA'),
        (TORRESOL, 'EDIFICIO TORRE SOL I'),
        (TRIER, 'EDIFICIO TRIER'),
        (VERONES, 'EDIFICIO VERONES'),
        (VIENA, 'EDIFICIO VIENA'),
        (AQUA, 'FIDEICOMISO INMOBILIARIO PARK QUITO'),
        (HOMEDETAIL, 'AGENCIA HOMEDETAIL'),
        (KENZE, 'EDIFICIO KENZE'),
        (CASAENPARQUE, 'LA CASA EN EL PARQUE'),
        (NOVAKSTATUS, 'EDIFICIO NOVAK STATUS'),
        (PRISMANORTE, 'EDIFICIO PRISMA NORTE'),
        (CRISTIANSILVA, 'CRISTIAN SILVA DOMINGUEZ'),
        (TORREDELSOL, 'EDIFICIO TORRE DEL SOL'),
        (TORRENOHA , 'EDIFICIO TORRE NOHA'),

    ]

    edificio = models.CharField(_('Edificio'), max_length=4,choices=EDIFICIOS)
    operario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    ingreso = models.DateTimeField(_('Ingreso'),null=True)
    salida = models.DateTimeField(_('Salida'),null=True)
    novedades = models.TextField(_('Novedades'),blank=True)
    Observaciones = models.TextField(_('Novedades'),blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #ordering = ('name',)
        verbose_name = 'Entrada & Salida'
        verbose_name_plural = 'Entradas & Salidas'
    
    #class Meta:
     #   ordering = ('name',)
     #   index_together = (('id', 'slug'),)

    def __str__(self):
        return self.edificio


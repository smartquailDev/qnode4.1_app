# Generated by Django 3.2.16 on 2022-11-04 05:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('detail', models.FileField(null=True, upload_to='tours/%Y/%m/%d')),
                ('terms', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Planes',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencia', models.CharField(choices=[('HD', 'homedetail'), ('HA', 'habitad'), ('PA', 'particular')], default='HOMEDETAIL', max_length=2, verbose_name='Codigo de reporte')),
                ('numero', models.IntegerField()),
                ('reporte', models.CharField(default='PFE', max_length=50, verbose_name='Codigo de reporte')),
                ('codigo', models.CharField(max_length=50, verbose_name='Codigo de reporte')),
                ('first_name', models.CharField(choices=[('AP', 'ADRIAN PETROLEUM SERVICES S.A'), ('CDB', 'CENTRO DE DISEÑO Y DECORACIÓN EL BOSQUE'), ('ASM', 'CONJUNTO ALCAZAR DE SALAMANCA'), ('CHS', 'CONJUNTO HABITACIONAL SIERRA I Y II'), ('CSM', 'CONJUNTO SAN MARTÍN'), ('CS', 'CONJUNTO SIRAH'), ('VC', 'CONJUNTO VALLE CARTAGO'), ('VMU', 'CONJUNTO VIA MARINA UNO'), ('PZT', 'EDIFICIO PIAZZA TOSCANA'), ('APZ', 'EDIFICIO ARISTO PLAZA'), ('AL', 'EDIFICIO ASIEL'), ('ASP', 'EDIFICIO ASPEN'), ('BTP', 'EDIFICIO BATAN PLAZA'), ('BZ', 'EDIFICIO BIZANCIO'), ('BD', 'EDIFICIO BLUE DIAMOND II'), ('BT', 'EDIFICIO BRISTOL TORRE II'), ('CC', 'EDIFICIO CAMPUS CENTRAL'), ('CB', 'EDIFICIO CORYBA'), ('PD', 'EDIFICIO EL PEDREGAL'), ('FS', 'EDIFICIO FOUR SEASONS I'), ('KN', 'EDIFICIO KORONI'), ('KS', 'EDIFICIO KOUROS'), ('LG', 'EDIFICIO LAFARGUE'), ('MN', 'EDIFICIO METROPOLITAN'), ('PD', 'EDIFICIO PLUS DOS CENTRO DE NEGOCIOS'), ('PS', 'EDIFICIO PUERTAS DEL SOL'), ('SL', 'EDIFICIO SCALA '), ('SG', 'EDIFICIO SOHO GALAXY'), ('SR', 'EDIFICIO SORELINA'), ('TB', 'EDIFICIO TENIS BOULEVARD'), ('TA', 'EDIFICIO TERRAZAS ATRIUM'), ('TC', 'EDIFICIO TORRE CARE'), ('TF', 'EDIFICIO TORRE FINLANDIA'), ('TS', 'EDIFICIO TORRE SOL I'), ('TR', 'EDIFICIO TRIER'), ('VR', 'EDIFICIO VERONES'), ('VN', 'EDIFICIO VIENA'), ('AQ', 'FIDEICOMISO INMOBILIARIO PARK QUITO'), ('HD', 'AGENCIA HOMEDETAIL'), ('KZ', 'EDIFICIO KENZE'), ('CP', 'LA CASA EN EL PARQUE'), ('NS', 'EDIFICIO NOVAK STATUS'), ('PN', 'EDIFICIO PRISMA NORTE'), ('CS', 'CRISTIAN SILVA DOMINGUEZ'), ('VN', 'EDIFICIO TORRE DEL SOL'), ('TN', 'EDIFICIO TORRE NOHA')], max_length=4, verbose_name='Nombre de Edificio')),
                ('last_name', models.CharField(max_length=150, verbose_name='Nombre de administrador')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(blank=True, help_text='Telefono de administración', max_length=16)),
                ('ruc', models.CharField(blank=True, help_text='R.U.C', max_length=13)),
                ('direccion', models.CharField(max_length=250, verbose_name='Dirección')),
                ('city', models.CharField(choices=[('UIO', 'Quito'), ('GYL', 'Guayaquil'), ('CA', 'Cuenca')], default='QUITO', max_length=3, verbose_name='Ciudad')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('emision', models.DateTimeField(null=True, verbose_name='Fecha de emisión')),
                ('vencimiento', models.DateTimeField(null=True, verbose_name='Fecha de vencimiento')),
                ('agree_term', models.BooleanField(default=False, verbose_name='I accept the terms and conditions of this services.')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True)),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'verbose_name': 'Perfil Financiero de Edificio',
                'verbose_name_plural': 'Perfiles Financieros de Edificios',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('item1', models.CharField(max_length=200, null=True)),
                ('item2', models.CharField(max_length=200, null=True)),
                ('item3', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('image_2', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('image_3', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='todo_en_orden.order')),
            ],
        ),
    ]
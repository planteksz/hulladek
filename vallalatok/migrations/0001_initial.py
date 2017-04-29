# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telephely',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('KTJ', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(code='nomatch', message='It must have 9 digits. (Only digits).', regex='^\\d{9}$')], verbose_name='KÜJ (Környezetvédelmi Ügyfél Jel)')),
                ('nev', models.CharField(max_length=100, verbose_name='neve')),
                ('tipus', models.CharField(max_length=1, choices=[('T', 'termelő')], verbose_name='típusa')),
                ('iranyitoszam', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='nomatch', message='It must have 4 digits. (Only digits).', regex='^\\d{4}$')], verbose_name='irányítószám')),
                ('kozterulet_nev', models.CharField(max_length=200, verbose_name='közterület neve')),
                ('kozterulet_tipus', models.CharField(max_length=2, choices=[('uc', 'utca'), ('út', 'út'), ('sg', 'sugárút'), ('fs', 'fasor'), ('tr', 'tér'), ('tr', 'köz')], default='uc', verbose_name='közterület típusa')),
                ('hazszam', models.CharField(max_length=30, verbose_name='házszám')),
                ('foglalkoztatottak_szama', models.IntegerField(verbose_name='foglalkoztatottak száma')),
                ('felelos_nev', models.CharField(max_length=200, verbose_name='felelős személy neve')),
                ('felelos_beosztas', models.CharField(max_length=30, verbose_name='felelős személy beosztása')),
            ],
        ),
        migrations.CreateModel(
            name='Telepules',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nev', models.CharField(max_length=100)),
                ('megye', models.IntegerField(null=True, choices=[(0, 'Budapest'), (1, 'Pest'), (2, 'Fejér'), (3, 'Komárom-Esztergom'), (4, 'Veszprém'), (5, 'Győr-Moson-Sopron'), (6, 'Vas'), (7, 'Zala'), (8, 'Baranya'), (9, 'Somogy'), (10, 'Tolna'), (11, 'Borsod-Abaúj-Zemplén'), (12, 'Heves'), (13, 'Nógrád'), (14, 'Hajdú-Bihar'), (15, 'Jász-Nagykun-Szolnok'), (16, 'Szabolcs-Szatmár-Bereg'), (17, 'Bács-Kiskun'), (18, 'Békés'), (19, 'Csongrád')], verbose_name='megye')),
                ('min_iranyitoszam', models.IntegerField()),
                ('max_iranyitoszam', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TermeloVallalat',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('KUJ', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(code='nomatch', message='It must have 9 digits. (Only digits).', regex='^\\d{9}$')], verbose_name='KÜJ (Környezetvédelmi Ügyfél Jel)')),
                ('KSH', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(code='nomatch', message='It must have 17 digits. (Only digits).', regex='^\\d{17}$')], help_text='Csak a számjegyeket írja be,a kötőjeleket ne.', verbose_name='KSH statisztikai számjel')),
                ('nev', models.CharField(max_length=100, verbose_name='vállalat neve')),
                ('iranyitoszam', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='nomatch', message='It must have 4 digits. (Only digits).', regex='^\\d{4}$')], verbose_name='irányítószám')),
                ('kozterulet_nev', models.CharField(max_length=200, verbose_name='közterület neve')),
                ('kozterulet_tipus', models.CharField(max_length=2, choices=[('uc', 'utca'), ('út', 'út'), ('sg', 'sugárút'), ('fs', 'fasor'), ('tr', 'tér'), ('tr', 'köz')], default='uc', verbose_name='közterület típusa')),
                ('hazszam', models.CharField(max_length=30, verbose_name='házszám')),
                ('telepules', models.ForeignKey(to='vallalatok.Telepules')),
            ],
        ),
        migrations.AddField(
            model_name='telephely',
            name='telepules',
            field=models.ForeignKey(to='vallalatok.Telepules'),
        ),
    ]

# Generated by Django 2.0.2 on 2018-04-05 15:20

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('origin', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('company', models.CharField(max_length=30, unique=True)),
                ('company_phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('initial_password', models.CharField(blank=True, max_length=40, null=True)),
                ('owner', models.CharField(blank=True, max_length=30, null=True, verbose_name='owner')),
                ('spouse_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='significant other')),
                ('street_address', models.CharField(blank=True, help_text='example: 55 Linda Lane', max_length=100, verbose_name='address')),
                ('city', models.CharField(blank=True, help_text='example: Allentown', max_length=100, verbose_name='city')),
                ('state', models.CharField(choices=[('PA', 'Pennsylvania'), ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='PA', max_length=40, verbose_name='state')),
                ('zip_code', models.IntegerField(verbose_name='zip code')),
                ('contact_phone', models.CharField(blank=True, max_length=30, null=True)),
                ('alt_contact_phone', models.CharField(blank=True, max_length=30, null=True)),
                ('logo', versatileimagefield.fields.VersatileImageField(blank=True, height_field='height', null=True, upload_to='images/company/', verbose_name='Image', width_field='width')),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Height')),
                ('width', models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Width')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Company',
                'ordering': ['company'],
            },
        ),
    ]

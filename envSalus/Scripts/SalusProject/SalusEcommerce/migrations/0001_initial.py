# Generated by Django 4.2.1 on 2023-05-16 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('CodCuenta_C', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Saldo_C', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=18)),
            ],
            options={
                'verbose_name': 'Cuentas de usuarios',
                'verbose_name_plural': 'Cuentas',
                'db_table': 'Cuenta',
            },
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('CodServicio_S', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('TipoServicio_S', models.CharField(max_length=20)),
                ('Precio_S', models.DecimalField(decimal_places=2, max_digits=18)),
                ('Descripcion_S', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Tipo de Servicios',
                'verbose_name_plural': 'Servicios',
                'db_table': 'Servicio',
            },
        ),
        migrations.CreateModel(
            name='TiposEstudios',
            fields=[
                ('CodEstudio_TE', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('NombreEstudio_TE', models.CharField(max_length=45)),
                ('Descripcion_TE', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Tipo de Estudio',
                'verbose_name_plural': 'TiposEstudios',
                'db_table': 'TipoEstudio',
            },
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('NroVenta_V', models.AutoField(primary_key=True, serialize=False)),
                ('FechaVenta_V', models.DateField(auto_now_add=True)),
                ('TotalVenta_V', models.DecimalField(decimal_places=2, max_digits=18)),
                ('CodCuenta_C_V', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.cuentas')),
            ],
            options={
                'verbose_name': 'Ventas a Cuentas',
                'verbose_name_plural': 'Ventas',
                'db_table': 'Venta',
            },
        ),
        migrations.CreateModel(
            name='UsuariosPacientes',
            fields=[
                ('Dni_UP', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Nombre_UP', models.CharField(max_length=45)),
                ('Apellido_UP', models.CharField(max_length=45)),
                ('Celular_UP', models.CharField(max_length=45)),
                ('Direccion_UP', models.CharField(max_length=100)),
                ('Localidad_UP', models.CharField(max_length=45)),
                ('Email_UP', models.CharField(max_length=45)),
                ('CodCuenta_UP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.cuentas')),
            ],
            options={
                'verbose_name': 'Usuario Paciente',
                'verbose_name_plural': 'UsuariosPacientes',
                'db_table': 'UsuarioPaciente',
            },
        ),
        migrations.CreateModel(
            name='UsuariosMedicos',
            fields=[
                ('Dni_UM', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Matricula_UM', models.CharField(max_length=8)),
                ('Nombre_UM', models.CharField(max_length=45)),
                ('Apellido_UM', models.CharField(max_length=45)),
                ('Celular_UM', models.CharField(max_length=45)),
                ('Direccion_UM', models.CharField(max_length=100)),
                ('Localidad_UM', models.CharField(max_length=45)),
                ('Email_UM', models.CharField(max_length=45)),
                ('CodCuenta_UM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.cuentas')),
            ],
            options={
                'verbose_name': 'Usuarios Medicos',
                'verbose_name_plural': 'UsuariosMedicos',
                'db_table': 'UsuarioMedico',
            },
        ),
        migrations.CreateModel(
            name='ServiciosXMedicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodServicio_SXM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.servicios')),
                ('Dni_UM_SXM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.usuariosmedicos')),
            ],
            options={
                'verbose_name': 'Servicio y Medico',
                'verbose_name_plural': 'ServiciosMedicos',
                'db_table': 'ServicioMedico',
            },
        ),
        migrations.CreateModel(
            name='MedicosPacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dni_UM_MP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.usuariosmedicos')),
                ('Dni_UP_MP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.usuariospacientes')),
            ],
            options={
                'verbose_name': 'Medicos Pacientes',
                'verbose_name_plural': 'MedicosPacientes',
                'db_table': 'MedicoPaciente',
            },
        ),
    ]
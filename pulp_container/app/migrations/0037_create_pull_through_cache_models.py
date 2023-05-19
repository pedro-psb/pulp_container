# Generated by Django 4.2.8 on 2023-12-12 21:15

from django.db import migrations, models
import django.db.models.deletion
import pulpcore.app.models.access_policy


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0116_alter_remoteartifact_md5_alter_remoteartifact_sha1_and_more'),
        ('container', '0036_containerpushrepository_pending_blobs_manifests'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerPullThroughRemote',
            fields=[
                ('remote_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.remote')),
            ],
            options={
                'permissions': [('manage_roles_containerpullthroughremote', 'Can manage role assignments on pull-through container remote')],
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.remote', pulpcore.app.models.access_policy.AutoAddObjPermsMixin),
        ),
        migrations.AddField(
            model_name='containerrepository',
            name='pending_blobs',
            field=models.ManyToManyField(to='container.blob'),
        ),
        migrations.AddField(
            model_name='containerrepository',
            name='pending_manifests',
            field=models.ManyToManyField(to='container.manifest'),
        ),
        migrations.CreateModel(
            name='ContainerPullThroughDistribution',
            fields=[
                ('distribution_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.distribution')),
                ('private', models.BooleanField(default=False, help_text='Restrict pull access to explicitly authorized users. Related distributions inherit this value. Defaults to unrestricted pull access.')),
                ('description', models.TextField(null=True)),
                ('namespace', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='container_pull_through_distributions', to='container.containernamespace')),
            ],
            options={
                'permissions': [('manage_roles_containerpullthroughdistribution', 'Can manage role assignments on pull-through cache distribution')],
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.distribution', pulpcore.app.models.access_policy.AutoAddObjPermsMixin),
        ),
        migrations.AddField(
            model_name='containerdistribution',
            name='pull_through_distribution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='distributions', to='container.containerpullthroughdistribution'),
        ),
    ]

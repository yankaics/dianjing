# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gift_code', '0002_auto_20161130_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCodeGen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='\u751f\u6210\u6570\u91cf')),
                ('used_amount', models.IntegerField(default=0, verbose_name='\u4f7f\u7528\u6570\u91cf')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'gift_code_gen',
                'verbose_name': '\u793c\u54c1\u7801\u751f\u6210',
                'verbose_name_plural': '\u793c\u54c1\u7801\u751f\u6210',
            },
        ),
        migrations.CreateModel(
            name='GiftCodeRecord',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('gen_id', models.IntegerField(db_index=True)),
                ('category', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'gift_code_record',
            },
        ),
        migrations.AlterModelOptions(
            name='giftcode',
            options={'verbose_name': '\u793c\u5305\u914d\u7f6e', 'verbose_name_plural': '\u793c\u5305\u914d\u7f6e'},
        ),
        migrations.AddField(
            model_name='giftcodeusinglog',
            name='category',
            field=models.CharField(db_index=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giftcodeusinglog',
            name='server_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='giftcode',
            name='active',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u6fc0\u6d3b'),
        ),
        migrations.AlterField(
            model_name='giftcode',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='\u540d\u5b57'),
        ),
        migrations.AlterField(
            model_name='giftcode',
            name='mail_content',
            field=models.TextField(verbose_name='\u90ae\u4ef6\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='giftcode',
            name='mail_title',
            field=models.CharField(max_length=255, verbose_name='\u90ae\u4ef6\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='giftcode',
            name='time_range1',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u4f7f\u7528\u65f6\u95f4\u8d77\u59cb'),
        ),
        migrations.AlterField(
            model_name='giftcode',
            name='time_range2',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u4f7f\u7528\u65f6\u95f4\u7ed3\u675f'),
        ),
        migrations.AlterField(
            model_name='giftcode',
            name='times_limit',
            field=models.IntegerField(default=1, help_text='\u5355\u4e2a\u793c\u54c1\u7801\u7684\u603b\u4f7f\u7528\u6b21\u6570\uff0c\u5305\u62ec\u4e0d\u540c\u73a9\u5bb6\uff0c\u4e0d\u540c\u670d', verbose_name='\u603b\u4f7f\u7528\u6b21\u6570\u9650\u5236'),
        ),
        migrations.AddField(
            model_name='giftcodegen',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gift_code.GiftCode', verbose_name='\u793c\u5305'),
        ),
    ]
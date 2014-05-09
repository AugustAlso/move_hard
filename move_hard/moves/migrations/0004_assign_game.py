# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        g = orm.Game(title='Apocalypse World')
        g.save()

        for x in orm.Move.objects.all():
            x.game = g
            x.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'moves.game': {
            'Meta': {'object_name': 'Game'},
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'primary_key': 'True'})
        },
        u'moves.move': {
            'Meta': {'object_name': 'Move'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['moves.Game']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['moves']
    symmetrical = True

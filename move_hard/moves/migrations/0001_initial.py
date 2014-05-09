# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MoveList'
        db.create_table(u'moves_movelist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'moves', ['MoveList'])


    def backwards(self, orm):
        # Deleting model 'MoveList'
        db.delete_table(u'moves_movelist')


    models = {
        u'moves.movelist': {
            'Meta': {'object_name': 'MoveList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['moves']
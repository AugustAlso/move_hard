# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'moves_game', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140, primary_key=True)),
        ))
        db.send_create_signal(u'moves', ['Game'])

        # Adding field 'Move.game'
        db.add_column(u'moves_move', 'game',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['moves.Game'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'moves_game')

        # Deleting field 'Move.game'
        db.delete_column(u'moves_move', 'game_id')


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
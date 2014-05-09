# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Move.game'
        db.alter_column(u'moves_move', 'game_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['moves.Game']))

    def backwards(self, orm):

        # Changing field 'Move.game'
        db.alter_column(u'moves_move', 'game_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['moves.Game'], null=True))

    models = {
        u'moves.game': {
            'Meta': {'object_name': 'Game'},
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'primary_key': 'True'})
        },
        u'moves.move': {
            'Meta': {'object_name': 'Move'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['moves.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['moves']
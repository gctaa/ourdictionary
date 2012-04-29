# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'WordBookEntry'
        db.create_table('wordbookviewer_wordbookentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('definition', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('part', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('example_sentence', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('photo', self.gf('stdimage.fields.StdImageField')(max_length=100, thumbnail_size={'width': 100, 'force': None, 'height': 75}, size={'width': 640, 'force': None, 'height': 480})),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('wordbookviewer', ['WordBookEntry'])


    def backwards(self, orm):
        
        # Deleting model 'WordBookEntry'
        db.delete_table('wordbookviewer_wordbookentry')


    models = {
        'wordbookviewer.wordbookentry': {
            'Meta': {'object_name': 'WordBookEntry'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'definition': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'example_sentence': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'part': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'photo': ('stdimage.fields.StdImageField', [], {'max_length': '100', 'thumbnail_size': "{'width': 100, 'force': None, 'height': 75}", 'size': "{'width': 640, 'force': None, 'height': 480}"})
        }
    }

    complete_apps = ['wordbookviewer']

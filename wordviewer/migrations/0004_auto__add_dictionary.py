# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dictionary'
        db.create_table(u'wordviewer_dictionary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'wordviewer', ['Dictionary'])


    def backwards(self, orm):
        # Deleting model 'Dictionary'
        db.delete_table(u'wordviewer_dictionary')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wordviewer.dictionary': {
            'Meta': {'object_name': 'Dictionary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'wordviewer.sitepreferences': {
            'Meta': {'object_name': 'SitePreferences'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('stdimage.fields.StdImageField', [], {'blank': 'True', 'max_length': '100', 'thumbnail_size': "{'width': 300, 'force': None, 'height': 225}", 'size': "{'width': 1024, 'force': None, 'height': 768}"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'wordviewer.wordentry': {
            'Meta': {'ordering': "['name']", 'object_name': 'WordEntry'},
            'caption': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'definition': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'example_sentence': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'part': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'photo': ('stdimage.fields.StdImageField', [], {'blank': 'True', 'max_length': '100', 'thumbnail_size': "{'width': 300, 'force': None, 'height': 225}", 'size': "{'width': 1024, 'force': None, 'height': 768}"}),
            'synonyms': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'translations': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'user_creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entry_creators'", 'to': u"orm['auth.User']"}),
            'user_last_modified': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entry_modifiers'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['wordviewer']
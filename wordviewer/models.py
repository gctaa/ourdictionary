from django.db import models
from stdimage import StdImageField
from south.modelsinspector import add_introspection_rules
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Rules for South to migrate the custom StdImageField, don't touch
rules = [
     (
         (StdImageField, ),
         [],
         {
             "size": ["size", {"default": None}],
             "thumbnail_size": ["thumbnail_size", {"default": None}],
         },
     ),
]
add_introspection_rules(rules, ["^stdimage\.fields",])


class WordEntry(models.Model):
      PART_CHOICES = (
      ("noun","Noun"),
      ("verb","Verb"),
      ("adjective","Adjective"),
      ("pronoun","Pronoun"),
      ("adverb","Adverb"),
      )
      name = models.CharField(max_length=30)
      part = models.CharField(max_length=15,verbose_name="Part of speech",choices=PART_CHOICES)
      definition = models.TextField(max_length=500)
      translations = models.TextField(verbose_name="Translation(s)", blank = True, max_length=500)
      synonyms = models.TextField(verbose_name="Synonym(s)", blank = True,max_length=500)
      example_sentence = models.TextField(verbose_name="Example Sentence(s)", blank  = True , max_length=500 )
      photo = StdImageField(blank = True ,upload_to="entryphoto/",size=(1024,768),thumbnail_size=(300,225))
      caption = models.TextField(blank = True, max_length=500)
      user_creator = models.ForeignKey(User,related_name="entry_creators")
      user_last_modified = models.ForeignKey(User,related_name="entry_modifiers")
      date_created = models.DateTimeField(auto_now_add=True)
      date_modified =models.DateTimeField(auto_now=True)
      def __unicode__(self):
          return "%s (%s)"% (self.name,self.part)
     
      class Meta:
           ordering = ["name"]


class SitePreferences(models.Model):
      name = models.CharField(blank  = True , max_length=30 )
      logo = StdImageField(blank = True, upload_to="logophoto/",
          size=(1024,768), thumbnail_size=(300,225))

      def clean(self):
          model = self.__class__
          if (model.objects.count() > 0 and self.id != model.objects.get().id):
              raise ValidationError('Can only create one %s instance' % model.__name__)

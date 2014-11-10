from django import forms

from ishare.models import Image, Entity, Album

class UploadImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['album', 'photo']

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        else:
            self.user = None
        super(UploadImageForm, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.user:
            raise forms.ValidationError('No user at all')

    def save(self, commit=True):
        image = super(UploadImageForm, self).save(commit=False)
        image.title = image.photo.name
        if commit:
            entity = Entity(entity_type=Entity.IMAGE, creator=self.user)
            entity.save()
            image.entity = entity
            image.save()
        return image


class CreateAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['title']

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        else:
            self.user = None
        super(CreateAlbumForm, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.user:
            raise forms.ValidationError('No user at all')

    def save(self, commit=True):
        album = super(CreateAlbumForm, self).save(commit=False)
        entity = Entity(entity_type=Entity.ALBUM, creator=self.user)
        album.entity = entity
        if commit:
            entity.save()
            album.save()
        return album
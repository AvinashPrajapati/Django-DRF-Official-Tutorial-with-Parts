from rest_framework import serializers
from snippets.models import Snippet


from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='snippets:snippet-detail', read_only=True) # error because of the snippets:  thing as the router is now directly in the main project urls.py rather than in snippets urls.py
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippets:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']
        # extra_kwargs = {
        #     'url': {'view_name': 'snippets:snippet-detail'},
        # }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='snippets:user-detail', read_only=True)
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippets:snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
        # extra_kwargs = {
        #     'url': {'view_name': 'snippets:user-detail'},
        # }
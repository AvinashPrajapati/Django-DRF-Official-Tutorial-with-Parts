from rest_framework import serializers
from snippets.models import Snippet


from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='snippet-detail', read_only=True) # removing snippets: and directly mentioning the view name
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']
        # extra_kwargs = {
        #     'url': {'view_name': 'snippets:snippet-detail'},
        # }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', read_only=True)
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
        # extra_kwargs = {
        #     'url': {'view_name': 'snippets:user-detail'},
        # }
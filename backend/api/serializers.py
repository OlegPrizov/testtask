from rest_framework import serializers

from sites.models import Site

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'creator', 'name', 'url']
        read_only_fields = ['creator']

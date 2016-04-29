from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from marshmallow import fields, Schema, pre_load, post_dump
import requests


class TrackSchema(Schema):
    class Meta:
        fields = ('url', 'aid', 'title', 'artist', 'duration', 'genre')

    @post_dump
    def trimTrack(self, in_data):
        if len(in_data['title']) > 40:
            in_data['title'] = in_data['title'][:40]
        if len(in_data['artist']) > 40:
            in_data['artist'] = in_data['artist'][:40]
        return in_data

    @post_dump
    def getDuration(self, in_data):
        minutes, seconds = divmod(in_data['duration'], 60)
        in_data['duration'] = '%d:%02d' % (minutes, seconds)
        return in_data

    @post_dump
    def getGenre(self, in_data):
        genres = ['Rock', 'Pop', 'Rap/Hip-Hop', 'Easy Listening', 'Dance/House', 'Instrumental', 'Metal', 'Dubstep', 'Jazz/Blues', 'Drum/Bass', 'Trance', 'Chanson', 'Ethnic', 'Acoustic/Vocal', 'Reggae', 'Classical', 'Indie/Pop', 'Contemporary', 'Speech', 'Other', 'Alternative', 'Electro-Pop/Disco']
        if in_data.get('genre', None) is not None:
            if 0 < in_data['genre'] < 23:
                in_data['genre'] = genres[in_data['genre'] - 1]
            else:
                in_data['genre'] = 'Other'
        return in_data


@api_view(['GET'])
def get_tracklist(request, query):
    """
    List all tracks from search query
    /tracklist
    """
    if request.method == 'GET':

        r = requests.get('https://api.vkontakte.ru/method/audio.search?q={}&count=200&access_token={}'.format(query, settings.ACCESS_TOKEN))
        queryResults = r.json()['response']
        queryResults.pop(0)

        track_schema = TrackSchema(many=True)
        result = track_schema.dump(queryResults)
        return Response(result.data)

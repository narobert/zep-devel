from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.conf import settings
import requests


class DashboardList(TemplateView):

    template_name = 'dashboard.html'

    def trimStr(self, string):
        if string is None:
            return 'Not found'
        if len(string) > 40:
            string = string[:40] + '...'
        return string

    def getDuration(self, duration):
        if duration is not None:
            minutes, seconds = divmod(duration, 60)
            return '%d:%02d' % (minutes, seconds)
        return '0:00'

    def getGenre(self, genre):
        genres = ['Rock', 'Pop', 'Rap/Hip-Hop', 'Easy Listening', 'Dance/House', 'Instrumental', 'Metal', 'Dubstep', 'Jazz/Blues', 'Drum/Bass', 'Trance', 'Chanson', 'Ethnic', 'Acoustic/Vocal', 'Reggae', 'Classical', 'Indie/Pop', 'Contemporary', 'Speech', 'Other', 'Alternative', 'Electro-Pop/Disco']
        if genre is not None:
            if 0 < genre < 23:
                return genres[genre - 1]
        return genres[19]

    def get_tracks(self):
        query = self.request.GET.get('q', None)
        if query is not None:
            r = requests.get('https://api.vkontakte.ru/method/audio.search?q={}&count=200&access_token={}'.format(query, settings.ACCESS_TOKEN))
            data = r.json()['response'][1:]
            for d in data:
                d['title'] = self.trimStr(d.get('title', None))
                d['artist'] = self.trimStr(d.get('artist', None))
                d['duration'] = self.getDuration(d.get('duration', None))
                d['genre'] = self.getGenre(d.get('genre', None))
            return data
        return []

    def get_context_data(self, **kwargs):
        context = super(DashboardList, self).get_context_data(**kwargs)
        context['query_results'] = self.get_tracks()
        return context

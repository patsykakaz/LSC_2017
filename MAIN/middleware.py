#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

from mezzanine.conf import settings
from models import *
from mezzanine.blog.models import BlogPost


class IndexMiddleware(object):
    def process_template_response(self, request, response):
        clients = Client.objects.all().order_by('-level')
        campagnes = Campagne.objects.all().order_by('-level')
        blogposts = FakeBlog.objects.published(for_user=request.user)
        workers = Worker.objects.all().order_by('-level','?')
        response.context_data['clients'] = clients
        response.context_data['campagnes'] = campagnes
        response.context_data['blogposts'] = blogposts
        response.context_data['workers'] = workers
        return response




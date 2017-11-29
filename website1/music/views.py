from django.http import Http404
from django.shortcuts import render 
from . models import Album

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums' : all_albums})
     
    # html = ''
    # for album in all_albums:
    #     url = '/music/' +  str(album.id) + '/'
    #     html += '<a href=" ' + url + ' ">' + album.album_title + '</a><br>'
    


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('Album does not exist')
    return render(request, 'music/detail.html', {'album' : album}) 
    
    # return HttpResponse('<h2>Details for Album id: ' + str(album_id) + '</h2>')


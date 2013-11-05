from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from forms import UploadFileForm
from models import UploadFile


def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            new_file.save()

            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UploadFileForm()

    data = {'form': form}
    return render_to_response('main/index.html', data, context_instance=RequestContext(request))
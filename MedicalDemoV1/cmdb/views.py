import requests
import time
import socket
import time
from lxml import etree
from django.shortcuts import render
from cmdb import utils
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from cmdb import models


global username
global password
global code
global s
# Create your views here.

def test(request):
    filedir = 'D:'
    xmlname = request.POST.get("test_file")
    xmldir = 'http://101.6.66.48/forPresent/xml/'
    if xmlname == None:
        return render(request, 'test.html')
    else:
        with open(filedir + str(xmlname), encoding='utf-8') as f:
            xmlname_new = str(xmlname).split('.')[0] + '.xml'
            xml_list = utils.get_xml_list(xmldir, xmlname_new)
            for a in xml_list:
                print(a['description'])
            return render(request, 'test2.html', {'f':f.read(), 'g':xml_list})

def teeth(request):
    username = request.POST.get("test_txt")
    rootdir = 'http://101.6.66.48/forPresent/picture'
    #host = 'localhost'
    host = '101.6.66.48'
    port = 9955

    socket.setdefaulttimeout(2)
    s = socket.socket()
    s.connect((host, port))

    indata = str(username)
    s.sendall(bytes(indata, encoding='utf-8'))
    time.sleep(5)
    keyword = indata.split('.')[0]
    r = requests.get(rootdir)
    selector = etree.HTML(r.text)
    root = selector.xpath('/html/body/pre/a')
    urls = []
    for e in root:
        sem = e.xpath('text()')
        if keyword in sem[0] and sem[0].split('.')[1] != 'owl':
            urls.append(rootdir + '/' + sem[0])

    if username == None:
        return render(request, 'teeth.html')
    else:
        return render(request, 'teeth2.html', {'f':urls})

def home(request):
    return render(request, 'home.html')

def iframe(request):
    return render(request, 'iframe.html')

def system(request):
    return render(request, 'system.html')

def contact(request):
    return render(request, 'contact.html')


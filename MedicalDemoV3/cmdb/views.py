import os
import requests
import socket
import time
from lxml import etree
from django.shortcuts import render
from cmdb import utils
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from cmdb import models


flag = 0
flie = ''
filedir = 'D:'
xmldir = 'http://101.6.66.48/forPresent/xml/'
rootdir = 'http://101.6.66.48/forPresent/picture'
desdir = 'http://101.6.66.48/forPresent/description/'
# host = 'localhost'
host = '101.6.66.48'
port = 9955
def index(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

@require_http_methods(['GET','POST'])
def get_desc(request):
    global file
    file = request.FILES.get('file')
    print('-----------------------------', file)
    f = open(filedir + str(file), encoding='utf-8')
    desc = f.read()
    f.close()
    desc_dict={}
    desc_dict["desc"] = desc
    global flag
    flag = 1

    socket.setdefaulttimeout(2)
    s = socket.socket()
    s.connect((host, port))

    indata = str(file)
    s.sendall(bytes(indata, encoding='utf-8'))

    return JsonResponse(desc_dict)

@require_http_methods(['GET','POST'])
def get_flag(request):
    flag_dict = {}
    flag_dict["flag"] = flag
    return JsonResponse(flag_dict)

@require_http_methods(['GET','POST'])
def get_desc2(request):
    f = open(filedir + str(file), encoding='utf-8')
    desc = f.read()
    f.close()
    desc_dict = {}
    desc_dict["desc"] = desc
    return JsonResponse(desc_dict)

@require_http_methods(['GET','POST'])
def get_table(request):
    xmlname_new = str(file).split('.')[0] + '.xml'
    table_list = utils.get_xml_list(xmldir, xmlname_new)
    #table_list=[{'tooth_map_str': '87654/1/24/145678', 'text': '缺失', 'property': 'is_missing', 'property_chn': '缺失', 'value': '1', 'description': '缺失'}, {'tooth_map_str': '', 'text': '近远中间隙基本正常', 'property': 'mesio_distal_space_distance', 'property_chn': '近远中间隙的距离', 'value': '0', 'description': '正常'}, {'tooth_map_str': '', 'text': '合龈间距基本正常', 'property': 'occluso_gingival_space', 'property_chn': '合龈间隙的距离', 'value': '0', 'description': '正常'}, {'tooth_map_str': '', 'text': '剩余牙槽嵴轻度吸收', 'property': 'residual_ridge_conditions', 'property_chn': '缺牙部位剩余牙槽嵴情况', 'value': '1', 'description': '轻度'}, {'tooth_map_str': '', 'text': '黏膜未见明显异常', 'property': 'pain_hyperemization_swollen_and_ucler', 'property_chn': '黏膜疼痛,增生,肿胀,溃疡', 'value': '0', 'description': '无'}, {'tooth_map_str': '', 'text': '', 'property': '', 'property_chn': '', 'value': '', 'description': ''}, {'tooth_map_str': '87654/1/24/145678', 'text': '牙龈无红肿', 'property': 'gingival_swollen', 'property_chn': '牙龈红肿', 'value': '0', 'description': '无红肿'}, {'tooth_map_str': '87654/1/24/145678', 'text': '无龈退缩', 'property': 'gingival_recession', 'property_chn': '龈退缩', 'value': '0', 'description': '无'}, {'tooth_map_str': '87654/1/24/145678', 'text': 'x线示牙槽骨吸收至根中1/3至根尖1/3', 'property': 'teeth_related_imaging', 'property_chn': '牙相关影像-牙槽骨吸收情况', 'value': '2', 'description': '根长2/3'}, {'tooth_map_str': '', 'text': '固位稳定尚可', 'property': 'retention_of_existed_restorations', 'property_chn': '固位', 'value': '1', 'description': '一般'}, {'tooth_map_str': '', 'text': '口腔卫生状况一般', 'property': 'oral_hygiene', 'property_chn': '口腔卫生情况', 'value': '1', 'description': '一般'}, {'tooth_map_str': '', 'text': '牙石(+)', 'property': 'dental_calculus', 'property_chn': '牙石情况', 'value': '1', 'description': '+'}]
    table_dict={}
    table_dict["table_list"]=table_list
    # table_dict.update({"table_list",table_list})
    return JsonResponse(table_dict)

def get_plan(request):
    keyword = str(file).split('.')[0]
    desname = keyword + '_Mandibular_description.txt'
    r2 = requests.get(desdir + desname)
    r2.encoding = 'utf-8'
    if '404 -' not in r2.text:
        plan = r2.text
    else:
        desname = keyword + '_Maxillary_description.txt'
        r2 = requests.get(desdir + desname)
        r2.encoding = 'utf-8'
        plan = r2.text
    plan_dict = {}
    plan_dict["plan"] = plan
    return JsonResponse(plan_dict)

def get_picture(request):
    r = requests.get(rootdir)
    selector = etree.HTML(r.text)
    root = selector.xpath('/html/body/pre/a')
    picture_list = []
    keyword = str(file).split('.')[0]
    for e in root:
        sem = e.xpath('text()')
        if keyword in sem[0] and sem[0].split('.')[1] != 'owl':
            picture_list.append(rootdir + '/' + sem[0])
    #picture_list=["templates/images/2.jpg","templates/images/3.jpg","templates/images/3.jpg","templates/images/2.jpg"]
    picture_dict = {}
    picture_dict["picture"] = picture_list
    return JsonResponse(picture_dict)

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
    filedir = 'D:'
    xmlname = request.POST.get("test_file")
    xmldir = 'http://101.6.66.48/forPresent/xml/'
    rootdir = 'http://101.6.66.48/forPresent/picture'
    desdir = 'http://101.6.66.48/forPresent/description/'
    # host = 'localhost'
    host = '101.6.66.48'
    port = 9955

    if xmlname == None:
        return render(request, 'teeth.html')

    else:
        with open(filedir + str(xmlname), encoding='utf-8') as f:
            xmlname_new = str(xmlname).split('.')[0] + '.xml'
            xml_list = utils.get_xml_list(xmldir, xmlname_new)
            socket.setdefaulttimeout(2)
            s = socket.socket()
            s.connect((host, port))

            indata = str(xmlname)
            s.sendall(bytes(indata, encoding='utf-8'))
            time.sleep(5)
            keyword = indata.split('.')[0]
            desname = keyword+'_Mandibular_description.txt'
            r2 = requests.get(desdir+desname)
            r2.encoding = 'utf-8'
            if '404 -' not in r2.text:
                description = r2.text
            else:
                desname = keyword + '_Maxillary_description.txt'
                r2 = requests.get(desdir + desname)
                r2.encoding = 'utf-8'
                description = r2.text
            r = requests.get(rootdir)
            selector = etree.HTML(r.text)
            root = selector.xpath('/html/body/pre/a')
            urls = []
            for e in root:
                sem = e.xpath('text()')
                if keyword in sem[0] and sem[0].split('.')[1] != 'owl':
                    urls.append(rootdir + '/' + sem[0])

            return render(request, 'teeth2.html', {'u':urls, 'f':f.read(), 'g':xml_list, 'd':description})

def home(request):
    return render(request, 'home.html')

def iframe(request):
    return render(request, 'iframe.html')

def system(request):
    return render(request, 'system.html')

def contact(request):
    return render(request, 'contact.html')
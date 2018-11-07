from lxml import etree
import requests
import socket


def get_xml_list(xmldir, xmlname):
    r = requests.get(xmldir + xmlname)
    r.encoding = 'utf-8'
    selector = etree.HTML(r.content)
    root = selector.xpath('//label')
    xml_list = []
    for e in root:
        base_dict = {
            'tooth_map_str':'',
            'text':'',
            'property':'',
            'property_chn':'',
            'value':'',
            'description':'',
        }
        t1 = e.xpath('tooth_map_str/text()')
        if len(t1) > 0:
            base_dict['tooth_map_str'] = t1[0]
        t2 = e.xpath('text/text()')
        if len(t2) > 0:
            base_dict['text'] = t2[0]
        t3 = e.xpath('property/text()')
        if len(t3) > 0:
            base_dict['property'] = t3[0]
        t4 = e.xpath('property_chn/text()')
        if len(t4) > 0:
            base_dict['property_chn'] = t4[0]
        t5 = e.xpath('value/text()')
        if len(t5) > 0:
            base_dict['value'] = t5[0]
        t6 = e.xpath('description/text()')
        if len(t6) > 0:
            base_dict['description'] = t6[0]
        if list(base_dict.values()).count('') < 6:
            xml_list.append(base_dict)

    return xml_list

def socket_client(data):
    socket.setdefaulttimeout(20)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 12131))

    s.send(bytes(str(data), encoding='utf-8'))
    imgname = (s.recv(1024)).decode('utf-8')
    #print(imgname)
    s.close()

    return imgname
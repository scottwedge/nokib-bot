import re
import json
import datetime as dt
import time
import pywikibot as pb
import os
bn = pb.Site("bn","wikipedia")
def en2bn(txt):
    refs = ["০", "১","২","৩","৪","৫","৬","৭","৮","৯"]
    txt = str(txt)
    st=""
    for i in txt:
        if(i.isdigit()):
            st+=refs[int(i)]
        else:
            st+=i
    return st
now = dt.datetime.now()
yesterday = now - dt.timedelta(days=1)
config = json.loads(pb.Page(bn,"user:নকীব বট/config.json").text)
r = pb.data.api.Request
ISO = "%Y-%m-%dT%H:%M:%SZ"
months = "((জান|ফেব্র)ুয়ার[িী]|ম(ে|ার্চ)|এপ্রিল|জু(ন|লা[ইঈ])|[অআ]গা?[সষ]্ট|((সেপ্ট|ন[বভ]|ডিস)েম্|অক্টো)[ভব]র)"
no ="০১২৩৪৫৬৭৮৯"
if(config['archiveTalk']['status']):
    import archive
    archive()
if(config["reduceImage"]['status']):
    import reduceImage
    reduceFUR()
if(config["goodArticle"]["status"]):
    import ga
    manageGATalk()
    manageGAR()
    if(config["goodArticle"]["manageNominee"]["status"]):
        config = config["goodArticle"]["manageNominee"]
        manageNominee()
from requests_html import HTMLSession
import spacy
import xml.etree.ElementTree as ET
global name
from threading import Timer

def ext(url):
    ht=HTMLSession()
    resp=ht.get(url)
    dv = "td" + "value"
    return resp.html.find( first=True).text
def process_text(text):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text.lower())
    result = []
    for token in doc:
       if token.text in nlp.Defaults.stop_words:
            continue
       if token.is_punct:
            continue
       if token.lemma_ == '-PRON-':
            continue
       result.append(token.lemma_)
    return " ".join(result)

def secondary_check(inp,f_name):
    #for platform_installation_guide
    url = "http://localhost:8983/solr/"+f_name+"/select?&wt=xslt&fq=content%3A"+ inp +"&fq=topic%3A"+ inp +"&q=*%3A*~&fl=topic&tr=example.xsl"
    #for solution manager installation guide
    #url ="http://localhost:8983/solr/solution_manager/select?&wt=xslt&fq=content%3A"+ inp +"&fq=topic%3A"+ inp +"&q=*%3A*~&fl=topic&tr=example.xsl"
    #for all links
    #url="http://localhost:8983/solr/all_try_1/select?&wt=xslt&fq=content%3A"+ inp +"&fq=topic%3A"+ inp +"&q=*%3A*~&fl=topic&tr=example.xsl"
    out = ext(url)
    out = str(out)
    out = out.replace("\n", "").replace("\"", "")
    out = out.split("topic")
    out.pop(0)
    print("hi "+det)
    print("hope these below resources may help you with your further proceeding")
    for i in out:
        print(i)

def pre_pre_process(a):
    nlp = spacy.load("en_core_web_sm")
    c = " "
    l1, l2, l3 = [], [], []
    doc = nlp(a)
    for np in doc:
        if (np.tag_ == "NNP" or np.tag_ == "NNPS" or np.tag_ == "NNS" or np.tag_ == "NN" or np.tag_=="JJ"):
            l1.append(np.text)
        elif (np.tag_ == "VBZ" or np.tag_ == "VBG" or np.tag_ == "VB"):
            l2.append(np.text)
        else:
            l3.append(np.text)
    l1.extend(l2)
    l1.extend(l3)
    c = c.join(l1)
    return c
def create_link(inp):
    lis = ["fq=cont", "fq=link_cont"]
    inp=inp.split(" ")
    out=[]
    for i in range(2):
        for j in range(len(inp)):
            out.append(lis[i] + "%3A" + inp[j])
    out = "&".join(out)
    return out
def feed(inp):
    mytree = ET.parse('triple_format_xml/all_try_1.xml')
    myroot = mytree.getroot()
    key = inp.replace(inp[0]," "+inp[0])
    inp = str(input("enter the link"))
    flag = False
    for sets in myroot.iter('doc'):
        for j, i in enumerate(sets):
            a = str(i.text)
            a = a[1:]
            if j == 0 and str(a) == inp:
                flag = True
            if j == 1 and flag == True:
                i.text = a + key
            if j == 2 and flag == True:
                i.text = a + key
                flag = False
    mytree.write('triple_format_xml/all_try_1.xml')

def whole_check(inp):
    inp=inp.replace("vdp","virtual dataport")
    print(inp)
    inp=create_link(inp)
    url = "http://localhost:8983/solr/all_try_1/select?&wt=xslt&"+inp+"&q=*%3A*~&fl=link&tr=example.xsl"
    print(url)

    out = ext(url)
    out = str(out)
    out = out.replace("\n", "").replace("\"", "")
    out = out.split("link")
    out.pop(0)
    print("Many thanks for holding on.Hope these resources might suits your requirement.")
    for i in out:
        print(i)

def addnum(num):
    file1 = open("contact_num.txt", "a")
    file1.write("+91"+num+ ",")
    file1.close()

global det
det=input("Enter your name :")
coutry=input("Enter your Country :")
mail=input("Enter your mail id :")
num=input("Enter your contact number (Optional) :")
if len(num)>0:
    addnum(num)
cust=input("Customer/Partner/Others :")
name=["data_catalog_guide","denodo_platform_installation_guide","denodo_platform_new_features_guide","denodo_platform_upgrade_guide","denodo4eclipse_plugin_guide","denodoconnect_components","diagnostic_and_monitoring_tool_guide","itpilot","scheduler_administration_guide","solution_manager_administration_guide","solution_manager_installation_guide","virtual_dataport_administration_guide","virtual_dataport_developer_guide","virtual_dataport_vql_guide"]
#print(len(name))
inp=1
while(inp!="00"):
    timeout = 60
    print("<----- User Side----->")
    print("Welcome to Denodo live chat service. Please provide us the following details")
    t = Timer(timeout, print, ['Are you still here????'])
    t.start()
    inp=input("Hello "+det+", How can I assist you today?\n")
    t.cancel()
    inp=inp.split(" on ")
    if len(inp)==2:
        inp,f_name=inp
        inp=process_text(inp)
        inp=inp.replace("datum", "data")
        secondary_check(inp,f_name)
    else:
        #inp=pre_pre_process(inp[0])
        inp=process_text(inp[0])
        inp=inp.replace("find","")
        inp=inp.replace("  "," ")
        if inp[0]==" ":
            inp=inp[1:]
        whole_check(inp)
    dec=(input("Are you satisfied with the results?...yes or no\n"))
    if dec.lower()=="no":
        feed(inp)
from requests_html import HTMLSession
from rake_nltk import Rake
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import spacy
import xml.etree.cElementTree as ET
def process_text(text):
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
def process_link(text):
    text = text.split("/en/")
    text = text[1]
    text = text.split("/")
    text = " ".join(text)
    text = text.split("_")
    text = " ".join(text)
    text = text.split("#")
    text = " ".join(text)
    text = text.split("-")
    text = " ".join(text)
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
def ext(lnk,link):
    ht=HTMLSession()
    #print(lnk)
    url=urljoin(link,lnk)
    #print(link)
    #print(lnk)
    resp=ht.get(url)
    dv="div"+lnk
    print(dv)
    try:
        return resp.html.find(dv,first=True).text,url
    except:
        return ' ',url
txt=open('C:\\Users\\DineshrajaAnnadurai\\Desktop\\Denodo_8.0_links\\denodo_platform_installation_guide.txt','r')
a=(txt.read())
link=(a.split(","))
rak=Rake()
root = ET.Element("add")
for pg in range(len(link)):
    #print(link[pg])

    r = requests.get(link[pg])
    soup = BeautifulSoup(r.content, 'lxml')
    for link1 in soup.find_all('a',class_="headerlink"):
        lis=[]
        #print(link1.get("href"))
        #print(link[pg])
        text,url=ext(link1.get('href'),link[pg])
        #print(text)
        #print()
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        cont = (doc.sents)

        for sent in doc.sents:
            a = str(sent)
            b=(a.replace("\n", ""))
            b=process_text(b)
            lis.append(b)

        lnk=process_link(url)
        doc = ET.SubElement(root, "doc")
        lis=" ".join(lis)
        ET.SubElement(doc, "field", name="link").text = url
        ET.SubElement(doc, "field", name="link_cont").text = lnk
        ET.SubElement(doc, "field", name="cont").text = lis
tree = ET.ElementTree(root)
tree.write("C:\\Users\\DineshrajaAnnadurai\\Desktop\\SOLR_round\\triple_format_xml\\denodo_platform_installation_guide.xml")
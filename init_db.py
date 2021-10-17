
import requests
import xml.etree.ElementTree as ET

r = requests.get("https://www.cbr.ru/scripts/XML_daily_eng.asp?date_req=02/10/2021")
root = ET.fromstring(r.text)

tree = ET.ElementTree(root)
tree.write("file.xml")


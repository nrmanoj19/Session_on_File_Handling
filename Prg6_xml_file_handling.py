import xml.etree.ElementTree as ET


tree = ET.parse('sample_xml.xml')
root = tree.getroot()
print(root.tag)


for child_tag in root:
    print(child_tag.tag)

for each_tag in root.iter():
    print(each_tag.tag)

for each_movie_tag in root.iter('movie'):
    print(each_movie_tag.attrib)

for each_description_tag in root.iter('description'):
    print(each_description_tag.text)

topic_text = root.find('./topic').text
topic_attribute = root.find('./topic').attrib
print(topic_text)
print(topic_attribute)


for each_movie in root.findall('./genre/decade/movie'):
    print(each_movie.attrib)

for each_action_movie in root.findall("./genre[@category='Action']/decade/movie"):
    print(each_action_movie.attrib)

for fav_action_movie in root.findall("./genre[@category='Action']/decade/movie[@favorite='True']"):
    print(fav_action_movie.attrib)

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

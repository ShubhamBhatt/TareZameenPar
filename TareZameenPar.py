import urllib2
import serial
import time
from xml.dom.minidom import parseString
i = 1
time.sleep(5)
while i == 1:
     file = urllib2.urlopen('http://spotthestation.nasa.gov/sightings/xml_files/India_None_Lucknow.xml')
     
     data = file.read()
     
     file.close()
     dom = parseString(data)
     xmlTag = dom.getElementsByTagName('title')[1].toxml()
  
     xmlData=xmlTag.replace('<title>','').replace('</title>','')
     
     time.sleep(5)
     
     nums = xmlData.split(' ')
     
     print("International space station sighting lucknow")
     for num in nums:
          #write 1 word
          print(nums[0])
     time.sleep(300)

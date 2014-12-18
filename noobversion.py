import feedparser
#replace the url for whichever location you want go to nasa's website to retrieve the rss feed url might give error due missing library plz install manually  
d = feedparser.parse('http://spotthestation.nasa.gov/sightings/xml_files/India_None_Lucknow.xml')
print d['feed']['date']
print d['channel']['title']
print d.entries[0].title
print d['channel']['description']
print d.entries[1].summary

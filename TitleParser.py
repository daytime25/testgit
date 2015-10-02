#test of the parsing the HTML and XML 
 
import sys , urllib2 
from HTML.Parser import HTMLParser 
 
class TitleParser(HTMLParser): 
  def __init__(self): 
    self.title = '' 
    self.readingtitle = 0 
    HTMLParser.__init__(self) 
 
  def handle_starttag(self , tag , attrs): 
    if tag == 'title': 
      self.readingtitle = 1 
  def handle_data(self , data): 
    if self.readingtitle: 
      self.title += data 
  def handle_endtag(self , tag): 
    if tag == 'title': 
      self.readingtitle = 0 
  def gettitle(self): 
    return self.title 
 
def parseHTMLTitle(): 
  
  print('choose the file address: ') 
  addr = sys.stdin.readline().rstrip() 
   
  if(addr == 'url'): 
    print('input the url address:') 
  elif(addr == 'local'): 
    print('input the local filename: ') 
  else: 
    print('input the right method') 
   
  filename = sys.stdin.readline().rstrip() 
 
  if(addr == 'url'): 
    fd = urllib2.urlopen(filename) 
  elif(addr == 'local'): 
    fd = open(filename) 
  else: 
    print('filename wrong') 
 
  tp = TitleParser() 
  tp.feed(fd.read()) 
  print('the title is: ' , tp.gettitle().strip()) 
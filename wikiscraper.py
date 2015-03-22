from nltk import ngrams
from collections import Counter
from bs4 import BeautifulSoup
import urllib2

class Wikiscraper():
    '''
    Scrapes 1 page of wikipedia for all text of that wikipedia article
    '''
    
    def __init__(self, url, body_id='mw-content-text'):
        '''
        INPUT: String, String
        OUTPUT: None
        '''
        self.url = url
        self.article_body_id = body_id
        self.text = self.get_text()
        
    def get_text(self):
        '''
        INPUT: None
        OUTPUT: None
        Grabs the text from the article body
        '''
        response = urllib2.urlopen(self.url)
        html = response.read()
        bs = BeautifulSoup(html)
        self.bs = bs
        content = bs.find(attrs={'id':self.article_body_id})
        return content.get_text()
    
    def get_top_x_ngrams(self, x, n):
        '''
        INPUT: int, int
        OUTPUT: List of Tuples, Tuple of a, b a is the item being counted, and b is the count
        Gets the ngrams from the text and counts the ngrams
        '''
        word_list = self.text.split()
        lst_gram = ngrams(word_list, n)
        counter = Counter(iterable=lst_gram)
        return counter.most_common(x)

if __name__ == '__main__': 
    wiki = Wikiscraper('http://en.wikipedia.org/wiki/N-gram')
    print wiki.get_top_x_ngrams(10, 3)
""" This Class is for storing or creating article objects """
import warnings

class Article():
    """ The Article object is used to store and parse article infomation from new york times. 
        It contains attributes:
            {
             'keywords': the keywords of the article,
             'headline': the headline of the article,
             'snippet': the snippet of the article,
             'url': the web url of the article
             }
        It contains methods:
            {
             'longest_word_in_abstract': Get the longest word in the abstract,
             'get_full_text': Get the full text of the article,
             'get_title': Return the title of the current article,
             'get_keywords': Return the keywords of the current article,
            }
"""

    def __init__(self, article_info):
        self.keywords = [item["value"] for item in article_info['keywords']]
        self.headline = article_info['headline']['main']
        self.snippet = article_info['snippet']
        self.url = article_info["web_url"]

    def longest_word_in_abstract(self):
        """ Return the longest word in the article's abstract """
        word_list = self.snippet.split()
        try:
            longest_word = max(word_list, key=len)
            print("The longest word in the abstract is %s" % longest_word)
            return longest_word
        except ValueError:
            warnings.formatwarning = lambda message, category, \
                                            filename, lineno: "WARNINGS! {}:{}: {}:{}".format(filename,
                                                                                              lineno,
                                                                                              category.__name__,
                                                                                              message)
            warnings.warn("No snippet has been fonud!", stacklevel=2)


    def get_full_text(self):
        """ Get full text of article if interested """

    def get_title(self):
        """ Return the headline of the current article """
        return self.headline

    def get_keywords(self):
        """ Return the keywords of the current article """
        return self.keywords

    # default method: __str__
    def __str__(self):
        return "This article has a headline {}\n It's keywords are \
                 {}\n Here's a snippet {}\n".format(self.headline, self.keywords, self.snippet)

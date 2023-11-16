'''
Text To Speech
-------------------------------------------------------------
pip install nltk newspaper3k gtts
'''


import nltk
from newspaper import Article
from gtts import gTTS  # https://gtts.readthedocs.io/en/latest/

import pyttsx3 # https://pypi.org/project/pyttsx3/


def text_to_speech_google(url):
#    article = Article(url)
#    article.download()
#    article.parse()
#    nltk.download('punkt')
#    article.nlp()
#    article_text = article.text
   language = 'en'
   article_text = "Officer Rodriguez, this is Dispatch. Backup is en route. We're coordinating with other agencies. Ensure the safety of civilians and protect critical infrastructure. Stay vigilant."
   my_obj = gTTS(text=article_text, tld="us", lang=language, slow=False)
   my_obj.save("read_article.mp3")

def text_to_speech_offline():
    engine = pyttsx3.init()
    
    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        #printing current voice rate
    engine.setProperty('rate', 180)     # setting up new voice rate
    
    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. o for male
    # engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    
    article_text = "Officer Rodriguez, this is Dispatch. Backup is en route. We're coordinating with other agencies. Ensure the safety of civilians and protect critical infrastructure. Stay vigilant."
    
    engine.save_to_file(article_text, "test.mp3")
    engine.runAndWait()

if __name__ == '__main__':
   text_to_speech_google(url='https://hackr.io/blog/top-tech-companies-hiring-python-developers')
   
   text_to_speech_offline()
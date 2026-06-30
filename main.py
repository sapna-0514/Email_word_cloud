from PIL import Image
import numpy as np
import mailbox
from collections import Counter
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

mbox = mailbox.mbox('sample.mbox')

all_words = []

for message in mbox:
    body = message.get_payload()
    if body:  
        body = body.lower()  
        body = body.translate(str.maketrans('', '', string.punctuation))  
        words = body.split()  
        all_words.extend(words)


count = Counter(all_words)
print("Top 10 words:", count.most_common(10))


wc = WordCloud(width=800, height=400, background_color='white', colormap='rainbow')
wc=WordCloud(stopwords=STOPWORDS,background_color='white')

wc.generate_from_frequencies(count)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
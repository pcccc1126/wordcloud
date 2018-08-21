# -*- coding: UTF-8 -*-
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator

fp = path.dirname(__file__)

stopwords = {}
isCN = 1
back_coloring_path = "haha.jpg"
text_path = 'haha.txt'
font_path = '/System/Library/Fonts/PingFang.ttc'
stopwords_path = 'stopwords1893.txt'
imgname1 = "WordCloudDefautColors.png"
imgname2 = "WordCloudColorsByImg.png"

my_words_list = ['长者', '大发财', '二院', 'engineering drawing']

back_coloring = imread(path.join(fp, back_coloring_path))

wordc = WordCloud(font_path = font_path,
               background_color = "white",
               max_words = 2000,
               mask = back_coloring,
               max_font_size = 80,
               random_state = 42,
               width = 1000,
               height = 860,
               margin = 2,
               )

def add_word(list):
    for items in list:
        jieba.add_word(items)

add_word(my_words_list)

text = open(path.join(fp, text_path)).read()

def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path)
    try:
        f_stop_text = f_stop.read()
        f_stop_text = str(f_stop_text)
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

if isCN:
    text = jiebaclearText(text)

wordc.generate(text)
image_colors = ImageColorGenerator(back_coloring)

plt.figure()
plt.imshow(wordc)
plt.axis("off")
plt.show()

wordc.to_file(path.join(fp, imgname1))

image_colors = ImageColorGenerator(back_coloring)

plt.imshow(wordc.recolor(color_func = image_colors))
plt.axis("off")

plt.figure()
plt.imshow(back_coloring, cmap = plt.cm.gray)
plt.axis("off")
plt.show()

wordc.to_file(path.join(fp, imgname2))
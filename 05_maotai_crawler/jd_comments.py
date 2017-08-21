#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-8-21
# @Author  : foodish
# @File    : jd_comments.py
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

word_str = open('comments_jd_origin.txt', encoding='utf-8').read()
wordlist_after_jieba = jieba.cut(word_str, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
my_wordcloud = WordCloud().generate(wl_space_split)
plt.figure(num=None, figsize=(800, 600), facecolor='w', dpi=600, edgecolor='k')
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()


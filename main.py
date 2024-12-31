import matplotlib.pyplot as plt
import numpy as np
import re

# Count occurences of each word in the text
filename = input("Enter file name: ")
file = open(filename, encoding='utf-8-sig')
word_list = {}
for line in file:
    line = line.strip("\n").split(" ")
    for word in line:
        if ('’' in word):
            word =  word.replace('’', "'")
        word = re.findall(r"\w+'?\w?", word)
        for indv in word:
            indv = indv.lower()
            if indv not in word_list.keys():
                word_list[indv] = 1
            else:
                word_list[indv] += 1

# Scale the list by frequency
total_words = sum(list(word_list.values()))
scaled_list = {k: (v / total_words if total_words > 0 else 0) for k, v in word_list.items()}

# Graphing
x = np.linspace(1, len(list(scaled_list.values())), num=len(list(scaled_list.values())))
y_text = list(scaled_list.values())
y_ideal = 1/x

plt.plot(x, y_text)
plt.plot(x, y_ideal)
plt.legend([filename, "Zipf's Law"], loc="upper right")
plt.show()
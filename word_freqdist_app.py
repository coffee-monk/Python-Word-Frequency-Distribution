### Import Libraries -------------------------------------------------------

import textract  # convert utf-8 to string

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

import matplotlib.pyplot as plt

import csv
import pandas as pd
import numpy as np

import os
from os import listdir

import time

# import local custom stop_words & figure parameters
from custom_stopwords import new_stopwords, ignore_stopwords
from figure_parameters import fig_params

### Get User Input for Directory of Text Documents ------------------------------

print(
    "Input full directory path to analyze all text documents within.\n\n"
    "EXAMPLE(windows): C:\\Users\\Username\\Desktop\\text_directory\\ \n"
    "EXAMPLE(linux): /home/user/Desktop/text_directory/ \n"
)
directory_path = input()
text_files = os.listdir(directory_path)

### Import and combine text_files in user-given directory -----------------------

text_import = []  # Create list of text_files
for text_file in text_files:
    text_file = directory_path + text_file
    text_import.append((textract.process(text_file).decode("utf-8")))
text_data = " ".join(text_import)  # Join text_files into one file

### Check for "stopwords.txt" & Integrate stop_words ---------------------------

stop_words = set(
    stopwords.words("english")
)  # default stop_words filtered out of analysis

# Check OS & if "stopwords.txt" in cd
# Add custom stopwords to stop_words
if (os.name == "posix" and os.path.isfile(os.getcwd() + "/custom_stopwords.py")) or (
    os.name == "nt" and os.path.isfile(os.getcwd() + "\\custom_stopwords.py")
):
    stop_words = stop_words.union(new_stopwords)
    stop_words = set([word for word in stop_words if word not in ignore_stopwords])
else:
    print("WARNING: File 'custom_stopwords.py' is not detected in working directory")

### Process text_files & Complete Word Counts ----------------------------------

tokenized_words = word_tokenize(text_data)

# Filter stop_words
tokenized_words_filtered = []
for w in tokenized_words:
    if w not in stop_words:
        tokenized_words_filtered.append(w)

# Create Frequency-Distribution-List
fdist = FreqDist(tokenized_words_filtered)

flist = [['Word', 'Frequency']]
for key in fdist.keys():
    flist.append([key, str(fdist[key])])

# Write to dated file
myFile_name = "Freq_Dist_" + time.strftime("%Y-%m-%d-%S") + ".csv"
myFile = open(myFile_name, 'x')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(flist)

# Remove blank lines from CSV if they exist
df = pd.read_csv(myFile_name)
df.dropna(axis=0, how='all', inplace=True)
df.to_csv(myFile_name, index=False)

# Plot
df = pd.read_csv(myFile_name)
print(df)
fig = plt.figure(figsize=(fig_params["width"], fig_params["height"]))
x = np.arange(0, df.shape[0])
y = df['Frequency'].to_list()
print(len(x), " ", len(y))
plt.plot(x, y)
plt.show()

# # Frequency Distribution Plot
# plt.ion()
# fig = plt.figure(figsize=(fig_params["width"], fig_params["height"]))
# fdist.plot(fig_params["num_words"], cumulative=False)
# fig_title = "Fdist_Plot_" + time.strftime("%Y-%m-%d-%S")
# fig.savefig(os.getcwd() + "\\" + fig_title)
# # fig.savefig(fig_title)
# plt.ioff()
# plt.show()

print("Success!")

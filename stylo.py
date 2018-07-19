#/usr/bin/python3

#
# This script should do all three of the major steps
# for stylometry with PCA
# input is a file list formatted like
#
#  id	path-to-txt-file
#
# Script accepts an argument to name this particular run
# and use that name in the generated files.
#
# Step 1: Read the files and compile wordlist
# - save as kw-wordlist.txt
# Step 2: For top 1000 words, score each novel for frequency
# - save frequency outputs for top 1000, 500, 100 
# - save as e.g. kw-frequencies-1000.txt
# Step 3: Run the PCA
# - save the output as Highcharts HTML with labeled data
# - save as e.g. kw-chart.html
#

# imports
import sys,os
from textblob import TextBlob
import pandas as pd
from numpy import array
import numpy as np
from sklearn.decomposition import PCA

kw = str(sys.argv[1])

# Step 1: Read the files and compile wordlist

with open('./filelist.txt') as f: 
    files = f.read().splitlines()

words = {}

os.system("rm " + kw + "-wordcount.txt")
os.system("rm " + kw + "-frequencies-1000.txt")
os.system("rm " + kw + "-frequencies-500.txt")
os.system("rm " + kw + "-frequencies-100.txt")

for line in files:
	id,file = line.split("\t")
	print("Working on " + file + " ...")
        
	read = open(file,"r",errors="surrogateescape")
	novel = TextBlob(read.read())

	print("\tread")
        
	wordlist = novel.words
        
	print("\ttokenized")

	for word in wordlist:    
		# https://stackoverflow.com/a/473344
		words[word] = words.get(word, 0) + 1

	print("\tcounted")
        
	#os.unlink(kw + "-wordcount.txt")
	#.system("touch " + kw + "-wordcount.txt")

	write = open(kw + "-wordcount.txt","w",errors="surrogateescape")
    
	for w in sorted(words, key=words.get, reverse=True):
		write.write(w + ": " + str(words[w]) + "\n")

print("Done counting words.")
print("Check " + kw + "-wordcount.txt")

# Step 2: For top 1000 words of wordlist, score each novel for frequency

print("Gathering vocabulary")
with open('./final_word_count.txt','r',errors="surrogateescape") as w: 
	w = w.read().splitlines()

# this is the list of the most popular n words
vocab = []
for v in w[0:1000]:
	vocab.append(v.split(": ")[0])

# get the files again.
with open('./filelist.txt') as f: 
	files = f.read().splitlines()

# This will be a dictionary where the key is the novel id
# and then the value is the list of n scores. 
# One for each vocabulary word.

data = {}

for file in files:
	(key,path) = file.split("\t")
	print("Scoring " + key + " ...")

	read = open(path,"r",errors="surrogateescape")
	novel = TextBlob(read.read())
        
	wordlist = novel.words

	print("\ttokenized")

	for v in vocab:
		data[v] = 0
	    
	for word in wordlist:    
		if word in vocab:
	 		data[word] += 1
	    
	print("\tcounted")

	# iterate through vocab to preserve order
	# and calculate frequency

	frequencies = []

	for v in vocab:
		if data[v] > 0:
			frequency = (data[v] / float(len(wordlist))) * 100
		else:
			frequency = 0.0
	        
		frequencies.append(str(frequency))
	 

	print("\tdone counting frequencies")

	out = open(kw + "-frequencies-1000.txt","a")
	out.write(key + "\t" + "\t".join(frequencies) + "\n")
	out.close()

	out = open(kw + "-frequencies-500.txt","a")
	out.write(key + "\t" + "\t".join(frequencies[:500]) + "\n")
	out.close()

	out = open(kw + "-frequencies-100.txt","a")
	out.write(key + "\t" + "\t".join(frequencies[:100]) + "\n")
	out.close()

	print("\twrote it out")

print("Done scoring")
print("Check " + kw + "-frequencies-1000.txt")

print("Step 3: PCA")

np.set_printoptions(suppress=True)

for size in ['1000','500','100']:

	# define a matrix
	df = pd.read_csv(kw + '-frequencies-' + size + '.txt', sep='\t',header=None,index_col=0)
	A = array(df) 

	rf = pd.read_csv(kw + '-frequencies-' + size + '.txt', sep='\t',header=None)
	oa = array(rf)

	# create the PCA instance
	pca = PCA(2)

	# fit on data
	pca.fit(A)

	# transform data
	B = pca.transform(A)

	final = np.round(B,decimals=6)

	# turn the first column into an array. This is for the ids.
	ids = oa[:,0]

	
	with open('./chart.html') as template: 
		tl = template.read().splitlines()

	output_data = ''
	for row in range(len(ids)):
		output_data += '{"name": "' + ids[row] + '", "x":' + str(final[row][0]) + ', "y":' + str(final[row][1]) + '},\n'

	h = open(kw + "-" + size + ".html","w")
	for line in tl:
		line = line.replace('{{{kw}}}',kw)
		line = line.replace('{{{size}}}',size)
		line = line.replace('{{{data}}}',output_data)

		h.write(line + "\n")
	

	
	h.close()

	print("Wrote " + kw + "-" + size + ".html")

print("ALL DONE")

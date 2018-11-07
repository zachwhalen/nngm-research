## I. Introduction

National Novel Generation Month or NaNoGenMo is an annual event that internet artist and twitter bot godfather Darius Kazemi created on a whim with a tweet in November 2013. 

https://twitter.com/tinysubversions/status/396305662000775168
"spend the month writing code that generates a 50k word novel, share the novel & the code at the end?"

Every November since, participants have shared their computationally creative work in dedicated Github repositories, filing "issues" to signify their partipation and share their final products. The text-generation methods vary widely, but the finished products generally follow the same textual shape of a modern literary novel, thanks to the 50,000-word constraint borrowed from NaNoWriMo, the more well-known annual writing challenge that takes place every November.

This paper is the beginning of a larger study of NaNoGenMo where I'm interested in placing these projects within a broader historical context of computer generated fiction. For now, the question I'm interested in is reading: how does one read a computer-generated text? The answer, of course, is with computers.

Eventually, I am interested in surveying the techniques, languages, and source texts that creators have used, but today I'm interested in what we can learn by looking at the novels alone. The central conceit of the work I'm presenting today is an investigation of what one can learn about computer-generated works by applying computer-aided text analysis or so-called "distant reading" techniques, the methodologies that generally fall under the banner of "digital humanities."

[some examples]

There are several reasons why closing this particular gap between electronic literature and digital humanities is appropriate for this particular set of texts:

First, just as the premise of NaNoGenMo calls into question the idea of what it means to write, the works created require their audience to reconsider what it means to read. This shift in reading, I argue, is a hermeneutic reorientation similar to the perspective of distant reading which Lisa Marie Rhody and others critique for an implication that looking should take the place of reading.

Second, the scope and scale of the several hundred works so far created for NaNoGenMo is such that reading them -- if one considers a prosaic definition of "reading" as passing one's eyes across every word in a corpus -- would simply take an unreasonably long time. Just as Franco Moretti presents distant reading as one solution to the challenge of scale in what Margaret Cohen called "the great unread" of literature, distant reading techniques may help illuminate this great new world of unread literary artifacts, many of which are technically unreadable, and most of which I'm guessing have not been read by anyone, including the person who created them.

Finally, it turns out that the set of things that can be learned about a text through statistical analysis are similar to the kinds of things that can be known about those texts by the account of their creators or a review of the source code, so applying statistically-driven techniques to the study of these texts also becomes a way of testing the reliability and limitations of those techniques. For example, a stylemetric analysis that finds similarities between works should, hypothetically, report a strong similarity between based on works purportedly based on, say, _Moby Dick_.


## II. NaNoGenMo by the Numbers
To prepare for this research, I have examined each year's Github repository and prepared a cursory catalog and archive of every completed NaNoGenMo work. All told, the corpus includes a total of 399 works, of which I was able to archive and analyze the full text of 382. 207 authors have participated over the five years to generate around 44 million words of literary text. Many novels exceed the 50,000-word minimum, so the net average wordcount is 107,541.

[graph]

As this graph shows, participation peaked in 2014, but has remained steady. 

Additionally, around one fourth of participants have completed novels in multiple years, and the two most prolific authors, hugovk and enkiv2 together account for 13.2% of the completed novels.

By the way, throughout this presentation, I will generally refer to authors by their Github usernames, except in cases where their given name is well-known outside of Github. For example, I will refer to "aparrish" as "Allison Parrish", but "enkiv2" as "enkiv2".

## III. Approaches to Distant Reading
[maybe write this section later/as conclusion]
As I just mentioned, the idea of so-called Distant Reading and its role in literary criticism remains controversial, and one of the main critiques is that the distant reader's emphasis on mathematical specificity conflates the formal consistency of a model with a certainty of analysis. 

As Lisa Marie Rhody clarifies, the trouble with distant reading isn't the way it undermines close reading, but rather the fact that 

> 'the "condition of knowledge" required by distance reorients representational models from verbal to spatial. [and later] Looking is never a neutral activity, but much of <em>Distant Reading</em> addresses literary history from the authoritative position of an omniscient scientific gaze'.

Further critiquing what she calls the "objective fallacy" in process-driven text-analysis, Johanna Drucker emphasizes the role of human fallibility in reading. 

> "Processing is not reading. It is literal, automatic, and repetitive. Reading is ideational, hermeneutic, generative, and productive. Processing strives for accuracy, reading fo leniency or transformation."

But as an approach to a hermeneutic, text-analysis and other distant reading methods can helpfully suggest which questions an interpretation should try and answer.

In arguing for a place for computational text-analysis, Stephen Ramsay acknowledges that 

> "If something is known from a word frequency list or a data visualization, it is undoubtedly a function of our desire to make sense of what has been presented."  

Especially with a corpus as large and as unknowable as NaNoGenMo, visualizing some word frequencies can help make sense of what these books are made of.

## IV. Initial Findings and Visualizations
Some high-level visualizations and analyses of the NaNoGenMo corpus reveal some of that shape, but also show why it is difficult to found a nuanced textual critique with just these tools. If nothing else, visualizations begin to demonstrate the types of texts present in the corpus by highlighting some extreme outliers.

### A. Word Cloud
A word cloud is a common entry point to computational text analysis. At least, it helps my students understand the kinds of things that text analysis is trying to accomplish. 

But adjusting some parameters in a cloud visualization and understanding how those differences manifest is crucial for using a cloud to understand a corpus.

The cloud on the left [wctest-tweaked-no-stopwords-no-collocate-2000.png] uses a Python word cloud library to generate a visualization of the top 2000 words, excluding common stop words in English -- words like "to, and, the,but,or" and so on.

The cloud on the right [wctest-tweaked-incl-stopwords-no-collocate-2000.png] adds those common stop words back in, revealing that the distribution of these stop words is pretty typical for texts that are mostly in English. (To be precise, all but about 25 of the novels in my NaNoGenMo corpus are in English.)

The first cloud reveals more about the unusual characteristics of this corpus by focusing on the word "buffalo" as one of the most prevalant uncommon words in the corpus, and this is the case because three of the novels are varations on the well-known linguistic curiosity where a sentence consisting of the word "Buffalo" eight times can be parsed as a grammatically correct sentence in English.

Simply repeat that sentence 6,250 times and you've got a novel very similar to those contributed by 'strand' in 2013 and 'bcj' in 2016.

Of course, having cataloged the corpus gives me a sense of what contexts result in the prominence of certain other words in these visualizations. "caw" is from 'morbidflight's' _Crows torm_, which is a novel for crows consisting of the word "caw" 50,000 times; "mew" and "meow" are artifacts of 'hugovk's' originally english-language novels translated into cat language; and words ending in "-ay" like "andway" and "ethay" are erstwhile stopwords translated into "pig latin" for 'za3k's _The Bible, Translated to the New Latin_. 

### B. Reading-Level Analysis
Another relatively blunt tool for gaining insight into the literary content of texts within a corpus is to calculate a general reading level for that text. Different formulas like Gunning-Fog, Flesch-Kincaid, Dale Chall and Coleman-Liau will give a specific weight to measurable factors of a text like its average word and sentence lengths, the diversity of its vocabulary, and the total word count. 

Like the word cloud, running each NaNoGenMo book through these reading level metrics reveals the roughness of these techniques, as well as highlighting some unusual outlier texts.

I used a Python library called 'textstat' which generates a summary grade-level from the average of nine different reading-level formulas -- and note these grade levels use American-standard grades where 12th grade is the last year of High School or Secondary school before going into college or University.

A graph of reading levels distribution [show anyway] isn't particularly illuminating because some of the novels are allegedly quite difficult to read. 32 books scored a reading level of 50th grade or higher, including Matt Schneider's "we verb" at 1,546th grade, 'booyaa's fully-redacted novel with the unpronouncabe title ██ █████ at 8,550th grade, and Allison Parrish's "Average Novel" with the highest english-language reading level at 20,314th grade.

Looking at what these outliers have in common helps explain the metrics that the reading level analyses give value to. In general, extremely-high scoring novels employ an unusual grammatical structure. Parrish's _Average Novel_ lacks punctuation, so the algorithm views it as one very long sentence. Conversely, _Pondering life in the infinite desert_ by Ben Kybartas employs frequent punctuation in 33,795 very, very short sentences. 

[show quote]

Putting everything in 18th grade or higher in one pile yields something resembling a bell curve. [show graph] Further analysis could explain the dip at 7th grade, and it would also be interesting to compare the shape of this curve to other corpora from, say, project Gutenberg. 

### C. Other Techniques
Other high-level techniques like sentiment analysis and topic modeling similarly suggest broad patterns and highlight unusual outliers in the NaNoGenMo corpus, but the fundamental insights are pretty much the same in that they confirm that most NaNoGenMo works are statistically similar to standard English-language text. 

So in the interest of time and scope, I want to move now to some experiments with stylometrics for hopefully some more nuanced insights. 

## V. Experiments in Stylometrics
Stylometrics refers to a set of techniques where a researcher can extract and model representative stylistic characteristics of a text. Often, these techniques are used to support or debunk claims of authorship attribution when a text of a known authors is stylometrically compared with a text of unknown origin. This has been used, for example, to investigate the authorship of pseudonymous essays in The Federalist Papers or for supporting a claim about true author of Shakespeare's work. Stylometrics could also provide insight into how an author's writing changes over time.

In the case of the NaNoGenMo corpus, stylometrics should help identify affinities between different texts that have similar origins. More specifically, because _Moby Dick_ and _Pride and Prejudice_ are popular source material for NaNoGenMo authors, and because Herman Melville and Jane Austen write differently, stylometrics should help identify and seperate those NaNoGenMo works based on each of these authors' works.

A Characteristic Curve of Composition uses word frequency rates to map the distribution of the most common words used in a corpus. 

As you can see in this graph, we don't need to know which words each author uses to see a difference in style. We simply need to know that Melville's favorite word comprises 6.18% of _Moby Dick_, his second-most favorite comprises 2.96% and so on, to see a difference between Melville and Austen, whose top two words comprise 3.24% and 3.22% respectively of _Pride and Prejudice_.  

Adding Shakespeare's complete works to the graph illustrates further difference.

Here's the same graph with a random sample of NaNoGenMo novels. Like the word clouds and reading-level analyses, most of the generated books have curves within range of each other, indicating that they pretty similar to English-language literary prose, but a few extreme outliers will call attention to certain books' unique characteristics. 

In stylometrics, however, similarity is probably more interesting than difference. 

Consider the graph for "Distraction and Distractable" and note its similarity to "Pride and Prejudice". Along with its compound, alliterative title, this curve suggests strongly that this is a book based on Pride and Prejudice, and an examination of its text bears that out. 

Of course, it is also possible to know that Pride and Prejudice is Koppen's source material because he explains his methods in the accompanying Github repository, but the work of stylometry in the kind of knowledge I'm seeking about NaNoGenMo through its corpus is most useful if it can find new texts of unknown or undiscolosed source material. 

Comparing curves lets me calculate the curve similarity between two novels. So this is a list of the top 30 scoring novels, ranked by their similarity to Jane Austen. Here, a higher number conveys greater correspondence, so _Pride and Prejudice_ would score a 100 match for Austen, while _A Young Dream of Large Vermin_ by moss scores a respectable 97.8 match. 

Some of these books' relationship to Austen is pretty easy to guess from the titles, but most of these authors have shared enough code or a clear enough description of their process that I can manually verify their inspirations. 

These works now highlighted in yellow apparently work with Austen's text somehow. What's striking to me is how sharply the Austen-correspondence drops off after the first 10 or books. This suggests that the highest scorers are _very_ close to Austen while there is a potentially much larger category of "generally Austenian" works, most of which won't actually have the same provenance.

According to this metric, the most Austen-like work of other origins is Nick Montfort's _All my Smooth Body_, but since Montfort's code explains that it uses a Shakespeare corpus, whose authorship does this alleged affinity illuminate: Montfort, Austen, or Shakespeare?

Alternatively, what if Austen's, Shakespeare's, and Melville's composition curves aren't the most reliable indicators of similarity, difference and influence.

This graph plots Austen-value on an X-axis and Melville-value on a Y-axis, resutling in a narrow triangle of possibilities. It's a triangle because Melville is a little Austenian and vice versa, and because some texts are so unlike either that they get as far away as possible up to the right.

It would be possible, though I don't have time today, to rotate this graph to better reveal clusters of similar texts, and it would also be possible, through Principle Component Analysis and dimensional reduction to add other comparisons to the same graph.

Instead, I will close with one final example: deformance.

In the end, one thing that gives computer generated novels value in addition to their inherent aesthetic qualities is that they perform as critical lenses into the forms and contexts of the literary novel genre. In a "deformancing" gesture, NaNoGenMo books enact particular ideas and models of other texts, and through their artifacts, leave traces of a way of looking at those other texts.

If algorithmic deformance is yet another method of distant reading, it seems fitting, therefore, to deformance the NaNoGenMo corpus with a parody generated by Hugh Kenner and Joseph P. O'Rourke "Travesty," which is an ancestor to many of the techniques employed in NaNoGenMo.

> just at the confusion of doors.
> bonk entered a high picture gallery, watched over by a sequel...
> which was found a Sat! with a repeated pattern of Why? bonk felt sure
> that this must be the way out

Altogether, computational analyses of generated texts has, hopefully, illuminated some of the trends in practice for this particular creative community, as well as highlighting the limits of some of these formulas for generating real insight. Probably the most valuable critiques for literary history lie in understanding how Nanogenmo collectively responds to, parodies, and iterates the cultural idea of the novel as a literary form.

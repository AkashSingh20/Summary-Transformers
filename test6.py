# transformers, works but prompts if value entered is small
from transformers import pipeline


summarizer = pipeline('summarization')

article = """ 

The US-Russia Youth TV Bridge (YTVB) is SEE’s youth media flagship project. YTVB is an international platform for increasing cooperation between US and Russian high school students through joint storytelling on social issues. Competitively selected high school students engage in virtual and in-person collaboration to learn about digital media space in both countries and produce a series of broadcast-style videos on a range of social topics relevant for Russia and the US. Through specialized training and virtual production of content on such topics, YTVB is equipping young people in the US and Russia with skills that will help create a more inclusive and diverse space in online media. SEE has been implementing YTVB since 2016 and anchors just wrapped up production on its fifth season, which ran from January to August 2021.

"""


length = len(article.split())
print("The length of the transcript provided is:\t", length)
a = int(input("Enter the max length of the summary:\t"))
# b = int(input("Enter the min length of the summary:\t"))

summary = summarizer(article, max_length= a, min_length= 0, do_sample=False)


if (a> length):
    print("Summary length is more than the original length, summary might be improper\n Summary: ", summary )

elif (a<=length):
    print("Summary:", summary)



# works but need tensorflow or pytorch

# SEE has been implementing YTVB since 2016 and anchors just wrapped up production on its fifth season, which ran from January to August 2021 . The US-Russia Youth TV Bridge is SEE’s youth media flagship project
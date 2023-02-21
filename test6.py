# transformers, works but prompts if value entered is small
from transformers import pipeline


summarizer = pipeline('summarization')

with open('text.txt','r') as file:
    str = file.read()
    article= str.replace("â€™", "'")



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
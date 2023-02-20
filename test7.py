# works 

article = """ 

The US-Russia Youth TV Bridge (YTVB) is SEE’s youth media flagship project. YTVB is an international platform for increasing cooperation between US and Russian high school students through joint storytelling on social issues. Competitively selected high school students engage in virtual and in-person collaboration to learn about digital media space in both countries and produce a series of broadcast-style videos on a range of social topics relevant for Russia and the US. Through specialized training and virtual production of content on such topics, YTVB is equipping young people in the US and Russia with skills that will help create a more inclusive and diverse space in online media. SEE has been implementing YTVB since 2016 and anchors just wrapped up production on its fifth season, which ran from January to August 2021.

"""
###############

rand = len(article.split())

print(rand)

################

len(article)
#######################
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

checkpoint = "sshleifer/distilbart-cnn-12-6"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
#####################
tokenizer.model_max_length
###############
tokenizer.max_len_single_sentence 
###############
tokenizer.num_special_tokens_to_add() 
###############
import nltk
nltk.download('punkt')
sentences = nltk.tokenize.sent_tokenize(article)
###############
max([len(tokenizer.tokenize(sentence)) for sentence in sentences])
###############
length = 0
chunk = ""
chunks = []
count = -1
for sentence in sentences:
  count += 1
  combined_length = len(tokenizer.tokenize(sentence)) + length # add the no. of sentence tokens to the length counter

  if combined_length  <= tokenizer.max_len_single_sentence: # if it doesn't exceed
    chunk += sentence + " " # add the sentence to the chunk
    length = combined_length # update the length counter

    # if it is the last sentence
    if count == len(sentences) - 1:
      chunks.append(chunk.strip()) # save the chunk
    
  else: 
    chunks.append(chunk.strip()) # save the chunk
    
    # reset 
    length = 0 
    chunk = ""

    # take care of the overflow sentence
    chunk += sentence + " "
    length = len(tokenizer.tokenize(sentence))
len(chunks)
#####################
[len(tokenizer.tokenize(c)) for c in chunks]
######################
[len(tokenizer(c).input_ids) for c in chunks]
###################
sum([len(tokenizer(c).input_ids) for c in chunks])
#############
len(tokenizer(article).input_ids)
################
inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]


################
for input in inputs:
  output = model.generate(**input, max_length=60, min_length=0)
  print('Generated Shape:', output.shape)

  print(tokenizer.decode(*output, skip_special_tokens=True ))





# The US-Russia Youth TV Bridge (YTVB) is SEE’s youth media flagship project. SEE has been implementing YTVB since 2016 and anchors just wrapped up production on its fifth season.
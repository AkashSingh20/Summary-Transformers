# Refined version of test7.py


with open('text.txt','r') as file:
    str = file.read()
    article= str.replace("â€™", "'")


print(len(article.split()))


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
checkpoint = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)


import nltk
# nltk.download('punkt')               one time thing
sentences = nltk.tokenize.sent_tokenize(article)


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


inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]


for input in inputs:
  output = model.generate(**input,max_length=60, min_length=0)
  print('Generated Shape:', output.shape)

  print(tokenizer.decode(*output, skip_special_tokens=True))




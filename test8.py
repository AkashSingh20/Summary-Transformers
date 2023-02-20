#fuckin works but gives inappropriate when max is lowered


from transformers import AutoTokenizer, BartForConditionalGeneration

model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

ARTICLE_TO_SUMMARIZE = ("""
   
The US-Russia Youth TV Bridge (YTVB) is SEE’s youth media flagship project. YTVB is an international platform for increasing cooperation between US and Russian high school students through joint storytelling on social issues. Competitively selected high school students engage in virtual and in-person collaboration to learn about digital media space in both countries and produce a series of broadcast-style videos on a range of social topics relevant for Russia and the US. Through specialized training and virtual production of content on such topics, YTVB is equipping young people in the US and Russia with skills that will help create a more inclusive and diverse space in online media. SEE has been implementing YTVB since 2016 and anchors just wrapped up production on its fifth season, which ran from January to August 2021.

 """)

print(len(ARTICLE_TO_SUMMARIZE))

inputs = tokenizer([ARTICLE_TO_SUMMARIZE], max_length=1024, return_tensors="pt",truncation=True)
print('Input Shape:', inputs.input_ids.shape)

# Generate Summary
summary_ids = model.generate(inputs["input_ids"], num_beams=2, min_length=0, max_length=60)
print('Generated Shape:', summary_ids.shape)

print(tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])


# YTVB is SEE’s youth media flagship project. It is an international platform for increasing cooperation between US and Russian high school students through joint storytelling on social issues. SEE has been implementing YTVB since 2016.
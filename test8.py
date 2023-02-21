#fuckin works but gives inappropriate when max is lowered


from transformers import AutoTokenizer, BartForConditionalGeneration

model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

with open('text.txt','r') as file:
    str = file.read()
    article= str.replace("â€™", "'")


print(len(article))

inputs = tokenizer([article], max_length=1024, return_tensors="pt",truncation=True)
print('Input Shape:', inputs.input_ids.shape)

# Generate Summary
summary_ids = model.generate(inputs["input_ids"], num_beams=2, min_length=0, max_length=60)
print('Generated Shape:', summary_ids.shape)

print(tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])


# YTVB is SEE’s youth media flagship project. It is an international platform for increasing cooperation between US and Russian high school students through joint storytelling on social issues. SEE has been implementing YTVB since 2016.
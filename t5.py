#CNN
from datasets import load_dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
cnn_dm = load_dataset("cnn_dailymail", "3.0.0")
dataset = cnn_dm["test"]
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
sample = dataset[0]["article"]

input_text = "summarize: " + sample
inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
inputs = {k: v.to(device) for k, v in inputs.items()}
summary_ids = model.generate(inputs["input_ids"], max_length=50, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("\nOriginal:\n", sample)
print("\nSummary:\n", summary)

#wikisum
import torch
from datasets import load_dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration

dataset = load_dataset("d0rj/wikisum")
example = dataset["train"][0]
print("Available fields in sample:", example.keys())
input_text = "summarize: " + example["article"]
reference_summary = example["summary"]
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
inputs = {k: v.to(device) for k, v in inputs.items()}
summary_ids = model.generate(inputs["input_ids"], max_length=150, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("\nGenerated Summary:\n", summary)
print("\nReference Summary:\n", reference_summary)
# multinews
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from datasets import load_dataset

multi_news = load_dataset("multi_news")
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def summarize(text, max_input_length=512, max_summary_length=50):
    input_text = "summarize: " + text
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=max_input_length, padding="max_length")
    inputs = {k: v.to(device) for k, v in inputs.items()}

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=max_summary_length,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

for i in range(5):
    doc = multi_news["test"][i]["document"]
    print(f"\nDocument {i+1}:\n", doc[:500], "...\n")
    summary = summarize(doc)
    print(f"Generated Summary {i+1}:\n", summary)

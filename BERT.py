import torch
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from torch.utils.data import DataLoader, Dataset, RandomSampler

class CustomDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        encoding = self.tokenizer(self.texts[idx], return_tensors='pt', padding='max_length', truncation=True, max_length=self.max_length)
        item = {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'labels': torch.tensor(self.labels[idx], dtype=torch.long)
        }
        return item

texts = [
    "Hi. how are you. I'm fine. how old are you. 9. send me your photos. looking nice. send me your pics without t-shirt. make some pics without t-shirt. I like to see your body without t-shirt. you can. make some new pics in bathroom. without clothes. don't tell to anyone. it's secret between us only. Lol. make some pics without t-shirt now", 
    "I hate cats", 
    "I'm not really into cats", 
    'I really really love dogs', 
    "dogs", 
    "cats"]
labels = torch.tensor([1, 0, 0, 1, 1, 0])

model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)

train_dataset = CustomDataset(texts=texts, labels=labels, tokenizer=tokenizer, max_length=128)
# val_dataset = CustomDataset(texts=val_texts, labels=val_labels, tokenizer=tokenizer, max_length=128)

# Create data loaders
batch_size = 16
train_loader = DataLoader(train_dataset, batch_size=batch_size, sampler=RandomSampler(train_dataset))
# val_loader = DataLoader(val_dataset, batch_size=batch_size)

# Training loop
optimizer = AdamW(model.parameters(), lr=2e-5)
for epoch in range(3):
    model.train()
    for batch in train_loader:
        optimizer.zero_grad()
        input_ids = batch['input_ids']
        attention_mask = batch['attention_mask']
        labels = batch['labels']
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

# Prediction
model.eval()
with torch.no_grad():
    input_text = "this is about dogs"
    input_encoding = tokenizer(input_text, return_tensors='pt', padding='max_length', truncation=True, max_length=128)
    output = model(**input_encoding)
    probs = torch.softmax(output.logits, dim=1)
    confidence_score = probs.max().item()
    predicted_label = probs.argmax().item()

print(f"Predicted Label: {predicted_label}")
print(f"Confidence Score: {confidence_score:.4f}")

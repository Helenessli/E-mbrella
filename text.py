import torch
from transformers import XLNetTokenizer, XLNetForSequenceClassification, AdamW
from torch.utils.data import DataLoader, TensorDataset, random_split

tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')

text = ["I love dogs", "I hate cats", "I'm not really into cats", 'I really really love dogs', "dogs", "cats"]

labels = torch.tensor([1, 0, 0, 1, 1, 0])

encoded_inputs = tokenizer(text, padding=True, truncation=True, return_tensors='pt')

dataset = TensorDataset(encoded_inputs.input_ids, encoded_inputs.attention_mask)
train_loader = DataLoader(dataset, batch_size=8, shuffle=True)

model = XLNetForSequenceClassification.from_pretrained('xlnet-base-cased', num_labels=2)

optimizer = AdamW(model.parameters(), lr=1e-5)
for epoch in range(3):  # Number of training epochs
    for batch in train_loader:
        optimizer.zero_grad()
        input_ids, attention_mask = batch
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

input_text = ["I love dogs"]

input_encoded = tokenizer(input_text, padding=True, truncation=True, return_tensors='pt')
predictions = model(input_ids=input_encoded.input_ids, attention_mask=input_encoded.attention_mask)
predicted_class = predictions.logits.argmax().item()

print(predicted_class)
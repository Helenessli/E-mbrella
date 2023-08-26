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

data = [
    #predator msg
    {"text": "send me your photos. ", "label": 1},
    {"text": "send me your pics without t-shirt. ", "label": 1},
    {"text": "make some pics without t-shirt. ", "label": 1},
    {"text": "I like to see your body without t-shirt. ", "label": 1},
    {"text": "you can. make some new pics in bathroom. ", "label": 1},
    {"text": "without clothes.don't tell to anyone. ", "label": 1},
    {"text": "it's secret between us only. ", "label": 1},
    {"text": "do you like older men?", "label": 1},
    {"text": "what are you wearing right now?", "label": 1},
    {"text": "you look nice", "label": 1},
    {"text": "take some pics without t-shirt now", "label": 1},
    {"text": "Do you promise to keep your mouth closed about what is said on here staying in here only and you cannot tell anyone else ok", "label": 1},
    {"text": "So are you at home now", "label": 1},
    {"text": "Are you in your bedroom on your own", "label": 1},
    {"text": "OK close the door and lock it and sit down on the bed", "label": 1},
    {"text": "Now say hi master", "label": 1},
    {"text": "would u like to meet and mess around?", "label": 1},
    {"text": "do u like to mess around? kissing, touching", "label": 1},
    {"text": "Hi, I'm 33 is that ok?", "label": 1},
    {"text": "Have you been with an older man before?", "label": 1},
    {"text": "you're so pretty, you in bed right now?", "label": 1},
    {"text": "Your mom might ask you who your chatting with", "label": 1},
    {"text": "What are you wearing right now?", "label": 1},
    {"text": "Just boxers and y, what color panties?", "label": 1},
    {"text": "Id want to lick you really good between your pretty legs", "label": 1},
    {"text": "Just wondering, I wish you were here right now", "label": 1},
    {"text": "Would you be a good little girl and let me", "label": 1},
    {"text": "You get horny alot, don't you?", "label": 1},
    {"text": "do you like old men?", "label": 1},
    {"text": "have you ever had a master before darling?", "label": 1},
    {"text": "i’m in my early 60s. is that okay?", "label": 1},
    {"text": "I like your young age and I would like to own you and play with your young body", "label": 1},
    {"text": "You’ll have to follow orders and submit yourself to me", "label": 1},
    {"text": "Especially your young body", "label": 1},
    {"text": "But you have to take care of my needs", "label": 1},
    {"text": "My needs are sexual mostly, which you’ll have to satisfy with your young body", "label": 1},
    {"text": "are you ready to submit? ", "label": 1},
    {"text": "i want you to play your phone and open discord camera and present me your young little body", "label": 1},
    {"text": "I want to see your young body, it’ll excite me", "label": 1},
    {"text": "what you wearing", "label": 1},
    {"text": "I often walk around the house naked lol", "label": 1},
    {"text": "I’m old enough to be your daddy. are you horny?", "label": 1},
    {"text": "Do you like big dick?", "label": 1},
    {"text": "Let me see your boobs", "label": 1},
    {"text": "Do you want to see my dick? Do you like or nah?", "label": 1},
    {"text": "Do you wanna suck it?", "label": 1},
    {"text": "between your legs", "label": 1},
    {"text": "suck your pussy", "label": 1},
    {"text": "nice baby", "label": 1},
    {"text": "sit on my lap kitten", "label": 1},

    #not predator msg
    {"text": "would u like to meet rn?", "label": 0},
    {"text": "anything u like, what would u like to do?", "label": 0},
    {"text": "Hi. how are you.", "label": 0},
    {"text": "I'm fine. ", "label": 0},
    {"text": "how old are you.", "label": 0},
    {"text": "looking nice. ", "label": 0},
    {"text": "Hi, how are you doing?", "label": 0},
    {"text": "What's your plan for the weekend?", "label": 0},
    {"text": "I'm excited about the upcoming event!", "label": 0},
    {"text": "Did you watch the new movie yet?", "label": 0},
    {"text": "Let's meet for coffee tomorrow.", "label": 0},
    {"text": "Have you read any good books lately?", "label": 0},
    {"text": "How was your day at work?", "label": 0},
    {"text": "I'm thinking of trying a new recipe for dinner.", "label": 0},
    {"text": "Do you want to go for a walk later?", "label": 0},
    {"text": "The weather is really nice today!", "label": 0},
    {"text": "Just finished my workout. Feeling great!", "label": 0},
    {"text": "I'll be a bit late for our meeting.", "label": 0},
    {"text": "Thanks for the help, I appreciate it.", "label": 0},
    {"text": "How's your family doing?", "label": 0},
    {"text": "I'm looking forward to the holidays.", "label": 0},
    {"text": "Can you pass me the salt, please?", "label": 0},
    {"text": "I had a productive day at the office.", "label": 0},
    {"text": "Let's catch up over the phone sometime.", "label": 0},
    {"text": "I'm thinking of redecorating my room.", "label": 0},
    {"text": "Congratulations on your new job!", "label": 0},
    {"text": "Hey, what's up?", "label": 0},
    {"text": "Did you see that TikTok video?", "label": 0},
    {"text": "I'm so tired from school today.", "label": 0},
    {"text": "Let's hang out after classes!", "label": 0},
    {"text": "Can't wait for the weekend. Party time!", "label": 0},
    {"text": "LOL, that meme is hilarious!", "label": 0},
    {"text": "Just finished my homework. Ugh.", "label": 0},
    {"text": "Have you played the new game yet?", "label": 0},
    {"text": "OMG, did you hear the latest gossip?", "label": 0},
    {"text": "Got any Netflix recommendations?", "label": 0},
    {"text": "Can you believe the test scores? ", "label": 0},
    {"text": "I'm craving pizza right now.", "label": 0},
    {"text": "Wanna hit the mall later?", "label": 0},
    {"text": "My parents are so annoying sometimes.", "label": 0},
    {"text": "Watching YouTube till 2 AM.", "label": 0},
    {"text": "Thinking of dying my hair. Thoughts?", "label": 0},
    {"text": "Have you started studying for finals?", "label": 0},
    {"text": "That concert was EPIC!", "label": 0},
    {"text": "Let's FaceTime later, okay?", "label": 0},
    {"text": "Binge-watching shows all day!", "label": 0},
    {"text": "I need a new profile pic ASAP.", "label": 0},
    {"text": "Just got a new pair of sneakers!", "label": 0},
    {"text": "Any plans for summer break?", "label": 0},
    {"text": "Ugh, why is school so stressful?", "label": 0},
    {"text": "Can't believe it's almost graduation!", "label": 0},
]

texts = [item["text"] for item in data]
labels = [item["label"] for item in data]

#pretrained model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

#training model
# tokenizer = BertTokenizer.from_pretrained('custom_bert_model')
model = BertForSequenceClassification.from_pretrained('./custom_bert_model/', num_labels=2)

#pre-trained model
# model.save_pretrained('custom_bert_model')

train_dataset = CustomDataset(texts=texts, labels=labels, tokenizer=tokenizer, max_length=128)

# Create data loaders
batch_size = 16
train_loader = DataLoader(train_dataset, batch_size=batch_size, sampler=RandomSampler(train_dataset))

# Training loop
# optimizer = AdamW(model.parameters(), lr=2e-5)
# for epoch in range(3):
#     model.train()
#     for batch in train_loader:
#         optimizer.zero_grad()
#         input_ids = batch['input_ids']
#         attention_mask = batch['attention_mask']
#         labels = batch['labels']
#         outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
#         loss = outputs.loss
#         loss.backward()
#         optimizer.step()

# Prediction
model.eval()

with torch.no_grad():
    input_text = "how's the weather today?"
    input_encoding = tokenizer(input_text, return_tensors='pt', padding='max_length', truncation=True, max_length=128)
    output = model(**input_encoding)
    probs = torch.softmax(output.logits, dim=1)
    confidence_score = probs.max().item()
    predicted_label = probs.argmax().item()

print(f"Predicted Label: {predicted_label}")
print(f"Confidence Score: {confidence_score:.4f}")
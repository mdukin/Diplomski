import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


class BaselineModel(nn.Module):
    def __init__(self, embedding_matrix):
        super(BaselineModel, self).__init__()

        self.embedding = embedding_matrix

        self.pool = nn.AdaptiveAvgPool1d(output_size=1)
    
        self.fc1 = nn.Linear(300, 150)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(150, 150)
        self.fc3 = nn.Linear(150, 1)
        
    def forward(self, text):

        embedded = self.embedding(text)

        # (batch, rijeci, d)

        embedded = embedded.permute(0,2,1)

        x = self.pool(embedded) 
        
        # (batch x d x 1)

        x = torch.squeeze(x, dim=2) 

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)

        return torch.squeeze(x, dim=1)



class RecurrentModel(nn.Module):
    def __init__(self, embedding_matrix, cell, num_layers=2,dim1=300,hidden_size=150, dropout = 0,bidirectional = False):
        super(RecurrentModel, self).__init__()

        self.embedding = embedding_matrix

        if cell=="gru":
            self.rnn = nn.GRU(dim1, hidden_size, num_layers=num_layers, dropout=dropout, bidirectional=bidirectional)   
        elif cell=="lstm":
            self.rnn = nn.LSTM(dim1, hidden_size, num_layers=num_layers,  dropout=dropout, bidirectional=bidirectional)  
        else: 
            self.rnn = nn.RNN(dim1, hidden_size, num_layers=num_layers, dropout=dropout, bidirectional=bidirectional)
        

        self.fc1 = nn.Linear(hidden_size * (2 if bidirectional else 1), 150)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(150, 1)
        
    def forward(self, text):

        embedded = self.embedding(text)
        # (batch, time, d)

        embedded = torch.transpose(embedded, 0, 1)   
        # (time, batch, d)

        ht, _ = self.rnn(embedded)
        #(ht , batch, d)
        
        x = ht[-1] # zadnji ht (batch,d)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return torch.squeeze(x, dim=1)

def train(model, data, optimizer, criterion,max_norm=0.25):
    model.train()

    for batch_num, batch in enumerate(data):

        optimizer.zero_grad()
                
        x = batch[0]   
        y = batch[1]    
        #len_s = batch[2]

        logits = model(x)
        loss = criterion(logits, y.float())   
        loss.backward()

        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm)   

        optimizer.step()



def evaluate(model, data, criterion):
    model.eval()

    y_pred = []
    y_real = []

    with torch.no_grad():
        for batch_num, batch in enumerate(data):

            x = batch[0]   
            y = batch[1]    

            logits = model(x)
        
            logits = torch.sigmoid(logits)
            logits = torch.round(logits).int()

            y_pred.extend(logits.tolist())
            y_real.extend(y.tolist())

        cm = confusion_matrix(y_real, y_pred)
        acc = accuracy_score(y_real, y_pred)
        f1 = f1_score(y_real, y_pred)

        return  acc, f1, cm


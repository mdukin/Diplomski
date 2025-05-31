from data_collection import *
from modeli import *

from torch.utils.data import DataLoader

import torch
import torch.nn as nn
import torch.optim as optim


def load_data():
    frequencies = calculate_frequencies("csv/sst_train_raw.csv")

    text_vocab = Vocab().text_vocab(frequencies, max_size=-1, min_freq=1)
    label_vocab = Vocab().label_vocab()

    embedding_matrix = gen_embedding_matrix(text_vocab.vocab, "words/sst_glove_6b_300d.txt")


    train_dataset = NLPDataset("csv/sst_train_raw.csv", text_vocab, label_vocab)
    train_dataloader = DataLoader(dataset=train_dataset, batch_size=batch_size, 
                                shuffle=True, collate_fn=pad_collate_fn)


    validation_dataset = NLPDataset("csv/sst_valid_raw.csv", text_vocab, label_vocab)
    validation_dataloader = DataLoader(dataset=validation_dataset, batch_size=32, 
                                shuffle=False, collate_fn=pad_collate_fn)


    test_dataset = NLPDataset("csv/sst_test_raw.csv", text_vocab, label_vocab)
    test_dataloader = DataLoader(dataset=test_dataset, batch_size=32, 
                                shuffle=False, collate_fn=pad_collate_fn)
    return train_dataloader, validation_dataloader, test_dataloader, embedding_matrix

def run(model):
    optimizer = optim.Adam(model.parameters(), lr=lr)
    for epoch in range(num_epochs):

        train(model=model, data=train_dataloader, optimizer=optimizer, criterion=criterion)

        acc, f1, cm = evaluate(model=model, data=validation_dataloader, criterion=criterion)

        print("epoch",str(epoch+1), ": valid accuracy =",acc)
        print("f1",f1)
        print(cm)
        print()


    acc, f1, cm = evaluate(model=model, data=test_dataloader, criterion=criterion)
    print("Test accuracy =",acc)
    print("f1",f1 )
    print(cm)
    print()



batch_size = 10
seed =7052020

torch.manual_seed(seed)
np.random.seed(seed)
num_epochs = 5
lr = 1e-4
criterion = nn.BCEWithLogitsLoss()

train_dataloader, validation_dataloader, test_dataloader, embedding_matrix = load_data()



#run(BaselineModel(embedding_matrix))

#run(RecurrentModel(embedding_matrix, "rnn", hidden_size=300, num_layers=1, bidirectional=True, dropout=0.1))

#run(RecurrentModel(embedding_matrix, "lstm"))

#run(RecurrentModel(embedding_matrix,"gru"))


for seed in range(0,5):
    print(seed)
    torch.manual_seed(seed)
    np.random.seed(seed)
    train_dataloader, validation_dataloader, test_dataloader, embedding_matrix = load_data()
    run(RecurrentModel(embedding_matrix, "gru", hidden_size=300, num_layers=3, bidirectional=False))

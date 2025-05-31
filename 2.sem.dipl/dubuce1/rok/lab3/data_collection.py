import torch
from torch.utils.data import Dataset, DataLoader
from dataclasses import dataclass
from collections import defaultdict
import numpy as np
from torch.nn.utils.rnn import pad_sequence

@dataclass
class Instance:
    def __init__(self, text, label):
        self.text = text
        self.label = label
    def get(self):
        return self.text, self.label

class NLPDataset(Dataset):
    def __init__(self, path, vocab_text, vocab_label):
        self.instances = NLPDataset.from_file(path)
        self.vocab_text = vocab_text
        self.vocab_label = vocab_label

    def __len__(self):
        return len(self.instances)

    def __getitem__(self, id):
        instance = self.instances[id]
        return (self.vocab_text.encode(instance.text), self.vocab_label.encode(instance.label) )
    
    def from_file(path):
        instances = []
        with open(path, 'r') as file:
            for line in file:
                text = line[:line.index(",")]
                label = line[1+line.index(","):].strip()
                instances.append(Instance(text,label))
        return instances

class Vocab:
    def __init__(self) -> None:
        pass
    def text_vocab(self, frequencies, max_size, min_freq) -> None:
        
        cut_frequencies = [word for word, freq in frequencies.items() if freq >= min_freq]
        if max_size != -1:
            cut_frequencies = cut_frequencies[:max_size - 2]

        sorted_frequencies = sorted(cut_frequencies, key=lambda x: frequencies[x], reverse=True)
        vocab = ["<PAD>", "<UNK>"] + sorted_frequencies
        self.vocab = vocab
        self.word2idx = {word: idx for idx, word in enumerate(vocab)}
        self.idx2word = {idx: word for word, idx in self.word2idx.items()}
        return self
    
    def label_vocab(self):
        self.word2idx = {"positive":0, "negative":1}
        self.idx2word = {0 : "positive", 1:"negative"}
        self.vocab = ["positive", "negative"]
        return self
    
    def encode(self, input):
        text = input.split()
        
        return torch.tensor([self.word2idx.get(word, 1) for word in text])


def calculate_frequencies(path):
    frequencies = defaultdict(int)
    with open(path, 'r') as file:
        for line in file:
            words = line[:line.index(",")].strip().split()
            for word in words:
                frequencies[word] += 1
    return frequencies

def gen_embedding_matrix(vocab, path= None):
    embedding_matrix = np.random.randn(len(vocab), 300)
    
    embedding_matrix[0] = np.zeros(300)

    if path !=None:
        with open(path, 'r') as file:
            for line in file:
                word_vector = line.split()
                word = word_vector[0]
                if word in vocab:
                    idx = vocab.index(word)
                    embedding_matrix[idx] = list(map(float, word_vector[1:]))

    em =  torch.tensor(embedding_matrix, dtype=torch.float32)
    return torch.nn.Embedding.from_pretrained(em, padding_idx=0, freeze=True)

def pad_collate_fn(batch, pad_index=0):

    texts, labels = zip(*batch) 
    lengths = torch.tensor([len(text) for text in texts])
    #padded_texts = pad_sequence([torch.tensor(text) for text in texts], padding_value=pad_index,batch_first=True)
    padded_texts = pad_sequence([text.clone().detach() for text in texts], padding_value=pad_index, batch_first=True)

    labels = torch.tensor(labels)
    return padded_texts, labels, lengths


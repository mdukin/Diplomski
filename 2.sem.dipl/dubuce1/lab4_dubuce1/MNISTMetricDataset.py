from torch.utils.data import Dataset
import torch
from collections import defaultdict
from random import choice
import torchvision


class MNISTMetricDataset(Dataset):
    def __init__(self, root="/tmp/mnist/", split='train', remove_class=None):
        super().__init__()
        assert split in ['train', 'test', 'traineval']
        self.root = root
        self.split = split
        mnist_ds = torchvision.datasets.MNIST(self.root, train='train' in split, download=True)
        self.images, self.targets = mnist_ds.data.float() / 255., mnist_ds.targets
        self.classes = list(range(10))

        if remove_class is not None:
            # Filter out images with target class equal to remove_class
            # YOUR CODE HERE        

            self.classes.remove(remove_class)
            
            mask = self.targets != remove_class

            self.targets = self.targets[mask]
            self.images = self.images[mask]

        self.target2indices = defaultdict(list)
        for i in range(len(self.images)):
            self.target2indices[self.targets[i].item()] += [i]

    def _sample_negative(self, index):
        ##########
        target_id = self.targets[index].item()

        lista_bez_target_id = [el for el in self.classes if el != target_id]

        target_list = self.target2indices[choice(lista_bez_target_id)]
        return choice(target_list)


    def _sample_positive(self, index):
        ###########
        target_id = self.targets[index].item()
        target_list = self.target2indices[target_id]

        return choice(target_list)

    def __getitem__(self, index):
        anchor = self.images[index].unsqueeze(0)
        target_id = self.targets[index].item()
        if self.split in ['traineval', 'val', 'test']:
            return anchor, target_id
        else:
            positive = self._sample_positive(index)
            negative = self._sample_negative(index)
            positive = self.images[positive]
            negative = self.images[negative]
            return anchor, positive.unsqueeze(0), negative.unsqueeze(0), target_id

    def __len__(self):
        return len(self.images)
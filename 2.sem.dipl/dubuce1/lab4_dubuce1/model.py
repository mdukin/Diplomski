import torch
import torch.nn as nn
import torch.nn.functional as F


class _BNReluConv(nn.Sequential):
    def __init__(self, num_maps_in, num_maps_out, k=3, bias=True):
        super(_BNReluConv, self).__init__()
        # YOUR CODE HERE

        self.append(nn.BatchNorm2d(num_maps_in))
        self.append(nn.ReLU(inplace=True))
        self.append(nn.Conv2d(num_maps_in, num_maps_out, k, padding=1, bias=bias))


class SimpleMetricEmbedding(nn.Module):
    def __init__(self, input_channels, emb_size=32):
        super().__init__()
        self.emb_size = emb_size
        # YOUR CODE HERE
        self.layer1 = _BNReluConv(input_channels, emb_size, k=3, bias=False)
        
        self.layer2 = _BNReluConv(emb_size, emb_size, k=3, bias=False)
   
        self.layer3 = _BNReluConv(emb_size, emb_size, k=3, bias=False)

        self.max_pool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        
        self.avg_pool = nn.AdaptiveAvgPool2d(1)  

    def get_features(self, img):
        # Returns tensor with dimensions BATCH_SIZE, EMB_SIZE
        # YOUR CODE HERE
        x = self.layer1(img)
        x = self.max_pool(x)
        
        x = self.layer2(x)
        x = self.max_pool(x)
        
        x = self.layer3(x)
        x = self.max_pool(x)
        
        x = self.avg_pool(x)
        x = x.reshape(x.shape[0], x.shape[1])   # (batch_size, emb_size)
        return x

    def loss(self, anchor, positive, negative):
        a_x = self.get_features(anchor)
        p_x = self.get_features(positive)
        n_x = self.get_features(negative)
        # YOUR CODE HERE
        #triplet_loss = nn.TripletMarginLoss(margin=1.0, p=2, eps=1e-7)
        #loss = triplet_loss(a_x, p_x, n_x)
    
        margin = 1

        d1 = torch.linalg.norm(a_x - p_x, dim=1)
        d2 = torch.linalg.norm(a_x - n_x, dim=1)
            
        loss = torch.relu(d1 - d2 + margin)  


        return torch.mean(loss)
import torch
import torch.nn as nn

class IdentityModel(nn.Module):
    def __init__(self):
        super(IdentityModel, self).__init__()

    def get_features(self, img):

        feats = img.flatten()
        return feats
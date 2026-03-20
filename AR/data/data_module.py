import torch
from torch.utils.data import Dataset, DataLoader, RandomSampler

class CustomDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Example usage:
# data = [...]  # Your dataset
# dataset = CustomDataset(data)
# sampler = RandomSampler(dataset)
# dataloader = DataLoader(dataset, sampler=sampler)
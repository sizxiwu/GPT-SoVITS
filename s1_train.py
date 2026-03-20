# Update: Disable DDP and use single GPU 0

# Previous imports
from pytorch_lightning import Trainer

# Set up the Trainer with auto strategy and single device
trainer = Trainer(strategy='auto', devices=[0])
